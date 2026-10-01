"""上線前檢查：答案與官方一致、排程題目都有解析與圖片、觀念代碼有效、題號不重複。

用法：python3 tools/validate.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import qyaml  # noqa: E402
from build import load_overlay  # noqa: E402
from ceec_data import answer_key  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SUBJECTS = ["chinese", "english", "mathA", "mathB", "science", "social"]


def main():
    errors, checked = [], 0
    seen = set()
    items = {}
    for s in SUBJECTS:
        qdir = ROOT / "data" / "questions" / s
        if not qdir.exists():
            continue
        cpath = ROOT / "data" / "concepts" / f"{s}.yaml"
        valid = set()
        if cpath.exists():
            valid = {c["id"] for m in qyaml.load(cpath)["modules"] for c in m["concepts"]}
        overlay = load_overlay(s)
        for path in sorted(qdir.glob("g*.yaml")):
            doc = qyaml.load(path)
            key = answer_key(s, doc["year"])
            for it in doc["items"]:
                if it["id"] in seen:
                    errors.append(f"重複題號 {it['id']}")
                seen.add(it["id"])
                it.update({k: v for k, v in overlay.get(it["id"], {}).items() if k in ("explain", "key", "reference")})
                items[it["id"]] = (s, it)
                official = key.get(str(it["no"]))
                if it["type"] == "fill" and it.get("cells"):  # 舊制選填題：官方答案依列號給
                    official = ",".join(key[c].replace("–", "－").replace("-", "－") for c in it["cells"])
                elif it["type"] == "fill":
                    subs = sorted((k for k in key if k.startswith(f"{it['no']}-")), key=lambda k: int(k.split("-")[1]))
                    official = ",".join(key[k] for k in subs)
                if it["type"] in ("single", "multi", "fill"):
                    checked += 1
                    if (it.get("answer") or "") != (official or ""):
                        errors.append(f"{it['id']} 答案 {it.get('answer')} ≠ 官方 {official}")
                for c in it.get("concepts") or []:
                    if valid and c not in valid:
                        errors.append(f"{it['id']} 觀念代碼 {c} 不存在")
    plan = qyaml.load(ROOT / "data" / "plan" / "days.yaml")
    scheduled = {q for d in plan["days"] for ids in d["sets"].values() for q in ids}
    scheduled |= {q for ids in (plan.get("diag") or {}).values() for q in ids}
    for q in sorted(scheduled):
        if q not in items:
            errors.append(f"排程題目不存在：{q}")
            continue
        s, it = items[q]
        if not (it.get("explain") or it.get("reference")):
            errors.append(f"{q} 沒有解析")
        if it.get("image") and not (ROOT / "docs" / it["image"]).exists():
            errors.append(f"{q} 圖片不存在：{it['image']}")
    for d in plan["days"]:
        for s, ids in d["sets"].items():
            if len(ids) != len(set(ids)):
                errors.append(f"Day {d['day']} {s} 有重複題目")
    print(f"檢查 {checked} 題選擇（填）題答案、{len(scheduled)} 題排程題目")
    if errors:
        print("\n".join("✗ " + e for e in errors))
        sys.exit(1)
    print("✓ 全部通過")


if __name__ == "__main__":
    main()
