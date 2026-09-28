// 老師儀表板（個人版）：只看一位學生——每天答題進度、每題作答紀錄、個人弱點分析。
import { bank, exportData, loadConfig, loadJSON } from "./api.js";
import { addDays, daysBetween, esc, fmtDate, fmtSec, todayStr } from "./util.js";

const $ = (s) => document.querySelector(s);
let CFG, SCHED, CONCEPTS, DATA, ITEMS = {};
let who = null; // 目前查看的學生代碼
const pct = (a, b) => (b ? Math.round((100 * a) / b) : 0);
const cls = (p) => (p >= 70 ? "good" : p < 40 ? "low" : "");
const MODE = { basic: "每日", extra: "加練", review: "錯題複習", wrong: "錯題重練", diag: "診斷", redo: "重做", single: "單題" };

async function init() {
  CFG = await loadConfig();
  [SCHED, CONCEPTS] = await Promise.all([loadJSON("data/schedule.json"), loadJSON("data/concepts.json")]);
  for (const s of CFG.subjects) Object.assign(ITEMS, (await bank(s.id)).items);
  try {
    $("#key").value = localStorage.getItem("g116:tkey") || "";
  } catch {
    /* 忽略 */
  }
  $("#load").addEventListener("click", load);
  $("#csv").addEventListener("click", csv);
  if ($("#key").value || CFG.backend === "mock") load();
}

async function load() {
  const key = $("#key").value.trim();
  try {
    localStorage.setItem("g116:tkey", key);
  } catch {
    /* 忽略 */
  }
  const days = Number($("#range").value);
  const since = days >= 120 ? "2000-01-01" : addDays(todayStr(), -(days - 1));
  $("#msg").textContent = "載入中…";
  const r = await exportData(key, since).catch((e) => ({ ok: false, error: e.message }));
  if (!r.ok) {
    $("#msg").textContent = "載入失敗：" + (r.error || "請確認密鑰與網路");
    return;
  }
  DATA = r;
  DATA.attempts.forEach((a) => (a.sec = a.sec ?? Math.round((a.ms || 0) / 1000)));
  const codes = [...new Set([...r.roster.filter((x) => x.active).map((x) => x.code), ...r.attempts.map((a) => a.code)])];
  // 預設看作答最多、且不是測試帳號的學生
  const count = (c) => r.attempts.filter((a) => a.code === c).length;
  codes.sort((a, b) => (a === "TEST01") - (b === "TEST01") || count(b) - count(a));
  who = who && codes.includes(who) ? who : codes[0] || null;
  $("#who").innerHTML = codes.map((c) => `<option value="${esc(c)}" ${c === who ? "selected" : ""}>${esc(nameOf(c))}</option>`).join("");
  $("#who").classList.toggle("hidden", codes.length < 2);
  $("#who").onchange = () => {
    who = $("#who").value;
    render("days");
  };
  $("#msg").textContent = `${since === "2000-01-01" ? "全部" : since + " 起"}：${mine().length} 筆作答`;
  $("#updated").textContent = "更新於 " + new Date().toLocaleTimeString("zh-TW", { hour: "2-digit", minute: "2-digit" });
  $("#csv").disabled = !mine().length;
  render("days");
}

function nameOf(code) {
  const r = DATA.roster.find((x) => x.code === code);
  return (r?.name ? r.name + "・" : "") + code;
}
const mine = () => (DATA?.attempts || []).filter((a) => a.code === who);
const subjName = (id) => CFG.subjects.find((s) => s.id === id)?.name || id;

function conceptName(s, id) {
  for (const m of CONCEPTS[s]?.modules || []) for (const c of m.concepts) if (c.id === id) return c.name;
  return id;
}

const TABS = { days: "每日進度", log: "作答紀錄", analysis: "個人分析" };

function render(tab) {
  if (!who) {
    $("#out").innerHTML = `<div class="card">還沒有學生作答紀錄。</div>`;
    return;
  }
  $("#out").innerHTML = `<div class="tabs">${Object.entries(TABS).map(([k, v]) => `<button data-t="${k}" class="${k === tab ? "on" : ""}">${v}</button>`).join("")}</div><div id="view"></div>`;
  $("#out").querySelectorAll("[data-t]").forEach((b) => b.addEventListener("click", () => render(b.dataset.t)));
  ({ days: viewDays, log: viewLog, analysis: viewAnalysis })[tab]();
}

function table(head, rows) {
  return `<div class="scroll"><table class="t"><thead><tr>${head.map((h) => `<th>${h}</th>`).join("")}</tr></thead><tbody>${rows.join("")}</tbody></table></div>`;
}

// ---------------------------------------------------------------- 每日進度
function viewDays() {
  const A = mine();
  const today = todayStr();
  const activeDays = [...new Set(A.map((a) => a.day))].sort();
  let streak = 0;
  for (let d = today; activeDays.includes(d); d = addDays(d, -1)) streak++;
  const last7 = A.filter((a) => a.day >= addDays(today, -6));
  const subs = CFG.subjects.filter((s) => SCHED.days.some((d) => (d.sets[s.id] || []).length) || A.some((a) => a.subject === s.id));

  // 列出開練日到今天（或最後一筆作答）之間的每一天
  const first = [SCHED.start, ...activeDays].sort()[0];
  const lastDay = [today, ...activeDays, ...A.map((a) => a.set).filter(Boolean)].sort().at(-1);
  const rows = [];
  for (let d = lastDay; d >= first; d = addDays(d, -1)) {
    const n = daysBetween(SCHED.start, d) + 1;
    const entry = SCHED.days.find((x) => x.d === n);
    const dayA = A.filter((a) => a.day === d);
    const cells = subs.map((s) => {
      const set = entry?.sets?.[s.id] || [];
      const done = A.filter((a) => a.set === d && a.subject === s.id && set.includes(a.qid));
      const uniq = new Set(done.map((a) => a.qid)).size;
      const sc = done.reduce((x, a) => x + a.score, 0);
      const mx = done.reduce((x, a) => x + a.max, 0);
      if (!set.length) return `<td class="muted">—</td>`;
      if (!uniq) return `<td class="${d < today ? "low" : "muted"}">0/${set.length}</td>`;
      return `<td class="${uniq >= set.length ? "good" : ""}">${uniq}/${set.length}${uniq >= set.length ? " ✓" : ""} <span class="small muted">${pct(sc, mx)}%</span></td>`;
    });
    const extra = dayA.filter((a) => a.mode !== "basic").length;
    const sec = dayA.reduce((x, a) => x + a.sec, 0);
    rows.push(`<tr><td>${n >= 1 ? `Day ${n}・` : ""}${fmtDate(d)}</td>${cells.join("")}<td>${extra || "—"}</td><td>${dayA.length}</td><td>${sec ? fmtSec(sec) : "—"}</td></tr>`);
  }
  const todayN = daysBetween(SCHED.start, today) + 1;
  const todayEntry = SCHED.days.find((x) => x.d === todayN);
  const todaySubs = subs.filter((s) => (todayEntry?.sets?.[s.id] || []).length);
  const todayDone = todaySubs.filter((s) => {
    const set = todayEntry.sets[s.id];
    return new Set(A.filter((a) => a.set === today && a.subject === s.id && set.includes(a.qid)).map((a) => a.qid)).size >= set.length;
  }).length;
  $("#view").innerHTML = `
    <div class="kpis">
      <div class="kpi"><span class="muted small">今天完成</span><b>${todaySubs.length ? `${todayDone}/${todaySubs.length} 科` : "—"}</b><span class="small muted">${todayN >= 1 ? `Day ${todayN}` : "尚未開練"}・${fmtDate(today)}</span></div>
      <div class="kpi"><span class="muted small">連續練習</span><b>${streak} 天</b><span class="small muted">共練習 ${activeDays.length} 天</span></div>
      <div class="kpi"><span class="muted small">近 7 天</span><b>${last7.length} 題</b><span class="small muted">得分率 ${pct(last7.reduce((x, a) => x + a.score, 0), last7.reduce((x, a) => x + a.max, 0))}%</span></div>
    </div>
    <h2>每天的完成狀況（每日題：完成題數／應做題數、得分率）</h2>
    ${table(["日期", ...subs.map((s) => esc(s.name)), "加練與複習", "當天總題數", "當天用時"], rows)}`;
}

// ---------------------------------------------------------------- 作答紀錄
function viewLog() {
  const A = mine().slice().sort((a, b) => (b.ts || "").localeCompare(a.ts || ""));
  const days = [...new Set(A.map((a) => a.day))].sort().reverse();
  $("#view").innerHTML = `
    <div class="controls" style="margin-bottom:10px">
      <select id="fDay"><option value="">全部日期</option>${days.map((d) => `<option value="${d}">${fmtDate(d)}</option>`).join("")}</select>
      <select id="fSub"><option value="">全部科目</option>${CFG.subjects.map((s) => `<option value="${s.id}">${esc(s.name)}</option>`).join("")}</select>
      <label class="small"><input type="checkbox" id="fWrong"> 只看答錯</label>
    </div>
    <div id="logTable"></div>`;
  const draw = () => {
    const d = $("#fDay").value, s = $("#fSub").value, w = $("#fWrong").checked;
    const rows = A.filter((a) => (!d || a.day === d) && (!s || a.subject === s) && (!w || !a.correct)).map((a) => {
      const it = ITEMS[a.qid] || {};
      const res = a.correct ? `<span class="good">✓</span>` : a.score > 0 ? `<span>部分</span>` : `<span class="low">✗</span>`;
      const time = a.ts ? new Date(a.ts).toLocaleTimeString("zh-TW", { timeZone: "Asia/Taipei", hour: "2-digit", minute: "2-digit", hour12: false }) : "";
      return `<tr><td>${fmtDate(a.day)} ${time ? `<span class="small muted">${esc(time)}</span>` : ""}</td><td>${esc(subjName(a.subject))}</td>
        <td><a href="index.html#/item/${esc(a.qid)}" target="_blank" rel="noopener">${esc(it.src || a.qid)}</a>${a.text ? `<div class="small wrapcell" style="max-width:420px">📝 ${esc(a.text)}</div>` : ""}</td>
        <td>${esc(MODE[a.mode] || a.mode)}</td><td><b>${esc(a.resp === "self" ? "自評" : a.resp || "（跳過）")}</b></td><td>${esc(it.a ?? "—")}</td>
        <td>${res}</td><td>${Math.round(a.score * 10) / 10}/${a.max}</td><td>${a.sec ? a.sec + " 秒" : "—"}</td><td>${it.P != null ? it.P + "%" : "—"}</td></tr>`;
    });
    $("#logTable").innerHTML = rows.length ? table(["日期", "科目", "題目", "模式", "學生答案", "正解", "結果", "得分", "用時", "全國答對率"], rows)
      : `<div class="card">沒有符合條件的作答。</div>`;
  };
  ["#fDay", "#fSub", "#fWrong"].forEach((id) => $(id).addEventListener("change", draw));
  draw();
}

// ---------------------------------------------------------------- 個人分析
function viewAnalysis() {
  const A = mine();
  const today = todayStr();
  // 各科
  const subRows = CFG.subjects.map((s) => {
    const m = A.filter((a) => a.subject === s.id);
    if (!m.length) return null;
    const recent = m.filter((a) => a.day >= addDays(today, -6));
    const withP = m.filter((a) => ITEMS[a.qid]?.P != null);
    const diff = withP.length ? Math.round(pct(withP.filter((a) => a.correct).length, withP.length) - withP.reduce((x, a) => x + ITEMS[a.qid].P, 0) / withP.length) : null;
    const uniq = new Set(m.map((a) => a.qid)).size;
    const pool = SCHED.pools?.[s.id]?.total || 0;
    const p = pct(m.reduce((x, a) => x + a.score, 0), m.reduce((x, a) => x + a.max, 0));
    const pr = pct(recent.reduce((x, a) => x + a.score, 0), recent.reduce((x, a) => x + a.max, 0));
    return `<tr><td>${esc(s.name)}</td><td>${m.length}</td><td class="${cls(p)}">${p}%</td><td>${recent.length ? `<span class="${cls(pr)}">${pr}%</span>` : "—"}</td>
      <td>${diff == null ? "—" : `<span class="${diff >= 0 ? "good" : "low"}">${diff >= 0 ? "+" : ""}${diff}</span>`}</td>
      <td>${Math.round(m.reduce((x, a) => x + a.sec, 0) / m.length)} 秒</td><td>${uniq}/${pool}</td></tr>`;
  }).filter(Boolean);

  // 觀念
  const agg = {};
  for (const a of A) {
    const it = ITEMS[a.qid];
    if (!it) continue;
    for (const c of it.c || []) {
      const k = it.s + ":" + c;
      agg[k] ??= { s: it.s, c, sc: 0, mx: 0, n: 0, wrong: [] };
      agg[k].sc += a.score;
      agg[k].mx += a.max;
      agg[k].n++;
      if (!a.correct) agg[k].wrong.push(it.src);
    }
  }
  const cRows = Object.values(agg).map((x) => ({ ...x, p: pct(x.sc, x.mx) })).sort((a, b) => a.p - b.p || b.n - a.n)
    .map((r) => `<tr><td>${esc(subjName(r.s))}</td><td>${esc(conceptName(r.s, r.c))}</td><td>${r.n}</td>
      <td class="${cls(r.p)}"><span class="bars"><i style="width:${r.p}%"></i></span> ${r.p}%</td>
      <td class="wrapcell small">${[...new Set(r.wrong)].slice(0, 6).map(esc).join("、") || "—"}</td></tr>`);

  // 以「第一次作答」判斷：全國多數人會、他卻錯的題（該拿沒拿到）；全國少數人會、他答對的題（強項）
  const firstTry = {};
  for (const a of A.slice().sort((x, y) => (x.ts || "").localeCompare(y.ts || ""))) firstTry[a.qid] ??= a;
  const miss = Object.values(firstTry).filter((a) => !a.correct && (ITEMS[a.qid]?.P ?? 0) >= 65).sort((a, b) => ITEMS[b.qid].P - ITEMS[a.qid].P);
  const strong = Object.values(firstTry).filter((a) => a.correct && (ITEMS[a.qid]?.P ?? 100) < 40);
  // 目前仍未訂正（最後一次作答仍錯）
  const lastTry = {};
  for (const a of A.slice().sort((x, y) => (x.ts || "").localeCompare(y.ts || ""))) lastTry[a.qid] = a;
  const open = Object.values(lastTry).filter((a) => !a.correct && a.resp !== "self");
  const li = (a, extra = "") => `<li><a href="index.html#/item/${esc(a.qid)}" target="_blank" rel="noopener">${esc(ITEMS[a.qid]?.src || a.qid)}</a>
    <span class="small muted">答 ${esc(a.resp || "跳過")}・正解 ${esc(ITEMS[a.qid]?.a ?? "")}${extra}</span></li>`;
  const diag = A.filter((a) => a.mode === "diag");

  $("#view").innerHTML = `
    <h2>各科表現</h2>
    ${subRows.length ? table(["科目", "作答題數", "得分率", "近 7 天", "和全國比（百分點）", "平均每題", "六屆經典題進度"], subRows) : `<div class="card">還沒有作答。</div>`}
    <p class="small muted">「和全國比」＝他在這些題目的答對率，減去全國考生在同一批題目的平均答對率。正數代表比全國平均好。</p>
    <h2>觀念強弱（得分率由低到高）</h2>
    ${cRows.length ? table(["科目", "觀念", "作答次數", "得分率", "答錯的題目"], cRows) : `<div class="card">還沒有資料。</div>`}
    <div class="row" style="align-items:flex-start;flex-wrap:wrap">
      <div class="card" style="min-width:280px"><b>該拿沒拿到（全國答對率 ≥ 65%，他第一次答錯）</b>
        <ul class="list">${miss.length ? miss.slice(0, 15).map((a) => li(a, `・全國 ${ITEMS[a.qid].P}%`)).join("") : "<li class='muted'>沒有，很穩 👍</li>"}</ul></div>
      <div class="card" style="min-width:280px"><b>強項（全國答對率 < 40%，他第一次就答對）</b>
        <ul class="list">${strong.length ? strong.slice(0, 15).map((a) => li(a, `・全國 ${ITEMS[a.qid].P}%`)).join("") : "<li class='muted'>還沒有</li>"}</ul></div>
    </div>
    <div class="card"><b>目前還沒訂正的錯題（${open.length} 題）</b>
      <ul class="list">${open.length ? open.slice(0, 30).map((a) => li(a)).join("") : "<li class='muted'>沒有</li>"}</ul></div>
    ${diag.length ? `<div class="card"><b>診斷小考</b>：${Math.round(diag.reduce((x, a) => x + a.score, 0) * 10) / 10}/${diag.reduce((x, a) => x + a.max, 0)} 分
      <ul class="list">${diag.map((a) => `<li>${a.correct ? "✓" : "✗"} ${esc(ITEMS[a.qid]?.src || a.qid)} <span class="small muted">答 ${esc(a.resp || "跳過")}・正解 ${esc(ITEMS[a.qid]?.a ?? "")}・${(ITEMS[a.qid]?.c || []).map((c) => esc(conceptName(ITEMS[a.qid].s, c))).join("、")}</span></li>`).join("")}</ul></div>` : ""}`;
}

function csv() {
  const cols = ["day", "ts", "subject", "qid", "mode", "resp", "correct", "score", "max", "sec", "text"];
  const lines = [["日期", "時間", "科目", "題號", "模式", "學生答案", "對錯", "得分", "滿分", "用時秒", "作答文字", "題目", "正解"].join(",")]
    .concat(mine().map((a) => cols.map((c) => a[c]).concat([ITEMS[a.qid]?.src || "", ITEMS[a.qid]?.a || ""])
      .map((v) => `"${String(v ?? "").replace(/"/g, '""')}"`).join(",")));
  const blob = new Blob(["﻿" + lines.join("\n")], { type: "text/csv;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = `作答紀錄_${who}_${todayStr()}.csv`;
  link.click();
  URL.revokeObjectURL(url);
}

init();
