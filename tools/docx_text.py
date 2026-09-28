"""把大考中心的 .docx 試卷轉成依序排列的文字區塊。

保留：底線 <u>、著重號 <em>、上下標、表格（HTML）、文字方塊（獨立區塊）、圖片位置。
用法：python3 tools/docx_text.py <試卷.docx>   → 印出區塊，供人工檢查
"""
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "mc": "http://schemas.openxmlformats.org/markup-compatibility/2006",
    "wps": "http://schemas.microsoft.com/office/word/2010/wordprocessingShape",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "pic": "http://schemas.openxmlformats.org/drawingml/2006/picture",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "v": "urn:schemas-microsoft-com:vml",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
}
W = "{%s}" % NS["w"]
MC = "{%s}" % NS["mc"]
WPS = "{%s}" % NS["wps"]
M = "{%s}" % NS["m"]


def _math_text(node):
    return "".join(t.text or "" for t in node.iter(M + "t"))


class Extractor:
    def __init__(self, path):
        self.zip = zipfile.ZipFile(path)
        self.root = ET.fromstring(self.zip.read("word/document.xml"))
        self.blocks = []

    # ---- runs ---------------------------------------------------------
    def _run_fmt(self, r):
        rpr = r.find("w:rPr", NS)
        fmt = set()
        if rpr is None:
            return fmt
        u = rpr.find("w:u", NS)
        if u is not None and u.get(W + "val") not in (None, "none"):
            fmt.add("u")
        em = rpr.find("w:em", NS)
        if em is not None and em.get(W + "val") not in (None, "none"):
            fmt.add("em")
        va = rpr.find("w:vertAlign", NS)
        if va is not None and va.get(W + "val") in ("superscript", "subscript"):
            fmt.add("sup" if va.get(W + "val") == "superscript" else "sub")
        return fmt

    def _run_parts(self, r, boxes):
        """回傳 [(文字, 格式)]；文字方塊與圖片另外放進 boxes。"""
        parts = []
        fmt = self._run_fmt(r)
        for child in r:
            tag = child.tag
            if tag == W + "t":
                parts.append((child.text or "", fmt))
            elif tag == W + "tab":
                parts.append(("\t", set()))
            elif tag in (W + "br", W + "cr"):
                parts.append(("\n", set()))
            elif tag == W + "sym":
                parts.append((chr(int(child.get(W + "char"), 16)) if child.get(W + "char") else "", fmt))
            elif tag in (W + "drawing", MC + "AlternateContent", W + "pict", W + "object"):
                self._collect_floating(child, boxes, parts)
        return parts

    def _collect_floating(self, node, boxes, parts):
        # mc:AlternateContent 只看 Choice，避免 VML Fallback 重複
        if node.tag == MC + "AlternateContent":
            choice = node.find("mc:Choice", NS)
            node = choice if choice is not None else node
        txbxs = list(node.iter(WPS + "txbx"))
        if txbxs:
            for tx in txbxs:
                content = tx.find("w:txbxContent", NS)
                if content is not None:
                    inner = Extractor.__new__(Extractor)
                    inner.zip, inner.root, inner.blocks = self.zip, None, []
                    inner._walk(content)
                    text = "\n".join(b["text"] for b in inner.blocks if b["text"].strip())
                    if text.strip():
                        boxes.append({"kind": "box", "text": text})
            return
        if node.tag == W + "object" or node.find(".//v:imagedata", NS) is not None and not list(node.iter(W + "t")):
            parts.append(("［公式］" if node.tag == W + "object" else "［圖］", set()))
            return
        if list(node.iter("{%s}blip" % NS["a"])):
            parts.append(("［圖］", set()))
        elif list(node.iter(WPS + "wsp")):
            parts.append(("［符號］", set()))

    # ---- paragraphs / tables -------------------------------------------
    def _para(self, p):
        parts, boxes = [], []
        for child in p:
            if child.tag == W + "r":
                parts += self._run_parts(child, boxes)
            elif child.tag in (W + "hyperlink", W + "smartTag", W + "ins"):
                for r in child.iter(W + "r"):
                    parts += self._run_parts(r, boxes)
            elif child.tag in (M + "oMath", M + "oMathPara"):
                parts.append((_math_text(child), set()))
        text = _merge(parts)
        self.blocks.append({"kind": "p", "text": text})
        self.blocks += boxes

    def _table(self, tbl):
        rows = []
        for tr in tbl.findall("w:tr", NS):
            cells = []
            for tc in tr.findall("w:tc", NS):
                inner = Extractor.__new__(Extractor)
                inner.zip, inner.root, inner.blocks = self.zip, None, []
                inner._walk(tc)
                span = tc.find("w:tcPr/w:gridSpan", NS)
                vmerge = tc.find("w:tcPr/w:vMerge", NS)
                cells.append({
                    "text": "<br>".join(b["text"] for b in inner.blocks if b["kind"] == "p" and b["text"].strip()),
                    "span": int(span.get(W + "val")) if span is not None else 1,
                    "vmerge": None if vmerge is None else (vmerge.get(W + "val") or "continue"),
                })
            rows.append(cells)
        self.blocks.append({"kind": "table", "rows": rows, "text": " | ".join(c["text"] for r in rows for c in r)})

    def _walk(self, node):
        for child in node:
            if child.tag == W + "p":
                self._para(child)
            elif child.tag == W + "tbl":
                self._table(child)
            elif child.tag == W + "sdt":
                content = child.find("w:sdtContent", NS)
                if content is not None:
                    self._walk(content)

    def run(self):
        self._walk(self.root.find("w:body", NS))
        return self.blocks


def _merge(parts):
    """合併相同格式的連續片段，輸出帶標籤的字串。"""
    out, cur_fmt, buf = [], None, ""

    def flush():
        if not buf:
            return
        s = buf
        for tag in ("sub", "sup", "em", "u"):
            if cur_fmt and tag in cur_fmt and s.strip():
                s = f"<{tag}>{s}</{tag}>"
        out.append(s)

    for text, fmt in parts:
        key = frozenset(fmt)
        if key != cur_fmt:
            flush()
            cur_fmt, buf = key, ""
        buf += text
    flush()
    s = "".join(out)
    return re.sub(r"</u><u>", "", s)


def docx_blocks(path):
    return Extractor(path).run()


if __name__ == "__main__":
    for i, b in enumerate(docx_blocks(sys.argv[1])):
        if b["text"].strip():
            print(f"{i:4d} [{b['kind']}] {b['text']}")
