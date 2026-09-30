"""大考中心《高中英文參考詞彙表（111 學年度起適用）》：單字 → (詞性, 級別)。

來源 PDF 放在 data/ceec/ref/english_wordlist_111.pdf（不進 repo；下載網址見 URL）。
著作權屬大考中心基金會，僅供非營利使用並註明出處；這裡只用來標出考題單字的級別。
"""
import re
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "data" / "ceec" / "ref" / "english_wordlist_111.pdf"
URL = ("https://www.ceec.edu.tw/files/file_pool/1/0k213571061045122620/"
       "%e9%ab%98%e4%b8%ad%e8%8b%b1%e6%96%87%e5%8f%83%e8%80%83%e8%a9%9e%e5%bd%99%e8%a1%a8"
       "%28111%e5%ad%b8%e5%b9%b4%e5%ba%a6%e8%b5%b7%e9%81%a9%e7%94%a8%29.pdf")
POS = r"(?:\(?(?:n|v|adj|adv|prep|conj|pron|art|aux|int|interj|det|num)\.\)?)"
LINE = re.compile(rf"^(?P<w>[A-Za-z][A-Za-z()' ,/.\-]*?)\s+(?P<pos>{POS}(?:/{POS})*)\s+(?P<lv>[1-6])$")


def _forms(head):
    """refine(ment) → refine, refinement；wood(s) → wood, woods；toward/towards → 兩個都收。"""
    out = set()
    for part in head.split("/"):
        part = part.strip()
        m = re.fullmatch(r"([A-Za-z' .\-]+)\(([a-z]+)\)", part)
        if m:
            out |= {m.group(1).strip(), (m.group(1) + m.group(2)).strip()}
        elif re.fullmatch(r"[A-Za-z' .\-]+", part):
            out.add(part.strip())
    return {w.lower() for w in out if w}


@lru_cache(maxsize=None)
def table():
    import fitz
    doc = fitz.open(PDF)
    start = next(i for i, p in enumerate(doc) if "依字母排序" in p.get_text() and re.search(r"\n[a-z]+ (?:n|v|adj)\.", p.get_text()))
    words, pending = {}, ""
    for p in doc[start:]:
        for raw in p.get_text().split("\n"):
            line = raw.strip()
            if not line or line in ("依字母排序",) or re.fullmatch(r"[A-Z]|\d+", line):
                continue
            if pending:
                line = pending + " " + line
            m = LINE.match(line)
            if m:
                for w in _forms(m.group("w")):
                    words.setdefault(w, (m.group("pos"), int(m.group("lv"))))
                pending = ""
            elif re.match(r"^[a-z]", line) and len(line) < 40 and not re.search(r"\d$", line):
                pending = line  # 詞條跨行，例如 you (your, yours, ...)
            else:
                pending = ""
    return words


IRREGULAR = {"brought": "bring", "made": "make", "taken": "take", "took": "take", "gave": "give", "given": "give",
             "went": "go", "gone": "go", "came": "come", "held": "hold", "kept": "keep", "left": "leave", "led": "lead",
             "sprang": "spring", "sprung": "spring", "fell": "fall", "fallen": "fall", "found": "find", "grew": "grow",
             "grown": "grow", "shrunk": "shrink", "shrank": "shrink", "struck": "strike", "stood": "stand", "sought": "seek"}


def _stems(w):
    """(候選原形, 需要的詞性)：-ed/-ing 要是動詞，-s 可以是名詞或動詞。"""
    out = []
    if w in IRREGULAR:
        out.append((IRREGULAR[w], None))
    if w.endswith("ied"):
        out.append((w[:-3] + "y", "v."))
    if w.endswith("ed"):
        out += [(w[:-1], "v."), (w[:-2], "v."), (w[:-3], "v.")]  # noted→note、halted→halt、stopped→stop
    if w.endswith("ing"):
        out += [(w[:-3], "v."), (w[:-3] + "e", "v."), (w[:-4], "v.")]  # bearing→bear、taking→take、running→run
    if w.endswith("ies"):
        out.append((w[:-3] + "y", None))
    if w.endswith("es"):
        out.append((w[:-2], None))
    if w.endswith("s"):
        out.append((w[:-1], None))
    return out


def level(word):
    """回傳 (詞性, 級別)；片語查第一個字（point to → point），變化形去掉字尾查原形。找不到回傳 None。"""
    t = table()
    w = word.lower().strip()
    if " " in w and w not in t:
        w = w.split()[0]
    if w in t:
        return t[w]
    for stem, pos in _stems(w):
        if stem in t and (pos is None or pos in t[stem][0]):
            return t[stem]
    return None


if __name__ == "__main__":
    t = table()
    from collections import Counter
    print(len(t), "個字形", Counter(v[1] for v in t.values()))
    for w in ["tight", "amateur", "vacancy", "dreads", "assaulted", "elbow", "grave", "tumbled", "kits", "resumed", "choked", "supposedly"]:
        print(w, level(w))
