// 本機儲存：個人設定、每日進度、作答歷史、間隔複習、待上傳佇列。
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

// ---- 每日進度：progress[日期][科目] = { answers: {qid: 作答紀錄}, done: bool } ----
export function getProgress() {
  return read("progress", {});
}
export function dayProgress(date, subject) {
  return getProgress()[date]?.[subject] || { answers: {} };
}
export function saveAnswer(date, subject, qid, rec, total) {
  const prog = getProgress();
  prog[date] ??= {};
  prog[date][subject] ??= { answers: {} };
  const dp = prog[date][subject];
  dp.answers[qid] = rec;
  if (total) dp.done = Object.keys(dp.answers).length >= total;
  write("progress", prog);
}

// ---- 作答歷史（錯題本、年度進度） history[qid] = [{d, ok, sc, mx}] ----
export function getHistory() {
  return read("history", {});
}
export function recordHistory(qid, rec) {
  const h = getHistory();
  (h[qid] ??= []).push({ d: todayStr(), ok: rec.correct ? 1 : 0, sc: rec.score, mx: rec.max });
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
export function updateSrs(qid, correct) {
  const srs = getSrs();
  const today = todayStr();
  if (!correct) {
    srs[qid] = { due: addDays(today, STEPS[0]), step: 0 };
  } else if (srs[qid]) {
    const step = srs[qid].step + 1;
    if (step >= STEPS.length) delete srs[qid];
    else srs[qid] = { due: addDays(today, STEPS[step]), step };
  }
  write("srs", srs);
}
export function dueReviews(today = todayStr()) {
  return Object.entries(getSrs())
    .filter(([, v]) => v.due <= today)
    .sort((a, b) => a[1].due.localeCompare(b[1].due))
    .map(([qid]) => qid);
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
