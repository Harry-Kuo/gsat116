# 116 學測快答

給一位 116 學測考生使用的「零碎時間快答」網站與題庫工具，包含：

- **學生練習網站**：`docs/`（GitHub Pages）。每天每科 5 題，點一下就判分，答錯的題目會在 1、3、7 天後回到加練；離線也能作答，恢復連線後自動上傳。
- **Notion 嵌入倒數時鐘**：`docs/countdown.html`（在 Notion 輸入 `/embed` 貼上網址）。
- **老師儀表板**：`docs/teacher.html`。可以看每天的答題進度、每題的作答答案，以及個人弱點分析。
- **作答紀錄後端**：`apps-script/Code.gs`（Google 試算表＋Apps Script），部署步驟見 `apps-script/部署說明.md`。

## 資料流程

```
大考中心原卷、答案、統計（data/ceec/，不進 repo）
  └─ tools/fetch_ceec.py 下載
  └─ tools/split_chinese.py、split_english.py、extract_images.py 抽題 → data/questions/<科目>/g<年度>.yaml
  └─ tools/apply_tags.py：套用 data/concepts/<科目>_tags.yaml 的觀念分類
人工撰寫：data/explain/<科目>_*.yaml（解析、重點、題幹修正；重新抽題也不會被覆蓋）
排程：data/plan/days.yaml（Day 1＝data/config.yaml 的 practice.start）
  └─ tools/build.py → docs/data/*.json（網站資料）
  └─ tools/notion_md.py → notion/pages/*.md（Notion 頁面草稿）
```

## 常用指令

```bash
python3 tools/validate.py                      # 上線前檢查（答案對官方、解析、圖片、排程）
python3 tools/build.py --strict                # 產生網站資料（正式）
python3 tools/build.py --backend=mock          # 本機測試用（作答存在瀏覽器的假後端）
python3 -m http.server 8765 -d docs            # 本機開站：http://localhost:8765
python3 tools/trends.py chinese                # 重新計算國文出題趨勢
python3 tools/pools.py                         # 重新計算各科六屆經典題池
python3 tools/notion_md.py --site=<網站網址>     # 產生 Notion 草稿
```

## 每週更新流程

1. 看老師儀表板的「個人分析」：弱點觀念、該拿沒拿到的題目。
2. 下載或抽出下一週要用的題目（`extract_images.py <科目> <年度>`、`split_*.py`），在 `data/concepts/<科目>_tags.yaml` 標上觀念。
3. 在 `data/explain/` 寫好解析，把下一週的題號排進 `data/plan/days.yaml`。
4. 依序執行 `validate.py`、`build.py --strict`，commit 並 push。GitHub Pages 約 1 分鐘後更新，學生的網站會自動換到新版本。
5. 更新 Notion 的「本週」公告與該科重點頁。

## 設定

- `data/config.yaml`：考試時間、里程碑、開練日、每日題數、後端網址（`backend`）。
- 學生代碼：Google 試算表的「名冊」工作表。
- 老師密鑰：Apps Script 執行 `setup()` 後，會出現在執行紀錄中（存在 Script Properties，不會進 repo）。

## 內容來源與著作權

題目、答案、答對率與評分原則均取自大考中心公開資料，並標註出處與原卷連結。依著作權法第 9 條第 1 項第 5 款，依法令舉行之考試試題不受著作權保護。解析由 Claude 撰寫，標記為待老師審閱。
