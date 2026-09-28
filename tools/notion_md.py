"""由題庫、觀念樹與解析產生 Notion 頁面草稿（Notion 風格 Markdown），存到 notion/pages/。

用法：python3 tools/notion_md.py [--site=https://…]
之後由 Claude 透過 Notion MCP 依這些草稿建立或更新頁面；網站網址用 --site 帶入（預設 {{SITE}} 佔位）。
"""
import datetime as dt
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import qyaml  # noqa: E402
from build import load_overlay  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "notion" / "pages"
SITE = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--site=")), "{{SITE}}")
PAPER = {"chinese": "國綜", "english": "英文", "mathA": "數學A", "science": "自然", "social": "社會"}


def clean(s):
    """把題庫裡的 HTML 標記轉成 Notion 可讀的 Markdown。"""
    s = str(s or "")
    s = s.replace("【框】", "▌ ")
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"</?b>", "**", s)
    s = re.sub(r"<span[^>]*>|</span>", "", s)
    s = re.sub(r"<table>.*?</table>", "（表格請見原卷或練習網站）", s, flags=re.S)
    return s.strip()


def load_items(subject):
    items, groups = {}, {}
    overlay = load_overlay(subject)
    for path in sorted((ROOT / "data" / "questions" / subject).glob("g*.yaml")):
        doc = qyaml.load(path)
        for g in doc.get("groups") or []:
            groups[g["id"]] = g
        for it in doc["items"]:
            it["_year"] = doc["year"]
            it["_pdf"] = (doc.get("source") or {}).get("pdf")
            for f in ("explain", "key", "reference", "stem", "options"):
                if f in overlay.get(it["id"], {}):
                    it[f] = overlay[it["id"]][f]
            items[it["id"]] = it
    return items, groups


def src(it, subject="chinese"):
    paper = "國文" if (subject == "chinese" and it["_year"] == 110) else PAPER[subject]
    return f"{it['_year']} 學測{paper} 第 {it['no']} 題"


def question_block(it, subject="chinese", with_stem=True):
    p = (it.get("stats") or {}).get("P")
    head = f"📝 {src(it, subject)}" + (f"（全國答對率 {p}%）" if p is not None else "")
    lines = [f"<details><summary>{head}</summary>", ""]
    if with_stem:
        if it.get("image"):
            lines.append(f"![題目]({SITE}/{it['image']})")
        if it.get("stem"):
            lines.append(clean(it["stem"]))
        for k, v in (it.get("options") or {}).items():
            if v:
                lines.append(f"({k}) {clean(v)}")
    lines += ["", "<details><summary>看答案與解析</summary>", ""]
    if it["type"] == "open":
        lines.append(clean(it.get("reference") or "參考答案見大考中心評分原則。"))
    else:
        lines.append(f"**答案：{it.get('answer')}**")
        if it.get("key"):
            lines.append(f"💡 {clean(it['key'])}")
        lines.append(clean(it.get("explain") or "（解析整理中）"))
    lines += ["", "</details>", "", f"[到練習網站作答]({SITE}/#/item/{it['id']})　[原卷 PDF]({it['_pdf']})", "", "</details>"]
    return "\n".join(lines)


# 國文觀念頁要內嵌的代表題（其餘相關題目列成清單）
FEATURED = {
    "A1": ["chn115-01", "chn114-01", "chn113-01", "chn112-01", "chn111-01", "chn110-01"],
    "A2": ["chn115-02", "chn114-02", "chn113-02", "chn112-02", "chn111-02", "chn110-02"],
    "A3": ["chn115-26", "chn114-26", "chn113-25", "chn112-03", "chn111-03", "chn110-38", "chn114-03", "chn112-06", "chn110-04"],
    "A4": ["chn115-25", "chn114-25", "chn113-27", "chn113-26", "chn112-26", "chn111-26", "chn110-35", "chn111-18"],
    "A5": ["chn114-29", "chn112-27", "chn110-37", "chn110-09"],
    "A6": ["chn115-05", "chn114-05", "chn113-05", "chn113-04", "chn110-03"],
    "B1": ["chn110-13"],
    "C7": ["chn115-07", "chn115-12", "chn115-36", "chn113-12", "chn112-16"],
    "D1": ["chn115-32", "chn115-33", "chn115-34"],
}


def chinese_page():
    items, _ = load_items("chinese")
    concepts = qyaml.load(ROOT / "data" / "concepts" / "chinese.yaml")
    trends = (ROOT / "notion" / "chinese_trends.md").read_text(encoding="utf-8")
    md = ["# 📚 國文", ""]
    md += ["<callout icon=\"🧭\">", "**考科結構（114、115 相同）**：國綜 90 分鐘＝單選 24 題×2 分＋多選 7 題×4 分＋混合題 1 題組 24 分（非選 20 分）；國寫 90 分鐘＝兩大題各 25 分。",
           "**國文原得總分＝國綜×0.5＋國寫**，所以國寫 1 分＝國綜 2 分。115 年國文級距 5.106 分（約國綜 5 題單選＝1 級分）。", "</callout>", ""]
    md += ["## 📈 近六屆出題趨勢（110–115）", "",
           "- **語文知識題是「固定班底」**：第 1 題字音、第 2 題字形六屆從未缺席，但全國平均答對率只有 39% 與 30%，是最容易拉開差距的 4 分。",
           "- **閱讀理解占一半以上配分**，白話知性閱讀與文言閱讀各約 49 題，是分數主體；圖表題答對率最高（65%），是穩拿分題型。",
           "- **文言與韻文占比約 35%–53%**，115 年回升到 46%，且文言題組常把核心選文拆成詞義、句式與佐證選項。",
           "- **15 篇核心選文**：〈虯髯客傳〉〈赤壁賦〉〈鴻門宴〉〈諫逐客書〉〈燭之武退秦師〉〈項脊軒志〉〈出師表〉是引用最多的前七名。",
           "- **研判題（①②符合／不符合／無法判斷）幾乎每年 2–3 題**，混合題非選 18–20 分（折合國文考科 9–10 分）。",
           "", "<details><summary>看完整統計表</summary>", "", trends, "", "*說明：主題分類與核心選文次數為 Claude 逐題判讀標註，持續校對中。*", "", "</details>", ""]
    md += ["## 🎯 必考觀念與對應考古題", "", "每個觀念先看重點，再做下面的考古題；點「看答案與解析」核對，或到練習網站作答（會記錄到老師的儀表板）。", ""]
    for mod in concepts["modules"]:
        md += [f"### {mod['id']}. {mod['name']}", ""]
        for c in mod["concepts"]:
            related = [it for it in items.values() if c["id"] in (it.get("concepts") or [])]
            related.sort(key=lambda it: (-it["_year"], it["no"]))
            md += [f"<details><summary><b>{c['id']} {c['name']}</b>（近六屆 {len(related)} 題）</summary>", ""]
            md += [f"<callout icon=\"💡\">{clean(c.get('summary', ''))}</callout>", ""]
            for pt in c.get("points") or []:
                md.append(f"- {clean(pt)}")
            feat = [items[q] for q in FEATURED.get(c["id"], []) if q in items]
            if feat:
                md += ["", "**📝 對應考古題**", ""]
                md += [question_block(it) for it in feat]
            others = [it for it in related if it["id"] not in FEATURED.get(c["id"], [])]
            if others:
                md += ["", "<details><summary>其他相關考古題</summary>", ""]
                md += [f"- [{src(it)}]({SITE}/#/item/{it['id']})" + (f"　全國答對率 {it['stats']['P']}%" if (it.get('stats') or {}).get('P') is not None else "") for it in others]
                md += ["", "</details>"]
            md += ["", "</details>", ""]
    md += ["## ✍️ 老師筆記", "", "（這一區留給老師補充，之後同步不會覆蓋。）", ""]
    return "\n".join(md)


def skeleton_page(subject, title, icon, structure, focus):
    items, _ = load_items(subject)
    concepts = qyaml.load(ROOT / "data" / "concepts" / f"{subject}.yaml")
    plan = qyaml.load(ROOT / "data" / "plan" / "days.yaml")
    md = [f"# {icon} {title}", "", f"<callout icon=\"🧭\">{structure}</callout>", "",
          f"> {focus}", "", "## 🎯 觀念大綱", ""]
    for mod in concepts["modules"]:
        md.append(f"### {mod['name']}")
        for c in mod["concepts"]:
            md.append(f"- **{c['name']}**：{clean(c.get('summary', ''))}")
        md.append("")
    md += ["## 📝 第 1 週每日練習（含解析）", ""]
    for day in plan["days"]:
        qids = day["sets"].get(subject) or []
        if not qids:
            continue
        md += [f"<details><summary>Day {day['day']}｜{day['theme'].get(subject, '')}</summary>", ""]
        md += [question_block(items[q], subject) for q in qids if q in items]
        md += ["", "</details>", ""]
    md += ["## ✍️ 老師筆記", "", "（輪到本科上課前一週，會補上完整的必考觀念與趨勢分析。）", ""]
    return "\n".join(md)


def exam_rules_page():
    return (ROOT / "notion" / "exam_rules.md").read_text(encoding="utf-8")


def week1_page():
    return (ROOT / "notion" / "week01_chinese.md").read_text(encoding="utf-8")


def home_page():
    cfg = qyaml.load(ROOT / "data" / "config.yaml")
    ms = "\n".join(f"| {m['date']} | {m['name']} |" for m in cfg["milestones"])
    return f"""# 116 學測衝刺基地

<embed src="{SITE}/countdown.html"></embed>

<callout icon="📌">**116 學測：2027/1/22（五）–1/24（日）**　｜　每日快答從 **2026/9/30（Day 1）** 開始，每天每科 5 題，12/31 前做完近六屆經典題。
👉 [打開今日練習]({SITE}/)（手機可「加入主畫面」，像 App 一樣一鍵開啟）</callout>

## 🧭 快速入口
- 📋 考試制度與作答策略
- 📚 國文｜英文｜數學｜自然｜社會
- 🗂️ 歷屆考古題總覽　・　🗃️ 考古題庫
- 📈 年度練習進度　・　📅 每週課程

## 📆 重要日程
| 日期 | 事項 |
|---|---|
{ms}
"""


def progress_page():
    sched = json.loads((ROOT / "docs" / "data" / "schedule.json").read_text(encoding="utf-8"))
    pools = json.loads((ROOT / "data" / "stats" / "pools.json").read_text(encoding="utf-8"))
    start = dt.date.fromisoformat(sched["start"])
    goal = dt.date.fromisoformat(sched["goal_end"])
    days = (goal - start).days + 1
    names = {"chinese": "國文", "english": "英文", "mathA": "數學A", "science": "自然", "social": "社會"}
    rows = []
    for s, n in names.items():
        total = pools[s]["total"]
        per = total / days
        rows.append(f"| {n} | {total} | {per:.1f} 題 | 每天 5 題約 {int((total + 4) // 5)} 天做完 | {sched['pools'][s]['published']} |")
    return f"""# 📈 年度練習進度（近六屆經典題）

目標：**{start.isoformat()} → {goal.isoformat()}（共 {days} 天）**做完 110–115 學測各科的經典題。
「經典題」＝選擇題與選填題（非選改在課堂與 Notion 練習），並排除官方鑑別度 D < 10 的題目。

| 科目 | 六屆經典題 | 平均每天需要 | 依每天 5 題 | 目前已上架 |
|---|---|---|---|---|
{chr(10).join(rows)}

- 每天「基本 5 題」走六屆主線；「加練」由網站自動排入錯題（1、3、7 天後再出現）。
- 國文、數學A 題池較小，預計 11 月就能做完六屆，之後改做錯題總複習與 105–109 年經典題。
- 一月：錯題總複習＋限時全真模擬。
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pages = {
        "00_home.md": home_page(),
        "01_exam_rules.md": exam_rules_page(),
        "10_chinese.md": chinese_page(),
        "11_english.md": skeleton_page("english", "英文", "🔤", "英文 100 分鐘：詞彙 10、綜合測驗 10、文意選填 10、篇章結構 8、閱讀測驗 24（選擇共 62 分）＋混合題 10＋中譯英 8＋英文作文 20。", "第 2 週上課前補齊：各大題解題法、高頻詞彙與搭配、翻譯與作文評分重點。"),
        "12_mathA.md": skeleton_page("mathA", "數學A", "📐", "數學A 100 分鐘：單選 6 題×5、多選 6 題×5、選填 5 題×5（全對才給分）＋混合題或非選 15 分。", "第 3 週上課前補齊：各單元必考觀念、常見題型與解題流程。"),
        "13_science.md": skeleton_page("science", "自然", "🔬", "自然 110 分鐘：選擇題（單選＋多選）36 題×2＝72 分＋混合題或非選 56 分，共 128 分；物化生地四科配分相當。", "第 4 週上課前補齊：四科必考觀念、圖表與實驗題解題法。"),
        "14_social.md": skeleton_page("social", "社會", "🌏", "社會 110 分鐘：單選 38 題×2＝76 分＋混合題或非選 68 分（115 年，共 144 分）；歷史、地理、公民三科配分相當。", "第 5 週上課前補齊：三科必考觀念、史料與圖表判讀法。"),
        "30_week01_chinese.md": week1_page(),
        "40_progress.md": progress_page(),
    }
    for name, text in pages.items():
        (OUT / name).write_text(text, encoding="utf-8")
        print(f"{name}: {len(text)} 字")


if __name__ == "__main__":
    main()
