"""檢查國文重點整理資料：核心古文的段落數、字詞與名句是否真的出自原文。
用法：python3 tools/check_reference.py"""
import glob
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import qyaml  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "data" / "reference"
VAR = str.maketrans({"于": "於", "嘆": "歎", "鉤": "鈎", "堤": "隄", "間": "閒"})


def han(s):
    return "".join(ch for ch in s.translate(VAR) if "㐀" <= ch <= "鿿")


def main():
    orig = {t["title"]: t for t in qyaml.load(REF / "chinese_core_orig.yaml")}
    bad = 0
    seen = set()
    for f in sorted(glob.glob(str(REF / "chinese_core" / "*.yaml"))):
        n = qyaml.load(f)
        t = orig.get(n["title"])
        if not t:
            print(f"✗ {f}：找不到原文〈{n['title']}〉"); bad += 1; continue
        seen.add(n["title"])
        text = han("".join(t["paras"]))
        if len(n["trans"]) != len(t["paras"]):
            print(f"✗ 〈{n['title']}〉翻譯 {len(n['trans'])} 段、原文 {len(t['paras'])} 段"); bad += 1
        for w in n.get("words") or []:
            term = w.split("：", 1)[0]
            if "：" not in w or han(term) not in text:
                print(f"✗ 〈{n['title']}〉字詞不在原文：{w}"); bad += 1
        for q in n.get("quotes") or []:
            if han(q) not in text:
                print(f"✗ 〈{n['title']}〉名句不在原文：{q}"); bad += 1
        for i in n.get("idioms") or []:
            src = i.split("：", 1)[1] if "：" in i else ""
            parts = [p for p in re.split(r"……", src) if p]
            if not src.startswith(("比喻", "李靖")) and not all(han(p) in text for p in parts):
                print(f"✗ 〈{n['title']}〉成語出處不在原文：{i}"); bad += 1
    # 文言虛詞：例句要出自標示的那一篇，[ ] 裡的字要在例句中
    x = qyaml.load(REF / "chinese_xuci.yaml")
    for w in x["words"]:
        for u in w["uses"]:
            ex, src = u["ex"], u["src"]
            m = re.search(r"\[(.+?)\]", ex)
            if src not in orig or not m or han(ex.replace("[", "").replace("]", "")) not in han("".join(orig[src]["paras"])):
                print(f"✗ 虛詞「{w['word']}」例句不在〈{src}〉：{ex}"); bad += 1
            elif m.group(1) not in w["word"] and not (w["word"].startswith("語氣詞") and m.group(1) in w["word"]):
                print(f"✗ 虛詞「{w['word']}」例句標的字不對：{ex}"); bad += 1
    sys.path.insert(0, str(ROOT / "tools"))
    for q in x.get("exams") or []:
        y = q[3:6]
        items = {it["id"] for it in qyaml.load(ROOT / "data" / "questions" / "chinese" / f"g{y}.yaml")["items"]}
        if q not in items:
            print(f"✗ 虛詞考古題代碼不存在：{q}"); bad += 1
    for title in orig:
        if title not in seen:
            print(f"✗ 〈{title}〉沒有翻譯檔"); bad += 1
    print("國文重點整理：" + ("全部通過 ✓" if not bad else f"{bad} 個問題"))
    return bad + math_patterns()


def math_patterns():
    """數學經典題型：觀念與題型組別要對得上，每一型欄位齊全，考過的題目代碼要存在。"""
    import json
    d = qyaml.load(REF / "math_patterns.yaml")
    links = json.loads((ROOT / "notion" / "notion_map.json").read_text(encoding="utf-8"))
    ids = {it["id"] for subj in ("mathA", "mathB")
           for f in sorted((ROOT / "data" / "questions" / subj).glob("g*.yaml")) for it in qyaml.load(f)["items"]}
    bad = 0
    for subj, cmap in d["concepts"].items():
        cids = {c["id"] for m in qyaml.load(ROOT / "data" / "concepts" / f"{subj}.yaml")["modules"] for c in m["concepts"]}
        for cid, gids in cmap.items():
            if cid not in cids:
                print(f"✗ 經典題型：{subj} 沒有觀念 {cid}"); bad += 1
            for g in gids:
                if g not in d["groups"]:
                    print(f"✗ 經典題型：{subj} {cid} 的組別 {g} 不存在"); bad += 1
    n = 0
    for gid, g in d["groups"].items():
        for p in g["items"]:
            n += 1
            where = f"{gid}「{p.get('name')}」"
            if not all(p.get(k) for k in ("name", "cue", "how")):
                print(f"✗ 經典題型 {where} 缺少 name、cue 或 how"); bad += 1
            if bool(p.get("ex")) != bool(p.get("sol")):
                print(f"✗ 經典題型 {where} 例題和解答要一起寫"); bad += 1
            if p.get("only") not in (None, "mathA", "mathB"):
                print(f"✗ 經典題型 {where} only 只能是 mathA 或 mathB"); bad += 1
            for q in p.get("qs") or []:
                if q not in ids:
                    print(f"✗ 經典題型 {where} 的題目代碼不存在：{q}"); bad += 1
                elif not links.get(f"q:{q}"):
                    print(f"△ 經典題型 {where} 的 {q} 還沒放進考古題庫，Notion 不會列出")
    print(f"數學經典題型（{n} 型）：" + ("全部通過 ✓" if not bad else f"{bad} 個問題"))
    return bad


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
