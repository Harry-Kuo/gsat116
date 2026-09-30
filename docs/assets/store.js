// 本機儲存：個人設定、作答紀錄、每日進度、作答歷史、間隔複習、待上傳佇列。
// 每日進度、作答歷史、間隔複習都可以由「作答紀錄」重算：合併其他裝置的紀錄後重算一次，手機和電腦就會一致。
// localStorage 可能不可用（無痕模式等），全部包在 try/catch，失敗時退回記憶體。
import { addDays, todayStr } from "./util.js";

const P = "g116:";
const mem = {};

function read(key, fallback) {
  try {
    const v = localStorage.getItem(P + key);
    return v == null ? fallback : JSON.parse(v);
  } catch {
    return key in mem ? mem[key] : fallback;
  }
}

function write(key, value) {
  mem[key] = value;
  try {
    localStorage.setItem(P + key, JSON.stringify(value));
  } catch {
    /* 容量不足或被封鎖時只留在記憶體 */
  }
}

// ---- 個人設定 ----
export function getProfile() {
  return read("profile", null);
}
export function setProfile(p) {
  write("profile", p);
}

// ---- 每日進度：progress[日期][科目] = { answers: {qid: 作答紀錄} } ----
export function getProgress() {
  return read("progress", {});
}
export function dayProgress(date, subject) {
  return getProgress()[date]?.[subject] || { answers: {} };
}
function putAnswer(prog, date, subject, qid, rec) {
  prog[date] ??= {};
  prog[date][subject] ??= { answers: {} };
  prog[date][subject].answers[qid] = rec;
}
export function saveAnswer(date, subject, qid, rec) {
  const prog = getProgress();
  putAnswer(prog, date, subject, qid, rec);
  write("progress", prog);
}

// ---- 作答歷史（錯題本、年度進度） history[qid] = [{d, ok, sc, mx}] ----
export function getHistory() {
  return read("history", {});
}
function putHistory(h, qid, rec, day) {
  (h[qid] ??= []).push({ d: day, ok: rec.correct ? 1 : 0, sc: rec.score, mx: rec.max });
}
export function recordHistory(qid, rec) {
  const h = getHistory();
  putHistory(h, qid, rec, todayStr());
  write("history", h);
}

// 錯題：最近一次作答沒有全對的題目
export function wrongItems() {
  const h = getHistory();
  return Object.entries(h)
    .filter(([, arr]) => arr.length && !arr[arr.length - 1].ok)
    .map(([qid, arr]) => ({ qid, last: arr[arr.length - 1].d, tries: arr.length }));
}

// ---- 間隔複習：答錯後 1、3、7 天再出現；連續答對三輪就移除 ----
const STEPS = [1, 3, 7];
export function getSrs() {
  return read("srs", {});
}
function stepSrs(srs, qid, correct, today) {
  if (!correct) {
    srs[qid] = { due: addDays(today, STEPS[0]), step: 0 };
  } else if (srs[qid]) {
    const step = srs[qid].step + 1;
    if (step >= STEPS.length) delete srs[qid];
    else srs[qid] = { due: addDays(today, STEPS[step]), step };
  }
}
export function updateSrs(qid, correct) {
  const srs = getSrs();
  stepSrs(srs, qid, correct, todayStr());
  write("srs", srs);
}
export function dueReviews(today = todayStr()) {
  return Object.entries(getSrs())
    .filter(([, v]) => v.due <= today)
    .sort((a, b) => a[1].due.localeCompare(b[1].due))
    .map(([qid]) => qid);
}

// ---- 作答紀錄：這台裝置的作答，加上從老師試算表取回的其他裝置作答 ----
// 欄位縮寫：s 科目、q 題號、m 模式、r 作答、c 對錯、sc 得分、mx 滿分、t 非選作答文字
function logEntry(a) {
  const e = {
    id: String(a.id), ts: String(a.ts || ""), day: String(a.day || ""), set: String(a.set || ""), s: String(a.subject || ""),
    q: String(a.qid || ""), m: String(a.mode || ""), r: String(a.resp ?? ""), c: Number(a.correct) ? 1 : 0,
    sc: Number(a.score) || 0, mx: Number(a.max) || 0, ms: Number(a.ms) || 0,
  };
  if (a.text) e.t = String(a.text);
  return e;
}
export function getLog() {
  return read("log", []);
}
export function logAttempt(attempt) {
  const log = getLog();
  log.push(logEntry(attempt));
  write("log", log);
}

// 合併後端傳回的作答。full＝後端給的是這個代碼的完整紀錄：本機已上傳、後端卻沒有的（例如老師刪掉的測試紀錄）一併移除。
// 回傳是否有變動。
export function mergeRemote(rows, full) {
  const pending = new Set(getQueue().map((a) => a.id));
  const remote = new Map(rows.map((a) => [String(a.id), a]));
  let changed = false;
  const out = [];
  for (const e of getLog()) {
    if (remote.has(e.id)) remote.delete(e.id);
    else if (full && !pending.has(e.id)) {
      changed = true;
      continue;
    }
    out.push(e);
  }
  for (const a of remote.values()) {
    out.push(logEntry(a));
    changed = true;
  }
  if (changed) write("log", out);
  return changed;
}

// 由作答紀錄重算每日進度、作答歷史、間隔複習（依作答時間先後重播一次）
export function rebuild() {
  const log = getLog().slice().sort((a, b) => a.ts.localeCompare(b.ts));
  const prog = {};
  const hist = {};
  const srs = {};
  for (const e of log) {
    const rec = { resp: e.r, correct: !!e.c, score: e.sc, max: e.mx, ms: e.ms };
    if (e.t) rec.text = e.t;
    if (e.set && e.m !== "single") putAnswer(prog, e.set, e.s, e.q, rec);
    putHistory(hist, e.q, rec, e.day);
    if (e.r !== "self") stepSrs(srs, e.q, rec.correct, e.day); // 非選自評題不進間隔複習
  }
  write("progress", prog);
  write("history", hist);
  write("srs", srs);
}

// 換成另一個代碼登入時，清掉前一個代碼留在這台裝置的練習資料
export function switchOwner(code) {
  const owner = getMeta("owner");
  if (owner && owner !== code) {
    ["log", "progress", "history", "srs", "session", "queue", "meta:pullCursor", "meta:lastPull", "meta:lastSync"].forEach((k) => {
      delete mem[k];
      try {
        localStorage.removeItem(P + k);
      } catch {
        /* 忽略 */
      }
    });
  }
  setMeta("owner", code);
}

// ---- 待上傳佇列 ----
export function getQueue() {
  return read("queue", []);
}
export function enqueue(attempt) {
  const q = getQueue();
  q.push(attempt);
  write("queue", q);
}
export function dequeue(ids) {
  const set = new Set(ids);
  write("queue", getQueue().filter((a) => !set.has(a.id)));
}

// ---- 進行中的練習（中斷後接續） ----
export function getSession() {
  return read("session", null);
}
export function setSession(s) {
  write("session", s);
}

export function getMeta(key, fallback = null) {
  return read("meta:" + key, fallback);
}
export function setMeta(key, value) {
  write("meta:" + key, value);
}

export function clearAll() {
  try {
    Object.keys(localStorage).filter((k) => k.startsWith(P)).forEach((k) => localStorage.removeItem(k));
  } catch {
    /* 忽略 */
  }
  Object.keys(mem).forEach((k) => delete mem[k]);
}
