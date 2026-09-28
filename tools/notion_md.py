"""由題庫、觀念樹與解析產生 Notion 頁面內容，存到 notion/pages/。

格式：Notion 風格 Markdown（notion://docs/enhanced-markdown-spec）：子區塊用 tab 縮排、表格用 <table>、
特殊字元 \\ * ~ ` $ [ ] < > { } | ^ 要跳脫。
用法：python3 tools/notion_md.py [--site=https://…]
- 已建立的 Notion 頁面網址記在 notion/notion_map.json，會自動變成頁內連結（例如 q:chn115-01 → 考古題庫的那一列）。
- 超過 PART_LIMIT 字的頁面切成 *.partN.md：第 1 段建立頁面，其餘依序接在頁面最後。
- 考古題庫與每週課程的資料列存成 notion/pages/db_*.json（屬性＋內容）。
"""
import datetime as dt
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import qyaml  # noqa: E402
from build import load_overlay, paper_name  # noqa: E402
from build import load_subject as _load_subject  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "notion" / "pages"
SITE = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--site=")), "{{SITE}}").rstrip("/")
MAP_FILE = ROOT / "notion" / "notion_map.json"
MAP = json.loads(MAP_FILE.read_text(encoding="utf-8")) if MAP_FILE.exists() else {}
NAMES = {"chinese": "國文", "english": "英文", "mathA": "數學A", "mathB": "數學B", "science": "自然", "social": "社會"}
TYPE_NAME = {"single": "單選", "multi": "多選", "fill": "選填", "open": "非選"}
WEEKDAY = "一二三四五六日"
PART_LIMIT = 14000

# ---------- 行內格式與區塊 ----------
_ESC = re.compile(r"([\\*~`$\[\]<>{}|^])")
_TAG = re.compile(r"""<(/?)(u|em|b|strong|i|br|span|div|p|ruby|rt)(?:\s+[A-Za-z-]+(?:=(?:"[^"]*"|'[^']*'|[^\s"'<>]+))?)*\s*/?>""")  # 屬性須為 name="值"，避免誤認數學不等式
_SUP = ("0123456789+-−=()n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻⁼⁽⁾ⁿ")
_SUB = ("0123456789+-−=()", "₀₁₂₃₄₅₆₇₈₉₊₋₋₌₍₎")


def esc(s):
    return _ESC.sub(r"\\\1", str(s))


def _supsub(s):
    def rep(m):
        keys, vals = _SUP if m.group(1) == "sup" else _SUB
        t = m.group(2)
        if all(ch in keys for ch in t):
            return t.translate(str.maketrans(keys, vals))
        return ("^" if m.group(1) == "sup" else "_") + t
    return re.sub(r"<(sup|sub)>(.*?)</\1>", rep, s)


def inline(s):
    """題庫文字 → Notion 行內格式：保留底線、粗體與換行，其餘特殊字元跳脫。"""
    s = _supsub(str(s or "").replace("［圖］", "［附圖請見原卷］").replace("\n", "<br>"))
    out, pos = [], 0
    for m in _TAG.finditer(s):
        out.append(esc(s[pos:m.start()]))
        close, tag = m.group(1), m.group(2)
        if tag == "u":
            out.append("</span>" if close else '<span underline="true">')
        elif tag in ("b", "strong", "em"):
            out.append("**")
        elif tag == "i":
            out.append("*")
        elif tag == "br":
            out.append("<br>")
        pos = m.end()
    out.append(esc(s[pos:]))
    return "".join(out).strip()


_MD_TOKEN = re.compile(r"(\*\*|\[[^\]]+\]\([^)\s]+\)|`[^`]+`)")


def md_inline(s):
    """手寫 Markdown 的一行：保留 **粗體**、[連結](網址)、`程式碼`，其餘特殊字元跳脫。"""
    out = []
    for part in _MD_TOKEN.split(s):
        if not part:
            continue
        if part == "**" or part.startswith("`"):
            out.append(part)
        elif part.startswith("[") and _MD_TOKEN.fullmatch(part):
            text, url = re.match(r"\[([^\]]+)\]\(([^)\s]+)\)", part).groups()
            out.append(f"[{esc(text)}]({url.replace('{{SITE}}', SITE)})")
        else:
            out.append(esc(part))
    return "".join(out)


def indent(block, n=1):
    return "\n".join(("\t" * n + ln) if ln else ln for ln in block.split("\n"))


def toggle(summary, children):
    return "\n".join(["<details>", f"<summary>{summary}</summary>"] + [indent(c) for c in children] + ["</details>"])


def callout(icon, children, color=None):
    attr = f' icon="{icon}"' + (f' color="{color}"' if color else "")
    return "\n".join([f"<callout{attr}>"] + [indent(c) for c in children] + ["</callout>"])


def table(rows, header=True):
    width = max(len(r) for r in rows)
    lines = [f'<table header-row="{"true" if header else "false"}">']
    for r in rows:
        lines.append("\t<tr>")
        lines += [f"\t\t<td>{c}</td>" for c in list(r) + [""] * (width - len(r))]
        lines.append("\t</tr>")
    lines.append("</table>")
    return "\n".join(lines)


def html_table(h):
    rows = [re.findall(r"<t([dh])[^>]*>(.*?)</t[dh]>", r, re.S) for r in re.findall(r"<tr[^>]*>(.*?)</tr>", h, re.S)]
    rows = [r for r in rows if r]
    header = bool(rows) and all(k == "h" for k, _ in rows[0])
    return table([[inline(c) for _, c in r] for r in rows], header=header)


def text_blocks(text):
    """題庫的多行文字 → 段落、表格、引文框。"""
    out = []
    for line in str(text or "").split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("【框】"):
            out.append("> " + inline(line[3:]))
        elif line.startswith("<table"):
            out.append(html_table(line))
        else:
            out.append(inline(line))
    return out


def convert_md(doc):
    """手寫的 Markdown 文件 → Notion 風格：pipe 表格轉 <table>、callout 子行縮排、巢狀清單改用 tab。第一行 # 標題略過。"""
    lines = doc.split("\n")
    out, i = [], 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if i == 0 and ln.startswith("# "):
            i += 1
            continue
        if ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                    rows.append([md_inline(c) for c in cells])
                i += 1
            out.append(table(rows))
            continue
        m = re.match(r'<callout icon="([^"]+)">(.*)', ln)
        if m:
            body, icon = [m.group(2)], m.group(1)
            while "</callout>" not in body[-1]:
                i += 1
                body.append(lines[i].rstrip())
            body[-1] = body[-1].replace("</callout>", "")
            out.append(callout(icon, [convert_line(b) for b in body if b.strip()]))
            i += 1
            continue
        if ln.strip():
            out.append(convert_line(ln))
        i += 1
    return out


def convert_line(ln):
    m = re.match(r"^( *)(#{1,4} |- |\d+\. )?(.*)$", ln)
    spaces, mark, text = m.group(1), m.group(2) or "", m.group(3)
    return "\t" * (len(spaces) // 2) + mark + md_inline(text)


# ---------- 題目 ----------
def load_subject(subject):
    """題目用 build.py 的載入（已套用解析）；題組保留原始文章（build.py 只留網站用的 HTML）。"""
    items, _ = _load_subject(subject)
    overlay = load_overlay(subject)
    groups = {}
    for path in sorted((ROOT / "data" / "questions" / subject).glob("g*.yaml")):
        for g in qyaml.load(path).get("groups") or []:
            if overlay.get(g["id"], {}).get("passage"):
                g["passage"] = overlay[g["id"]]["passage"]
            groups[g["id"]] = g
    return items, groups


def src(it, subject):
    return f"{it['_year']} 學測{paper_name(subject, it['_year'])} 第 {it['no']} 題"


def answer_text(it):
    a = str(it.get("answer") or "")
    if it["type"] == "fill":
        return "　".join(f"{it['no']}-{i + 1}：{v}" for i, v in enumerate(a.split(",")))
    return a


def stats_line(it):
    st = it.get("stats") or {}
    parts = []
    if st.get("P") is not None:
        parts.append(f"全國答對率 {st['P']}%")
    if st.get("T") is not None and it["type"] == "multi":
        parts.append(f"全對率 {st['T']}%")
    if st.get("D") is not None:
        parts.append(f"鑑別度 {st['D']}")
    if st.get("opt"):
        parts.append("各選項選答率 " + "、".join(f"{k} {v}%" for k, v in st["opt"].items()))
    return "📊 " + "｜".join(parts) if parts else ""


def question_body(it, subject, groups, published, shown=None):
    """shown：同一區已經列過文章的題組；同一題組的後續題目不再重複文章。"""
    blocks = []
    g = groups.get(it.get("group")) if it.get("group") else None
    if g and shown is not None and g["id"] in shown:
        blocks.append("📖 題組文章同上一題。")
    elif g:
        if shown is not None:
            shown.add(g["id"])
        r = g.get("range") or []
        head = f"題組文章（第 {r[0]}–{r[-1]} 題共用）" if r else "題組文章"
        body = [f"**{head}**"] + ([inline(g["intro"])] if g.get("intro") else []) + text_blocks(g.get("passage"))
        blocks.append(callout("📖", body, color="gray_bg"))
    if it.get("image"):
        blocks.append(f"![{src(it, subject)}]({SITE}/{it['image']})")
    blocks += text_blocks(it.get("stem"))
    for k, v in (it.get("options") or {}).items():
        if v:
            blocks.append(f"({k}) {inline(v)}")
    ans = []
    if it["type"] == "open":
        if it.get("key"):
            ans.append("💡 " + inline(it["key"]))
        ans += text_blocks(it.get("reference") or "參考答案見大考中心評分原則。")
    else:
        ans.append(f"**答案：{esc(answer_text(it))}**")
        if it.get("key"):
            ans.append("💡 " + inline(it["key"]))
        ans += text_blocks(it.get("explain") or "（解析整理中）")
    if stats_line(it):
        ans.append(stats_line(it))
    blocks.append(toggle("✅ 看答案與解析", ans))
    links = []
    if it["id"] in published:
        links.append(f"[到練習網站作答]({SITE}/#/item/{it['id']})")
    if it.get("_url"):
        links.append(f"[原卷 PDF]({it['_url']})")
    if links:
        blocks.append("　".join(links))
    return blocks


def question_toggle(it, subject, groups, published, shown=None):
    p = (it.get("stats") or {}).get("P")
    head = f"📝 {src(it, subject)}" + (f"（全國答對率 {p}%）" if p is not None else "")
    return toggle(head, question_body(it, subject, groups, published, shown))


def ref(it, subject, published):
    """題目的連結：已入考古題庫就用頁面提及，已上架就連到練習網站，否則連到原卷。"""
    p = (it.get("stats") or {}).get("P")
    tail = f"　全國答對率 {p}%" if p is not None else ""
    url = MAP.get(f"q:{it['id']}")
    if url:
        return f'<mention-page url="{url}"/>{tail}'
    if it["id"] in published:
        return f"[{src(it, subject)}]({SITE}/#/item/{it['id']}){tail}"
    return f"[{src(it, subject)}]({it['_url']}){tail}" if it.get("_url") else src(it, subject) + tail


def plan_info():
    cfg = qyaml.load(ROOT / "data" / "config.yaml")
    plan = qyaml.load(ROOT / "data" / "plan" / "days.yaml")
    start = dt.date.fromisoformat(cfg["practice"]["start"])
    published = {q for d in plan["days"] for ids in d["sets"].values() for q in ids}
    published |= {q for ids in (plan.get("diag") or {}).values() for q in ids}
    return cfg, plan, start, published


def fmt_day(d):
    return f"{d.month}/{d.day}（{WEEKDAY[d.weekday()]}）"


# ---------- 頁面 ----------
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
    _, _, _, published = plan_info()
    items, groups = load_subject("chinese")
    concepts = qyaml.load(ROOT / "data" / "concepts" / "chinese.yaml")
    trends = convert_md("# x\n" + (ROOT / "notion" / "chinese_trends.md").read_text(encoding="utf-8"))
    b = [callout("🧭", [
        "**考科結構（114、115 相同）**：國綜 90 分鐘＝單選 24 題×2 分＋多選 7 題×4 分＋混合題 1 題組 24 分（非選 20 分）；國寫 90 分鐘＝兩大題各 25 分。",
        "**國文原得總分＝國綜×0.5＋國寫**，所以國寫 1 分＝國綜 2 分。115 年國文級距 5.106 分（約國綜 5 題單選＝1 級分）。"])]
    b += ["## 📈 近六屆出題趨勢（110–115）",
          "- **語文知識題是「固定班底」**：第 1 題字音、第 2 題字形六屆從未缺席，但全國平均答對率只有 39% 與 30%，是最容易拉開差距的 4 分。",
          "- **閱讀理解占一半以上配分**，白話知性閱讀與文言閱讀各約 49 題，是分數主體；圖表題答對率最高（65%），是穩拿分題型。",
          "- **文言與韻文占比約 35%–53%**，115 年回升到 46%，且文言題組常把核心選文拆成詞義、句式與佐證選項。",
          "- **15 篇核心選文**：〈虯髯客傳〉〈赤壁賦〉〈鴻門宴〉〈諫逐客書〉〈燭之武退秦師〉〈項脊軒志〉〈出師表〉是引用最多的前七名。",
          "- **研判題（①②符合／不符合／無法判斷）幾乎每年 2–3 題**，混合題非選 18–20 分（折合國文考科 9–10 分）。",
          toggle("看完整統計表", trends + ["說明：主題分類與核心選文出現次數依 110–115 年試題逐題整理。"]),
          "## 🎯 必考觀念與對應考古題",
          "每個觀念先看重點，再做下面的考古題：點「✅ 看答案與解析」核對，或點「到練習網站作答」（作答紀錄會同步給老師）。"]
    for mod in concepts["modules"]:
        b.append(f"### {mod['id']}. {esc(mod['name'])}")
        for c in mod["concepts"]:
            related = sorted((it for it in items.values() if c["id"] in (it.get("concepts") or [])),
                             key=lambda it: (-int(it["_year"]), int(it["no"])))
            ch = [callout("💡", [inline(c.get("summary", ""))])] + [f"- {inline(pt)}" for pt in c.get("points") or []]
            feat = [items[q] for q in FEATURED.get(c["id"], []) if q in items]
            if feat:
                ch.append("**📝 對應考古題**")
                shown = set()
                ch += [question_toggle(it, "chinese", groups, published, shown) for it in feat]
            others = [it for it in related if it["id"] not in FEATURED.get(c["id"], [])]
            if others:
                ch.append(toggle(f"其他相關考古題（{len(others)} 題）", [f"- {ref(it, 'chinese', published)}" for it in others]))
            b.append(toggle(f"**{c['id']} {esc(c['name'])}**" + (f"（近六屆 {len(related)} 題）" if related else ""), ch))
    return b


def skeleton_page(subject, structure, focus):
    _, plan, start, published = plan_info()
    items, _ = load_subject(subject)
    concepts = qyaml.load(ROOT / "data" / "concepts" / f"{subject}.yaml")
    week = [q for d in plan["days"] for q in d["sets"].get(subject) or []]
    b = [callout("🧭", [md_inline(structure)]), callout("📌", [md_inline(focus)], color="yellow_bg"),
         "## 🎯 觀念大綱與第 1 週考古題",
         "每個觀念底下列出第 1 週練習到的考古題；點開可以看題目、答案與解析。"]
    for mod in concepts["modules"]:
        b.append(f"### {esc(mod['name'])}")
        for c in mod["concepts"]:
            line = f"- **{esc(c['name'])}**：{inline(c.get('summary', ''))}"
            qs = [items[q] for q in week if c["id"] in (items[q].get("concepts") or [])]
            if len(qs) > 8:
                qs_lines = [f"\t- 第 1 週共 {len(qs)} 題，依日期列在下方「📝 第 1 週每日練習」。"]
            else:
                qs_lines = [f"\t- {ref(it, subject, published)}" for it in qs]
            b.append("\n".join([line] + qs_lines))
    b.append("## 📝 第 1 週每日練習")
    for d in plan["days"]:
        qids = d["sets"].get(subject) or []
        if qids:
            date = start + dt.timedelta(days=d["day"] - 1)
            b.append(toggle(f"**Day {d['day']}**　{fmt_day(date)}　{esc(d['theme'].get(subject, ''))}",
                            [f"- {ref(items[q], subject, published)}" for q in qids]))
    return b


def exam_rules_page():
    return convert_md((ROOT / "notion" / "exam_rules.md").read_text(encoding="utf-8"))


def week1_page():
    """第 1 週上課講義（學生看得到）：原稿中的 [[題目:代碼]] 換成完整題目與折疊解析，[[診斷小考]] 換成 12 題。"""
    _, plan, _, published = plan_info()
    items, groups = load_subject("chinese")
    doc = (ROOT / "notion" / "week01_chinese.md").read_text(encoding="utf-8").replace("{{SITE}}", SITE)
    blocks, chunk, shown = [], [], set()

    def flush():
        if chunk:
            blocks.extend(convert_md("# x\n" + "\n".join(chunk)))
            chunk.clear()

    for i, line in enumerate(doc.split("\n")):
        if i == 0 and line.startswith("# "):
            continue
        if line.startswith("## "):
            shown = set()  # 每一節重新顯示題組文章，不要「同上一題」跨到上一節
        m = re.fullmatch(r"\[\[題目:([a-z0-9-]+)\]\]", line.strip())
        if m:
            flush()
            blocks.append(question_toggle(items[m.group(1)], "chinese", groups, published, shown))
        elif line.strip() == "[[診斷小考]]":
            flush()
            diag = (plan.get("diag") or {}).get("chinese") or []
            dshown = set()
            blocks.append(toggle(f"📝 診斷小考 {len(diag)} 題與解析（做完小考再打開）",
                                 [question_toggle(items[q], "chinese", groups, published, dshown) for q in diag]))
        else:
            chunk.append(line)
    flush()
    return blocks


def progress_page():
    sched = json.loads((ROOT / "docs" / "data" / "schedule.json").read_text(encoding="utf-8"))
    pools = json.loads((ROOT / "data" / "stats" / "pools.json").read_text(encoding="utf-8"))
    start = dt.date.fromisoformat(sched["start"])
    goal = dt.date.fromisoformat(sched["goal_end"])
    days = (goal - start).days + 1
    rows = [["科目", "六屆經典題", "平均每天需要", "依每天 5 題", "目前已上架"]]
    for s, n in NAMES.items():
        total = pools[s]["total"]
        rows.append([n, str(total), f"{total / days:.1f} 題", f"約 {(total + 4) // 5} 天做完", str(sched["pools"][s]["published"])])
    return [f"目標：**{start.month}/{start.day} → {goal.month}/{goal.day}（共 {days} 天）**做完 110–115 學測各科的經典題。",
            "「經典題」＝選擇題與選填題（非選改在課堂與 Notion 練習），並排除官方鑑別度 D \\< 10 的題目。",
            table(rows),
            "- 每天「基本 5 題」走六屆主線；「加練」由網站自動排入錯題（1、3、7 天後再出現）。",
            "- 依每天 5 題：數學A、數學B 約 10 月下旬，國文約 11 月上旬，英文約 11 月下旬，自然與社會約 12 月初做完六屆。",
            "- 提早做完的科目改做錯題總複習與 105–109 年經典題。",
            "- 一月：錯題總複習＋限時全真模擬。"]


PAST_COLS = [("111–115 年（108 課綱）", range(115, 110, -1), ["國綜", "國寫", "英文", "數學A", "數學B", "社會", "自然"]),
             ("107–110 年", range(110, 106, -1), ["國文（選擇題）", "國寫", "英文", "數學", "社會", "自然"]),
             ("96–106 年", range(106, 95, -1), ["國文", "英文", "數學", "社會", "自然"]),
             ("85–95 年", range(95, 84, -1), ["國文", "英文", "數學", "社會", "自然"])]


def _pick(files, test):
    cand = [f for f in files if test(f["label"])]
    pdf = [f for f in cand if f["url"].lower().endswith(".pdf")]
    return (pdf or cand or [None])[0]


def past_exams_page():
    rows = json.loads((ROOT / "data" / "stats" / "past_exams.json").read_text(encoding="utf-8"))
    by = {}
    for r in rows:
        by.setdefault(r["year"], {})[r["subject"]] = r["files"]
    b = [callout("🗂️", [
        "大考中心公布的學測歷屆試題，每格依序是 **試題**・**答案**・**評分**（非選擇題評分原則）的 PDF。",
        "110–115 六屆的經典題已經依觀念整理在各科頁面與「🗃️ 考古題庫」，做完再回來挑更早的年度練習。"])]
    for title, years, cols in PAST_COLS:
        b.append(f"## {title}")
        t = [["年度"] + [c.replace("（選擇題）", "") for c in cols]]
        for y in years:
            row = [f"**{y}**"]
            for c in cols:
                files = by.get(y, {}).get(c) or []
                links = []
                for name, test in (("試題", lambda l: l == "試題內容"), ("答案", lambda l: "答案" in l), ("評分", lambda l: "評分" in l)):
                    f = _pick(files, test)
                    if f:
                        url = re.sub(r"^https?://dev\.iifun\.com\.tw/ceec", "https://www.ceec.edu.tw", f["url"])
                        links.append(f"[{name}]({url})")
                row.append("・".join(links) or "—")
            t.append(row)
        b.append(table(t))
    b += ["## 📊 答對率、五標與級分",
          "- [學科能力測驗統計圖表（各年度答對率、鑑別度、五標、級分人數）](https://www.ceec.edu.tw/xmdoc?xsmsid=0J018604485538810196)",
          "- [大考中心歷屆試題與答案（官方頁面）](https://www.ceec.edu.tw/xmfile?xsmsid=0J052424829869345634)"]
    return b


def home_page():
    cfg, _, start, _ = plan_info()
    pg = lambda k, t: f'<page url="{MAP["page:" + k]}">{t}</page>' if MAP.get("page:" + k) else f"（{t}：建立中）"
    db = lambda k, t: f'<database url="{MAP[k]}" inline="false">{t}</database>' if MAP.get(k) else f"（{t}：建立中）"
    ms = [["日期", "事項"]] + [[f"{dt.date.fromisoformat(m['date']).month}/{dt.date.fromisoformat(m['date']).day}（{WEEKDAY[dt.date.fromisoformat(m['date']).weekday()]}）", esc(m["name"])] for m in cfg["milestones"]]
    w1 = f'<mention-page url="{MAP["week:1"]}"/>' if MAP.get("week:1") else "📅 每週課程 W1"
    return [f'<embed src="{SITE}/countdown.html">距離 116 學測倒數</embed>',
            callout("📌", ["**116 學測：2027/1/22（五）–1/24（日）**｜每日快答 **9/30（三）Day 1** 開始，每天每科 5 題，12/31 前做完近六屆經典題。",
                          f"👉 [打開今日練習]({SITE}/)（手機用瀏覽器打開後選「加入主畫面」，之後像 App 一樣一鍵開啟）"], color="orange_bg"),
            "## 📣 本週：W1 國文（9/30–10/6）",
            f"- 上課：國綜診斷 × 語文知識 × 文言虛詞 × 閱讀研判 → {w1}",
            "- 每日練習：國文、英文、數學A、數學B、自然、社會各 5 題，合計約 45 分鐘（數學A、數學B 各約 14 分鐘，其他科各 3–6 分鐘），分散在零碎時間做；答錯的題目 1、3、7 天後會自動回來複習。",
            "## 🧭 學習地圖",
            pg("rules", "考試制度與作答策略"),
            "### 📚 各科重點與考古題",
            pg("chinese", "國文"), pg("english", "英文"), pg("mathA", "數學A"), pg("mathB", "數學B"), pg("science", "自然"), pg("social", "社會"),
            "### 🗂️ 考古題",
            db("db:questions", "🗃️ 考古題庫"), pg("past", "歷屆考古題總覽"),
            "### 📅 課程與進度",
            db("db:weeks", "📅 每週課程"), pg("progress", "年度練習進度"),
            "## 📆 重要日程", table(ms),
            "## 📱 練習網站怎麼用",
            "1. 第一次打開，輸入老師給的學生代碼（只要輸入一次）。",
            "2. 首頁按「▶ 繼續今日練習」：單選點一下就判分，多選、選填按「送出」。",
            "3. 車來了直接關掉也沒關係，每題作答完就存好；沒網路也能做，連上網路後自動上傳。",
            "4. 答錯的題目會在 1、3、7 天後回到「加練」，也可以在「錯題本」依科目複習。"]


def teacher_page():
    return [callout("🔒", ["**這一頁只給老師看**：不要分享給學生，也不要搬到「116 學測陪考衝刺」底下（那一頁會分享給學生）。"], color="red_bg"),
            "## 🔗 常用連結",
            f"- [老師儀表板]({SITE}/teacher.html)：輸入老師密鑰（Apps Script 執行 setup 時顯示在執行紀錄）。可以看每天進度、每題作答與個人弱點。",
            "- Google 試算表：「名冊」管理學生代碼，「作答紀錄」是每一題的原始紀錄，「總覽」是每天、每科的統計。",
            f"- [練習網站]({SITE}/)　[倒數時鐘]({SITE}/countdown.html)　[GitHub repo](https://github.com/Harry-Kuo/gsat116)",
            (f'- 給學生的頁面：<mention-page url="{MAP["page:root"]}"/>' if MAP.get("page:root") else "- 給學生的頁面：116 學測陪考衝刺"),
            "## 🧑‍🎓 學生代碼",
            "- 只有試算表「名冊」裡「是否啟用」為 TRUE 的代碼能進入練習網站（不分大小寫）；網站每次開啟都會重新確認，停用或刪除的代碼會自動登出。",
            "- 學生代碼只記在試算表，不要寫進 GitHub（repo 是公開的）。",
            "- TEST01 是老師測試用代碼；測試留下的紀錄可以在「作答紀錄」直接刪除。",
            "## 📅 每週備課流程",
            "1. 上課前看儀表板「個人分析」：弱點觀念、全國答對率高但答錯的題目。",
            "2. 請 Claude 準備下一週：各科 35 題解析與排程、下一個輪到的科目完整重點頁與教案（在 exam_tools 資料夾開 Claude Code）。",
            "3. 看過 Claude 寫的解析：在「🗃️ 考古題庫」勾選「老師已審閱」；有錯直接告訴 Claude 修正（網站與 Notion 會一起更新）。",
            "4. 上課後把重點寫進該週的「📅 每週課程」頁（學生看得到），私人觀察寫在下面。",
            "## ✍️ 備課筆記（私人）",
            toggle("W1 國文", ["- 診斷小考結果：", "- 卡關點：", "- 下週要補："])]


def db_question_rows():
    cfg, plan, start, published = plan_info()
    rows = []
    sched = {}
    for s, ids in (plan.get("diag") or {}).items():
        for q in ids:
            sched[q] = ("課堂診斷", None)
    for d in plan["days"]:
        for s, ids in d["sets"].items():
            for q in ids:
                sched[q] = (f"Day {d['day']}", start + dt.timedelta(days=d["day"] - 1))
    for s in NAMES:
        items, groups = load_subject(s)
        cdoc = qyaml.load(ROOT / "data" / "concepts" / f"{s}.yaml")
        cname = {c["id"]: c["name"] for m in cdoc["modules"] for c in m["concepts"]}
        order = [q for q in (plan.get("diag") or {}).get(s, [])] + [q for d in plan["days"] for q in d["sets"].get(s) or []]
        for q in order:
            it = items[q]
            st = it.get("stats") or {}
            p = st.get("P")
            slot, date = sched[q]
            props = {"題目": f"{it['_year']} {paper_name(s, it['_year'])} 第 {it['no']} 題｜{cname.get(it.get('topic'), '')}",
                     "科目": NAMES[s], "年度": str(it["_year"]), "題號": int(it["no"]), "題型": TYPE_NAME[it["type"]],
                     "觀念": [cname[c] for c in it.get("concepts") or [] if c in cname],
                     "答案": answer_text(it).replace("　", " "), "排程": slot, "代碼": it["id"],
                     "練習連結": f"{SITE}/#/item/{it['id']}", "原卷": it.get("_url") or None, "老師已審閱": "__NO__"}
            if p is not None:
                props["全國答對率"] = p / 100
                props["難度"] = "易" if p >= 70 else ("中" if p >= 40 else "難")
            if st.get("D") is not None:
                props["鑑別度"] = st["D"]
            if date:
                props["date:日期:start"] = date.isoformat()
                props["date:日期:is_datetime"] = 0
            rows.append({"qid": q, "properties": props,
                         "content": "\n".join(question_body(it, s, groups, published))})
    return rows


WEEK_SUBJECTS = ["國文", "英文", "數學", "自然", "社會"]  # 數學週同時上數A、數B
WEEK_LABEL = {"數學": "數學（數A＋數B）"}


def db_week_rows():
    _, _, start, _ = plan_info()
    rows = []
    for w in range(1, 17):
        a = start + dt.timedelta(days=7 * (w - 1))
        e = a + dt.timedelta(days=6)
        subj = WEEK_SUBJECTS[(w - 1) % 5] if w < 16 else "總複習"
        props = {"週次": f"W{w} {WEEK_LABEL.get(subj, subj)}", "科目": subj, "date:日期:start": a.isoformat(), "date:日期:end": e.isoformat(),
                 "date:日期:is_datetime": 0, "狀態": "已公布" if w == 1 else "未開始",
                 "每日練習": f"Day {7 * (w - 1) + 1}–{7 * w}"}
        if w == 1:
            props["上課主題"] = "國綜診斷 × 語文知識 × 文言虛詞 × 閱讀研判"
            content = "\n".join(week1_page())
        else:
            props["上課主題"] = "考前全真模擬＋錯題總複習" if w == 16 else "（上課前公布）"
            content = callout("🗓️", [f"{fmt_day(a)}–{fmt_day(e)}｜第 {w} 週：**{WEEK_LABEL.get(subj, subj)}**。上課內容與重點整理會在上課前放上來。"])
        rows.append({"week": w, "properties": props, "content": content})
    return rows


def write_page(name, blocks):
    parts, cur = [], []
    for blk in blocks:
        if cur and sum(len(x) + 1 for x in cur) + len(blk) > PART_LIMIT:
            parts.append(cur)
            cur = []
        cur.append(blk)
    parts.append(cur)
    for old in OUT.glob(f"{name}*.md"):
        old.unlink()
    for i, p in enumerate(parts, 1):
        fn = f"{name}.md" if len(parts) == 1 else f"{name}.part{i}.md"
        (OUT / fn).write_text("\n".join(p) + "\n", encoding="utf-8")
    longest = max(len(ln) for p in parts for blk in p for ln in blk.split("\n"))
    print(f"{name}: {sum(len(x) for p in parts for x in p)} 字、{len(parts)} 段（最長一行 {longest} 字）")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.md"):
        old.unlink()
    write_page("00_home", home_page())
    write_page("01_exam_rules", exam_rules_page())
    write_page("10_chinese", chinese_page())
    write_page("11_english", skeleton_page("english", "英文 100 分鐘：詞彙 10、綜合測驗 10、文意選填 10、篇章結構 8、閱讀測驗 24（選擇共 62 分）＋混合題 10＋中譯英 8＋英文作文 20。", "**第 2 週（10/7–10/13）上課重點**：各大題解題法、高頻詞彙與搭配、翻譯與作文評分重點。完整整理會在上課前放上來。"))
    write_page("12_mathA", skeleton_page("mathA", "數學A 100 分鐘：單選 6 題×5、多選 6 題×5、選填 5 題×5（全對才給分）＋混合題或非選 15 分。", "**第 3 週（10/14–10/20）上課重點**：各單元必考觀念、常見題型與解題流程。完整整理會在上課前放上來。"))
    write_page("12b_mathB", skeleton_page("mathB", "數學B 100 分鐘：單選 7 題×5、多選 5 題×5、選填 5 題×5（全對才給分）＋混合題或非選 15 分。", "**第 3 週（10/14–10/20）上課重點**：數A、數B 共同的觀念，以及數B 特有單元（經緯度、透視、圓錐截痕、數據分析）的解題流程。完整整理會在上課前放上來。"))
    write_page("13_science", skeleton_page("science", "自然 110 分鐘：選擇題（單選＋多選）36 題×2＝72 分＋混合題或非選 56 分，共 128 分；物化生地四科配分相當。", "**第 4 週（10/21–10/27）上課重點**：四科必考觀念、圖表與實驗題解題法。完整整理會在上課前放上來。"))
    write_page("14_social", skeleton_page("social", "社會 110 分鐘：單選 38 題×2＝76 分＋混合題或非選 68 分（115 年，共 144 分）；歷史、地理、公民三科配分相當。", "**第 5 週（10/28–11/3）上課重點**：三科必考觀念、史料與圖表判讀法。完整整理會在上課前放上來。"))
    write_page("20_past_exams", past_exams_page())
    write_page("30_week01", week1_page())  # 每週課程 W1 的頁面內容（分段寫入 Notion 用）
    write_page("40_progress", progress_page())
    write_page("90_teacher", teacher_page())
    q = db_question_rows()
    (OUT / "db_questions.json").write_text(json.dumps(q, ensure_ascii=False, indent=1), encoding="utf-8")
    w = db_week_rows()
    (OUT / "db_weeks.json").write_text(json.dumps(w, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"db_questions: {len(q)} 列、內容 {sum(len(r['content']) for r in q)} 字；db_weeks: {len(w)} 列")


if __name__ == "__main__":
    main()
