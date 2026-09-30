"""學測英文：抽出所有選擇題（詞彙、綜合測驗、文意選填、篇章結構、閱讀測驗），合併官方答案與統計，輸出 YAML。

用法：python3 tools/split_english.py 110 115
輸出：data/questions/english/g<年度>.yaml
題組題的題幹放「空格所在的句子」（篇章結構放前後句），文章收合時也看得懂在問哪一格。
混合題與非選擇題不進快答，不抽。
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import qyaml  # noqa: E402
from ceec_data import answer_key, item_stats, option_stats, paper_file  # noqa: E402
from docx_text import docx_blocks  # noqa: E402
from split_chinese import table_html  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "docs" / "img" / "english"
SECTION = re.compile(r"^[一二三四五六]、\s*(詞彙題|綜合測驗|文意選填|篇章結構|閱讀測驗)")
GROUP = re.compile(r"第\s*(\d+)\s*至\s*(\d+)\s*題為題組")
TOPIC = {"詞彙題": "V1", "綜合測驗": "V2", "文意選填": "R1", "篇章結構": "R2", "閱讀測驗": "R3"}
POINTS = {"詞彙題": 1, "綜合測驗": 1, "文意選填": 1, "篇章結構": 2, "閱讀測驗": 2}
N_OPTS = {"詞彙題": {4}, "綜合測驗": {4}, "文意選填": {10}, "篇章結構": {4, 5}, "閱讀測驗": {4}}


def plain(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


def bare(s):
    """去掉段首的［圖］標記（圖片位置），用來判斷題號。"""
    return re.sub(r"^(?:［圖］\s*)+", "", plain(s))


def one_line(s):
    """段落內的換行改成空白（網站以換行分段），空格標記統一成 <u> 11 </u>。"""
    s = re.sub(r"\s*\n\s*", " ", s or "").replace("\t", " ")
    s = re.sub(r"\s*\uf0e0\s*", " → ", s)  # 原卷用 Symbol 字型的箭頭
    s = re.sub(r"<u>\s*(\d+)\s*</u>", r"<u> \1 </u>", s)
    return re.sub(r" {2,}", " ", s).strip()


def split_options(text):
    text = re.sub(r"\s*\uf0e0\s*", " → ", text)
    parts = re.split(r"\(([A-J])\)", text)
    return {parts[k]: re.sub(r"\s+", " ", parts[k + 1]).strip() for k in range(1, len(parts) - 1, 2)}


def block_text(b):
    if b["kind"] == "table":
        return table_html(b["rows"])
    if b["kind"] == "box":
        return "【框】" + one_line(b["text"])
    return one_line(b["text"])


def sentences(par):
    """把一段英文切成句子（保留 <u> 空格標記）。"""
    parts = re.split(r"(?<=[.!?])(?:[”’\"]|\s*\)\s*)?\s+(?=[A-Z“\"(<])", par)
    return [p.strip() for p in parts if p.strip()]


def blank_context(passage, no, kind):
    """回傳空格 no 所在的句子；篇章結構回傳前一句＋空格＋後一句。目標空格加粗。"""
    mark = f"<u> {no} </u>"
    for par in passage.split("\n"):
        if mark not in par:
            continue
        sents = sentences(par)
        k = next(i for i, s in enumerate(sents) if mark in s)
        if kind == "篇章結構":
            prev = sents[k - 1] if k > 0 else ""
            nxt = sents[k + 1] if k + 1 < len(sents) else ""
            if not prev:  # 空格在段首：補上一段最後一句
                pars = passage.split("\n")
                j = pars.index(par)
                if j > 0 and not pars[j - 1].startswith(("<table", "【框】")):
                    prev = sentences(pars[j - 1])[-1]
            ctx = " ".join(x for x in (prev, sents[k], nxt) if x)
        else:
            ctx = sents[k]
            if len(plain(ctx)) < 45:
                pars = passage.split("\n")
                j = pars.index(par)
                if k > 0:
                    ctx = sents[k - 1] + " " + ctx
                elif j > 0 and not pars[j - 1].startswith(("<table", "【框】")):
                    ctx = sentences(pars[j - 1])[-1] + " " + ctx
                elif k + 1 < len(sents):
                    ctx = ctx + " " + sents[k + 1]
        return ctx.replace(mark, f"<b><u> {no} </u></b>")
    return None


def attach_stats(it, stats, opts):
    s = stats.get(str(it["no"]))
    if s:
        it["stats"] = {k: v for k, v in s.items() if v is not None}
        if opts.get(str(it["no"]), {}).get("T"):
            it["stats"]["opt"] = opts[str(it["no"])]["T"]


def make_item(year, no, kind, stem, options, key, group=None):
    it = {"id": f"eng{year}-{no:02d}", "no": no, "type": "single", "points": POINTS[kind], "group": group,
          "stem": stem, "options": options, "answer": key.get(str(no)),
          "topic": TOPIC[kind], "concepts": [TOPIC[kind]], "classic": True, "explain": "", "reviewed": False}
    if len(options) not in N_OPTS[kind]:
        it.setdefault("flags", []).append(f"選項數 {len(options)}，請對照原卷")
    return it


def parse_vocab(year, body, key):
    """body：詞彙題說明之後的段落文字（依序為題目句、選項列）。"""
    items, i, no = [], 0, None
    while i + 1 < len(body):
        sentence = re.sub(r"^\d+\.\s*", "", body[i])
        m = re.match(r"^(\d+)\.", body[i])
        no = int(m.group(1)) if m else (no + 1 if no else 1)
        sentence = re.sub(r"_{3,}|\s{4,}", " ＿＿＿＿ ", sentence).replace("  ", " ").strip()
        line = body[i + 1]
        if not line.startswith("(A)"):
            line = "(A) " + line
        items.append(make_item(year, no, "詞彙題", sentence.replace("______", "＿＿＿＿"), split_options(line), key))
        i += 2
    return items


def parse_group(year, kind, a, b, blks, key):
    """一個題組：文章＋各題。回傳 (group, items)。"""
    blks = [x for x in blks if x["kind"] != "p" or plain(x["text"])]
    passage, rest = [], []
    for k, x in enumerate(blks):
        t = bare(x["text"]) if x["kind"] == "p" else ""
        if kind == "綜合測驗" and re.match(rf"^{a}\.\s*", t):
            rest = blks[k:]
            break
        if kind in ("文意選填", "篇章結構") and t.startswith("(A)"):
            rest = blks[k:]
            break
        if kind == "閱讀測驗" and re.match(rf"^{a}\.\s", t):
            rest = blks[k:]
            break
        piece = block_text(x)
        # 原卷排版把一句話斷成兩段（上一段沒有句末標點）時，接回同一段
        if (passage and x["kind"] == "p" and not passage[-1].startswith(("<table", "【框】"))
                and not passage[-1].rstrip().endswith("</u>")  # 篇章結構的空格在段尾（整句空格）
                and not re.search(r"[.!?:;”’\")]\s*$", plain(passage[-1]))):
            passage[-1] += " " + piece
        else:
            passage.append(piece)
    passage_text = "\n".join(passage)
    gid = f"eng{year}-g{a:02d}"
    group = {"id": gid, "range": [a, b], "intro": f"第{a}至{b}題為題組", "passage": passage_text}
    items = []
    if kind == "綜合測驗":
        text = "\t".join(plain(x["text"]) if x["kind"] == "p" else "" for x in rest)
        segs = re.split(r"(?:^|(?<=\s))(\d{1,2})\.(?=\s*\(A\))", text)
        for k in range(1, len(segs) - 1, 2):
            no = int(segs[k])
            items.append(make_item(year, no, kind, blank_context(passage_text, no, kind) or f"第 {no} 題空格",
                                   split_options(segs[k + 1]), key, gid))
    elif kind in ("文意選填", "篇章結構"):
        if kind == "文意選填":
            options = split_options("\t".join(plain(x["text"]) for x in rest if x["kind"] == "p"))
        else:
            options = {}
            for x in rest:
                options.update(split_options(one_line(x["text"])) if x["kind"] == "p" else {})
        for no in range(a, b + 1):
            ctx = blank_context(passage_text, no, kind)
            stem = ctx if kind == "文意選填" else f"{ctx}<br>空格 {no} 應填入哪一句？" if ctx else f"第 {no} 題空格"
            items.append(make_item(year, no, kind, stem or f"第 {no} 題空格", dict(options), key, gid))
    else:  # 閱讀測驗
        cur = None
        for x in rest:
            t = one_line(x["text"]) if x["kind"] == "p" else ""
            fig = "［圖］" in t
            t = re.sub(r"(?:［圖］\s*)+", "", t).strip()
            m = re.match(r"^(\d{1,2})\.\s*(.*)$", plain(t)) if t else None
            if m and cur is None or (m and cur and int(m.group(1)) == cur["no"] + 1):
                if cur:
                    items.append(cur)
                no = int(m.group(1))
                stem = re.sub(r"^\d{1,2}\.\s*", "", t)
                cur = {"no": no, "stem": stem, "opt": "", "fig": fig}
                continue
            if cur is None:
                continue
            if x["kind"] in ("table", "box") or fig:
                cur["fig"] = True  # 表格、文字方塊（地圖標籤）或圖片
            if x["kind"] == "p" and t and not cur["opt"].strip() and not re.search(r"\([A-D]\)", t):
                cur["stem"] += ("<br>" if re.match(r"^[a-f]\.\s", t) else " ") + t  # 題目文字換行到下一段
            elif x["kind"] == "p":
                cur["opt"] += "\t" + t
        if cur:
            items.append(cur)
        out = []
        for c in items:
            options = split_options(c["opt"])
            it = make_item(year, c["no"], kind, c["stem"], options, key, gid)
            if c["fig"] or any(not v for v in options.values()):
                it.setdefault("flags", []).append("選項或題目含圖表，需裁原卷圖片")
            out.append(it)
        items = out
    return group, items


def find_line(doc, no, start_page=0, after=None, stop=False):
    """原卷 PDF 中「題號.」所在的 (頁, y)；stop=True 時遇到題組標題或大題標題也算。"""
    for p in range(start_page, len(doc)):
        pg = doc[p]
        lines = [(ln["bbox"][1], ln["bbox"][0], "".join(sp["text"] for sp in ln["spans"]).strip())
                 for b in pg.get_text("dict")["blocks"] for ln in b.get("lines", [])]
        for y, x, t in sorted(lines):
            if (after and (p, y) <= after) or x > pg.rect.width * 0.2:
                continue
            if re.match(rf"^{no}\s*[.．]", t) or (stop and re.search(r"題為題組|^第[貳參]部分|^[一二三四五六]、", t)):
                return p, y
    return None


def crop_figure(year, no):
    """選項是圖片的題目：從題號行裁到下一題（或下一個題組標題）為止，存成 docs/img/english/<年度>-<題號>.webp。"""
    import fitz
    from PIL import Image
    from extract_images import page_bounds, render
    pdf, _ = paper_file("english", year, "試題內容", ".pdf")
    doc = fitz.open(pdf)
    p0, y0 = find_line(doc, no)
    p1, y1 = find_line(doc, no + 1, p0, after=(p0, y0), stop=True) or (p0, page_bounds(doc[p0])[1])
    pieces = []
    for p in range(p0, p1 + 1):
        top, bottom = page_bounds(doc[p])
        a, z = (y0 - 1 if p == p0 else top), (y1 - 3 if p == p1 else bottom)
        if z - a > 15:
            pieces.append((p, a, z))
    img = render(doc, pieces)
    g = img.convert("L")
    w, h = g.size
    px = g.load()
    # 上緣若帶到前一行字的下半部，切到第一條全白的列；下緣若有頁尾小字，切在最後一條水平框線下
    white = [y for y in range(0, 30) if all(px[x, y] > 235 for x in range(0, w, 2))]
    lines = [y for y in range(int(h * 0.8), h) if sum(1 for x in range(0, w, 2) if px[x, y] < 110) > w * 0.3]
    img = img.crop((0, white[0] if white and white[0] < 20 else 0, w, min(h, lines[-1] + 4) if lines else h))
    IMG.mkdir(parents=True, exist_ok=True)
    img.save(IMG / f"{year}-{no}.webp", "WEBP", quality=82, method=6)


def parse(year):
    path, docx_url = paper_file("english", year, "試題內容", ".docx")
    _, pdf_url = paper_file("english", year, "試題內容", ".pdf")
    blocks = docx_blocks(path)
    key = answer_key("english", year)
    stats = item_stats("english", year)
    opts = option_stats("english", year)
    heads = []
    for i, b in enumerate(blocks):
        t = plain(b.get("text", ""))
        m = SECTION.match(t)
        if m:
            heads.append((i, m.group(1)))
        elif re.match(r"^第[貳參]部分", t):
            heads.append((i, None))
            break
    groups, items = [], []
    for (s, kind), (e, _) in zip(heads, heads[1:]):
        if kind is None:
            continue
        sec = blocks[s + 1:e]
        if kind == "詞彙題":
            body = [b["text"].strip() for b in sec if b["kind"] == "p" and b["text"].strip()]
            body = [t for t in body if not t.startswith("說明")]
            items += parse_vocab(year, body, key)
            continue
        marks = [(k, int(m.group(1)), int(m.group(2))) for k, b in enumerate(sec)
                 if b["kind"] == "p" and (m := GROUP.search(plain(b["text"])))]
        for j, (k, a, bb) in enumerate(marks):
            end = marks[j + 1][0] if j + 1 < len(marks) else len(sec)
            g, its = parse_group(year, kind, a, bb, sec[k + 1:end], key)
            groups.append(g)
            items += its
    for it in items:
        attach_stats(it, stats, opts)
        if any("圖表" in f for f in it.get("flags", [])):
            if not (IMG / f"{year}-{it['no']}.webp").exists():
                crop_figure(year, it["no"])
            it["image"] = f"img/english/{year}-{it['no']}.webp"
            it["stem"] = ""  # 題目文字已在圖片裡
            it["options"] = {k: "" for k in "ABCD"}
            it.pop("flags")
    items.sort(key=lambda it: it["no"])
    return {"exam": "學測", "year": year, "subject": "english", "paper": "英文",
            "source": {"pdf": pdf_url, "docx": docx_url}, "groups": groups, "items": items}


def check(doc):
    """題號連續、答案齊全、選項數正確。"""
    nos = [it["no"] for it in doc["items"]]
    problems = []
    if nos != list(range(1, len(nos) + 1)):
        problems.append(f"題號不連續：{nos}")
    for it in doc["items"]:
        if not it.get("answer"):
            problems.append(f"{it['id']} 沒有答案")
        elif it["answer"] not in it["options"]:
            problems.append(f"{it['id']} 答案 {it['answer']} 不在選項中")
        if it.get("flags"):
            problems.append(f"{it['id']}：{'；'.join(it['flags'])}")
    return problems


def main():
    lo, hi = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) >= 3 else (110, 115)
    for year in range(lo, hi + 1):
        doc = parse(year)
        out = ROOT / "data" / "questions" / "english" / f"g{year}.yaml"
        qyaml.dump(doc, out)
        print(f"{out.name}: {len(doc['items'])} 題、{len(doc['groups'])} 題組")
        for p in check(doc):
            print("  ⚠", p)


if __name__ == "__main__":
    main()
