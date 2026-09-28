"""抓大考中心「學測歷屆試題」清單（85–115 年），只記錄檔案連結、不下載，存到 data/stats/past_exams.json。

用法：python3 tools/past_exams.py [起始年 結束年]   預設 85 115
給 notion_md.py 產生「歷屆考古題總覽」頁使用。
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_ceec import exam_rows  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "stats" / "past_exams.json"


def main():
    lo, hi = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (85, 115)
    rows = exam_rows(set(range(lo, hi + 1)))
    out = []
    for r in rows:
        m = re.match(r"(\d+)學年度學科能力測驗\s*[－-]\s*(.+)", r["title"])
        if not m:
            continue
        out.append({"year": int(m.group(1)), "subject": m.group(2).strip(),
                    "files": [{"label": f["label"], "title": f["title"], "url": f["url"]} for f in r["files"]]})
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(out)} 筆，{min(o['year'] for o in out)}–{max(o['year'] for o in out)} 年 → {OUT}")


if __name__ == "__main__":
    main()
