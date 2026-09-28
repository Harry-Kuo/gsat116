"""把學測國文（110 國文、111+ 國綜）.docx 切成題組與題目，合併官方答案與統計，輸出 YAML 草稿。

用法：python3 tools/split_chinese.py 110 115 [--force]
輸出：data/questions/chinese/g<年度>.yaml。檔案已存在時不覆蓋（避免蓋掉人工校對），除非加 --force。
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ceec_data import answer_key, item_stats, option_stats, paper_file  # noqa: E402
from docx_text import docx_blocks  # noqa: E402
import qyaml  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "questions" / "chinese"
PLAIN = re.compile(r"</?(u|em|sup|sub)>")


def plain(s):
    return PLAIN.sub("", s)


def table_html(rows):
    grid = []
    for r in rows:
        cells = []
        for c in r:
            if c["vmerge"] == "continue":
                # 往上找同欄的起始格，rowspan+1
                col = sum(x.get("span", 1) for x in cells)
                for prev in reversed(grid):
                    acc, target = 0, None
                    for pc in prev:
                        if acc == col:
                            target = pc
                            break
                        acc += pc.get("span", 1)
                    if target is not None and not target.get("hidden"):
                        target["rowspan"] = target.get("rowspan", 1) + 1
                        break
                cells.append({"span": c["span"], "hidden": True, "text": ""})
            else:
                cells.append({"span": c["span"], "text": c["text"]})
        grid.append(cells)
    html = ["<table>"]
    for r in grid:
        tds = []
        for c in r:
            if c.get("hidden"):
                continue
            attrs = ""
            if c["span"] > 1:
                attrs += f' colspan="{c["span"]}"'
            if c.get("rowspan", 1) > 1:
                attrs += f' rowspan="{c["rowspan"]}"'
            tds.append(f"<td{attrs}>{c['text']}</td>")
        html.append("<tr>" + "".join(tds) + "</tr>")
    html.append("</table>")
    return "".join(html)


MARK = r"(?:［(?:符號|圖|公式)］)*"
# 自動加總無法判斷的非選配分（例如「各占2分」），以原卷人工核對後寫死
OPEN_POINTS = {"chn111-34": 6, "chn112-35": 6, "chn113-33": 8}
OPT_START = re.compile(r"^" + MARK + r"\s*\(([A-J])\)")
ITEM_START = re.compile(r"^" + MARK + r"(\d{1,2})\.\s*\t?")
GROUP_START = re.compile(r"^(\d{1,2})[-–](\d{1,2})\s*為題組")


def split_options(text):
    parts = re.split(r"\(([A-J])\)", text)
    opts = {}
    for i in range(1, len(parts) - 1, 2):
        opts[parts[i]] = parts[i + 1].strip().strip("\t").strip()
    return opts


def parse(year):
    path, docx_url = paper_file("chinese", year, "試題內容", ".docx")
    pdf_path, pdf_url = paper_file("chinese", year, "試題內容", ".pdf")
    _, ans_url = paper_file("chinese", year, "選擇", ".pdf")
    _, rubric_url = paper_file("chinese", year, "非選擇題", ".pdf")
    blocks = docx_blocks(path)

    groups, items = {}, []
    section = {"type": "single", "points": 2, "mixed": False}
    ranges = {}  # 題號 → 分數（說明：第a題至第b題，每題c分）
    group = None
    item = None
    mode = None  # 'stem' | 'options'
    expect = 1

    def container_append(text):
        nonlocal item
        if item is not None:
            if mode == "options" and item["options"]:
                last = list(item["options"])[-1]
                item["options"][last] += "\n" + text
            else:
                item["stem"] += ("\n" if item["stem"] else "") + text
        elif group is not None:
            group["passage"] += ("\n" if group["passage"] else "") + text

    for b in blocks:
        raw = b["text"].strip()
        if not raw:
            continue
        txt = plain(raw)
        if b["kind"] == "table":
            if item is None and group is None:
                continue  # 作答注意事項
            container_append(table_html(b["rows"]))
            if item is not None:
                item.setdefault("flags", []).append("含表格，請確認選項是否在表格內")
            continue
        if b["kind"] == "box":
            if item is None and group is None:
                continue
            container_append("【框】" + raw.replace("\n", "<br>"))
            continue
        # 區段標題
        if re.match(r"^第[壹貳參]部分", txt):
            section["mixed"] = "貳" in txt[:3]
            item, group, mode = None, None, None
            continue
        if re.match(r"^[一二三四]、單選題", txt):
            section["type"] = "single"
            continue
        if re.match(r"^[一二三四]、多選題", txt):
            section["type"] = "multi"
            continue
        m = re.match(r"^說明：第(\d+)題至第(\d+)題.*?(?:每題(\d+)分|得(\d+)分)", txt)
        if m:
            pts = int(m.group(3) or m.group(4))
            for n in range(int(m.group(1)), int(m.group(2)) + 1):
                ranges[n] = pts
            continue
        if txt.startswith("說明："):
            continue
        m = GROUP_START.match(txt)
        if m:
            a, z = int(m.group(1)), int(m.group(2))
            gid = f"chn{year}-g{a:02d}"
            group = {"id": gid, "range": [a, z], "intro": re.sub(r"^.*?為題組。?", "", txt).strip(), "passage": ""}
            groups[gid] = group
            item, mode = None, None
            continue
        m = ITEM_START.match(txt)
        if m and int(m.group(1)) == expect:
            no = int(m.group(1))
            expect = no + 1
            if group is not None and not (group["range"][0] <= no <= group["range"][1]):
                group = None
            stem = ITEM_START.sub("", re.sub("^" + MARK, "", raw), count=1)
            item = {
                "id": f"chn{year}-{no:02d}",
                "no": no,
                "type": "open" if section["mixed"] else section["type"],
                "points": ranges.get(no, 2 if section["mixed"] else section["points"]),
                "group": group["id"] if group else None,
                "stem": stem.strip(),
                "options": {},
                "part": 2 if section["mixed"] else 1,
            }
            if "［符號］" in raw or "［圖］" in raw:
                item.setdefault("flags", []).append("含圖形符號，請對照原卷")
            items.append(item)
            mode = "stem"
            continue
        if item is not None and OPT_START.match(txt):
            mode = "options"
            item["options"].update(split_options(re.sub("^" + MARK, "", raw)))
            if "［符號］" in raw:
                item.setdefault("flags", []).append("選項含圖形符號，請對照原卷")
            continue
        if item is not None and mode == "options" and item["group"] is None and not section["mixed"]:
            # 單題的選項後又出現文字：多半是下一題前的雜訊，保留並標記
            item.setdefault("flags", []).append("選項後有多餘文字：" + txt[:30])
            continue
        container_append(raw)

    key = answer_key("chinese", year)
    stats = item_stats("chinese", year)
    opts = option_stats("chinese", year)
    for it in items:
        k = str(it["no"])
        ans = key.get(k)
        if ans is None:
            it.setdefault("flags", []).append("官方答案缺")
        elif ans == "／":
            it["type"] = "open"
            it["answer"] = None
        else:
            it["answer"] = ans
            if it["type"] == "open":  # 混合題中的選擇題
                it["type"] = "multi" if len(ans) > 1 or "多選" in it["stem"] else "single"
                m = re.search(r"占(\d+)分", plain(it["stem"]))
                it["points"] = int(m.group(1)) if m else 2
            elif it["type"] == "single" and len(ans) > 1:
                it.setdefault("flags", []).append("單選區但答案多於一個")
        if it["type"] == "open":
            body = re.sub(r"第[一二三四五]題（占\d+分）", "", plain(it["stem"]))
            it["points"] = OPEN_POINTS.get(it["id"]) or sum(int(x) for x in re.findall(r"占(\d+)分", body)) or it["points"]
            it.pop("options", None)
        s = stats.get(k)
        if s:
            it["stats"] = {kk: v for kk, v in s.items() if v is not None}
            if k in opts and "T" in opts[k]:
                it["stats"]["opt"] = opts[k]["T"]
        if it["type"] in ("single", "multi") and it.get("options") is not None and len(it["options"]) < 4:
            it.setdefault("flags", []).append(f"只抓到 {len(it['options'])} 個選項")
        it.update({"topic": None, "concepts": [], "classic": None, "explain": "", "reviewed": False})
        it["flags"] = sorted(set(it.get("flags", []))) or None
        if it["flags"] is None:
            it.pop("flags")

    mixed_total = re.search(r"第貳部分[^（]*（占(\d+)\s*分", "\n".join(plain(b["text"]) for b in blocks))
    if mixed_total:
        got = sum(it["points"] for it in items if it.get("part") == 2)
        if got != int(mixed_total.group(1)):
            print(f"  ⚠ {year} 混合題配分加總 {got} ≠ 官方 {mixed_total.group(1)}")
    for it in items:
        it.pop("part", None)
    found = [it["no"] for it in items]
    expected = max([int(k.split("-")[0]) for k in key] + found)
    missing = [n for n in range(1, expected + 1) if n not in found]
    doc = {
        "exam": "學測",
        "year": year,
        "subject": "chinese",
        "paper": "國文" if year == 110 else "國綜",
        "source": {"pdf": pdf_url, "docx": docx_url, "answer": ans_url, "rubric": rubric_url},
        "missing": missing or None,
        "groups": [{k: v for k, v in g.items()} for g in groups.values()],
        "items": items,
    }
    if not missing:
        doc.pop("missing")
    return doc


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    lo, hi = (int(args[0]), int(args[1])) if len(args) == 2 else (110, 115)
    for year in range(lo, hi + 1):
        dest = OUT / f"g{year}.yaml"
        if dest.exists() and "--force" not in sys.argv:
            print(f"略過 {dest.name}（已存在，要覆蓋請加 --force）")
            continue
        if dest.exists() and "--force-all" not in sys.argv:
            old = qyaml.load(dest)
            if any(it.get("explain") or it.get("reviewed") for it in old["items"]):
                print(f"略過 {dest.name}：已有人工撰寫的解析或校對，重新產生會覆蓋（確定要覆蓋請加 --force-all）")
                continue
        doc = parse(year)
        qyaml.dump(doc, dest)
        n_flag = sum(1 for it in doc["items"] if it.get("flags"))
        print(f"{dest.name}: {len(doc['items'])} 題、{len(doc['groups'])} 題組、待確認 {n_flag} 題、缺題號 {doc.get('missing')}")


if __name__ == "__main__":
    main()
