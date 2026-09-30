"""產生網站資料：docs/data/{config,schedule,concepts}.json 與 docs/data/bank/<科目>.json。

用法：python3 tools/build.py [--strict] [--backend=mock]
  --strict：排程中的題目缺解析就失敗（正式發布前使用）
  --backend=mock：本機測試用假後端（不寫入 config.yaml）
"""
import datetime as dt
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import qyaml  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "docs" / "data"
PAPER_NAME = {"chinese": {110: "國文", "default": "國綜"}, "english": "英文", "mathA": {110: "數學", "default": "數學A"},
              "mathB": {110: "數學", "default": "數學B"}, "social": "社會", "science": "自然"}
# 屬性必須是 name="值" 的形式，避免把數學的「a<b ⇒ t>1」誤認成 <b> 標籤
ALLOWED = r"""</?(?:u|em|sup|sub|br|b|i|table|tbody|tr|td|th|span|div|p|ruby|rt)(?:\s+[A-Za-z-]+(?:=(?:"[^"]*"|'[^']*'|[^\s"'<>]+))?)*\s*/?>"""


def paper_name(subject, year):
    v = PAPER_NAME[subject]
    return v.get(year, v["default"]) if isinstance(v, dict) else v


def safe_inline(s):
    """保留允許的標籤，其餘 < > & 轉義。"""
    out, pos = [], 0
    for m in re.finditer(ALLOWED, s):
        out.append(html.escape(s[pos:m.start()], quote=False))
        out.append(m.group(0))
        pos = m.end()
    out.append(html.escape(s[pos:], quote=False))
    return "".join(out).replace("［圖］", '<span class="fig">［附圖請見原卷］</span>')


def to_html(text):
    if not text:
        return ""
    parts = []
    for line in str(text).split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("【框】"):
            parts.append(f'<div class="box">{safe_inline(line[3:])}</div>')
        elif line.startswith("<table"):
            parts.append(f'<div class="tbl">{safe_inline(line)}</div>')
        elif line.startswith("<img"):
            parts.append(line)
        else:
            parts.append(f"<p>{safe_inline(line)}</p>")
    return "".join(parts)


def plain_len(s):
    return len(re.sub(r"<[^>]+>", "", s or ""))


IMAGE_SECONDS = {"mathA": {"single": 150, "multi": 180, "fill": 180}, "mathB": {"single": 150, "multi": 180, "fill": 180},
                 "science": {"single": 70, "multi": 100}, "social": {"single": 60, "multi": 90}}


def est_seconds(item, group, subject=None):
    """預估作答秒數：短題約 30–60 秒；題組文章另計閱讀時間（約每秒 8 字）；圖片題依科目估計。"""
    if item.get("image"):
        return IMAGE_SECONDS.get(subject, {}).get(item["type"], 90)
    n = plain_len(item.get("stem")) + sum(plain_len(v) for v in (item.get("options") or {}).values())
    base = {"single": 25, "multi": 40, "fill": 90, "open": 150}.get(item["type"], 30)
    sec = base + n / 9
    return int(round(sec / 5) * 5)


def load_overlay(subject):
    """人工撰寫的內容（解析、重點、題幹修正）放在 data/explain/<科目>*.yaml，與自動抽題的題庫分開保存。"""
    ov = {}
    for path in sorted((DATA / "explain").glob(f"{subject}*.yaml")):
        for k, v in (qyaml.load(path) or {}).items():
            ov.setdefault(k, {}).update(v or {})
    return ov


def load_subject(subject):
    bank = {}
    groups = {}
    overlay = load_overlay(subject)
    for path in sorted((DATA / "questions" / subject).glob("g*.yaml")):
        doc = qyaml.load(path)
        src_url = (doc.get("source") or {}).get("pdf")
        for g in doc.get("groups") or []:
            if g["id"] in overlay and overlay[g["id"]].get("passage"):
                g["passage"] = overlay[g["id"]]["passage"]
            html = to_html(g.get("passage"))
            if g.get("image"):
                # 數學、自然、社會的題組文章以原卷裁切圖呈現（抽出的文字含公式與圖表標籤，無法直接閱讀）
                img = f'<img class="qimg" src="{g["image"]}" alt="題組文章與圖表" loading="lazy">'
                html = img if subject in IMAGE_SECONDS else html + img
            groups[g["id"]] = {"id": g["id"], "range": g["range"], "intro": g.get("intro", ""),
                               "html": html, "read": int(plain_len(g.get("passage")) / 8)}
        for it in doc["items"]:
            for field in ("explain", "key", "reference", "stem", "options", "image"):
                if field in overlay.get(it["id"], {}):
                    it[field] = overlay[it["id"]][field]
            it["_year"] = doc["year"]
            it["_url"] = src_url
            bank[it["id"]] = it
    return bank, groups


def item_json(subject, it, groups, concept_summary):
    g = groups.get(it.get("group")) if it.get("group") else None
    stats = it.get("stats") or {}
    j = {
        "id": it["id"], "s": subject, "y": it["_year"], "no": it["no"],
        "src": f"{it['_year']}學測{paper_name(subject, it['_year'])} 第{it['no']}題",
        "t": it["type"], "p": it["points"], "g": it.get("group"),
        "stem": to_html(it.get("stem")),
        "o": [[k, to_html(v)] for k, v in (it.get("options") or {}).items()],
        "a": it.get("answer"),
        "ex": to_html(it.get("explain")),
        "k": it.get("key") or concept_summary.get(it.get("topic"), ""),
        "c": it.get("concepts") or [],
        "est": est_seconds(it, g, subject),
        "url": it["_url"],
    }
    if it.get("image"):
        j["img"] = it["image"]
    if it["type"] == "open":
        j["ref"] = to_html(it.get("reference"))
    for k in ("P", "D", "T"):
        if stats.get(k) is not None:
            j[k] = stats[k]
    if stats.get("opt"):
        j["op"] = stats["opt"]
    if g and g["read"] > 60:
        j["long"] = True
    return j


def main():
    strict = "--strict" in sys.argv
    cfg = qyaml.load(DATA / "config.yaml")
    plan = qyaml.load(DATA / "plan" / "days.yaml")
    notion_map = {}
    nm = ROOT / "notion" / "notion_map.json"
    if nm.exists():
        notion_map = json.loads(nm.read_text(encoding="utf-8"))
    start = dt.date.fromisoformat(cfg["practice"]["start"])
    pool_file = DATA / "stats" / "pools.json"
    official_pools = json.loads(pool_file.read_text(encoding="utf-8")) if pool_file.exists() else {}
    subjects = [s["id"] for s in cfg["subjects"]]

    errors, warnings = [], []
    concepts_out, banks, pools = {}, {}, {}
    used = {s: set() for s in subjects}
    for day in plan["days"]:
        for s, ids in (day.get("sets") or {}).items():
            used[s].update(ids)
    for s, ids in (plan.get("diag") or {}).items():
        used[s].update(ids)

    for s in subjects:
        cpath = DATA / "concepts" / f"{s}.yaml"
        csum = {}
        if cpath.exists():
            cdoc = qyaml.load(cpath)
            concepts_out[s] = {"name": cdoc.get("name"), "modules": [
                {"id": m["id"], "name": m["name"], "concepts": [
                    {"id": c["id"], "name": c["name"], "summary": c.get("summary", ""),
                     "notion": notion_map.get(f"{s}:{c['id']}")} for c in m["concepts"]]}
                for m in cdoc["modules"]]}
            csum = {c["id"]: c.get("summary", "") for m in cdoc["modules"] for c in m["concepts"]}
        if not (DATA / "questions" / s).exists():
            pools[s] = {"total": 0, "published": 0}
            continue
        bank, groups = load_subject(s)
        pools[s] = {"total": official_pools.get(s, {}).get("total") or sum(1 for it in bank.values() if it.get("classic")),
                    "published": len(used[s])}
        items, gout = {}, {}
        for qid in sorted(used[s]):
            it = bank.get(qid)
            if it is None:
                errors.append(f"排程中的題目不存在：{qid}")
                continue
            if it["type"] != "open" and not it.get("answer"):
                errors.append(f"{qid} 沒有答案")
            if it["type"] in ("single", "multi") and len(it.get("options") or {}) < 2 and not it.get("image"):
                errors.append(f"{qid} 缺選項（請人工補齊）")
            if not it.get("explain"):
                (errors if strict else warnings).append(f"{qid} 尚無解析")
            items[qid] = item_json(s, it, groups, csum)
            if it.get("group"):
                gout[it["group"]] = groups[it["group"]]
        banks[s] = {"items": items, "groups": gout}

    days_out = []
    for day in plan["days"]:
        date = start + dt.timedelta(days=day["day"] - 1)
        days_out.append({"d": day["day"], "date": date.isoformat(), "theme": day.get("theme") or {},
                         "sets": day.get("sets") or {}})
    schedule = {"start": start.isoformat(), "goal_end": cfg["practice"]["goal_end"], "days": days_out,
                "diag": plan.get("diag") or {}, "pools": pools}
    version = dt.datetime.now().strftime("%Y%m%d%H%M%S")
    backend = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--backend=")), cfg.get("backend") or "")
    config = {"exam": cfg["exam"], "milestones": cfg["milestones"], "practice": cfg["practice"],
              "backend": backend, "subjects": cfg["subjects"], "version": version,
              "notion": {k: v for k, v in notion_map.items() if ":" not in k}}

    for w in warnings:
        print("提醒：", w)
    if errors:
        for e in errors:
            print("錯誤：", e)
        sys.exit(1)

    (OUT / "bank").mkdir(parents=True, exist_ok=True)
    dump = lambda obj, p: p.write_text(json.dumps(obj, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    dump(config, OUT / "config.json")
    dump(schedule, OUT / "schedule.json")
    dump(concepts_out, OUT / "concepts.json")
    for s, b in banks.items():
        dump(b, OUT / "bank" / f"{s}.json")
    # 讓 service worker 換版
    sw = ROOT / "docs" / "sw.js"
    if sw.exists():
        sw.write_text(re.sub(r'const VERSION = "[^"]*";', f'const VERSION = "{version}";', sw.read_text(encoding="utf-8")),
                      encoding="utf-8")
    total = sum(len(b["items"]) for b in banks.values())
    print(f"完成：{len(days_out)} 天排程、{total} 題上架、版本 {version}")
    for s in subjects:
        print(f"  {s}: 經典題池 {pools[s]['total']}，已上架 {pools[s]['published']}")


if __name__ == "__main__":
    main()
