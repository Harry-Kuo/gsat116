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
IMAGE_SUBJECTS = {"mathA", "mathB", "science", "social"}  # 題目與題組文章以原卷裁切圖呈現
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
        if m.group(1) == "sup" and t in ("st", "nd", "rd", "th"):
            return t  # 12<sup>th</sup> → 12th
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
    """HTML 表格 → Notion 表格。Notion 表格沒有合併儲存格：rowspan、colspan 先展開成完整格子（文字放在第一格），欄位才會對齊。"""
    cell_re = re.compile(r"<t([dh])([^>]*)>(.*?)</t[dh]>", re.S)
    span = lambda attrs, name: int((re.search(name + r'="(\d+)"', attrs) or [0, 1])[1])
    grid, pending = [], {}  # pending[(列, 欄)]：上方 rowspan 佔用的格子
    for r, row in enumerate(re.findall(r"<tr[^>]*>(.*?)</tr>", h, re.S)):
        cells, out, c = cell_re.findall(row), [], 0
        if not cells:
            continue
        for kind, attrs, text in cells:
            while (r, c) in pending:
                out.append(pending.pop((r, c)))
                c += 1
            rs, cs = span(attrs, "rowspan"), span(attrs, "colspan")
            for dc in range(cs):
                out.append((kind, text if dc == 0 else ""))
                for dr in range(1, rs):
                    pending[(r + dr, c + dc)] = (kind, "")
            c += cs
        while (r, c) in pending:
            out.append(pending.pop((r, c)))
            c += 1
        grid.append(out)
    header = bool(grid) and all(k == "h" for k, _ in grid[0])
    return table([[inline(t) for _, t in r] for r in grid], header=header)


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
    return f"{it['_year']} 學測{paper_name(subject, it['_year'])} " + (it.get("label") or f"第 {it['no']} 題")


def answer_text(it):
    a = str(it.get("answer") or "")
    if it["type"] == "fill":
        names = it.get("cells") or [f"{it['no']}-{i + 1}" for i in range(len(a.split(",")))]
        return "　".join(f"{n}：{v}" for n, v in zip(names, a.split(",")))
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
        if g.get("image") and subject in IMAGE_SUBJECTS:
            body = [f"**{head}**", f"![{head}]({SITE}/{g['image']})"]
        else:
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


def class_days(w, cfg=None):
    """第 w 週的上課日：config.yaml 的 classes（第一次上課日＋每週上課的星期）。"""
    c = (cfg or plan_info()[0])["classes"]
    first = dt.date.fromisoformat(c["first"])
    monday = first - dt.timedelta(days=first.weekday()) + dt.timedelta(weeks=w - 1)
    return [monday + dt.timedelta(days=WEEKDAY.index(x)) for x in c["weekdays"]]


def fmt_class(w, cfg=None):
    return "、".join(fmt_day(d) for d in class_days(w, cfg))


def focus(w, text):
    """各科頁頂端的「第 N 週上課重點」說明。"""
    return f"**第 {w} 週上課重點**：{text}{fmt_class(w)}上課，完整整理會在上課前放上來。"


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
    if any(MAP.get(k) for k, _ in REF_PAGES):
        b += ["## 📚 重點整理", "文言虛詞、15 篇核心古文的原文與白話翻譯，以及月份、節日、年齡、題辭等國學常識，都整理在下面三頁。"]
        b += [f'<page url="{MAP[k]}">{t}</page>' for k, t in REF_PAGES if MAP.get(k)]
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


def skeleton_page(subject, structure, focus, focus_raw=False):
    """focus_raw＝True 時 focus 已是 Notion 格式（含頁面提及），不再跳脫。"""
    _, plan, start, published = plan_info()
    items, _ = load_subject(subject)
    concepts = qyaml.load(ROOT / "data" / "concepts" / f"{subject}.yaml")
    week = [q for d in plan["days"] for q in d["sets"].get(subject) or []]
    b = [callout("🧭", [md_inline(structure)]), callout("📌", [focus if focus_raw else md_inline(focus)], color="yellow_bg")]
    if subject in MATH_REF_PAGES and MAP.get(MATH_REF_PAGES[subject][0]):
        key, title = MATH_REF_PAGES[subject]
        b += ["## 📚 重點整理", "各單元的必背公式、解題流程與容易錯的地方，以及前兩週答對率最低的代表題。", f'<page url="{MAP[key]}">{title}</page>']
    if subject in NOTE_PAGES and any(MAP.get(note_key(subject, m)) for m, _, _ in NOTE_PAGES[subject]):
        b += ["## 📚 重點整理", NOTE_INTRO[subject]]
        b += [f'<page url="{MAP[note_key(subject, m)]}">{t}</page>' for m, t, _ in NOTE_PAGES[subject] if MAP.get(note_key(subject, m))]
    b += ["## 🎯 觀念大綱與每日練習考古題",
          "每個觀念底下列出每日練習做到的考古題；點開可以看題目、答案與解析。"]
    for mod in concepts["modules"]:
        b.append(f"### {esc(mod['name'])}")
        for c in mod["concepts"]:
            line = f"- **{esc(c['name'])}**：{inline(c.get('summary', ''))}"
            qs = [items[q] for q in week if c["id"] in (items[q].get("concepts") or [])]
            if len(qs) > 8:
                qs_lines = [f"\t- 每日練習共 {len(qs)} 題，依日期列在下方「📝 每日練習」。"]
            else:
                qs_lines = [f"\t- {ref(it, subject, published)}" for it in qs]
            b.append("\n".join([line] + qs_lines))
    b.append("## 📝 每日練習")
    for d in plan["days"]:
        qids = d["sets"].get(subject) or []
        if qids:
            date = start + dt.timedelta(days=d["day"] - 1)
            b.append(toggle(f"**Day {d['day']}**　{fmt_day(date)}　{esc(d['theme'].get(subject, ''))}",
                            [f"- {ref(items[q], subject, published)}" for q in qids]))
    return b


def exam_rules_page():
    return convert_md((ROOT / "notion" / "exam_rules.md").read_text(encoding="utf-8"))


def daily_table(plan, start, w):
    """第 w 週的每日練習（Day 7(w−1)+1 到 7w）：每天六科的主題。"""
    subs = list(NAMES)
    rows = [["日期"] + [NAMES[x] for x in subs]]
    for d in plan["days"]:
        if 7 * (w - 1) < d["day"] <= 7 * w:
            date = start + dt.timedelta(days=d["day"] - 1)
            rows.append([f"Day {d['day']}<br>{fmt_day(date)}"] + [esc(d["theme"].get(x, "")) for x in subs])
    return table(rows)


def week_page(w, md_name, subject):
    """每週上課講義（學生看得到）：原稿中的 [[題目:代碼]] 換成完整題目與折疊解析，[[診斷小考]] 換成診斷題，
    [[每日練習表]] 換成這一週的每日練習主題；{{CLASS1}}、{{CLASS2}}、{{CLASS_W7}} 換成上課日期。
    subject 可以是一個科目或科目清單（數學週同時用數A、數B 的題目）。"""
    cfg, plan, start, published = plan_info()
    subjects = [subject] if isinstance(subject, str) else list(subject)
    items, groups, subj_of = {}, {}, {}
    for s in subjects:
        b_items, b_groups = load_subject(s)
        items.update(b_items)
        groups.update(b_groups)
        subj_of.update({q: s for q in b_items})
    subject = subjects[0]
    d1, d2 = class_days(w, cfg)
    doc = (ROOT / "notion" / md_name).read_text(encoding="utf-8").replace("{{SITE}}", SITE) \
        .replace("{{CLASS1}}", fmt_day(d1)).replace("{{CLASS2}}", fmt_day(d2))
    doc = re.sub(r"\{\{CLASS_W(\d+)\}\}", lambda m: fmt_class(int(m.group(1)), cfg), doc)
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
            blocks.append(question_toggle(items[m.group(1)], subj_of[m.group(1)], groups, published, shown))
        elif line.strip() == "[[診斷小考]]":
            flush()
            diag = (plan.get("diag") or {}).get(subject) or []
            dshown = set()
            blocks.append(toggle(f"📝 診斷小考 {len(diag)} 題與解析（做完小考再打開）",
                                 [question_toggle(items[q], subject, groups, published, dshown) for q in diag]))
        elif line.strip() == "[[每日練習表]]":
            flush()
            blocks.append(daily_table(plan, start, w))
        else:
            chunk.append(line)
    flush()
    subs = {"REF_XUCI": mention("ref:xuci", "〈文言虛詞整理〉"), "REF_CORE": mention("ref:core", "〈核心古文 15 篇〉"),
            "REF_EN_VOCAB": mention("ref:en_vocab", "〈常考單字〉"), "REF_EN_PHRASE": mention("ref:en_phrase", "〈轉折語與片語〉"),
            "REF_EN_WRITING": mention("ref:en_writing", "〈混合題與寫作〉"), "REF_EN_CARDS": mention("ref:en_cards", "〈單字卡〉"),
            "REF_EN_CLOZE": mention("ref:en_cloze", "〈克漏字解題〉"), "REF_EN_READING": mention("ref:en_reading", "〈閱讀與篇章結構〉"),
            "REF_EN_ROOTS": mention("ref:en_roots", "〈字首字根字尾〉"), "REF_EN_CONFUSE": mention("ref:en_confuse", "〈易混淆字〉"),
            "REF_MATH_A": mention("ref:mathA_notes", "〈數學A 公式與解題流程〉"), "REF_MATH_B": mention("ref:mathB_notes", "〈數學B 公式與解題流程〉")}
    return [re.sub(r"\\\{\\\{(REF_[A-Z_]+)\\\}\\\}", lambda m: subs[m.group(1)], blk) for blk in blocks]


def week1_page():
    return week_page(1, "week01_chinese.md", "chinese")


def week2_page():
    return week_page(2, "week02_english.md", "english")


def week3_page():
    return week_page(3, "week03_math.md", ["mathA", "mathB"])


# ---------- 數學重點整理：各觀念的必背公式、解題流程、易錯點 ----------
MATH_REF_PAGES = {"mathA": ("ref:mathA_notes", "數學A 公式與解題流程"), "mathB": ("ref:mathB_notes", "數學B 公式與解題流程")}


def math_focus(subject):
    """數學頁頂端的說明：第 3 週講義與重點整理的連結（頁面建立後才會變成提及）。"""
    key, title = MATH_REF_PAGES[subject]
    return (f"**第 3 週上課**（{esc(fmt_class(3))}）的講義、上課練習題與混合題參考答案在 {mention('week:3', '📅 每週課程 W3')}；"
            f"各單元的必背公式、解題流程與容易錯的地方在 {mention(key, '〈' + title + '〉')}。")


def math_notes_page(subject):
    """依觀念列出必背公式、解題流程、易錯點；最後附前兩週（Day 1–14）每日練習中全國答對率最低的題目。"""
    _, plan, _, published = plan_info()
    items, _ = load_subject(subject)
    concepts = qyaml.load(ROOT / "data" / "concepts" / f"{subject}.yaml")
    notes = qyaml.load(REF / "math_notes.yaml")[subject]
    done = [q for d in plan["days"] if d["day"] <= 14 for q in d["sets"].get(subject) or []]
    b = [callout("🧭", ["依單元整理必背公式、解題流程和容易錯的地方。標「考卷附」的公式，考卷最後會附上，但還是要熟到不用查。",
                       "每個觀念最後列出前兩週每日練習中全國答對率最低的題目，點進去可以看題目、答案與解析。"])]
    for mod in concepts["modules"]:
        b.append(f"## {esc(mod['name'])}")
        for c in mod["concepts"]:
            n = notes.get(c["id"])
            if not n:
                continue
            ch = [callout("💡", [inline(c.get("summary", ""))]), "**📌 必背**"]
            ch += [f"- {inline(x)}" for x in n.get("must") or []]
            ch.append("**🧭 解題流程**")
            ch += [f"{i}. {inline(x)}" for i, x in enumerate(n.get("steps") or [], 1)]
            ch.append("**⚠️ 容易錯的地方**")
            ch += [f"- {inline(x)}" for x in n.get("traps") or []]
            qs = sorted((items[q] for q in done if c["id"] in (items[q].get("concepts") or [])
                         and (items[q].get("stats") or {}).get("P") is not None), key=lambda it: it["stats"]["P"])[:3]
            if qs:
                ch.append("**📝 代表題**（前兩週做過、全國答對率最低的題目）")
                ch += [f"- {ref(it, subject, published)}" for it in qs]
            b.append(toggle(f"**{esc(c['name'])}**", ch))
    return b


# ---------- 自然、社會重點整理：每一科（物理、化學、生物、地科；公民、歷史、地理）一頁 ----------
NOTE_PAGES = {
    "science": [("P", "物理重點整理", "🧲"), ("C", "化學重點整理", "🧪"), ("B", "生物重點整理", "🧬"), ("E", "地球科學重點整理", "🌏")],
    "social": [("G", "公民與社會重點整理", "⚖️"), ("H", "歷史重點整理", "📜"), ("D", "地理重點整理", "🗺️")],
}
NOTE_INTRO = {
    "science": "物理、化學、生物、地球科學各一頁：必背觀念、解題步驟、容易錯的地方，以及前兩週答對率最低的代表題。",
    "social": "公民與社會、歷史、地理各一頁：必背觀念、作答步驟、容易錯的地方，以及前兩週答對率最低的代表題。",
}
STEP_TITLE = {"science": "解題步驟", "social": "作答步驟"}


def note_key(subject, mod_id):
    return f"ref:{subject}_{mod_id}"


def notes_page(subject, mod_id):
    """一科（例如物理）的重點整理：每個觀念一個切換區塊，依序是一句話重點、必背、表格、解題步驟、易錯點，
    最後附前兩週（Day 1–14）每日練習中、已放進考古題庫的全國答對率最低題目。"""
    _, plan, _, published = plan_info()
    items, _ = load_subject(subject)
    concepts = qyaml.load(ROOT / "data" / "concepts" / f"{subject}.yaml")
    notes = qyaml.load(REF / f"{subject}_notes.yaml")
    mod = next(m for m in concepts["modules"] if m["id"] == mod_id)
    done = [q for d in plan["days"] if d["day"] <= 14 for q in d["sets"].get(subject) or []]
    b = [callout("🧭", [f"依單元整理{esc(mod['name'])}的必背觀念、{STEP_TITLE[subject]}和容易錯的地方。",
                       "每個觀念最後列出前兩週每日練習中全國答對率最低的題目，點進去可以看題目、答案與解析。"])]
    for c in mod["concepts"]:
        n = notes.get(c["id"])
        if not n:
            continue
        ch = [callout("💡", [inline(n.get("summary") or c.get("summary", ""))]), "**📌 必背**"]
        ch += [f"- {inline(x)}" for x in n.get("must") or []]
        for t in n.get("tables") or []:
            ch += [f"**📋 {inline(t['title'])}**", table([[inline(x) for x in r] for r in t["rows"]])]
        ch.append(f"**🧭 {STEP_TITLE[subject]}**")
        ch += [f"{i}. {inline(x)}" for i, x in enumerate(n.get("steps") or [], 1)]
        ch.append("**⚠️ 容易錯的地方**")
        ch += [f"- {inline(x)}" for x in n.get("traps") or []]
        qs = sorted((items[q] for q in done if c["id"] in (items[q].get("concepts") or [])
                     and (items[q].get("stats") or {}).get("P") is not None and MAP.get(f"q:{q}")),
                    key=lambda it: it["stats"]["P"])[:3]
        if qs:
            ch.append("**📝 代表題**（前兩週做過、全國答對率最低的題目）")
            ch += [f"- {ref(it, subject, published)}" for it in qs]
        b.append(toggle(f"**{esc(n.get('name') or c['name'])}**", ch))
    return b


# ---------- 國文重點整理：文言虛詞、核心古文、國學常識 ----------
REF = ROOT / "data" / "reference"
REF_PAGES = [("ref:xuci", "文言虛詞整理"), ("ref:core", "核心古文 15 篇"), ("ref:guoxue", "國學常識")]


def core_texts():
    """15 篇核心古文：原文（chinese_core_orig.yaml）加上翻譯與重點（chinese_core/NN.yaml），依檔名順序。"""
    orig = {t["title"]: t for t in qyaml.load(REF / "chinese_core_orig.yaml")}
    return [{**orig[n["title"]], **n} for n in (qyaml.load(f) for f in sorted((REF / "chinese_core").glob("*.yaml")))]


def core_hits(title, items):
    """近六屆國綜引用這篇核心古文的題目（依題目的「核心:篇名」標籤）。"""
    return sorted((it for it in items.values() if f"核心:{title}" in (it.get("tags") or [])),
                  key=lambda it: (-int(it["_year"]), int(it["no"])))


def mention(key, fallback):
    return f'<mention-page url="{MAP[key]}"/>' if MAP.get(key) else fallback


def mark(ex):
    """例句中用 [ ] 標出的字改成粗體。"""
    return re.sub(r"\\\[(.+?)\\\]", r"**\1**", esc(ex))


def xuci_page():
    _, _, _, published = plan_info()
    items, _ = load_subject("chinese")
    d = qyaml.load(REF / "chinese_xuci.yaml")
    b = [callout("🔤", [esc(d["intro"])]), "## 答題技巧"] + [f"- {esc(t)}" for t in d["tips"]]
    b += ["## 常考虛詞",
          f"點開每個字，看它的各種用法和例句；例句裡的粗體字就是要判斷的字。例句都出自核心古文，原文和翻譯見 {mention('ref:core', '〈核心古文 15 篇〉')}。"]
    for w in d["words"]:
        b.append(f'### {esc(w["word"])} {{toggle="true"}}')
        for u in w["uses"]:
            line = f"- **{esc(u['use'])}**：「{mark(u['ex'])}」〈{esc(u['src'])}〉"
            b.append(indent(line + (f"（{esc(u['note'])}）" if u.get("note") else "")))
    b.append("## 學測考過的虛詞題")
    b += [f"- {ref(items[q], 'chinese', published)}" for q in d["exams"] if q in items]
    return b


def core_index_page():
    items, _ = load_subject("chinese")
    texts = core_texts()
    rows = [["篇名", "作者", "時代", "近六屆引用"]]
    for t in texts:
        rows.append([mention("core:" + t["title"], f"〈{esc(t['title'])}〉"), esc(t["by"]), esc(t["era"]),
                     f"{len(core_hits(t['title'], items))} 題"])
    b = [callout("📜", ["108 課綱推薦的 15 篇文言文。學測常把核心古文拆成詞義、句式和佐證選項來考，近六屆國綜有很多題目直接引用這些課文。",
                        "每一篇都有題解、原文和逐段白話翻譯、閱讀重點、重要字詞、名句與成語，以及引用這篇課文的考古題。"]),
         table(rows),
         "原文依國語文學科中心「高中國文學習網」，並對照維基文庫與歷屆試題的引文校訂；白話翻譯以好懂為主，字詞解釋以課本注釋為準。",
         "## 15 篇課文"]
    b += [f'<page url="{MAP["core:" + t["title"]]}">{esc(t["title"])}</page>' for t in texts if MAP.get("core:" + t["title"])]
    return b


def core_text_page(t):
    _, _, _, published = plan_info()
    items, _ = load_subject("chinese")
    b = [callout("📜", [f"**{esc(t['by'])}｜{esc(t['era'])}**", esc(t["intro"]), esc(t["author"])]),
         "## 原文與白話翻譯",
         "引文框裡是原文，下面接著是白話翻譯。"]
    for o, tr in zip(t["paras"], t["trans"]):
        b += [f"> {esc(o)}", esc(tr)]
    b.append("## 閱讀重點")
    b += [f"- {esc(x)}" for x in t["focus"]]
    b.append("## 重要字詞")
    b += ["- **{}**：{}".format(*map(esc, w.split("：", 1))) for w in t["words"]]
    b.append("## 名句")
    b += [f"- {esc(q)}" for q in t["quotes"]]
    if t.get("idioms"):
        b.append("## 出自本文的成語與典故")
        b += ["- **{}**：{}".format(*map(esc, x.split("：", 1))) for x in t["idioms"]]
    hits = core_hits(t["title"], items)
    if hits:
        b.append(f"## 近六屆引用本文的考古題（{len(hits)} 題）")
        b += [f"- {ref(it, 'chinese', published)}" for it in hits]
    b.append(f"原文出處：[國語文學科中心高中國文學習網]({t['source']})")
    return b


def guoxue_page():
    return convert_md((ROOT / "notion" / "chinese_guoxue.md").read_text(encoding="utf-8"))


# ---------- 英文：考科頁與重點整理（常考單字、轉折語與片語、混合題與寫作） ----------
EN_REF_PAGES = [("ref:en_cards", "單字卡"), ("ref:en_vocab", "常考單字"), ("ref:en_roots", "字首字根字尾"), ("ref:en_confuse", "易混淆字"),
                ("ref:en_cloze", "克漏字解題"), ("ref:en_phrase", "轉折語與片語"), ("ref:en_reading", "閱讀與篇章結構"), ("ref:en_writing", "混合題與寫作")]
EN_FEATURED = {"V1": ["eng111-09", "eng110-09", "eng110-10", "eng110-15"]}
YEARS = range(115, 109, -1)


def en_qref(q, items, published):
    """重點整理裡的出處：已入考古題庫就用頁面提及，否則只寫年度題號。"""
    it = items.get(q)
    if not it:
        return ""
    return ref(it, "english", published) if MAP.get(f"q:{q}") else f"{it['_year']} 年第 {it['no']} 題"


def en_level(w):
    """大考詞彙表級別：單字本身在表上就標級別；衍生字標原形；片語不標。"""
    from wordlist import table
    t = table()
    word = w["word"].lower()
    if word in t:
        return f"第 {t[word][1]} 級"
    base = (w.get("base") or "").lower()
    if base and base in t:
        return f"由 {esc(w['base'])}（第 {t[base][1]} 級）衍生"
    return "" if " " in word else "詞彙表未收"


def en_word_line(q, w, items, published):
    lv = en_level(w)
    head = f"**{esc(w['word'])}** *{esc(w['pos'])}* {esc(w['mean'])}" + (f"（{lv}）" if lv else "")
    parts = [head + (f"：{esc(w['use'])}" if w.get("use") else "")]
    if w.get("confuse"):
        parts.append("易混淆：" + "、".join(esc(c) for c in w["confuse"]))
    src_ = en_qref(q, items, published)
    return "- " + "｜".join(parts) + (f"　→ {src_}" if src_ else "")


def wordlist_note():
    from wordlist import URL
    return (f"級別依大學入學考試中心[〈高中英文參考詞彙表〉（111 學年度起適用）]({URL})標註（第 1–6 級，數字越大越難）。"
            "著作權屬財團法人大學入學考試中心基金會所有，僅供非營利目的使用，轉載請註明出處。")


def en_vocab_page():
    _, _, _, published = plan_info()
    items, _ = load_subject("english")
    d = qyaml.load(REF / "english_words.yaml")
    b = [callout("🔤", ["這一頁整理近六屆（110–115 年）學測英文**詞彙題**與**文意選填**的正確答案：意思、常見搭配與大考詞彙表級別；詞彙題另外列出全國考生最常誤選的字。"]),
         "## 怎麼用這一頁",
         "- 先看搭配：學測常考固定搭配，例如 a tight schedule、grave concerns、stand the test of time。",
         "- 「易混淆」是誤選率最高的選項：想一想它為什麼不能填，比多背一個字更有用。",
         "- 近六屆詞彙題的答案近九成（65 題中有 57 題）是第 3–5 級的字，背單字時以這三級為主。",
         "## 詞彙題（第 1–10 題）的正確答案"]
    for y in YEARS:
        rows = [en_word_line(q, w, items, published) for q, w in d["vocab"].items() if q.startswith(f"eng{y}-")]
        if rows:
            b.append(toggle(f"**{y} 年**（{len(rows)} 題）", rows))
    b.append("## 文意選填（第 21–30 題）的正確答案")
    b.append("文意選填的 10 個選項要依詞性分類；下面列出每一格的正確答案，括號是詞性與意思。")
    for y in YEARS:
        rows = [en_word_line(q, w, items, published) for q, w in d["fill"].items() if q.startswith(f"eng{y}-")]
        if rows:
            b.append(toggle(f"**{y} 年**（{len(rows)} 題）", rows))
    b += ["## 資料來源", "- 正確答案與誤選率：大考中心各年度學測英文考科試題、答案與選項分析。", "- " + wordlist_note()]
    return b


def en_phrase_page():
    _, _, _, published = plan_info()
    items, _ = load_subject("english")
    d = qyaml.load(REF / "english_words.yaml")
    line = lambda q, key, v: f"- **{esc(v[key])}**：{esc(v['mean'])}" + (f"　→ {en_qref(q, items, published)}" if en_qref(q, items, published) else "")
    b = [callout("🔗", ["綜合測驗（第 11–20 題）近六屆 65 題中，**轉折語、文法、片語搭配**三類的答對率最低（42%–43%）。這一頁整理轉折語的分類，以及近六屆考過的轉折語、片語與文法考點。"]),
         "## 轉折語怎麼選",
         "先判斷空格前後兩句的關係，再從對應的一類裡選：",
         table([["關係", "常用轉折語"]] + [[esc(t["kind"]), esc(t["words"])] for t in d["transitions"]]),
         "## 近六屆考過的轉折語"]
    b += [line(q, "phrase", v) for q, v in d["transition_items"].items()]
    b.append("## 近六屆考過的片語搭配")
    b += [line(q, "phrase", v) for q, v in d["phrase_items"].items()]
    b.append("## 近六屆考過的文法考點")
    b += [line(q, "point", v) for q, v in d["grammar_items"].items()]
    b += ["## 資料來源", "- 大考中心各年度學測英文考科試題、答案與答對率。"]
    return b


def en_writing_page():
    x = qyaml.load(REF / "english_writing.yaml")
    mx, tr, es = x["mixed"], x["translation"], x["essay"]
    b = [callout("✍️", ["非選擇題共 38 分：混合題 10 分、中譯英 8 分、英文作文 20 分。這一頁整理評分方式、近五屆題目與得分重點；評分原則出自大考中心各年度〈英文考科非選擇題閱卷評分原則說明〉。"]),
         "## 混合題（10 分）", esc(mx["intro"])]
    b += [f"- {esc(r)}" for r in mx["rules"]]
    b.append(toggle("近五屆混合題", [f"- **{h['year']} 年**：{esc(h['text'])}" for h in mx["history"]]))
    b += ["## 中譯英（8 分）"] + [f"- {esc(r)}" for r in tr["rules"]]
    b.append("近五屆考題與官方參考答案（括號內是也可以接受的寫法）。先自己翻，再打開對照：")
    for y in YEARS:
        its = [t for t in tr["items"] if t["year"] == y]
        if its:
            b.append(toggle(f"**{y} 年**", [ln for t in its for ln in (f"{t['n']}. {esc(t['zh'])}",
                                                                        f"\t- 參考答案：{esc(t['en'])}",
                                                                        f"\t- 提醒：{esc(t['tip'])}")]))
    b.append(f"- {esc(es['scores_115']['translation'])}")
    b += ["## 英文作文（20 分）"] + [f"- {esc(r)}" for r in es["rules"]]
    b.append(table([["評分項目", "高分的表現"]] + [[esc(r["item"]), esc(r["good"])] for r in es["rubric"]]))
    b.append(toggle("近五屆作文題目", [f"- **{p_['year']} 年**：{esc(p_['text'])}" for p_ in es["prompts"]]))
    b.append(f"- {esc(es['scores_115']['essay'])}")
    b += ["### 寫作提醒"] + [f"{i}. {esc(t)}" for i, t in enumerate(es["tips"], 1)]
    b += ["## 資料來源", "- 大考中心各年度〈英文考科非選擇題閱卷評分原則說明〉與試題。",
          "- 得分分布：大考中心公布的 115 學年度學測英文非選擇題各題得分人數百分比。"]
    return b


# ---------- 英文：單字卡（依級別分 Unit，點開看意思）與解題技巧頁 ----------
EN_CARD_PAGES = [("ref:en_cards_l12", "第 1–2 級（基礎字）", (1, 2)), ("ref:en_cards_l3", "第 3 級", (3,)),
                 ("ref:en_cards_l4", "第 4 級", (4,)), ("ref:en_cards_l56", "第 5–6 級與詞表外", (5, 6, None))]
EN_ROLE = {("V1", True): "詞彙題答案", ("V1", False): "詞彙題選項", ("R1", True): "文意選填答案",
           ("V2", True): "綜合測驗答案", ("V2", False): "綜合測驗選項"}
UNIT = 20


def en_cards():
    """近六屆詞彙題四個選項、文意選填答案、綜合測驗「詞彙」類選項 → 依原形整理的單字卡。
    答案字沿用 english_words.yaml 的意思與搭配，其他字用 english_cards.yaml。"""
    import wordlist
    t = wordlist.table()
    words = qyaml.load(REF / "english_words.yaml")
    extra = qyaml.load(REF / "english_cards.yaml")
    alias, cards = extra["alias"], extra["cards"]
    known = {}
    for q, w in list(words["vocab"].items()) + list(words["fill"].items()):
        known.setdefault(w["word"].lower(), []).append(w)
    tags = qyaml.load(ROOT / "data" / "concepts" / "english_tags.yaml")
    items, _ = load_subject("english")

    def lemma(form):
        f = form.lower().strip()
        f = alias.get(f, f)
        if f in known or f in cards:
            return f
        for stem, pos in wordlist._stems(f):
            if (stem in known or stem in cards) and (stem not in t or pos is None or pos in t[stem][0]):
                return stem
        return f

    out, missing = {}, []
    for q in sorted(items, key=lambda q: (-int(items[q]["_year"]), int(items[q]["no"]))):
        it, tg = items[q], tags.get(q) or [None]
        opts = it.get("options") or {}
        if tg[0] == "V1":
            picks = [(v, k == it["answer"]) for k, v in opts.items()]
        elif tg[0] == "R1":
            picks = [(opts.get(it["answer"]), True)]
        elif tg[0] == "V2" and "詞彙" in tg:
            picks = [(v, k == it["answer"]) for k, v in opts.items()]
        else:
            continue
        for form, is_ans in picks:
            form = str(form or "").strip()
            if not re.fullmatch(r"[A-Za-z][A-Za-z' \-]*", form):
                continue
            lm = words["vocab"][q]["word"].lower() if tg[0] == "V1" and is_ans and q in words["vocab"] else lemma(form)
            if lm not in known and lm not in cards:
                missing.append((q, form))
                continue
            c = out.setdefault(lm, {"word": lm, "forms": set(), "refs": []})
            if form.lower() != lm:
                c["forms"].add(form.lower())
            c["refs"].append((it, EN_ROLE[(tg[0], is_ans)]))
    for lm, c in out.items():
        ws = (known.get(lm) or []) + ([cards[lm]] if lm in cards else [])  # 答案字的解釋在前，其他題目的用法接在後面
        c["pos"] = "／".join(dict.fromkeys(w["pos"] for w in ws))
        c["mean"] = "；".join(dict.fromkeys(w["mean"] for w in ws))
        c["use"] = "／".join(dict.fromkeys(w["use"] for w in ws if w.get("use")))
        c["confuse"] = [x for w in ws for x in w.get("confuse") or []]
        base = next((w.get("base") for w in ws if w.get("base")), None)
        c["level"] = t[lm][1] if lm in t else None
        c["base"] = base if c["level"] is None and base and base.lower() in t else None
        c["base_level"] = t[base.lower()][1] if c["base"] else None
        c["phrase"] = " " in lm
    if missing:
        print("單字卡找不到解釋：", missing)
    return out


def en_card_group(c):
    if c["phrase"]:
        return None
    lv = c["level"] or c["base_level"]
    return next(k for k, _, lvs in EN_CARD_PAGES if lv in lvs)


def en_card_toggle(c):
    lines = [f"**{esc(c['mean'])}**"]
    if c["use"]:
        lines.append(f"例：{esc(c['use'])}")
    if c["forms"]:
        lines.append("考題中的寫法：" + "、".join(esc(f) for f in sorted(c["forms"])))
    if c["base"]:
        lines.append(f"由 {esc(c['base'])}（第 {c['base_level']} 級）衍生")
    if c["confuse"]:
        lines.append("易混淆：" + "、".join(esc(x) for x in c["confuse"]))
    seen = list(dict.fromkeys(f"{it['_year']} 年第 {it['no']} 題（{role}）" for it, role in c["refs"]))
    lines.append("出處：" + "；".join(seen))
    return toggle(f"**{esc(c['word'])}**　*{esc(c['pos'])}*", lines)


def en_cards_level_page(key):
    cards = sorted((c for c in en_cards().values() if en_card_group(c) == key), key=lambda c: c["word"])
    title = next(t for k, t, _ in EN_CARD_PAGES if k == key)
    n_units = max(1, -(-len(cards) // UNIT))
    size = -(-len(cards) // n_units)
    b = [callout("📇", [f"**{title}**：{len(cards)} 個字，分成 {n_units} 個 Unit。看到英文先在心裡說出中文意思和一個搭配，再點開確認；每個 Unit 最後有總表可以快速複習。"])]
    for u in range(n_units):
        chunk = cards[u * size:(u + 1) * size]
        if not chunk:
            continue
        b.append(f"## Unit {u + 1}｜{esc(chunk[0]['word'])} – {esc(chunk[-1]['word'])}")
        b += [en_card_toggle(c) for c in chunk]
        b.append(toggle(f"📋 Unit {u + 1} 總表（複習用）",
                        [table([["單字", "詞性", "意思"]] + [[f"**{esc(c['word'])}**", esc(c["pos"]), esc(c["mean"])] for c in chunk])]))
    b += ["## 資料來源", "- 單字取自大考中心 110–115 學年度學測英文考科試題（詞彙題、文意選填、綜合測驗）。", "- " + wordlist_note()]
    return b


def en_cards_index_page():
    cards = en_cards()
    count = {k: sum(1 for c in cards.values() if en_card_group(c) == k) for k, _, _ in EN_CARD_PAGES}
    phrases = sorted((c for c in cards.values() if c["phrase"]), key=lambda c: c["word"])
    b = [callout("📇", [f"近六屆（110–115 年）學測英文考過的 **{len(cards)} 個單字與片語**，做成可以自己測驗的單字卡：看到英文先想中文，再點開確認。",
                       "收錄範圍：詞彙題的四個選項、文意選填的答案，以及綜合測驗「詞彙」類題目的選項；級別依大考中心〈高中英文參考詞彙表〉。"]),
         "## 怎麼背",
         "1. 每天背 1 個 Unit（約 20 字），利用等車、下課的零碎時間。",
         "2. 看英文，先在心裡說出中文意思和一個搭配，再點開確認；想不起來的字記在筆記本或手機備忘錄。",
         "3. 隔天先把前一天的 Unit 再測一次；三天後、一週後各再測一次。",
         "4. 每個 Unit 最後有「總表」，搭車時可以快速掃過整個 Unit。",
         "5. 建議順序：先快速掃過第 1–2 級（不熟的字才背），再依序背第 3 級、第 4 級、第 5–6 級。學測詞彙題的答案近九成是第 3–5 級的字。",
         "## 依級別分頁"]
    b += [f"- {t}：{count[k]} 個字" for k, t, _ in EN_CARD_PAGES]
    b += [f'<page url="{MAP[k]}">{t}</page>' for k, t, _ in EN_CARD_PAGES if MAP.get(k)]
    if phrases:
        b += ["## 文意選填考過的片語"] + [en_card_toggle(c) for c in phrases]
    b += ["## 資料來源", "- 單字取自大考中心 110–115 學年度學測英文考科試題（詞彙題、文意選填、綜合測驗）。", "- " + wordlist_note()]
    return b


def en_type_stats(kind):
    """依 english_tags 計算某大題各類型的題數與全國平均答對率：{類型: (題數, 平均答對率)}。"""
    items, _ = load_subject("english")
    tags = qyaml.load(ROOT / "data" / "concepts" / "english_tags.yaml")
    acc = {}
    for q, tg in tags.items():
        p = (items.get(q, {}).get("stats") or {}).get("P")
        if tg and tg[0] == kind and p is not None:
            acc.setdefault(tg[1] if len(tg) > 1 else "", []).append(p)
    return {k: (len(v), round(sum(v) / len(v))) for k, v in acc.items()}


def en_src(q):
    m = re.match(r"eng(\d+)-(\d+)", q or "")
    return f"{m.group(1)} 年第 {int(m.group(2))} 題" if m else ""


def en_cloze_page():
    s = qyaml.load(REF / "english_skills.yaml")
    st, fill, total = en_type_stats("V2"), en_type_stats("R1").get("", (0, 0)), sum(n for n, _ in en_type_stats("V2").values())
    avg = round(sum(n * p for n, p in st.values()) / total) if total else 0
    b = [callout("🧩", [f"綜合測驗（第 11–20 題）與文意選填（第 21–30 題）各 10 分；近六屆綜合測驗 {total} 題平均答對率 {avg}%、文意選填 {fill[0]} 題平均答對率 {fill[1]}%。兩大題的解題方法熟了，是最快拉分的地方。"]),
         "## 綜合測驗：四個步驟"] + [f"{i}. {esc(x)}" for i, x in enumerate(s["cloze_steps"], 1)]
    b += ["## 五類考點與線索",
          table([["類型", "近六屆", "全國答對率", "線索在哪裡", "學測例子"]]
                + [[f"**{esc(k)}**", f"{st.get(k, (0, 0))[0]} 題", f"{st.get(k, (0, 0))[1]}%", esc(clue), esc(ex)] for k, clue, ex in s["cloze_types"]])]
    b.append("## 文法考點速查")
    for point, how, ex, q in s["cloze_grammar"]:
        b.append(f"- **{esc(point)}**：{esc(how)}")
        b.append(f"\t- 例：{esc(ex)}" + (f"（{en_src(q)}）" if q else "（自編例句）"))
    b += ["## 常見陷阱"] + [f"- {esc(x)}" for x in s["cloze_traps"]]
    b += ["## 文意選填：先判斷詞性",
          "1. 把 10 個選項依詞性分類：名詞、動詞（注意原形、過去式、V-ing）、形容詞、副詞。",
          "2. 看空格的位置決定需要的詞性（見下表），每一格通常只剩 3–4 個選項。",
          "3. 再用單複數、時態與文意決定；最有把握的先填，用過的劃掉。",
          table([["空格的位置", "需要的詞性"]] + [[esc(a), esc(b_)] for a, b_ in s["fill_positions"]])]
    b += ["## 練習",
          f"- 近六屆考過的轉折語、片語與文法考點：{mention('ref:en_phrase', '〈轉折語與片語〉')}",
          f"- 文意選填與詞彙題的答案字：{mention('ref:en_vocab', '〈常考單字〉')}",
          "## 資料來源", "- 題數與答對率：大考中心 110–115 學年度學測英文考科試題與答對率統計。"]
    return b


def en_reading_page():
    s = qyaml.load(REF / "english_skills.yaml")
    st, r2 = en_type_stats("R3"), en_type_stats("R2").get("", (0, 0))
    total = sum(n for n, _ in st.values())
    avg = round(sum(n * p for n, p in st.values()) / total) if total else 0
    b = [callout("📖", ["閱讀測驗（第 35–46 題）12 題 24 分＋篇章結構（第 31–34 題）4 題 8 分，共 32 分，占選擇題 62 分的一半以上。",
                       f"近六屆閱讀測驗 {total} 題平均答對率 {avg}%、篇章結構 {r2[0]} 題平均答對率 {r2[1]}%。"]),
         "## 閱讀測驗的作答順序",
         "1. 先看題目（先不看選項），圈出關鍵字：人名、年代、數字、專有名詞。",
         "2. 讀文章時，在和題目有關的句子旁做記號。",
         "3. 每個選項都回原文找依據，再用刪去法。",
         "## 題型與解法"]
    for kind, ask, how in s["reading_types"]:
        n, p = st.get(kind, (0, 0))
        b.append(f"- **{esc(kind)}**（近六屆 {n} 題，全國答對率 {p}%）")
        b.append(f"\t- 問法：{esc(ask)}")
        b.append(f"\t- 做法：{esc(how)}")
    b += ["## 刪去法：看到這些就刪"] + [f"- {esc(x)}" for x in s["eliminate"]]
    b += ["## 題目常見的字",
          table([["英文", "中文"]] + [[f"**{esc(a)}**", esc(c)] for a, c in s["stem_words"]]),
          "態度、語氣題常見的形容詞：",
          table([["英文", "中文"]] + [[f"**{esc(a)}**", esc(c)] for a, c in s["attitude_words"]])]
    b += ["## 篇章結構（第 31–34 題）",
          "- 4 個空格，每題 2 分。111–114 年是 4 個句子剛好各用一次；115 年改成 5 個句子選 4 個，有 1 個多餘。",
          "### 線索"] + [f"- **{esc(a)}**：{esc(c)}" for a, c in s["structure_clues"]]
    b += ["### 作答步驟"] + [f"{i}. {esc(x)}" for i, x in enumerate(s["structure_steps"], 1)]
    b += ["## 時間分配",
          "- 篇章結構約 6 分鐘、閱讀測驗約 25 分鐘（三篇各約 8 分鐘）；卡住的題目先跳過，最後再回來。",
          "## 資料來源", "- 題數與答對率：大考中心 110–115 學年度學測英文考科試題與答對率統計。"]
    return b


def en_roots_page():
    s = qyaml.load(REF / "english_skills.yaml")
    tbl = lambda head, rows: table([head] + [[f"**{esc(a)}**", esc(m), esc(e)] for a, m, e in rows])
    return [callout("🌱", ["學測閱讀常出現詞彙表以外的字。認識常見的字首、字根、字尾，就能先拆字猜意思，再用上下文確認。",
                          "★ 表示這個字在近六屆（110–115 年）學測英文考題中出現過。"]),
            "## 怎麼拆字",
            "- unproductive＝un（不）＋product（生產）＋ive（形容詞）→ 沒有生產力的。",
            "- vacancy＝vac（空）＋ancy（名詞）→ 空缺、職缺。",
            "- disrupt＝dis（分開）＋rupt（破裂）→ 擾亂、使中斷。",
            "- 拆字只能幫你猜方向，最後一定要放回句子確認意思。",
            f"## 字首（{len(s['prefixes'])} 個）", tbl(["字首", "意思", "例字"], s["prefixes"]),
            f"## 字根（{len(s['roots'])} 個）", tbl(["字根", "意思", "例字"], s["roots"]),
            f"## 字尾（{len(s['suffixes'])} 個）", tbl(["字尾", "詞性與意思", "例字"], s["suffixes"]),
            "## 資料來源", "- 標 ★ 的例字出自大考中心 110–115 學年度學測英文考科試題。"]


def en_confuse_page():
    s = qyaml.load(REF / "english_skills.yaml")
    items, _ = load_subject("english")
    words = qyaml.load(REF / "english_words.yaml")["vocab"]
    cards = en_cards()
    by_form = {f: c for c in cards.values() for f in c["forms"] | {c["word"]}}
    hard = []
    for q, w in words.items():
        it = items.get(q)
        stats = (it or {}).get("stats") or {}
        if not it or stats.get("P") is None or not stats.get("opt"):
            continue
        wrong = max(((k, v) for k, v in stats["opt"].items() if k != it["answer"]), key=lambda kv: kv[1], default=None)
        if wrong:
            hard.append((stats["P"], q, it, w, (it.get("options") or {}).get(wrong[0]), wrong[1]))
    hard.sort(key=lambda x: x[0])
    rows = [["題目", "正確答案", "最多人誤選", "全國答對率"]]
    for p, q, it, w, opt, pct in hard[:12]:
        c = by_form.get(str(opt).lower()) or {}
        rows.append([f"{it['_year']} 年第 {it['no']} 題", f"**{esc(w['word'])}** {esc(w['mean'])}　{esc(w.get('use', ''))}",
                     f"{esc(opt)}" + (f" {esc(c['mean'])}" if c.get("mean") else "") + f"（{pct}%）", f"{p}%"])
    return [callout("⚖️", ["拼字相近、意思相近或用法容易搞混的字。考試時選錯，常常不是不認識，而是把兩個字弄混了。",
                          "★ 表示這個字在近六屆（110–115 年）學測英文考題中出現過。"]),
            "## 拼字相近的字"] + [f"- **{esc(a)}**：{esc(m)}" for a, m in s["confuse"]] + \
           ["## 用法容易搞混的字"] + [f"- **{esc(a)}**：{esc(m)}" for a, m in s["usage"]] + \
           ["## 詞彙題最常選錯的 12 題",
            "答對率最低的 12 題詞彙題，以及全國考生最常誤選的選項。想一想誤選的字為什麼不能填，比多背一個字更有用。",
            table(rows),
            "## 資料來源", "- 答對率與選項選答率：大考中心 110–115 學年度學測英文考科答對率與選項分析。"]


def english_page():
    cfg, plan, start, published = plan_info()
    items, groups = load_subject("english")
    concepts = qyaml.load(ROOT / "data" / "concepts" / "english.yaml")
    wk = mention("week:2", "📅 每週課程 W2")
    b = [callout("🧭", ["**考科結構**：英文 100 分鐘、滿分 100 分＝選擇題 62 分（詞彙 10、綜合測驗 10、文意選填 10、篇章結構 8、閱讀測驗 24）＋混合題 10 分＋中譯英 8 分＋英文作文 20 分。",
                       "115 年英文級距 6.1 分：差 6 題詞彙題或 3 題閱讀題，大約就差 1 級分。"])]
    if any(MAP.get(k) for k, _ in EN_REF_PAGES):
        b += ["## 📚 重點整理",
              "- **背單字**：從「單字卡」開始（近六屆考過的字，依級別分 Unit，點開看意思）；「常考單字」依年度列出每一題的答案，「字首字根字尾」「易混淆字」幫你猜字、分辨相近的字。",
              "- **綜合測驗、文意選填**：看「克漏字解題」（題型、線索、文法速查），考過的轉折語與片語在「轉折語與片語」。",
              "- **閱讀測驗、篇章結構**：看「閱讀與篇章結構」（題型、刪去法、題目常見的字）；非選擇題看「混合題與寫作」。"]
        b += [f'<page url="{MAP[k]}">{t}</page>' for k, t in EN_REF_PAGES if MAP.get(k)]
    b += ["## 📈 近六屆出題趨勢（110–115）",
          "- **各大題平均答對率**：詞彙 50%、綜合測驗 46%、文意選填 46%、篇章結構 50%、閱讀測驗 56%。閱讀測驗 12 題共 24 分，是選擇題配分最重的大題。",
          "- **綜合測驗**考點分五類：詞彙 22 題、片語搭配 15 題、文法 11 題、轉折語 10 題、語意 7 題；轉折語、文法、片語搭配的答對率最低（42%–43%）。",
          "- **閱讀測驗**以細節題最多（35 題，答對率 57%）；段落結構題（作者怎麼安排文章）答對率最低，只有 45%。",
          "- **詞彙題**的答案近九成是大考詞彙表第 3–5 級的字。",
          "- **混合題**的多選題近五屆全對率只有 7%–37%；**作文**115 年 12 分以上約 22%、15 分以上約 5%。",
          "## 🎯 必考觀念與對應考古題",
          f"第 2 週上課的講義與 115 年逐題解析在 {wk}。每個觀念下面列出已經排進每日練習的考古題，點進去可以看題目、答案與解析。"]
    for mod in concepts["modules"]:
        b.append(f"### {mod['id']}. {esc(mod['name'])}")
        for c in mod["concepts"]:
            related = sorted((it for it in items.values() if c["id"] in (it.get("concepts") or [])),
                             key=lambda it: (-int(it["_year"]), int(it["no"])))
            ch = [callout("💡", [inline(c.get("summary", ""))])] + [f"- {inline(pt)}" for pt in c.get("points") or []]
            feat = [items[q] for q in EN_FEATURED.get(c["id"], []) if q in items]
            if feat:
                ch.append("**📝 上課練習題**")
                ch += [question_toggle(it, "english", groups, published, set()) for it in feat]
            done = [it for it in related if MAP.get(f"q:{it['id']}")]
            if done:
                ch.append(toggle(f"已排進每日練習的考古題（{len(done)} 題）", [f"- {ref(it, 'english', published)}" for it in done]))
            if c["id"] in ("M1", "W1", "W2"):
                ch.append(f"評分方式、近五屆題目與參考答案整理在 {mention('ref:en_writing', '〈混合題與寫作〉')}。")
            b.append(toggle(f"**{c['id']} {esc(c['name'])}**" + (f"（近六屆 {len(related)} 題）" if related else ""), ch))
    b.append("## 📝 每日練習")
    for d in plan["days"]:
        qids = d["sets"].get("english") or []
        if qids:
            date = start + dt.timedelta(days=d["day"] - 1)
            b.append(toggle(f"**Day {d['day']}**　{fmt_day(date)}　{esc(d['theme'].get('english', ''))}",
                            [f"- {ref(items[q], 'english', published)}" for q in qids]))
    return b



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
            "- 每天「基本 5 題」走六屆主線；「加練」由網站自動排入錯題（1、3、7 天後再出現）。"] + \
           [f"- {NAMES[s]}另排了 {sched['pools'][s]['extra']} 題 109 年學測（109、110 年數學只有一份試卷，數學A、數學B 各排不同的題目），不算在上表。"
            for s in NAMES if sched["pools"][s].get("extra")] + [
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
    w2 = f'<mention-page url="{MAP["week:2"]}"/>' if MAP.get("week:2") else "📅 每週課程 W2"
    w3 = f'<mention-page url="{MAP["week:3"]}"/>' if MAP.get("week:3") else "📅 每週課程 W3"
    return [f'<embed src="{SITE}/countdown.html">距離 116 學測倒數</embed>',
            callout("📌", ["**116 學測：2027/1/22（五）–1/24（日）**｜每日快答 **9/30（三）Day 1** 開始，每天每科 5 題，12/31 前做完近六屆經典題。",
                          f"👉 [打開今日練習]({SITE}/)（手機用瀏覽器打開後選「加入主畫面」，之後像 App 一樣一鍵開啟）"], color="orange_bg"),
            "## 📣 上課安排",
            f"- **W1 國文**｜{fmt_class(1, cfg)}｜國綜診斷 × 語文知識 × 文言虛詞 × 閱讀研判 → {w1}",
            f"- **W2 英文**｜{fmt_class(2, cfg)}｜{WEEK_TOPIC[2]} → {w2}",
            f"- **W3 數學**｜{fmt_class(3, cfg)}｜{WEEK_TOPIC[3]} → {w3}",
            f"- 每週二、四各上課 {cfg['classes']['hours']:g} 小時，國→英→數→自→社輪替，課程到 1/14（W16 總複習）；各週主題見「📅 每週課程」。",
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
            "- 老師自己的測試代碼可以自訂（不要用學生的代碼）；測試留下的紀錄可以在「作答紀錄」直接刪除，學生的裝置下次同步時也會一併移除。",
            "- 同一個代碼在手機、電腦登入，作答進度會自動合併（網站開啟、切回分頁或按「立即同步」時從試算表取回）。",
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
            props = {"題目": f"{it['_year']} {paper_name(s, it['_year'])} " + (it.get("label") or f"第 {it['no']} 題") + f"｜{cname.get(it.get('topic'), '')}",
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
WEEK_TOPIC = {1: "國綜診斷 × 語文知識 × 文言虛詞 × 閱讀研判",
              2: "英文考科結構 × 詞彙 × 綜合測驗 × 文意選填 × 篇章結構 × 閱讀測驗",
              3: "數A、數B 考科結構 × 代數 × 幾何 × 向量與矩陣 × 機率統計與計數 × 混合題"}
WEEK_PAGES = {1: week1_page, 2: week2_page, 3: week3_page}


def db_week_rows():
    """每週課程：日期＝該週上課日（週二、週四）；每日練習＝上課後的 7 天（到學測前一天為止）。"""
    cfg, _, start, _ = plan_info()
    last = (dt.date.fromisoformat(cfg["exam"]["days"][0]) - start).days  # 學測前一天是 Day last
    rows = []
    for w in range(1, cfg["classes"]["weeks"] + 1):
        days = class_days(w, cfg)
        if w <= 15:
            subj = WEEK_SUBJECTS[(w - 1) % 5]
            label, topic = WEEK_LABEL.get(subj, subj), "（上課前公布）"
        elif w == 16:
            subj, label, topic = "總複習", "總複習", "考前全真模擬＋錯題總複習"
        else:
            subj, label, topic = "總複習", "考前衝刺", "考前最後複習＋考場提醒"
        props = {"週次": f"W{w} {label}", "科目": subj, "date:日期:start": days[0].isoformat(), "date:日期:end": days[-1].isoformat(),
                 "date:日期:is_datetime": 0, "狀態": "已公布" if w in WEEK_PAGES else "未開始",
                 "每日練習": f"Day {7 * (w - 1) + 1}–{min(7 * w, last)}"}
        if w in WEEK_PAGES:
            props["上課主題"] = WEEK_TOPIC[w]
            content = "\n".join(WEEK_PAGES[w]())
        else:
            props["上課主題"] = topic
            content = callout("🗓️", [f"{fmt_class(w, cfg)}上課｜第 {w} 週：**{label}**。上課內容與重點整理會在上課前放上來。"])
        rows.append({"week": w, "properties": props, "content": content})
    return rows


def write_page(name, blocks, limit=PART_LIMIT, first_alone=False):
    """first_alone＝True：第 1 段只放第一個區塊（建立頁面用），其餘內容分段接在頁面最後。"""
    parts, cur = [], []
    for i, blk in enumerate(blocks):
        if cur and (sum(len(x) + 1 for x in cur) + len(blk) > limit or (first_alone and i == 1)):
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
    write_page("11_english", english_page())
    write_page("18_en_vocab", en_vocab_page())
    write_page("18_en_phrase", en_phrase_page())
    write_page("18_en_writing", en_writing_page())
    write_page("19_en_cards", en_cards_index_page())
    for k, _, _ in EN_CARD_PAGES:
        write_page("19_en_cards_" + k.split("_")[-1], en_cards_level_page(k))
    write_page("19_en_roots", en_roots_page())
    write_page("19_en_confuse", en_confuse_page())
    write_page("19_en_cloze", en_cloze_page())
    write_page("19_en_reading", en_reading_page())
    write_page("12_mathA", skeleton_page("mathA", "數學A 100 分鐘：單選 6 題×5、多選 6 題×5、選填 5 題×5（全對才給分）＋混合題或非選 15 分。", math_focus("mathA"), focus_raw=True))
    write_page("12b_mathB", skeleton_page("mathB", "數學B 100 分鐘：單選 7 題×5、多選 5 題×5、選填 5 題×5（全對才給分）＋混合題或非選 15 分。", math_focus("mathB"), focus_raw=True))
    write_page("12c_mathA_notes", math_notes_page("mathA"))
    write_page("12d_mathB_notes", math_notes_page("mathB"))
    write_page("13_science", skeleton_page("science", "自然 110 分鐘：選擇題（單選＋多選）36 題×2＝72 分＋混合題或非選 56 分，共 128 分；物化生地四科配分相當。", focus(4, "四科必考觀念、圖表與實驗題解題法。")))
    write_page("14_social", skeleton_page("social", "社會 110 分鐘：單選 38 題×2＝76 分＋混合題或非選 68 分（115 年，共 144 分）；歷史、地理、公民三科配分相當。", focus(5, "三科必考觀念、史料與圖表判讀法。")))
    for s, prefix in (("science", "13n"), ("social", "14n")):
        for m, _, _ in NOTE_PAGES[s]:
            write_page(f"{prefix}_{s}_{m}", notes_page(s, m), limit=7000, first_alone=True)
    write_page("15_chinese_xuci", xuci_page())
    write_page("16_chinese_core", core_index_page())
    for i, t in enumerate(core_texts(), 1):
        write_page(f"16_core_{i:02d}", core_text_page(t))
    write_page("17_chinese_guoxue", guoxue_page())
    write_page("20_past_exams", past_exams_page())
    write_page("30_week01", week1_page())  # 每週課程的頁面內容（分段寫入 Notion 用）
    write_page("30_week02", week2_page())
    write_page("30_week03", week3_page())
    write_page("40_progress", progress_page())
    write_page("90_teacher", teacher_page())
    q = db_question_rows()
    (OUT / "db_questions.json").write_text(json.dumps(q, ensure_ascii=False, indent=1), encoding="utf-8")
    w = db_week_rows()
    (OUT / "db_weeks.json").write_text(json.dumps(w, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"db_questions: {len(q)} 列、內容 {sum(len(r['content']) for r in q)} 字；db_weeks: {len(w)} 列")


if __name__ == "__main__":
    main()
