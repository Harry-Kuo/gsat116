"""核對解析：打 ✓ 的選項＝官方答案；「全國 N% 誤選」「全國答對率 N%」與官方統計一致。

用法：python3 tools/check_explain.py [科目…]
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import load_subject  # noqa: E402

SUBJECTS = sys.argv[1:] or ["chinese", "english", "mathA", "mathB", "science", "social"]
bad = 0
for s in SUBJECTS:
    bank, _ = load_subject(s)
    n = 0
    for qid, it in bank.items():
        ex = it.get("explain") or ""
        if not ex:
            continue
        n += 1
        ans = str(it.get("answer") or "")
        opt = (it.get("stats") or {}).get("opt") or {}
        K = "1-9" if qid.startswith(("ma", "mb")) else "A-J"  # 數學選項是 (1)–(5)
        # 「本題選錯誤」的題目：✓ 表示敘述正確，答案是寫「→ 錯誤 ✓」「→ 不正確 ✓」的選項
        pick_wrong = bool(re.search(r"本題選「(?:錯誤|不正確)」", ex))
        if pick_wrong:
            picked = set()
            for line in ex.split("\n"):
                for m in re.finditer(rf"\(([{K}])\)[^()\n]*?→ (?:錯誤|不正確) ✓", line):
                    picked.add(m.group(1))
            if picked != set(ans.replace(",", "")):
                bad += 1
                print(f"✗ {qid} 選錯誤題標出 {''.join(sorted(picked)) or '（無）'}，官方答案 {ans}")
        # 打勾的選項：單選要等於答案；多選時，以 (X) 開頭的各行打勾集合要等於答案集合
        for m in re.finditer(rf"\(([{K}])\)[^()\n]*?✓", "" if pick_wrong else ex):
            if it["type"] == "single" and m.group(1) != ans:
                bad += 1
                print(f"✗ {qid} 解析打勾 ({m.group(1)})，官方答案 {ans}")
        if it["type"] == "multi" and not pick_wrong:
            marked = {m.group(1) for line in ex.split("\n") if (m := re.match(rf"\(([{K}])\)", line.strip())) and "✓" in line}
            if marked and marked != set(ans.replace(",", "")):
                bad += 1
                print(f"✗ {qid} 多選打勾 {''.join(sorted(marked))}，官方答案 {ans}")
        # 誤選比例
        for line in ex.split("\n"):
            for m in re.finditer(r"全國 (\d+)% 誤選", line):
                pct = int(m.group(1))
                before = line[:m.start()]
                letters = re.findall(rf"\(([{K}])\)", before)
                if not letters:
                    print(f"？ {qid} 無法判斷「全國 {pct}% 誤選」指哪個選項：{line[:60]}")
                    continue
                k = letters[-1]
                if opt and opt.get(k) != pct:
                    bad += 1
                    print(f"✗ {qid} ({k}) 誤選率寫 {pct}%，官方 {opt.get(k)}%")
        for m in re.finditer(r"全國答對率(?:只有)? ?(\d+)%", ex):
            p = (it.get("stats") or {}).get("P")
            if p is not None and int(m.group(1)) != p:
                bad += 1
                print(f"✗ {qid} 答對率寫 {m.group(1)}%，官方 {p}%")
    print(f"{s}: 檢查 {n} 題解析")
print("全部一致 ✓" if not bad else f"有 {bad} 處不一致")
