"""下載大考中心學測歷屆試題、答案、評分原則與統計檔（答對率、級分對照、五標）。

用法：python3 tools/fetch_ceec.py [起始年 結束年]   預設 110 115
下載到 data/ceec/<年度>/，並把清單寫入 data/ceec/index.json。已存在的檔案不重抓。
"""
import html
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import unquote, urljoin

import requests

BASE = "https://www.ceec.edu.tw"
EXAM_LIST = BASE + "/xmfile?xsmsid=0J052424829869345634&PageSize=50&page={page}"
STATS_LIST = BASE + "/xmdoc?xsmsid=0J018604485538810196&PageSize=50"
ROOT = Path(__file__).resolve().parent.parent / "data" / "ceec"
HEADERS = {"User-Agent": "Mozilla/5.0 (exam_tools; educational use)"}


def get(url):
    for attempt in range(3):
        try:
            r = requests.get(url, headers=HEADERS, timeout=60)
            r.raise_for_status()
            return r
        except requests.RequestException:
            if attempt == 2:
                raise
            time.sleep(2)


def parse_exam_rows(page_html):
    rows = []
    for tr in re.findall(r"<tr>(.*?)</tr>", page_html, re.S):
        title = re.search(r'<td class="title">\s*(.*?)\s*</td>', tr, re.S)
        if not title:
            continue
        files = [
            {"url": urljoin(BASE, html.unescape(href)), "title": html.unescape(ftitle), "label": label.strip()}
            for href, ftitle, label in re.findall(r'<a href="([^"]+)"[^>]*title="([^"]*)"\s*>([^<]*)</a>', tr)
        ]
        rows.append({"title": html.unescape(title.group(1)).strip(), "files": files})
    return rows


def exam_rows(years):
    rows, page = [], 1
    while True:
        batch = parse_exam_rows(get(EXAM_LIST.format(page=page)).text)
        rows += batch
        found = [int(m.group(1)) for r in batch if (m := re.match(r"(\d+)學年度", r["title"]))]
        if not batch or (found and min(found) < min(years)):
            break
        page += 1
    return [r for r in rows if (m := re.match(r"(\d+)學年度", r["title"])) and int(m.group(1)) in years]


def stats_files(year):
    listing = get(STATS_LIST).text
    m = re.search(r'href="([^"]*xmdoc/cont[^"]*)"[^>]*>\s*%d學年度學科能力測驗統計' % year, listing)
    if not m:
        return []
    page = get(urljoin(BASE, html.unescape(m.group(1)))).text
    out = []
    for href in re.findall(r'href="([^"]*file_pool[^"]*\.xlsx?)"', page):
        url = urljoin(BASE, html.unescape(href))
        out.append({"url": url, "title": unquote(url.rsplit("/", 1)[-1]), "label": "統計"})
    return out


def download(url, dest):
    if dest.exists() and dest.stat().st_size > 0:
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(get(url).content)
    time.sleep(0.3)
    return True


def main():
    lo, hi = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) == 3 else (110, 115)
    years = set(range(lo, hi + 1))
    index = {"exams": [], "stats": {}}
    for row in exam_rows(years):
        year = int(re.match(r"(\d+)", row["title"]).group(1))
        subject = row["title"].split("－")[-1].strip()
        entry = {"year": year, "subject": subject, "title": row["title"], "files": []}
        for f in row["files"]:
            name = unquote(f["url"].rsplit("/", 1)[-1])
            dest = ROOT / str(year) / name
            new = download(f["url"], dest)
            entry["files"].append({**f, "path": str(dest.relative_to(ROOT.parent.parent))})
            print(("下載 " if new else "已有 ") + name)
        index["exams"].append(entry)
    for year in sorted(years):
        index["stats"][year] = []
        for f in stats_files(year):
            dest = ROOT / str(year) / "stats" / f["title"]
            new = download(f["url"], dest)
            index["stats"][year].append({**f, "path": str(dest.relative_to(ROOT.parent.parent))})
            print(("下載 " if new else "已有 ") + f["title"])
    (ROOT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"完成：{len(index['exams'])} 份試題、{sum(len(v) for v in index['stats'].values())} 個統計檔")


if __name__ == "__main__":
    main()
