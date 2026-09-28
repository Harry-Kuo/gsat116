"""把數學、自然、社會等含公式或圖表的試題，依題號從原卷 PDF 裁成圖片，並建立題庫 YAML。

用法：python3 tools/extract_images.py <科目> <年度> [--force]
輸出：docs/img/<科目>/<年度>-<題號>.webp（題組文章為 <年度>-g<起始題號>.webp）
      data/questions/<科目>/g<年度>.yaml（題型、配分、答案、官方統計、圖片路徑、題目文字）
"""
import io
import re
import sys
from pathlib import Path

import fitz
from PIL import Image, ImageChops

sys.path.insert(0, str(Path(__file__).resolve().parent))
import qyaml  # noqa: E402
from ceec_data import answer_key, item_stats, option_stats, paper_file  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
groups_stop = []
PREFIX = {"mathA": "ma", "mathB": "mb", "science": "sci", "social": "soc", "english": "eng"}
DPI = 170
TOP, BOTTOM = 52, 50  # 頁首、頁尾（pt）


def page_bounds(page):
    """依頁首（年度、考科、頁碼、簽名提醒）與頁尾頁碼決定內容的上下界。"""
    top, bottom = 40, page.rect.height - 40
    for b in page.get_text("dict")["blocks"]:
        for line in b.get("lines", []):
            t = "".join(s["text"] for s in line["spans"]).strip()
            y0, y1 = line["bbox"][1], line["bbox"][3]
            if y1 < 110 and re.search(r"學測|考科|頁|簽名|能力測驗", t):
                top = max(top, y1 + 2)
            if y0 > page.rect.height - 70 and re.fullmatch(r"[-－–\s\d]+|第\s*\d+\s*頁.*|.*共\s*\d+\s*頁", t):
                bottom = min(bottom, y0 - 2)
    return top, bottom


def occupied(page, top, bottom):
    """內容所占的垂直區間（文字行、圖形、圖片），用來找題目之間的空白。"""
    spans = []
    for b in page.get_text("dict")["blocks"]:
        if b.get("type") == 1:
            spans.append((b["bbox"][1], b["bbox"][3]))
        for line in b.get("lines", []):
            spans.append((line["bbox"][1], line["bbox"][3]))
    for d in page.get_drawings():
        r = d.get("rect")
        if r is not None and r.height < page.rect.height * 0.9:
            spans.append((r.y0, r.y1))
    spans = sorted((max(top, a), min(bottom, z)) for a, z in spans if z > top and a < bottom)
    merged = []
    for a, z in spans:
        if merged and a <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], z))
        else:
            merged.append((a, z))
    return merged


def cut_between(occ, ya, yb):
    """在 ya（本題開頭）與 yb（下一題題號行）之間，找最大的空白帶，回傳切割位置。"""
    blocks = [(a, z) for a, z in occ if z > ya + 1 and a < yb]
    best, cut = -1, yb - 2
    for (a1, z1), (a2, z2) in zip(blocks, blocks[1:]):
        gap = a2 - z1
        if gap > best and z1 >= ya:
            best, cut = gap, (z1 + a2) / 2
    return cut


def question_starts(doc):
    """找出每題開頭的位置：左側的「數字.」。回傳 [(題號, 頁, y0)] 與題組標題位置。"""
    starts, groups = [], []
    global groups_stop
    groups_stop = []
    for pno, page in enumerate(doc):
        width = page.rect.width
        for b in page.get_text("dict")["blocks"]:
            for line in b.get("lines", []):
                text = "".join(s["text"] for s in line["spans"]).strip()
                x0, y0 = line["bbox"][0], line["bbox"][1]
                top, bottom = page_bounds(page) if not hasattr(page, "_b") else page._b
                if y0 < top or y0 > bottom:
                    continue
                m = re.match(r"^(\d{1,2})\s*[.．]", text)
                if m and x0 < width * 0.2:
                    starts.append((int(m.group(1)), pno, y0))
                if x0 < width * 0.2 and re.match(r"^(第[壹貳參肆]部分|[一二三四五六]、\S{1,8}（占|說明：)", text):
                    groups_stop.append((pno, y0))
                g = re.match(r"^(\d{1,2})\s*[-–]\s*(\d{1,2})\s*題?\s*為題組", text)
                if g and x0 < width * 0.2:
                    groups.append((int(g.group(1)), int(g.group(2)), pno, y0))
    # 只保留遞增的題號序列（排除文章中的編號）
    seq, expect = [], 1
    for no, pno, y in sorted(starts, key=lambda t: (t[1], t[2])):
        if no == expect:
            seq.append((no, pno, y))
            expect += 1
    return seq, groups


def trim(img, pad=12):
    bg = Image.new(img.mode, img.size, (255, 255, 255))
    box = ImageChops.difference(img, bg).convert("L").point(lambda v: 255 if v > 18 else 0).getbbox()
    if not box:
        return None
    l, t, r, b = box
    return img.crop((max(0, l - pad), max(0, t - pad), min(img.width, r + pad), min(img.height, b + pad)))


def render(doc, pieces):
    """pieces：[(頁, y0, y1)]，裁切後上下拼接。"""
    imgs = []
    for pno, y0, y1 in pieces:
        page = doc[pno]
        clip = fitz.Rect(0, y0 - 5, page.rect.width, y1 + 1)
        if clip.height < 8:
            continue
        pix = page.get_pixmap(dpi=DPI, clip=clip)
        piece = trim(Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB"))
        if piece is not None:
            imgs.append(piece)
    if not imgs:
        return None
    w = max(i.width for i in imgs)
    out = Image.new("RGB", (w, sum(i.height for i in imgs)), (255, 255, 255))
    y = 0
    for i in imgs:
        out.paste(i, (0, y))
        y += i.height
    return out


def region(doc, bounds, occs, start, stop):
    """從 start=(頁, y) 到 stop=(頁, y) 的題目範圍，依空白帶決定切點，可跨頁。"""
    (pno, y0), (epno, ey) = start, stop
    pieces = []
    for p in range(pno, epno + 1):
        top, bottom = bounds[p]
        a = y0 if p == pno else top
        if p == epno:
            # 直接切在下一題（已含題號上方的公式）的上緣；題目之間常常沒有明顯空白
            z = max(a, ey - 1)
        else:
            z = bottom
        pieces.append((p, a, z))
    return pieces


MATH = False


def next_start_top(page, y_line, floor=0):
    """題目真正的上緣。數學題的矩陣、分數常高出題號行，把題號右側、緊貼在上方的公式也算進來；
    其他科直接用題號行。"""
    if not MATH or page is None:
        return y_line
    floor = max(floor, page_bounds(page)[0])
    top = y_line
    boxes = [line["bbox"] for b in page.get_text("dict")["blocks"] for line in b.get("lines", [])]
    boxes += [tuple(d["rect"]) for d in page.get_drawings() if d.get("rect") is not None and d["rect"].height < 40]
    for x0, y0, _, y1 in boxes:
        if y_line - 20 <= y1 <= y_line + 4 and x0 > 150 and y0 > floor and y0 < y_line:
            top = min(top, y0)
    return top


def region_text(doc, pieces):
    parts = []
    for pno, y0, y1 in pieces:
        parts.append(doc[pno].get_text(clip=fitz.Rect(0, y0 - 2, doc[pno].rect.width, y1)))
    return re.sub(r"[ \t]+\n", "\n", "\n".join(parts)).strip()


def main():
    global MATH
    subject, year = sys.argv[1], int(sys.argv[2])
    force = "--force" in sys.argv
    MATH = subject.startswith("math")
    pdf, pdf_url = paper_file(subject, year, "試題內容", ".pdf")
    doc = fitz.open(pdf)
    seq, groups = question_starts(doc)
    key = answer_key(subject, year)
    stats = item_stats(subject, year)
    opts = option_stats(subject, year)
    img_dir = ROOT / "docs" / "img" / subject
    img_dir.mkdir(parents=True, exist_ok=True)
    pre = PREFIX[subject]

    bounds = [page_bounds(pg) for pg in doc]
    occs = [occupied(pg, *bounds[i]) for i, pg in enumerate(doc)]
    items, gout = [], []
    heads = sorted([(n, p, y) for n, p, y in seq] + [(g[0] - 0.5, g[2], g[3]) for g in groups]
                   + [(0, p, y) for p, y in groups_stop], key=lambda t: (t[1], t[2]))
    for idx, (no, pno, y0) in enumerate(seq):
        later = [h for h in heads if (h[1], h[2]) > (pno, y0)]
        if later:
            _, np_, ny = later[0]
            nt = next_start_top(doc[np_], ny, y0 + 12 if np_ == pno else 0)
            stop = (np_, nt - 7 if nt < ny else nt)  # 下一題上方有公式時多留一點空隙
        else:
            stop = (len(doc) - 1, bounds[-1][1])
        prev_same = [t for t in seq[:idx] if t[1] == pno]
        my_top = next_start_top(doc[pno], y0, prev_same[-1][2] + 12 if prev_same else 0)
        pieces = region(doc, bounds, occs, (pno, my_top), stop)
        img = render(doc, pieces)
        name = f"{year}-{no:02d}.webp"
        if img is not None and (force or not (img_dir / name).exists()):
            img.save(img_dir / name, "WEBP", quality=82, method=6)
        text = region_text(doc, pieces)
        # 題型
        sub_keys = [k for k in key if k.startswith(f"{no}-")]
        ans = key.get(str(no))
        if sub_keys:
            typ, answer = "fill", ",".join(key[k] for k in sorted(sub_keys, key=lambda k: int(k.split("-")[1])))
        elif ans in (None, "／"):
            typ, answer = "open", None
        else:
            typ = "multi" if (len(ans.replace(",", "")) > 1) or "多選" in text[:80] else "single"
            answer = ans
        if subject.startswith("math"):
            options = {str(i): "" for i in range(1, 6)} if typ in ("single", "multi") else None
        else:
            letters = [c for c in "ABCDE" if f"({c})" in text]
            options = {c: "" for c in (letters or list("ABCD"))} if typ in ("single", "multi") else None
        grp = next((g for g in groups if g[0] <= no <= g[1]), None)
        it = {
            "id": f"{pre}{year}-{no:02d}", "no": no, "type": typ, "points": None,
            "group": f"{pre}{year}-g{grp[0]:02d}" if grp else None,
            "image": f"img/{subject}/{name}", "stem": "", "options": options, "answer": answer,
            "text": text,
        }
        s_ = stats.get(str(no)) or {}
        if s_:
            it["stats"] = {k: v for k, v in s_.items() if v is not None}
            o = opts.get(str(no), {}).get("T")
            if o:
                it["stats"]["opt"] = o
        items.append(it)

    # 題組文章圖：從「a-b為題組」到第 a 題題號前
    for g in groups:
        a, z, gp, gy = g
        first = next((i for i, t in enumerate(seq) if t[0] == a), None)
        if first is None:
            continue
        fp, fy = seq[first][1], seq[first][2]
        pieces = region(doc, bounds, occs, (gp, gy), (fp, next_start_top(doc[fp], fy)))
        img = render(doc, pieces)
        name = f"{year}-g{a:02d}.webp"
        if img is not None and (force or not (img_dir / name).exists()):
            img.save(img_dir / name, "WEBP", quality=82, method=6)
        gout.append({"id": f"{pre}{year}-g{a:02d}", "range": [a, z], "intro": f"閱讀下文，回答{a}-{z}題。",
                     "image": f"img/{subject}/{name}", "passage": region_text(doc, pieces)})

    # 配分與題型：從「單選題／多選題」標題後的「說明：第a題至第b題…每題c分」推得
    full = "\n".join(p.get_text() for p in doc)
    for kind, typ in (("單選題", "single"), ("多選題", "multi")):
        for m in re.finditer(kind + r"[^\n]*\n+\s*說明[:：]\s*第\s*(\d+)\s*題至第\s*(\d+)\s*題", full):
            for it in items:
                if int(m.group(1)) <= it["no"] <= int(m.group(2)) and it["type"] in ("single", "multi"):
                    it["type"] = typ
    for m in re.finditer(r"第\s*(\d+)\s*題至第\s*(\d+)\s*題[^。]*?每題\s*(\d+)\s*分", full):
        for it in items:
            if int(m.group(1)) <= it["no"] <= int(m.group(2)):
                it["points"] = int(m.group(3))
    for it in items:
        if it["points"] is None:
            m = re.search(r"占\s*(\d+)\s*分", it["text"])
            it["points"] = int(m.group(1)) if m else 2
        it.update({"topic": None, "concepts": [], "classic": None, "explain": "", "reviewed": False})

    out = ROOT / "data" / "questions" / subject / f"g{year}.yaml"
    doc_out = {"exam": "學測", "year": year, "subject": subject, "source": {"pdf": pdf_url},
               "groups": gout, "items": items}
    found = [i["no"] for i in items]
    expected = max(int(k.split("-")[0]) for k in key)
    missing = [n for n in range(1, expected + 1) if n not in found]
    if missing:
        doc_out["missing"] = missing
    qyaml.dump(doc_out, out)
    print(f"{out.relative_to(ROOT)}：{len(items)} 題、{len(gout)} 題組、缺 {missing or '無'}")


if __name__ == "__main__":
    main()
