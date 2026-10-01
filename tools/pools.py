"""計算各科「近六屆經典題」題池大小（依官方答案與答對率表，不需先抽題）。

規則：選擇題與選填題（非選不列入快答）、官方鑑別度 D ≥ 10；英文混合題不列入；110 年數學另扣除 108 課綱範圍外的題目。
輸出：data/stats/pools.json  {科目: {年度: 題數, "total": 合計}}
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import qyaml  # noqa: E402
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
            if s == "english" and y >= 111:
                # 英文 111 年起第 47–50 題是混合題，和非選一樣不進快答（第 49 題雖是選擇題也不列入）
                nos = {no for no in nos if int(no) < 47}
            n = sum(1 for no in nos if (stats.get(no) or {}).get("D") is None or stats[no]["D"] >= 10)
            bank = ROOT / "data" / "questions" / s / f"g{y}.yaml"
            if s.startswith("math") and y in (109, 110) and bank.exists():
                # 110 年是舊課綱的數學卷：選填題答案依列號給（不能用來數題數），且要扣掉 108 課綱範圍外的題目
                n = sum(1 for it in qyaml.load(bank)["items"] if it.get("classic"))
            out[s][str(y)] = n
        out[s]["total"] = sum(v for k, v in out[s].items() if k != "total")
    path = ROOT / "data" / "stats" / "pools.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    for s, v in out.items():
        print(s, v)


if __name__ == "__main__":
    main()
