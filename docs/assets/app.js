// 116 學測快答：首頁、作答、錯題本、設定。純前端，資料來自 data/*.json。
import { bank, backendMode, flushQueue, hello, loadConfig, loadJSON, pull } from "./api.js";
import * as S from "./store.js";
import { addDays, countdown, daysBetween, esc, fmtDate, fmtScore, fmtSec, pad, todayStr, toast, uid } from "./util.js";

const app = document.getElementById("app");
let CFG, SCHED, CONCEPTS;
const SUBJ = {};
let tick = null;

// ---------------------------------------------------------------- 啟動
async function boot() {
  applyLook(S.getProfile());
  try {
    CFG = await loadConfig();
    [SCHED, CONCEPTS] = await Promise.all([loadJSON("data/schedule.json"), loadJSON("data/concepts.json")]);
  } catch (e) {
    app.innerHTML = `<div class="wrap"><div class="card">資料載入失敗，請確認網路後重新整理。<br><span class="small muted">${esc(e.message)}</span></div></div>`;
    return;
  }
  CFG.subjects.forEach((s) => (SUBJ[s.id] = s));
  const p = S.getProfile();
  if (p && !S.getMeta("owner")) S.setMeta("owner", p.code);
  startCountdown();
  if ("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(() => {});
  window.addEventListener("hashchange", route);
  window.addEventListener("online", () => sync());
  // 切回這個分頁或 App 時，取回其他裝置的作答
  document.addEventListener("visibilitychange", () => document.visibilityState === "visible" && sync());
  window.addEventListener("focus", () => sync());
  route();
  sync(true);
  recheck();
}

// 每次開啟都向老師的試算表確認代碼仍有效：名冊裡被刪除或停用的代碼會被登出（本機作答紀錄保留）
async function recheck() {
  const p = S.getProfile();
  if (!p || backendMode() !== "live" || !navigator.onLine) return;
  const r = await hello(p.code).catch(() => null);
  if (r && r.ok === false && !r.error) {
    S.setProfile(null);
    go("#/welcome");
    toast("這個代碼已停用，請跟老師確認");
  }
}

function applyLook(p) {
  const root = document.documentElement;
  if (p?.theme && p.theme !== "auto") root.dataset.theme = p.theme;
  else delete root.dataset.theme;
  if (p?.font === "large") root.dataset.font = "large";
  else delete root.dataset.font;
}

function startCountdown() {
  const el = document.getElementById("cd");
  const draw = () => {
    const c = countdown(CFG.exam.start);
    el.innerHTML = c.ms > 0 ? `距學測 <b>${c.days}</b> 天 ${pad(c.hours)}:${pad(c.minutes)}:${pad(c.seconds)}` : "學測加油！";
  };
  draw();
  clearInterval(tick);
  tick = setInterval(draw, 1000);
}

// 同步：先上傳這台裝置的作答，再取回其他裝置的作答並合併。同一時間只跑一個，避免上傳和取回互相干擾。
const PULL_GAP = 15000;
let syncing = null;
let again = false;
let forceNext = false;
let lastPull = 0;

async function sync(force = false) {
  forceNext ||= force;
  if (syncing) {
    again = true;
    return syncing;
  }
  syncing = (async () => {
    do {
      again = false;
      const p = S.getProfile();
      if (!p) break;
      await flushQueue(p.code).catch(() => null);
      if (!forceNext && Date.now() - lastPull < PULL_GAP) continue;
      forceNext = false;
      const r = await pull(p.code).catch(() => null);
      if (!r || S.getProfile()?.code !== p.code) continue;
      lastPull = Date.now();
      const changed = S.mergeRemote(r.rows, r.full);
      if (r.cursor) S.setMeta("pullCursor", r.cursor);
      S.setMeta("lastPull", new Date().toISOString());
      if (changed || r.full) {
        S.rebuild();
        refreshView();
      }
    } while (again);
  })();
  try {
    await syncing;
  } finally {
    syncing = null;
  }
  const el = document.getElementById("synctext");
  if (el) el.textContent = syncText();
}

// 取回新的作答後，首頁與錯題本重畫；作答中的畫面不打斷
function refreshView() {
  const view = location.hash.replace(/^#\/?/, "").split("/")[0];
  if (!S.getProfile()) return;
  if (!view) viewHome();
  else if (view === "wrong") viewWrong();
}

function syncText() {
  const pending = S.getQueue().length;
  const mode = backendMode();
  if (mode === "offline") return "目前為離線模式：作答只存在這台裝置";
  if (pending) return `還有 ${pending} 筆作答等待上傳（連上網路會自動補送）`;
  const pulled = S.getMeta("lastPull");
  if (pulled) {
    const t = new Intl.DateTimeFormat("zh-TW", { timeZone: "Asia/Taipei", hour: "2-digit", minute: "2-digit", hour12: false }).format(new Date(pulled));
    return `作答已同步 ✓（${t}）手機、電腦的進度會自動合併`;
  }
  return S.getMeta("lastSync") ? "作答已同步給老師 ✓" : "作答會自動同步給老師";
}

function syncHTML() {
  const live = backendMode() !== "offline";
  return `<div class="sync"><span id="synctext">${syncText()}</span>${live ? ` <button class="linkbtn" id="syncnow">🔄 立即同步</button>` : ""}</div>`;
}

function bindSync() {
  app.querySelector("#syncnow")?.addEventListener("click", async (ev) => {
    const btn = ev.currentTarget;
    btn.disabled = true;
    btn.textContent = "同步中…";
    const before = S.getMeta("lastPull");
    await sync(true);
    const ok = S.getMeta("lastPull") !== before;
    if (btn.isConnected) {
      btn.disabled = false;
      btn.textContent = "🔄 立即同步";
    }
    toast(ok ? "已取回最新進度" : "目前連不上老師的試算表，稍後會自動再試");
  });
}

// ---------------------------------------------------------------- 路由
function route() {
  const h = location.hash.replace(/^#\/?/, "");
  const [view, arg] = h.split("/");
  window.scrollTo(0, 0);
  if (!S.getProfile() && view !== "welcome") return viewWelcome();
  if (view === "q") return viewQuiz();
  if (view === "wrong") return viewWrong();
  if (view === "settings") return viewSettings();
  if (view === "diag") return viewDiagIntro(arg || "chinese");
  if (view === "item" && arg) return startSession({ mode: "single", items: [{ qid: arg, s: subjectOf(arg) }] });
  if (view === "welcome") return viewWelcome();
  return viewHome();
}

function go(hash) {
  if (location.hash === hash) route();
  else location.hash = hash;
}

function subjectOf(qid) {
  const map = { chn: "chinese", eng: "english", ma: "mathA", mb: "mathB", sci: "science", soc: "social" };
  const m = qid.match(/^([a-z]+)/);
  return map[m?.[1]] || "chinese";
}

// ---------------------------------------------------------------- 日期與題目
function dayIndex() {
  return daysBetween(SCHED.start, todayStr()) + 1;
}
function dayEntry(n) {
  return SCHED.days.find((d) => d.d === n);
}
function dateOf(n) {
  return addDays(SCHED.start, n - 1);
}
function mySubjects() {
  return (S.getProfile()?.subjects || []).filter((s) => SUBJ[s]);
}
function lastDay() {
  return SCHED.days.reduce((m, d) => Math.max(m, d.d), 0);
}
function currentDay() {
  const n = dayIndex();
  if (n < 1) return 1;
  return n;
}

async function setEst(qids, s) {
  const b = await bank(s);
  let sec = 0;
  const seen = new Set();
  for (const q of qids) {
    const it = b.items[q];
    if (!it) continue;
    sec += it.est || 45;
    if (it.g && !seen.has(it.g)) {
      seen.add(it.g);
      sec += b.groups[it.g]?.read || 0;
    }
  }
  return sec;
}

// ---------------------------------------------------------------- 首頁
async function viewHome() {
  const p = S.getProfile();
  const n = currentDay();
  const early = dayIndex() < 1;
  const entry = dayEntry(n);
  const date = dateOf(n);
  const subs = mySubjects();
  const cards = [];
  let totalSec = 0;
  let firstTodo = null;
  for (const s of subs) {
    const qids = entry?.sets?.[s] || [];
    const dp = S.dayProgress(date, s);
    const answered = qids.filter((q) => dp.answers[q]).length;
    const score = qids.reduce((a, q) => a + (dp.answers[q]?.score || 0), 0);
    const max = qids.reduce((a, q) => a + (dp.answers[q]?.max || 0), 0);
    const est = qids.length ? await setEst(qids.filter((q) => !dp.answers[q]), s) : 0;
    totalSec += est;
    if (qids.length && answered < qids.length && !firstTodo) firstTodo = s;
    cards.push({ s, qids, answered, score, max, est, theme: entry?.theme?.[s] });
  }
  const pools = SCHED.pools || {};
  const hist = S.getHistory();
  const due = S.dueReviews().length;
  const wrong = S.wrongItems().length;
  const behind = catchupList(n).length;

  app.innerHTML = `
  <div class="wrap">
    <div class="card hero">
      <div class="muted small">${early ? `開練日 ${fmtDate(SCHED.start)}，可以先搶先練習` : `Day ${n}・${fmtDate(date)}`}${p.name ? `・${esc(p.name)}` : ""}</div>
      <h1>${firstTodo ? "今天的快答還沒完成" : entry ? "今天的題目都完成了 🎉" : "今天的題目準備中"}</h1>
      ${firstTodo ? `<button class="btn primary" id="go">▶ 繼續今日練習（約 ${Math.max(1, Math.round(totalSec / 60))} 分鐘）</button>`
        : `<button class="btn primary" id="extra" ${due + behind ? "" : "disabled"}>🔁 加練（錯題複習 ${due} 題${behind ? `、補做 ${behind} 題` : ""}）</button>`}
    </div>
    <div class="grid">
      ${cards.map((c) => {
        const cls = !c.qids.length ? "off" : c.answered >= c.qids.length ? "done" : "";
        const state = !c.qids.length ? "今日無題" : c.answered >= c.qids.length ? `完成・${fmtScore(c.score)}/${fmtScore(c.max)} 分`
          : `${c.answered}/${c.qids.length} 題・約 ${Math.max(1, Math.round(c.est / 60))} 分`;
        const pool = pools[c.s]?.total || 0;
        const doneN = Object.keys(hist).filter((q) => subjectOf(q) === c.s).length;
        return `<button class="subj ${cls}" data-s="${c.s}" style="--c:${SUBJ[c.s].color}">
          <div class="name">${esc(SUBJ[c.s].name)}</div>
          <div class="state">${state}</div>
          ${c.theme ? `<div class="state">${esc(c.theme)}</div>` : ""}
          <div class="bar" title="近六屆經典題完成度"><i style="width:${pool ? Math.min(100, (100 * doneN) / pool) : 0}%"></i></div>
          <div class="state small">六屆經典題 ${doneN}/${pool || "—"}</div>
        </button>`;
      }).join("")}
    </div>
    <div class="row" style="margin-top:12px">
      ${firstTodo ? `<button class="btn" id="extra2" ${due + behind ? "" : "disabled"}>🔁 加練 ${due + behind || ""}</button>` : ""}
      <button class="btn" id="wrong">📕 錯題本 ${wrong || ""}</button>
      <button class="btn" id="set">⚙️ 設定</button>
    </div>
    ${syncHTML()}
  </div>`;

  bindSync();
  app.querySelector("#go")?.addEventListener("click", () => startToday(firstTodo));
  app.querySelector("#extra")?.addEventListener("click", startExtra);
  app.querySelector("#extra2")?.addEventListener("click", startExtra);
  app.querySelector("#wrong").addEventListener("click", () => go("#/wrong"));
  app.querySelector("#set").addEventListener("click", () => go("#/settings"));
  app.querySelectorAll(".subj").forEach((b) =>
    b.addEventListener("click", () => {
      const c = cards.find((x) => x.s === b.dataset.s);
      if (!c.qids.length) return toast("這一科今天還沒有題目");
      startToday(c.s, c.answered >= c.qids.length);
    }));
}

function startToday(s, review = false) {
  const n = currentDay();
  const date = dateOf(n);
  const qids = dayEntry(n)?.sets?.[s] || [];
  const dp = S.dayProgress(date, s);
  const todo = review ? qids : qids.filter((q) => !dp.answers[q]);
  startSession({ mode: review ? "redo" : "basic", items: todo.map((qid) => ({ qid, s, date })), title: `${SUBJ[s].name}・今日快答` });
}

function catchupList(n) {
  const out = [];
  for (const d of SCHED.days) {
    if (d.d >= n) continue;
    const date = dateOf(d.d);
    for (const s of mySubjects()) {
      const dp = S.dayProgress(date, s);
      for (const q of d.sets?.[s] || []) if (!dp.answers[q]) out.push({ qid: q, s, date });
    }
  }
  return out;
}

function startExtra() {
  const max = CFG.practice.extra_max || 5;
  const items = [];
  const seen = new Set();
  for (const q of S.dueReviews()) {
    if (items.length >= max) break;
    if (!mySubjects().includes(subjectOf(q))) continue;
    items.push({ qid: q, s: subjectOf(q), review: true });
    seen.add(q);
  }
  for (const it of catchupList(currentDay())) {
    if (items.length >= max) break;
    if (!seen.has(it.qid)) items.push(it);
  }
  if (!items.length) return toast("目前沒有需要複習的題目 👍");
  startSession({ mode: "extra", items, title: "加練：錯題複習與補做" });
}

// ---------------------------------------------------------------- 作答流程
function startSession({ mode, items, title }) {
  if (!items.length) return toast("沒有可以練習的題目");
  S.setSession({ id: uid(), mode, items, idx: 0, answers: {}, title: title || "練習", started: Date.now() });
  go("#/q");
}

let shownAt = 0;

async function viewQuiz() {
  const sess = S.getSession();
  if (!sess) return go("#/");
  if (sess.idx >= sess.items.length) return viewSummary(sess);
  const entry = sess.items[sess.idx];
  const b = await bank(entry.s);
  const it = b.items[entry.qid];
  if (!it) {
    toast("找不到題目 " + entry.qid);
    sess.idx++;
    S.setSession(sess);
    return viewQuiz();
  }
  const g = it.g ? b.groups[it.g] : null;
  const rec = sess.answers[entry.qid] || answeredElsewhere(sess, entry);
  const prevSameGroup = sess.idx > 0 && sess.items[sess.idx - 1] && b.items[sess.items[sess.idx - 1].qid]?.g === it.g && it.g;
  const pct = Math.round((100 * sess.idx) / sess.items.length);

  app.innerHTML = `
  <div class="wrap">
    <div class="qhead"><span>${esc(sess.title)}・${sess.idx + 1}/${sess.items.length}</span>
      <button class="x" id="exit" aria-label="離開">×</button></div>
    <div class="progress"><i style="width:${pct}%"></i></div>
    ${entry.review ? `<div class="small muted" style="margin-top:8px"><span class="pill">錯題複習</span></div>` : ""}
    ${g ? `<details class="passage" ${prevSameGroup ? "" : "open"}><summary>📄 題組文章（${g.range[0]}–${g.range[1]} 題）</summary><div class="body">${g.html}</div></details>` : ""}
    <div class="stem">${it.img ? `<img class="qimg" src="${esc(it.img)}" alt="題目圖片" loading="lazy">` : ""}${it.stem}</div>
    <div id="answer"></div>
    <div id="feedback"></div>
    <div class="meta">${esc(it.src)}${it.P != null ? `・全國答對率 ${it.P}%` : ""}・<a href="${esc(it.url)}" target="_blank" rel="noopener">原卷</a></div>
  </div>
  <div class="dock"><div class="wrap" id="dock"></div></div>`;

  app.querySelector("#exit").addEventListener("click", () => go("#/"));
  shownAt = performance.now();
  if (it.t === "open") renderOpen(sess, entry, it, rec);
  else if (it.t === "fill") renderFill(sess, entry, it, rec);
  else renderChoice(sess, entry, it, rec);
}

// 今日快答或補做的題目，如果已經在其他裝置作答過（同步後出現在每日進度裡），直接顯示那次的結果
function answeredElsewhere(sess, entry) {
  if (!entry.date || entry.review || !["basic", "extra"].includes(sess.mode)) return null;
  const rec = S.dayProgress(entry.date, entry.s).answers[entry.qid];
  if (!rec) return null;
  sess.answers[entry.qid] = rec;
  S.setSession(sess);
  return rec;
}

function answerKeys(it) {
  return String(it.a || "").includes(",") ? String(it.a).split(",") : String(it.a || "").split("");
}

function renderChoice(sess, entry, it, rec) {
  const box = app.querySelector("#answer");
  const multi = it.t === "multi";
  box.innerHTML = `${multi ? `<div class="small muted">多選題：可選多個，選好按「送出」</div>` : ""}
    <div class="opts">${it.o.map(([k, v]) => `<button class="opt" data-k="${esc(k)}"><span class="k">${esc(k)}</span><span class="v">${v}</span><span class="pct"></span></button>`).join("")}</div>`;
  const chosen = new Set();
  const dock = app.querySelector("#dock");
  if (rec) return showChoiceResult(sess, entry, it, rec);
  if (multi) {
    dock.innerHTML = `<button class="btn primary" id="submit" disabled>送出</button>`;
    dock.querySelector("#submit").addEventListener("click", () => {
      commit(sess, entry, it, gradeMulti(it, [...chosen]));
    });
  } else {
    dock.innerHTML = `<button class="btn ghost" id="skip">先跳過</button>`;
    dock.querySelector("#skip").addEventListener("click", () => skip(sess));
  }
  box.querySelectorAll(".opt").forEach((btn) =>
    btn.addEventListener("click", () => {
      const k = btn.dataset.k;
      if (multi) {
        chosen.has(k) ? chosen.delete(k) : chosen.add(k);
        btn.classList.toggle("sel");
        dock.querySelector("#submit").disabled = chosen.size === 0;
      } else {
        commit(sess, entry, it, gradeSingle(it, k));
      }
    }));
}

function gradeSingle(it, k) {
  const ok = k === String(it.a);
  return { resp: k, correct: ok, score: ok ? it.p : 0, max: it.p };
}

function gradeMulti(it, sels) {
  const ans = new Set(answerKeys(it));
  const n = it.o.length;
  if (!sels.length) return { resp: "", correct: false, score: 0, max: it.p, wrong: n };
  let k = 0;
  for (const [key] of it.o) if (ans.has(key) !== sels.includes(key)) k++;
  const score = Math.round(Math.max(0, (n - 2 * k) / n) * it.p * 100) / 100;
  return { resp: [...sels].sort().join(it.o[0][0].length > 1 || /\d/.test(it.o[0][0]) ? "," : ""), correct: k === 0, score, max: it.p, wrong: k };
}

function showChoiceResult(sess, entry, it, rec) {
  const ans = new Set(answerKeys(it));
  const sel = new Set(String(rec.resp || "").includes(",") ? rec.resp.split(",") : String(rec.resp || "").split(""));
  const wrongN = rec.wrong ?? it.o.filter(([k]) => ans.has(k) !== sel.has(k)).length;
  app.querySelectorAll(".opt").forEach((btn) => {
    const k = btn.dataset.k;
    btn.disabled = true;
    if (ans.has(k)) btn.classList.add("ok");
    else if (sel.has(k)) btn.classList.add("bad");
    if (sel.has(k) && !ans.has(k)) btn.classList.add("bad");
    const p = it.op?.[k];
    if (p != null) btn.querySelector(".pct").textContent = `全國 ${p}% 選`;
  });
  const fb = app.querySelector("#feedback");
  let cls = "ok";
  let head = "✅ 答對了！";
  if (!rec.correct) {
    cls = rec.score > 0 ? "part" : "bad";
    head = it.t === "multi"
      ? `${rec.score > 0 ? "🟡" : "❌"} 得 ${fmtScore(rec.score)}／${it.p} 分（錯 ${wrongN} 個選項）・正解 ${[...ans].join("")}`
      : rec.resp ? `❌ 正解是 ${it.a}` : `⏭ 跳過・正解是 ${it.a}`;
  }
  let trap = "";
  if (!rec.correct && it.t === "single" && it.op && rec.resp) {
    const top = Object.entries(it.op).sort((a, b) => b[1] - a[1])[0];
    if (top && top[0] === rec.resp && top[0] !== String(it.a)) trap = `你選的 ${rec.resp} 是全國最多人掉進去的陷阱（${top[1]}%）。`;
  }
  if (rec.correct && it.P != null && it.P < 40) trap = `這題全國只有 ${it.P}% 答對，很厲害！`;
  fb.innerHTML = feedbackHTML(it, cls, head, trap);
  dockNext(sess);
}

function feedbackHTML(it, cls, head, extra = "") {
  const tags = conceptTags(it.s, it.c);
  return `<div class="fb ${cls}">
    <h3>${head}</h3>
    ${extra ? `<div class="small">${esc(extra)}</div>` : ""}
    ${it.k ? `<p class="keyline">💡 ${esc(it.k)}</p>` : ""}
    ${tags ? `<div>${tags}</div>` : ""}
    <details class="ex"><summary>看完整解析</summary><div class="body">${it.ex || '<p class="muted">解析整理中，先看上面的重點，或請老師在課堂講解。</p>'}</div></details>
  </div>`;
}

function findConcept(s, cid) {
  for (const m of CONCEPTS[s]?.modules || []) for (const c of m.concepts) if (c.id === cid) return c;
  return null;
}

// 觀念標籤：有對應的 Notion 重點頁就做成連結，在新分頁開啟
function conceptTags(s, cids) {
  return (cids || []).map((cid) => findConcept(s, cid)).filter(Boolean).map((c) => c.notion
    ? `<a class="tag" href="${esc(c.notion)}" target="_blank" rel="noopener">📚 ${esc(c.name)}</a>`
    : `<span class="tag">${esc(c.name)}</span>`).join("");
}

// 選填題的作答格名稱：新制是「題號-第幾格」（13-1）；110 年以前是原卷的列號（14、15…）
const cellName = (it, i) => (it.cells && it.cells[i]) || `${it.no}-${i + 1}`;

function renderFill(sess, entry, it, rec) {
  const blanks = answerKeys(it).length;
  const box = app.querySelector("#answer");
  box.innerHTML = `<div class="small muted">選填題：每格填一個數字或符號，全部正確才給分</div>
    <div class="fill">${Array.from({ length: blanks }, (_, i) => `<label>${cellName(it, i)}<input type="text" inputmode="text" maxlength="2" autocomplete="off" data-i="${i}"></label>`).join("")}</div>
    <div class="small muted">負號請輸入「-」</div>`;
  const dock = app.querySelector("#dock");
  if (rec) {
    box.querySelectorAll("input").forEach((inp, i) => {
      inp.value = String(rec.resp || "").split(",")[i] || "";
      inp.disabled = true;
    });
    return showSimpleResult(sess, it, rec, `正解：${answerKeys(it).map((a, i) => `${cellName(it, i)}＝${a}`).join("、")}`);
  }
  dock.innerHTML = `<button class="btn primary" id="submit">送出</button>`;
  dock.querySelector("#submit").addEventListener("click", () => {
    const vals = [...box.querySelectorAll("input")].map((x) => x.value.trim());
    const norm = (v) => String(v).replace(/\s/g, "").replace(/[−–—－]/g, "-");
    const ok = answerKeys(it).every((a, i) => norm(a) === norm(vals[i] || ""));
    commit(sess, entry, it, { resp: vals.join(","), correct: ok, score: ok ? it.p : 0, max: it.p });
  });
}

function showSimpleResult(sess, it, rec, extra) {
  const cls = rec.correct ? "ok" : rec.score > 0 ? "part" : "bad";
  const head = rec.correct ? "✅ 答對了！" : rec.score > 0 ? `🟡 得 ${fmtScore(rec.score)}／${it.p} 分` : "❌ 再想想";
  app.querySelector("#feedback").innerHTML = feedbackHTML(it, cls, head, extra);
  dockNext(sess);
}

function renderOpen(sess, entry, it, rec) {
  const box = app.querySelector("#answer");
  box.innerHTML = `<textarea id="txt" placeholder="寫下你的答案（可以簡短條列）">${esc(rec?.text || "")}</textarea>`;
  const dock = app.querySelector("#dock");
  const reveal = () => {
    box.querySelector("#txt").disabled = !!rec;
    app.querySelector("#feedback").innerHTML = `<div class="card"><b>官方參考答案與評分原則</b>${it.ref || '<p class="muted">請見原卷評分原則</p>'}
      ${rec ? "" : `<p class="small muted">對照後替自己打分：</p><div class="selfscore">
        <button class="btn" data-v="0">0 分</button><button class="btn" data-v="${it.p / 2}">部分 ${it.p / 2} 分</button><button class="btn" data-v="${it.p}">完整 ${it.p} 分</button></div>`}</div>`;
    if (rec) {
      app.querySelector("#feedback").insertAdjacentHTML("beforeend", feedbackHTML(it, rec.correct ? "ok" : "part", `自評 ${fmtScore(rec.score)}／${it.p} 分`));
      return dockNext(sess);
    }
    dock.innerHTML = "";
    app.querySelectorAll(".selfscore .btn").forEach((b) =>
      b.addEventListener("click", () => {
        const v = Number(b.dataset.v);
        commit(sess, entry, it, { resp: "self", text: box.querySelector("#txt").value.slice(0, 1000), correct: v >= it.p, score: v, max: it.p });
      }));
  };
  if (rec) return reveal();
  dock.innerHTML = `<button class="btn primary" id="rev">看參考答案</button>`;
  dock.querySelector("#rev").addEventListener("click", reveal);
}

function skip(sess) {
  sess.items.push(sess.items.splice(sess.idx, 1)[0]);
  if (sess.items.slice(sess.idx).every((e) => sess.answers[e.qid])) sess.idx = sess.items.length;
  S.setSession(sess);
  viewQuiz();
}

function commit(sess, entry, it, result) {
  const ms = Math.min(600000, Math.round(performance.now() - shownAt));
  const rec = { ...result, ms };
  sess.answers[entry.qid] = rec;
  S.setSession(sess);
  if (entry.date && sess.mode !== "single") S.saveAnswer(entry.date, entry.s, entry.qid, rec);
  S.recordHistory(entry.qid, rec);
  if (it.t !== "open") S.updateSrs(entry.qid, rec.correct);
  const p = S.getProfile();
  const attempt = {
    id: uid(), ts: new Date().toISOString(), code: p.code, name: p.name || "", day: todayStr(), set: entry.date || "",
    subject: entry.s, qid: entry.qid, mode: entry.review ? "review" : sess.mode, resp: rec.resp || "",
    correct: rec.correct ? 1 : 0, score: rec.score, max: rec.max, ms, text: rec.text || "",
  };
  S.logAttempt(attempt);
  S.enqueue(attempt);
  sync();
  if (it.t === "open") return viewQuiz();
  if (it.t === "fill") return showSimpleResult(sess, it, rec, `正解：${answerKeys(it).map((a, i) => `${cellName(it, i)}＝${a}`).join("、")}`);
  showChoiceResult(sess, entry, it, rec);
}

function dockNext(sess) {
  const last = sess.idx >= sess.items.length - 1;
  const dock = app.querySelector("#dock");
  dock.innerHTML = `<button class="btn primary" id="next">${last ? "看結果" : "下一題 →"}</button>`;
  dock.querySelector("#next").addEventListener("click", () => {
    sess.idx++;
    S.setSession(sess);
    viewQuiz();
  });
}

async function viewSummary(sess) {
  const recs = sess.items.map((e) => ({ e, r: sess.answers[e.qid] })).filter((x) => x.r);
  const score = recs.reduce((a, x) => a + x.r.score, 0);
  const max = recs.reduce((a, x) => a + x.r.max, 0);
  const sec = recs.reduce((a, x) => a + x.r.ms, 0) / 1000;
  const wrong = recs.filter((x) => !x.r.correct);
  for (const x of wrong) x.it = (await bank(x.e.s)).items[x.e.qid];
  app.innerHTML = `
  <div class="wrap">
    <div class="card center">
      <div class="muted">${esc(sess.title)}</div>
      <div class="big">${fmtScore(score)} / ${fmtScore(max)}</div>
      <div class="muted">答對 ${recs.length - wrong.length}/${recs.length} 題・用時 ${fmtSec(sec)}</div>
    </div>
    ${wrong.length ? `<div class="card"><b>這幾題會在 1、3、7 天後再出現：</b><ul class="list">${wrong.map((x) => `<li><span class="t">${esc(x.it?.src || x.e.qid)}</span>
      <div>${conceptTags(x.e.s, x.it?.c)}</div></li>`).join("")}</ul></div>`
      : `<div class="card center">全對！🎉</div>`}
    <div class="sync"><span id="synctext">${syncText()}</span></div>
  </div>
  <div class="dock"><div class="wrap"><button class="btn primary" id="home">回首頁</button></div></div>`;
  app.querySelector("#home").addEventListener("click", () => {
    S.setSession(null);
    go("#/");
  });
}

// ---------------------------------------------------------------- 錯題本
async function viewWrong() {
  const list = S.wrongItems().filter((w) => mySubjects().includes(subjectOf(w.qid)));
  const rows = [];
  for (const w of list) {
    const s = subjectOf(w.qid);
    const it = (await bank(s)).items[w.qid];
    if (it) rows.push({ ...w, s, it });
  }
  rows.sort((a, b) => b.last.localeCompare(a.last));
  app.innerHTML = `
  <div class="wrap">
    <div class="qhead"><span>📕 錯題本（${rows.length} 題）</span><button class="x" id="exit">×</button></div>
    ${rows.length ? `<div class="card"><ul class="list">${rows.map((r) => `<li data-q="${esc(r.qid)}">
        <div class="t">${esc(r.it.src)}</div>
        <div>${conceptTags(r.s, r.it.c)}<span class="muted small">錯 ${r.tries} 次・${esc(r.last)}</span></div>
        <button class="btn" style="margin-top:8px;min-height:44px" data-redo="${esc(r.qid)}">重練這題</button></li>`).join("")}</ul></div>`
      : `<div class="card center">目前沒有錯題 👍</div>`}
  </div>
  ${rows.length ? `<div class="dock"><div class="wrap"><button class="btn primary" id="all">全部重練（最多 10 題）</button></div></div>` : ""}`;
  app.querySelector("#exit").addEventListener("click", () => go("#/"));
  app.querySelectorAll("[data-redo]").forEach((b) =>
    b.addEventListener("click", () => startSession({ mode: "wrong", items: [{ qid: b.dataset.redo, s: subjectOf(b.dataset.redo), review: true }], title: "錯題重練" })));
  app.querySelector("#all")?.addEventListener("click", () =>
    startSession({ mode: "wrong", items: rows.slice(0, 10).map((r) => ({ qid: r.qid, s: r.s, review: true })), title: "錯題重練" }));
}

// ---------------------------------------------------------------- 診斷小考
function viewDiagIntro(s) {
  const qids = SCHED.diag?.[s] || [];
  app.innerHTML = `
  <div class="wrap">
    <div class="card">
      <h2 style="margin-top:0">${esc(SUBJ[s]?.name || s)}診斷小考</h2>
      <p>共 ${qids.length} 題，約 25 分鐘。請獨立作答，結果會即時傳給老師，用來決定上課的重點。</p>
    </div>
  </div>
  <div class="dock"><div class="wrap"><button class="btn primary" id="start" ${qids.length ? "" : "disabled"}>開始</button></div></div>`;
  app.querySelector("#start").addEventListener("click", () =>
    startSession({ mode: "diag", items: qids.map((qid) => ({ qid, s })), title: `${SUBJ[s]?.name || ""}診斷小考` }));
}

// ---------------------------------------------------------------- 歡迎與設定
function viewWelcome() {
  app.innerHTML = `
  <div class="wrap">
    <div class="card">
      <h2 style="margin-top:0">歡迎加入 116 學測快答 👋</h2>
      <p>每天每科 5 題，等車、下課的零碎時間就能完成。請輸入老師給你的<b>學生代碼</b>。</p>
      <input type="text" id="code" autocomplete="off" autocapitalize="characters" placeholder="例如 A01" maxlength="12">
      <p class="small muted" id="msg"></p>
      <button class="btn primary" id="ok">開始</button>
    </div>
  </div>`;
  const inp = app.querySelector("#code");
  inp.focus();
  app.querySelector("#ok").addEventListener("click", async () => {
    const code = inp.value.trim().toUpperCase();
    const msg = app.querySelector("#msg");
    if (!/^[A-Z0-9]{2,12}$/.test(code)) return (msg.textContent = "代碼只能是 2–12 個英文字母或數字");
    msg.textContent = "確認中…";
    const r = await hello(code).catch(() => null);
    if (!r) return (msg.textContent = "目前連不上老師的試算表，請確認網路後再試一次");
    if (!r.ok) return (msg.textContent = "找不到這個代碼，請跟老師確認");
    S.switchOwner(code);
    S.setProfile({ code, name: r.name || "", subjects: CFG.subjects.map((s) => s.id), theme: "auto", font: "normal" });
    go("#/settings");
    toast("先選擇你要考的科目");
    sync(true);
  });
}

function viewSettings() {
  const p = S.getProfile();
  const all = CFG.subjects;
  app.innerHTML = `
  <div class="wrap">
    <div class="qhead"><span>⚙️ 設定</span><button class="x" id="exit">×</button></div>
    <div class="card">
      <div class="muted small">學生代碼</div><div><b>${esc(p.code)}</b> ${p.name ? esc(p.name) : ""}</div>
    </div>
    <div class="card checks">
      <b>我要考的科目</b>
      ${all.map((s) => `<label><input type="checkbox" value="${s.id}" ${p.subjects.includes(s.id) ? "checked" : ""}> ${esc(s.name)}</label>`).join("")}
      <p class="small muted">數學 A、B 依你報考的科目勾選。</p>
    </div>
    <div class="card">
      <b>字級</b>
      <div class="row" style="margin-top:8px"><button class="btn ${p.font !== "large" ? "primary" : ""}" data-font="normal">標準</button><button class="btn ${p.font === "large" ? "primary" : ""}" data-font="large">放大</button></div>
      <b style="display:block;margin-top:12px">外觀</b>
      <div class="row" style="margin-top:8px">${["auto", "light", "dark"].map((t) => `<button class="btn ${(p.theme || "auto") === t ? "primary" : ""}" data-theme="${t}">${{ auto: "自動", light: "淺色", dark: "深色" }[t]}</button>`).join("")}</div>
    </div>
    <div class="card">
      <b>本機資料</b>
      <p class="small muted">手機、電腦用同一個代碼登入，進度、錯題本會自動合併（需要連上網路）。待上傳 ${S.getQueue().length} 筆。</p>
      <button class="btn" id="reset">清除這台裝置的資料</button>
    </div>
  </div>
  <div class="dock"><div class="wrap"><button class="btn primary" id="save">完成</button></div></div>`;
  app.querySelector("#exit").addEventListener("click", () => go("#/"));
  app.querySelectorAll("[data-font]").forEach((b) => b.addEventListener("click", () => {
    p.font = b.dataset.font;
    S.setProfile(p);
    applyLook(p);
    viewSettings();
  }));
  app.querySelectorAll("[data-theme]").forEach((b) => b.addEventListener("click", () => {
    p.theme = b.dataset.theme;
    S.setProfile(p);
    applyLook(p);
    viewSettings();
  }));
  let armed = false;
  app.querySelector("#reset").addEventListener("click", (ev) => {
    if (!armed) {
      armed = true;
      ev.target.textContent = "再按一次確認清除（無法復原）";
      return;
    }
    S.clearAll();
    go("#/welcome");
  });
  app.querySelector("#save").addEventListener("click", () => {
    const subs = [...app.querySelectorAll(".checks input:checked")].map((x) => x.value);
    if (!subs.length) return toast("至少選一科");
    p.subjects = subs;
    S.setProfile(p);
    go("#/");
  });
}

boot();
