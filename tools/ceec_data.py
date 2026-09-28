"""讀取大考中心官方資料：選擇題答案、逐題答對率/鑑別度、選項分析、檔案位置。"""
import json
import re
from functools import lru_cache
from pathlib import Path

import fitz
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
CEEC = ROOT / "data" / "ceec"

# 內部科目代碼 → (各年度試題清單的科目名稱, 統計表工作表名稱)
SUBJECTS = {
    "chinese": {"paper": {110: "國文（選擇題）", "default": "國綜"}, "sheet": "國文"},
    "english": {"paper": {"default": "英文"}, "sheet": "英文"},
    "mathA": {"paper": {110: "數學", "default": "數學A"}, "sheet": {110: "數學", "default": "數學A"}},
    "mathB": {"paper": {110: "數學", "default": "數學B"}, "sheet": {110: "數學", "default": "數學B"}},
    "social": {"paper": {"default": "社會"}, "sheet": "社會"},
    "science": {"paper": {"default": "自然"}, "sheet": "自然"},
}


def _pick(v, year):
    return v.get(year, v["default"]) if isinstance(v, dict) else v


@lru_cache(maxsize=None)
def index():
    return json.loads((CEEC / "index.json").read_text(encoding="utf-8"))


def paper_entry(subject, year):
    name = _pick(SUBJECTS[subject]["paper"], year)
    for e in index()["exams"]:
        if e["year"] == year and e["subject"] == name:
            return e
    raise KeyError((subject, year))


def paper_file(subject, year, label, ext):
    """label：試題內容／選擇題答案／非選擇題評分原則…；ext：pdf 或 docx。"""
    for f in paper_entry(subject, year)["files"]:
        if f["label"].startswith(label) and f["path"].lower().endswith(ext):
            return ROOT / f["path"], f["url"]
    return None, None


def answer_key(subject, year):
    """回傳 {題號字串: 答案}，例如 {'1': 'C', '25': 'BE', '13-1': '9', '32': '／'}。"""
    path, _ = paper_file(subject, year, "選擇", ".pdf")
    tokens = []
    for page in fitz.open(path):
        tokens += [t.strip() for t in page.get_text().split("\n") if t.strip()]
    key, i = {}, 0
    while i < len(tokens) and not re.fullmatch(r"\d+", tokens[i]):
        i += 1
    while i < len(tokens):
        tok = tokens[i]
        if tok.startswith("※"):
            break
        nxt = tokens[i + 1] if i + 1 < len(tokens) else None
        if re.fullmatch(r"\d+", tok) and nxt and re.fullmatch(r"\d+-\d+", nxt):
            i += 1  # 選填題的題號標頭
            continue
        if re.fullmatch(r"\d+(-\d+)?", tok) and nxt is not None:
            key[tok] = nxt.replace(" ", "")
            i += 2
            continue
        i += 1
    return key


STATS_KEYWORDS = {"42-46": "答對率及鑑別度表", "51-55": "選項分析", "26": "成績標準一覽表", "21": "級分對照表"}


def _stats_file(year, prefix):
    """依關鍵字找統計檔（各年檔名不一定有編號前綴）。"""
    keyword = STATS_KEYWORDS[prefix]
    hits = sorted(f for f in (CEEC / str(year) / "stats").glob("*.xls*") if keyword in f.name)
    return hits[0] if hits else None


def item_stats(subject, year):
    """逐題 P（答對率）、Ph、Pl、D（鑑別度）、T（多選全對率）。"""
    f = _stats_file(year, "42-46")
    sheet = _pick(SUBJECTS[subject]["sheet"], year)
    df = pd.read_excel(f, sheet_name=sheet, header=None)
    head = next(i for i in range(len(df)) if str(df.iloc[i, 0]).strip() == "題號")
    cols = [str(c).strip() for c in df.iloc[head]]
    out = {}
    for i in range(head + 1, len(df)):
        no = str(df.iloc[i, 0]).strip()
        if not re.fullmatch(r"\*?\d+(-\d+)?", no):
            continue
        row = {cols[j]: df.iloc[i, j] for j in range(1, len(cols))}
        rec = {k: (None if pd.isna(row.get(k)) else int(row[k])) for k in ("P", "Ph", "Pl", "D", "T") if k in row}
        out[no.lstrip("*")] = rec
    return out


def option_stats(subject, year):
    """選項分析：{題號: {'T': {'A': 49, ...}, 'H': {...}, 'L': {...}, 'blank': 0}}（百分比）。"""
    f = _stats_file(year, "51-55")
    if f is None:
        return {}
    sheet = _pick(SUBJECTS[subject]["sheet"], year)
    df = pd.read_excel(f, sheet_name=sheet, header=None)
    head = next(i for i in range(len(df)) if str(df.iloc[i, 0]).strip() == "題號")
    cols = [str(c).strip() for c in df.iloc[head]]
    out, cur = {}, None
    for i in range(head + 1, len(df)):
        no = df.iloc[i, 0]
        if not pd.isna(no) and re.fullmatch(r"\*?\d+(-\d+)?", str(no).strip()):
            cur = str(no).strip().lstrip("*")
            out[cur] = {}
        if cur is None:
            continue
        grp = str(df.iloc[i, 1]).strip()
        if grp not in ("T", "H", "L"):
            continue
        dist = {}
        for j in range(3, len(cols)):
            v = df.iloc[i, j]
            if pd.isna(v):
                continue
            s = str(v).replace("*", "").strip()
            if re.fullmatch(r"-?\d+(\.\d+)?", s):
                dist[cols[j]] = int(float(s))
        out[cur][grp] = dist
        if grp == "T" and not pd.isna(df.iloc[i, 2]):
            out[cur]["blank"] = int(float(str(df.iloc[i, 2]).replace("*", "")))
    return out


if __name__ == "__main__":
    import sys

    subj, yr = sys.argv[1], int(sys.argv[2])
    print(answer_key(subj, yr))
    print(list(item_stats(subj, yr).items())[:3])
    print(list(option_stats(subj, yr).items())[:2])
