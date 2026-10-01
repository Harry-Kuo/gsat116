"""把 data/concepts/<科目>_tags.yaml 的分類寫進題庫 YAML（topic、tags、concepts、classic）。

用法：python3 tools/apply_tags.py chinese
經典必考（classic）規則：非選題不進快答主線；官方鑑別度 D < 10 視為低鑑別，不列入主線（仍保留在題庫）。
舊課綱（110 年）超出 108 課綱範圍的題目，在 _tags.yaml 寫成 {topic: M9, tags: [], out: 理由}，同樣不進主線。
109、110 年學測數學只有一份試卷，數A、數B 題庫各存一份；每題只排在一科，另一科寫成 {topic: B1, tags: [], dup: mathA}。
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import qyaml  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def concept_ids(topic, tags, concepts_doc):
    ids = [topic]
    for mod in concepts_doc["modules"]:
        for c in mod["concepts"]:
            m = c.get("match") or {}
            if "tag" in m and m["tag"] in tags:
                ids.append(c["id"])
            if "tag_prefix" in m and any(t.startswith(m["tag_prefix"]) for t in tags):
                ids.append(c["id"])
    return list(dict.fromkeys(ids))


def main(subject):
    tags_map = qyaml.load(ROOT / "data" / "concepts" / f"{subject}_tags.yaml")
    concepts_doc = qyaml.load(ROOT / "data" / "concepts" / f"{subject}.yaml")
    valid = {c["id"] for m in concepts_doc["modules"] for c in m["concepts"]}
    for path in sorted((ROOT / "data" / "questions" / subject).glob("g*.yaml")):
        doc = qyaml.load(path)
        for it in doc["items"]:
            entry = tags_map.get(it["id"])
            out_note = dup = None
            if isinstance(entry, dict):
                out_note, dup = entry.get("out"), entry.get("dup")
                entry = [entry["topic"], *(entry.get("tags") or [])]
            if entry:
                topic, tags = entry[0], entry[1:]
                assert topic in valid, (it["id"], topic)
                it["topic"] = topic
                it["tags"] = tags
                # 標籤裡若也是觀念代碼（例如數學一題跨兩個觀念），一併列入
                it["concepts"] = list(dict.fromkeys(concept_ids(topic, tags, concepts_doc) + [t for t in tags if t in valid]))
            elif subject == "chinese":
                print("未分類：", it["id"])
            d = (it.get("stats") or {}).get("D")
            if out_note:
                it["classic"] = False
                it["classic_note"] = f"108 課綱範圍外：{out_note}"
            elif dup:
                it["classic"] = False
                it["classic_note"] = f"{it['id'][2:5]} 年學測數學只有一份試卷，這題排在{ {'mathA': '數學A', 'mathB': '數學B'}[dup] }的練習"
            elif it["type"] == "open":
                it["classic"] = False
                it["classic_note"] = "非選題：放在課堂與 Notion 練習，不進快答主線"
            elif d is not None and d < 10:
                it["classic"] = False
                it["classic_note"] = f"官方鑑別度 D={d}，低鑑別題不進主線"
            else:
                it["classic"] = True
                it.pop("classic_note", None)
        # 欄位順序整理：把分類欄位放在 answer 後面
        order = ["id", "no", "type", "points", "group", "stem", "options", "answer", "topic", "tags", "concepts",
                 "classic", "classic_note", "stats", "explain", "key", "reviewed", "flags"]
        doc["items"] = [{k: it[k] for k in order if k in it} | {k: v for k, v in it.items() if k not in order}
                        for it in doc["items"]]
        qyaml.dump(doc, path)
        n = sum(1 for it in doc["items"] if it.get("classic"))
        print(f"{path.name}: 經典主線 {n}/{len(doc['items'])}")


if __name__ == "__main__":
    main(sys.argv[1])
