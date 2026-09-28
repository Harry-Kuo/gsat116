"""計算各科「近六屆經典題」題池大小（依官方答案與答對率表，不需先抽題）。

規則：選擇題與選填題（非選不列入快答）、官方鑑別度 D ≥ 10。
輸出：data/stats/pools.json  {科目: {年度: 題數, "total": 合計}}
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ceec_data import answer_key, item_stats  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SUBJECTS = ["chinese", "english", "mathA", "mathB", "science", "social"]


def main(lo=110, hi=115):
    out = {}
    for s in SUBJECTS:
        out[s] = {}
        for y in range(lo, hi + 1):
            try:
                key = answer_key(s, y)
                stats = item_stats(s, y)
            except Exception as e:  # noqa: BLE001
                print("略過", s, y, e)
                continue
            nos = {k.split("-")[0] for k, v in key.items() if v != "／"}
            n = sum(1 for no in nos if (stats.get(no) or {}).get("D") is None or stats[no]["D"] >= 10)
            out[s][str(y)] = n
        out[s]["total"] = sum(v for k, v in out[s].items() if k != "total")
    path = ROOT / "data" / "stats" / "pools.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    for s, v in out.items():
        print(s, v)


if __name__ == "__main__":
    main()
