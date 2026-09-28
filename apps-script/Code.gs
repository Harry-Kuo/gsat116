/**
 * 116 學測快答：作答紀錄後端（Google Apps Script 網頁應用程式，資料存在這份試算表）
 *
 * 第一次使用：
 *   1. 在試算表選「擴充功能 › Apps Script」，把本檔內容整份貼上並儲存。
 *   2. 上方函式選單選 setup → 執行 → 依畫面完成授權。執行紀錄會顯示「老師密鑰」。
 *   3. 「部署 › 新增部署作業 › 類型：網頁應用程式」，執行身分：我；存取權：任何人 → 部署，複製網址給 Claude。
 *   4. 在「名冊」工作表填入學生代碼（英數 2–12 碼，不分大小寫）與暱稱，「是否啟用」設 TRUE。
 *      名冊裡沒有、或「是否啟用」為 FALSE 的代碼都進不了練習網站。
 * 之後修改程式要重新部署：「部署 › 管理部署作業 › 編輯（鉛筆）› 版本：新版本」，網址不變。
 */
const SHEET_ROSTER = "名冊";
const SHEET_ATTEMPTS = "作答紀錄";
const SHEET_SUMMARY = "總覽";
const HEADERS = ["id", "上傳時間", "作答時間", "學生代碼", "暱稱", "練習日", "題目所屬日", "科目", "題號", "模式",
  "作答", "對錯", "得分", "滿分", "用時秒", "作答文字"];

function setup() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const roster = ss.getSheetByName(SHEET_ROSTER) || ss.insertSheet(SHEET_ROSTER);
  if (roster.getLastRow() === 0) {
    roster.appendRow(["學生代碼", "暱稱", "是否啟用", "備註"]);
    roster.appendRow(["TEST01", "老師測試", "TRUE", "老師自己測試用，可刪除"]);
    roster.appendRow(["STUDENT", "學生", "FALSE", "代碼改成學生的代碼，再把是否啟用改成 TRUE"]);
    roster.setFrozenRows(1);
    roster.getRange("A:A").setNumberFormat("@");
  }
  const att = ss.getSheetByName(SHEET_ATTEMPTS) || ss.insertSheet(SHEET_ATTEMPTS);
  if (att.getLastRow() === 0) {
    att.appendRow(HEADERS);
    att.setFrozenRows(1);
  }
  // 代碼、日期、作答等欄位固定為純文字，避免被自動轉成日期或數字
  ["A:K", "P:P"].forEach((r) => att.getRange(r).setNumberFormat("@"));

  const sum = ss.getSheetByName(SHEET_SUMMARY) || ss.insertSheet(SHEET_SUMMARY);
  sum.clear();
  sum.getRange("A1").setValue("每天、每科的作答量與得分（自動更新；逐題答案請看「作答紀錄」或老師儀表板）");
  sum.getRange("A3").setFormula(
    '=IFERROR(QUERY(作答紀錄!A:P, "select F, H, count(I), sum(L), sum(M), sum(N), sum(O) where F is not null group by F, H order by F desc label F \'練習日\', H \'科目\', count(I) \'題數\', sum(L) \'答對\', sum(M) \'得分\', sum(N) \'滿分\', sum(O) \'用時秒\'", 1), "還沒有作答紀錄")');

  const props = PropertiesService.getScriptProperties();
  if (!props.getProperty("TEACHER_KEY")) props.setProperty("TEACHER_KEY", Utilities.getUuid().replace(/-/g, "").slice(0, 10));
  Logger.log("老師密鑰（登入老師儀表板用，請勿分享給學生）：" + props.getProperty("TEACHER_KEY"));
}

function doGet(e) {
  const p = (e && e.parameter) || {};
  try {
    if (p.action === "hello") return json_(hello_(p.code));
    if (p.action === "export") return json_(export_(p.key, p.since));
    return json_({ ok: true, service: "116 學測快答後端" });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  }
}

function doPost(e) {
  try {
    const body = JSON.parse(e.postData.contents);
    if (body.action === "submit") return json_(submit_(body.code, body.attempts || []));
    return json_({ ok: false, error: "unknown action" });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  }
}

function json_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

function roster_() {
  const sh = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_ROSTER);
  return sh.getDataRange().getValues().slice(1)
    .filter((r) => String(r[0]).trim())
    .map((r) => ({
      code: String(r[0]).trim().toUpperCase(),
      name: String(r[1] || ""),
      active: String(r[2]).toUpperCase() !== "FALSE",
    }));
}

function hello_(code) {
  code = String(code || "").trim().toUpperCase();
  const s = roster_().find((r) => r.code === code && r.active);
  return s ? { ok: true, name: s.name } : { ok: false };
}

function submit_(code, attempts) {
  code = String(code || "").trim().toUpperCase();
  const s = roster_().find((r) => r.code === code && r.active);
  if (!s) return { ok: false, error: "unknown code" };
  const lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    const sh = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_ATTEMPTS);
    const seen = recentIds_(sh);
    const now = new Date();
    const rows = [];
    const saved = [];
    attempts.slice(0, 200).forEach((a) => {
      const id = String(a.id || "");
      if (!id) return;
      saved.push(id);
      if (seen.has(id)) return;
      seen.add(id);
      rows.push([id, now, String(a.ts || ""), code, s.name, String(a.day || ""), String(a.set || ""),
        String(a.subject || ""), String(a.qid || ""), String(a.mode || ""), String(a.resp || ""),
        Number(a.correct) || 0, Number(a.score) || 0, Number(a.max) || 0, Math.round((Number(a.ms) || 0) / 1000),
        String(a.text || "").slice(0, 1000)]);
    });
    if (rows.length) sh.getRange(sh.getLastRow() + 1, 1, rows.length, HEADERS.length).setValues(rows);
    return { ok: true, saved: saved };
  } finally {
    lock.releaseLock();
  }
}

function recentIds_(sh) {
  const last = sh.getLastRow();
  if (last < 2) return new Set();
  const start = Math.max(2, last - 3000);
  return new Set(sh.getRange(start, 1, last - start + 1, 1).getValues().map((r) => String(r[0])));
}

function export_(key, since) {
  const expected = PropertiesService.getScriptProperties().getProperty("TEACHER_KEY");
  if (!key || key !== expected) return { ok: false, error: "老師密鑰錯誤" };
  since = String(since || "2000-01-01");
  const values = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_ATTEMPTS).getDataRange().getValues();
  const fmt = (v) => (v instanceof Date ? Utilities.formatDate(v, "Asia/Taipei", "yyyy-MM-dd") : String(v));
  const out = [];
  for (let i = 1; i < values.length; i++) {
    const r = values[i];
    const day = fmt(r[5]);
    if (day < since) continue;
    out.push({
      id: String(r[0]), ts: String(r[2]), code: String(r[3]), name: String(r[4]), day: day, set: fmt(r[6]),
      subject: String(r[7]), qid: String(r[8]), mode: String(r[9]), resp: String(r[10]), correct: Number(r[11]),
      score: Number(r[12]), max: Number(r[13]), sec: Number(r[14]), text: String(r[15]),
    });
  }
  return { ok: true, attempts: out, roster: roster_() };
}
