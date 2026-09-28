"""出題趨勢統計：題型配分、觀念分布、文言比例、核心選文命中、各觀念答對率/鑑別度。

用法：python3 tools/trends.py chinese   → 輸出 notion/<科目>_trends.md 與 data/stats/<科目>_trends.json
"""
import json
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import qyaml  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TYPE_NAME = {"single": "單選", "multi": "多選", "open": "非選", "fill": "選填"}


def load(subject):
    docs = [qyaml.load(p) for p in sorted((ROOT / "data" / "questions" / subject).glob("g*.yaml"))]
    concepts = qyaml.load(ROOT / "data" / "concepts" / f"{subject}.yaml")
    names = {c["id"]: c["name"] for m in concepts["modules"] for c in m["concepts"]}
    modules = {c["id"]: m["name"] for m in concepts["modules"] for c in m["concepts"]}
    return docs, names, modules


def main(subject):
    docs, names, modules = load(subject)
    years = [d["year"] for d in docs]
    out = {"years": years, "structure": {}, "module_points": {}, "topic_count": defaultdict(dict),
           "classical_share": {}, "core_hits": {}, "topic_quality": {}}
    all_items = []
    for d in docs:
        y = d["year"]
        items = d["items"]
        all_items += [(y, it) for it in items]
        by_type = Counter()
        pts_type = Counter()
        for it in items:
            by_type[it["type"]] += 1
            pts_type[it["type"]] += it["points"]
        out["structure"][y] = {TYPE_NAME[t]: f"{by_type[t]} 題／{pts_type[t]} 分" for t in by_type}
        mod_pts = Counter()
        for it in items:
            mod_pts[modules[it["topic"]]] += it["points"]
            out["topic_count"][it["topic"]][y] = out["topic_count"][it["topic"]].get(y, 0) + 1
        out["module_points"][y] = dict(mod_pts)
        cls = sum(it["points"] for it in items if {"文言", "韻文"} & set(it.get("tags") or []))
        total = sum(it["points"] for it in items)
        out["classical_share"][y] = round(100 * cls / total)
        hits = Counter(t.split(":", 1)[1] for it in items for t in (it.get("tags") or []) if t.startswith("核心:"))
        out["core_hits"][y] = dict(hits)
    for topic in names:
        ps = [it["stats"]["P"] for _, it in all_items if it["topic"] == topic and it.get("stats", {}).get("P") is not None]
        ds = [it["stats"]["D"] for _, it in all_items if it["topic"] == topic and it.get("stats", {}).get("D") is not None]
        if ps:
            out["topic_quality"][topic] = {"n": len(ps), "P": round(statistics.mean(ps)), "D": round(statistics.mean(ds))}

    (ROOT / "data" / "stats").mkdir(parents=True, exist_ok=True)
    (ROOT / "data" / "stats" / f"{subject}_trends.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1, default=dict), encoding="utf-8")

    # ---- Markdown ----
    md = []
    md.append("### 題型與配分\n")
    md.append("| 年度 | " + " | ".join(["單選", "多選", "非選"]) + " |")
    md.append("|---|---|---|---|")
    for y in years:
        s = out["structure"][y]
        md.append(f"| {y} | " + " | ".join(s.get(k, "—") for k in ["單選", "多選", "非選"]) + " |")
    md.append("\n### 各模組配分（分）\n")
    mods = ["語文知識", "國學與文化常識", "閱讀理解", "混合題"]
    md.append("| 年度 | " + " | ".join(mods) + " | 文言與韻文占比 |")
    md.append("|---|" + "---|" * (len(mods) + 1))
    for y in years:
        mp = out["module_points"][y]
        md.append(f"| {y} | " + " | ".join(str(mp.get(m, 0)) for m in mods) + f" | {out['classical_share'][y]}% |")
    md.append("\n### 各觀念出題次數與全國表現（110–115 合計）\n")
    md.append("| 觀念 | " + " | ".join(str(y) for y in years) + " | 合計 | 平均答對率 | 平均鑑別度 |")
    md.append("|---|" + "---|" * (len(years) + 3))
    for topic, name in names.items():
        row = out["topic_count"].get(topic, {})
        if not row:
            continue
        q = out["topic_quality"].get(topic, {})
        md.append(f"| {topic} {name} | " + " | ".join(str(row.get(y, 0)) for y in years)
                  + f" | {sum(row.values())} | {q.get('P', '—')}% | {q.get('D', '—')} |")
    md.append("\n### 15 篇核心選文被引用次數\n")
    total_hits = Counter()
    for y in years:
        total_hits.update(out["core_hits"][y])
    md.append("| 篇名 | " + " | ".join(str(y) for y in years) + " | 合計 |")
    md.append("|---|" + "---|" * (len(years) + 1))
    for name, n in total_hits.most_common():
        md.append(f"| {name} | " + " | ".join(str(out['core_hits'][y].get(name, 0)) for y in years) + f" | {n} |")
    path = ROOT / "notion" / f"{subject}_trends.md"
    path.parent.mkdir(exist_ok=True)
    path.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main(sys.argv[1])
