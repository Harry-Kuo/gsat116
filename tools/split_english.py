"""學測英文：先抽「詞彙題」（最適合零碎時間快答），合併官方答案與統計，輸出 YAML。

用法：python3 tools/split_english.py 110 115
輸出：data/questions/english/g<年度>.yaml（其他大題之後再擴充）
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import qyaml  # noqa: E402
from ceec_data import answer_key, item_stats, option_stats, paper_file  # noqa: E402
from docx_text import docx_blocks  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def parse_vocab(year):
    path, docx_url = paper_file("english", year, "試題內容", ".docx")
    _, pdf_url = paper_file("english", year, "試題內容", ".pdf")
    blocks = [b for b in docx_blocks(path) if b["kind"] == "p" and b["text"].strip()]
    start = next(i for i, b in enumerate(blocks) if re.search(r"詞彙", b["text"]) and "占" in b["text"])
    m = re.search(r"第\s*(\d+)\s*題至第\s*(\d+)\s*題", blocks[start + 1]["text"])
    first, last = int(m.group(1)), int(m.group(2))
    body = [b["text"].strip() for b in blocks[start + 2:]]
    key = answer_key("english", year)
    stats = item_stats("english", year)
    opts = option_stats("english", year)
    items, i = [], 0
    for no in range(first, last + 1):
        sentence = re.sub(r"^\d+\.\s*", "", body[i])
        sentence = re.sub(r"_{3,}|\s{4,}", " ＿＿＿＿ ", sentence).replace("  ", " ").strip()
        line = body[i + 1]
        if not line.startswith("(A)"):
            line = "(A) " + line
        parts = re.split(r"\(([A-D])\)", line)
        options = {parts[k]: parts[k + 1].strip() for k in range(1, len(parts) - 1, 2)}
        i += 2
        it = {"id": f"eng{year}-{no:02d}", "no": no, "type": "single", "points": 1, "group": None,
              "stem": sentence.replace("______", "＿＿＿＿"), "options": options, "answer": key.get(str(no)),
              "topic": "V", "concepts": ["V1"], "classic": True, "explain": "", "reviewed": False}
        s = stats.get(str(no))
        if s:
            it["stats"] = {k: v for k, v in s.items() if v is not None}
            if opts.get(str(no), {}).get("T"):
                it["stats"]["opt"] = opts[str(no)]["T"]
        if len(options) != 4:
            it["flags"] = [f"選項數 {len(options)}，請對照原卷"]
        items.append(it)
    return {"exam": "學測", "year": year, "subject": "english", "paper": "英文",
            "source": {"pdf": pdf_url, "docx": docx_url}, "groups": [], "items": items}


def main():
    lo, hi = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) >= 3 else (110, 115)
    for year in range(lo, hi + 1):
        doc = parse_vocab(year)
        out = ROOT / "data" / "questions" / "english" / f"g{year}.yaml"
        qyaml.dump(doc, out)
        flags = [it["id"] for it in doc["items"] if it.get("flags")]
        print(f"{out.name}: 詞彙題 {len(doc['items'])} 題，待確認 {flags or '無'}")


if __name__ == "__main__":
    main()
