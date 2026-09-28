// 共用工具：台北時區日期、倒數、亂數 id、轉義
export const TZ = "Asia/Taipei";
const DAY = 86400000;

export function todayStr(d = new Date()) {
  return new Intl.DateTimeFormat("en-CA", { timeZone: TZ, year: "numeric", month: "2-digit", day: "2-digit" }).format(d);
}

function atMidnight(dateStr) {
  return new Date(dateStr + "T00:00:00+08:00");
}

export function addDays(dateStr, n) {
  return todayStr(new Date(atMidnight(dateStr).getTime() + n * DAY + 3600000));
}

export function daysBetween(a, b) {
  return Math.round((atMidnight(b) - atMidnight(a)) / DAY);
}

export function fmtDate(dateStr) {
  const [, m, d] = dateStr.split("-");
  const w = "日一二三四五六"[new Date(dateStr + "T12:00:00+08:00").getUTCDay()];
  return `${+m}/${+d}（${w}）`;
}

export function countdown(targetIso, now = Date.now()) {
  const ms = Math.max(0, new Date(targetIso).getTime() - now);
  const s = Math.floor(ms / 1000);
  return { ms, days: Math.floor(s / 86400), hours: Math.floor((s % 86400) / 3600), minutes: Math.floor((s % 3600) / 60), seconds: s % 60 };
}

export const pad = (n) => String(n).padStart(2, "0");

export function uid() {
  if (crypto.randomUUID) return crypto.randomUUID();
  return "id-" + Date.now().toString(36) + "-" + Math.random().toString(36).slice(2, 10);
}

export function esc(s) {
  return String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

export function fmtScore(x) {
  return Number.isInteger(x) ? String(x) : x.toFixed(1);
}

export function fmtSec(sec) {
  if (sec < 60) return `${Math.round(sec)} 秒`;
  return `${Math.floor(sec / 60)} 分 ${pad(Math.round(sec % 60))} 秒`;
}

export function toast(msg, ms = 2200) {
  const el = document.createElement("div");
  el.className = "toast";
  el.textContent = msg;
  document.body.appendChild(el);
  setTimeout(() => el.remove(), ms);
}
