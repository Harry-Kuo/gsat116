"""檢查解析、重點整理、觀念摘要與講義裡用 $…$ 包起來的數學式：用網站同一份 KaTeX 實際排版，有錯就列出來。
用法：python3 tools/check_tex.py      （需要 node；沒有 node 時略過）
規則：數學式裡不能直接放中文（要用 \\text{…}）；錢字號寫成 \\$。
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KATEX = ROOT / "docs" / "assets" / "katex" / "katex.min.js"
MATH = re.compile(r"(?<!\\)\$(.+?)(?<!\\)\$")
SOURCES = ["data/explain/*.yaml", "data/reference/*.yaml", "data/concepts/*.yaml", "notion/*.md"]
JS = """
const katex = require(process.argv[1]);
let buf = '';
process.stdin.on('data', d => buf += d);
process.stdin.on('end', () => {
  const bad = [];
  for (const [where, tex] of JSON.parse(buf)) {
    try {
      katex.renderToString(tex, { throwOnError: true, strict: (c) => (c === 'unicodeTextInMathMode' ? 'error' : 'ignore') });
    } catch (e) { bad.push([where, tex, e.message.split('\\n')[0]]); }
  }
  console.log(JSON.stringify(bad));
});
"""


def spans():
    out = []
    for pattern in SOURCES:
        for path in sorted(ROOT.glob(pattern)):
            if path.name.endswith("_orig.yaml"):
                continue
            for no, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
                for m in MATH.finditer(line):
                    out.append([f"{path.relative_to(ROOT)}:{no}", m.group(1)])
    return out


def main():
    if not shutil.which("node"):
        print("沒有 node，略過數學式檢查")
        return 0
    items = spans()
    r = subprocess.run(["node", "-e", JS, str(KATEX)], input=json.dumps(items, ensure_ascii=False),
                       capture_output=True, text=True, check=True)
    bad = json.loads(r.stdout)
    for where, tex, msg in bad:
        print(f"✗ {where}：${tex}$\n   {msg}")
    print(f"數學式 {len(items)} 個，" + (f"錯誤 {len(bad)} 個" if bad else "全部可以排版 ✓"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
