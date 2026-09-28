// 資料載入與後端（Google Apps Script）溝通。
// backend 設定：空字串＝離線模式（只存本機）；"mock"＝本機測試用假後端；其他＝Apps Script 網址。
import { dequeue, getQueue, setMeta } from "./store.js";

let cfg = null;
const cache = {};

export async function loadJSON(path) {
  if (cache[path]) return cache[path];
  const v = cfg?.version ? `?v=${cfg.version}` : `?t=${Date.now()}`;
  const res = await fetch(path + v, { cache: "no-cache" });
  if (!res.ok) throw new Error(`讀取 ${path} 失敗（${res.status}）`);
  cache[path] = await res.json();
  return cache[path];
}

export async function loadConfig() {
  const res = await fetch("data/config.json?t=" + Date.now(), { cache: "no-store" }).catch(() => null);
  if (res && res.ok) cfg = await res.json();
  else cfg = await (await fetch("data/config.json")).json();
  return cfg;
}

export const bank = (subject) => loadJSON(`data/bank/${subject}.json`).catch(() => ({ items: {}, groups: {} }));

// ---- 假後端（本機測試） ----
function mockDb() {
  try {
    return JSON.parse(localStorage.getItem("g116:mockdb") || "[]");
  } catch {
    return [];
  }
}
function mockSave(rows) {
  try {
    localStorage.setItem("g116:mockdb", JSON.stringify(rows));
  } catch {
    /* 忽略 */
  }
}

async function call(params, body) {
  const url = cfg.backend + "?" + new URLSearchParams(params).toString();
  const res = body
    ? await fetch(cfg.backend, { method: "POST", body: JSON.stringify(body), headers: { "Content-Type": "text/plain;charset=utf-8" } })
    : await fetch(url);
  if (!res.ok) throw new Error("後端回應 " + res.status);
  return res.json();
}

export function backendMode() {
  if (!cfg?.backend) return "offline";
  return cfg.backend === "mock" ? "mock" : "live";
}

export async function hello(code) {
  const mode = backendMode();
  if (mode === "offline") return { ok: true, offline: true, name: "" };
  if (mode === "mock") return { ok: /^[A-Za-z0-9]{3,12}$/.test(code), name: "測試學生 " + code };
  return call({ action: "hello", code });
}

export async function flushQueue(code) {
  const mode = backendMode();
  const queue = getQueue();
  if (!queue.length || mode === "offline" || !navigator.onLine) return { sent: 0, pending: queue.length };
  let sent = 0;
  for (let i = 0; i < queue.length; i += 50) {
    const batch = queue.slice(i, i + 50);
    if (mode === "mock") {
      mockSave(mockDb().concat(batch));
      dequeue(batch.map((a) => a.id));
      sent += batch.length;
      continue;
    }
    const r = await call({}, { action: "submit", code, attempts: batch }).catch(() => null);
    if (!r || !r.ok) break;
    dequeue(r.saved || batch.map((a) => a.id));
    sent += (r.saved || batch).length;
  }
  if (sent) setMeta("lastSync", new Date().toISOString());
  return { sent, pending: getQueue().length };
}

// ---- 老師端 ----
export async function exportData(key, since) {
  const mode = backendMode();
  if (mode === "mock") {
    const rows = mockDb().filter((r) => r.day >= since);
    const codes = [...new Set(rows.map((r) => r.code))];
    return { ok: true, attempts: rows, roster: codes.map((c) => ({ code: c, name: "測試學生 " + c, active: true })) };
  }
  if (mode === "offline") return { ok: false, error: "尚未設定後端網址（config.yaml 的 backend）" };
  return call({ action: "export", key, since });
}
