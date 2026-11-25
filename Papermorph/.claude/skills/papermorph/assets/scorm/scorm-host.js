// SCORM host for a Papermorph book. Runs in launch.html, the one page the LMS launches.
// It opens the LMS session once, keeps the book's progress, and reports it to the LMS.
// Book pages reach it as parent.PapermorphSCORM through scorm-bridge.js.
'use strict';
(function () {
  const CFG = window.PAPERMORPH_SCORM_CONFIG;
  const TOTAL = CFG.chapters.length;
  const NUMS = new Set(CFG.chapters.map(c => c.n));   // the book's chapter numbers (they need not start at 1)
  const known = n => Number.isInteger(n) && NUMS.has(n);

  /* ---------- finding and talking to the LMS ---------- */
  // SCORM 2004 exposes API_1484_11 and SCORM 1.2 exposes API, on a parent frame or the opener.
  function findAPI(name) {
    const look = w => {
      for (let i = 0; w && i < 12; i++) {
        try { if (w[name]) return w[name]; } catch { return null; }   // a cross-origin frame ends the search
        if (w.parent === w) break;
        w = w.parent;
      }
      return null;
    };
    return look(window) || (window.opener ? look(window.opener) : null) ||
      (window.top && window.top.opener ? look(window.top.opener) : null);
  }

  const v2004 = CFG.version === '2004';
  const raw = findAPI(v2004 ? 'API_1484_11' : 'API');
  const lms = raw && (v2004 ? {
    init: () => raw.Initialize(''), get: k => raw.GetValue(k), set: (k, v) => raw.SetValue(k, String(v)),
    commit: () => raw.Commit(''), finish: () => raw.Terminate(''), err: () => raw.GetLastError(),
    diag: c => { try { return raw.GetDiagnostic(c); } catch { return ''; } },
  } : {
    init: () => raw.LMSInitialize(''), get: k => raw.LMSGetValue(k), set: (k, v) => raw.LMSSetValue(k, String(v)),
    commit: () => raw.LMSCommit(''), finish: () => raw.LMSFinish(''), err: () => raw.LMSGetLastError(),
    diag: c => { try { return raw.LMSGetDiagnostic(c); } catch { return ''; } },
  });
  let live = false;
  if (lms) live = String(lms.init()) === 'true';
  if (!live) console.warn(`[scorm] No SCORM ${CFG.version} API found; progress is kept for this visit only.`);
  const get = k => live ? String(lms.get(k) ?? '') : '';
  const set = (k, v) => {
    if (!live) return;
    if (String(lms.set(k, v)) !== 'true') {
      const code = lms.err();
      console.warn(`[scorm] ${k} = ${v} refused (error ${code}: ${lms.diag(code)})`);
    }
  };

  /* ---------- the learner's state ---------- */
  // Kept in suspend_data as {done: [chapter numbers], last: chapter number, s: {chapter: [right, total]},
  // q: {interaction id: {d, rows: [{k, t, ok, r, c}]}}. s holds each chapter's best first-try score; q holds
  // every question's or row's first-ever answer, locked in forever, so cmi.interactions can be rebuilt on any
  // later launch without needing a chapter page open. Both stay well under SCORM 1.2's 4096-character limit
  // for a single-chapter package (see trimForLimit below for the degrade path if a book ever outgrows that).
  let S = { done: [], last: 0, s: {}, q: {} };
  try {
    const saved = JSON.parse(get('cmi.suspend_data') || 'null');
    if (saved && typeof saved === 'object') S = {
      done: Array.isArray(saved.done) ? saved.done.filter(known) : [],
      last: Number.isInteger(saved.last) ? saved.last : 0,
      s: saved.s && typeof saved.s === 'object' ? saved.s : {},
      q: saved.q && typeof saved.q === 'object' ? saved.q : {},
    };
  } catch { console.warn('[scorm] Unreadable suspend_data; starting fresh.'); }

  const pad = n => String(n).padStart(2, '0');
  function score() {
    let r = 0, t = 0;
    for (const [right, total] of Object.values(S.s)) { r += right; t += total; }
    return t ? Math.round(100 * r / t) : null;
  }

  // suspend_data must stay under the LMS's limit (4096 chars for 1.2, ~64000 for 2004). A single-chapter
  // package's q map is normally a few hundred bytes, but if it ever grows close to the limit, degrade
  // gracefully by dropping the least essential fields first rather than silently losing a whole question.
  function suspendPayload() {
    const limit = v2004 ? 64000 : 4000;
    let json = JSON.stringify(S);
    if (json.length <= limit) return json;
    // Drop the description first (cosmetic only), then response/correct detail (keeps id/type/result,
    // enough to still rebuild a valid, if less detailed, interaction on the next launch).
    for (const strip of [
      q => ({ d: '', rows: q.rows }),
      q => ({ d: '', rows: q.rows.map(r => ({ k: r.k, t: r.t, ok: r.ok })) }),
    ]) {
      const thin = { ...S, q: {} };
      for (const [id, qv] of Object.entries(S.q)) thin.q[id] = strip(qv);
      json = JSON.stringify(thin);
      if (json.length <= limit) { S = thin; return json; }
    }
    console.warn('[scorm] suspend_data exceeds the size limit even after trimming; some question history will not persist.');
    return json;
  }

  function report() {
    const finished = S.done.length >= TOTAL;
    const pct = score();
    const passed = CFG.mastery == null || (pct ?? 0) >= CFG.mastery;
    set('cmi.suspend_data', suspendPayload());
    if (S.last) set(v2004 ? 'cmi.location' : 'cmi.core.lesson_location', 'ch' + pad(S.last));
    if (pct != null) {
      const base = v2004 ? 'cmi.score.' : 'cmi.core.score.';
      set(base + 'min', 0); set(base + 'max', 100); set(base + 'raw', pct);
      if (v2004) set('cmi.score.scaled', (pct / 100).toFixed(4));
    }
    if (v2004) {
      set('cmi.progress_measure', (S.done.length / TOTAL).toFixed(4));
      set('cmi.completion_status', finished ? 'completed' : 'incomplete');
      if (CFG.mastery != null && finished) set('cmi.success_status', passed ? 'passed' : 'failed');
    } else {
      set('cmi.core.lesson_status', !finished ? 'incomplete' : CFG.mastery == null ? 'completed' : passed ? 'passed' : 'failed');
    }
    // One objective per chapter, so LMS reports can show which chapters a learner finished.
    CFG.chapters.forEach((ch, i) => {
      const o = `cmi.objectives.${i}.`, done = S.done.includes(ch.n), cs = S.s[ch.n];
      set(o + 'id', 'ch' + pad(ch.n));
      if (cs && cs[1]) {
        const p = Math.round(100 * cs[0] / cs[1]);
        set(o + 'score.min', 0); set(o + 'score.max', 100); set(o + 'score.raw', p);
        if (v2004) set(o + 'score.scaled', (p / 100).toFixed(4));
      }
      if (v2004) set(o + 'completion_status', done ? 'completed' : 'incomplete');
      else set(o + 'status', done ? 'completed' : 'incomplete');
    });
    if (live) lms.commit();
  }

  /* ---------- cmi.interactions: one record per question, or per row for a grouping/matching or
     multi-step practice question. A book page reports an answer the moment it's first graded
     (host.answered below); every launch also rewrites every answer already in suspend_data, so a
     learner who never opens a chapter again still has a complete, LMS-visible interaction list. */
  const TYPES = new Set(['true-false', 'choice', 'fill-in', 'long-fill-in', 'matching', 'performance', 'sequencing', 'likert', 'numeric', 'other']);
  const IK = v2004 ? {
    count: 'cmi.interactions._count',
    id: n => `cmi.interactions.${n}.id`, type: n => `cmi.interactions.${n}.type`, obj: n => `cmi.interactions.${n}.objectives.0.id`,
    when: n => `cmi.interactions.${n}.timestamp`, weight: n => `cmi.interactions.${n}.weighting`,
    resp: n => `cmi.interactions.${n}.learner_response`, correct: n => `cmi.interactions.${n}.correct_responses.0.pattern`,
    result: n => `cmi.interactions.${n}.result`, latency: n => `cmi.interactions.${n}.latency`, desc: n => `cmi.interactions.${n}.description`,
  } : {
    id: n => `cmi.interactions.${n}.id`, type: n => `cmi.interactions.${n}.type`, obj: n => `cmi.interactions.${n}.objectives.0.id`,
    when: n => `cmi.interactions.${n}.time`, weight: n => `cmi.interactions.${n}.weighting`,
    resp: n => `cmi.interactions.${n}.student_response`, correct: n => `cmi.interactions.${n}.correct_responses.0.pattern`,
    result: n => `cmi.interactions.${n}.result`, latency: n => `cmi.interactions.${n}.latency`,
  };
  const clip = (s, n) => { s = String(s ?? ''); return s.length > n ? s.slice(0, n) : s; };
  // "ch01.c-kelompok", or "ch01.c-kelompok.bea-masuk" for a row: [A-Za-z0-9._-] only, max 64 chars,
  // with a deterministic short hash appended if a row's own text makes it run long.
  function fitId(s) {
    s = s.replace(/[^A-Za-z0-9._-]/g, '-');
    if (s.length <= 64) return s;
    let hash = 0;
    for (let i = 0; i < s.length; i++) hash = (hash * 31 + s.charCodeAt(i)) >>> 0;
    return s.slice(0, 56) + '-' + hash.toString(36);
  }
  const wallTime = () => { const d = new Date(); return `${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`; };
  const latency12 = sec => {
    sec = Math.max(0, sec || 0);
    const hh = Math.floor(sec / 3600), mm = Math.floor(sec / 60) % 60, ss = sec % 60;
    return `${String(hh).padStart(4, '0')}:${pad(mm)}:${ss.toFixed(2).padStart(5, '0')}`;
  };
  const latency2004 = sec => `PT${(Math.round(Math.max(0, sec || 0) * 100) / 100)}S`;

  const seenThisSession = new Set();   // ids already written to cmi.interactions this session (1.2 and 2004 alike)
  let nextN = 0;                       // next free cmi.interactions index this session
  let existingById = null;             // 2004 only: id -> its existing index, read once, so a later launch
  function existingIndex() {           // updates the same record instead of appending a duplicate
    if (existingById) return existingById;
    existingById = {};
    const count = parseInt(get(IK.count), 10) || 0;
    for (let i = 0; i < count; i++) { const id = get(IK.id(i)); if (id) existingById[id] = i; }
    nextN = Math.max(nextN, count);
    return existingById;
  }
  function writeOne(id, objId, type, ok, response, correct, description, latencySec) {
    id = fitId(id);
    if (!live || seenThisSession.has(id)) return;
    seenThisSession.add(id);
    let n = v2004 ? existingIndex()[id] : undefined;
    if (n === undefined) { n = nextN++; if (v2004) existingById[id] = n; }
    set(IK.id(n), id);
    set(IK.type(n), TYPES.has(type) ? type : 'choice');
    set(IK.obj(n), objId);
    set(IK.when(n), v2004 ? new Date().toISOString() : wallTime());
    set(IK.weight(n), 1);
    set(IK.resp(n), clip(response, 255));
    set(IK.correct(n), clip(correct, 255));
    set(IK.result(n), ok ? 'correct' : (v2004 ? 'incorrect' : 'wrong'));
    set(IK.latency(n), v2004 ? latency2004(latencySec) : latency12(latencySec));
    if (v2004) set(IK.desc(n), clip(description, 250));
  }
  // base: "ch01.c-kelompok" (no row suffix yet). stored: {d, rows: [{k, t, ok, r, c}]}. A single row writes
  // one interaction at the bare base id; several rows (a grouping/matching or multi-step question) write one
  // interaction per row, suffixed with that row's own stable key.
  function writeInteractionsFor(base, stored, latencySec) {
    const rows = stored.rows && stored.rows.length ? stored.rows : [{ t: 'choice', ok: false, r: '', c: '' }];
    const objId = base.split('.')[0];
    if (rows.length === 1) {
      const r = rows[0];
      writeOne(base, objId, r.t, r.ok, r.r, r.c, stored.d, latencySec);
    } else {
      for (const r of rows) {
        const id = base + '.' + (r.k || 'row');
        const desc = stored.d + (r.k ? ' — ' + r.k.replace(/-/g, ' ') : '');
        writeOne(id, objId, r.t, r.ok, r.r, r.c, desc, latencySec);
      }
    }
  }
  function rewriteAllInteractions() {
    if (v2004) existingIndex();
    for (const [base, stored] of Object.entries(S.q)) writeInteractionsFor(base, stored, 0);
  }

  /* ---------- session start and end ---------- */
  const t0 = Date.now();
  if (live) {
    if (v2004) {
      if (get('cmi.completion_status') === 'not attempted' || get('cmi.completion_status') === 'unknown') set('cmi.completion_status', 'incomplete');
      set('cmi.exit', 'suspend');
    } else {
      if (get('cmi.core.lesson_status') === 'not attempted') set('cmi.core.lesson_status', 'incomplete');
      set('cmi.core.exit', 'suspend');
    }
    rewriteAllInteractions();
    lms.commit();
  }

  function sessionTime() {
    const s = Math.max(0, Math.round((Date.now() - t0) / 1000));
    const hh = Math.floor(s / 3600), mm = Math.floor(s / 60) % 60, ss = s % 60;
    return v2004 ? `PT${hh}H${mm}M${ss}S` : `${String(hh).padStart(4, '0')}:${pad(mm)}:${pad(ss)}`;
  }
  let ended = false;
  function end() {
    if (!live || ended) return;
    ended = true;
    set(v2004 ? 'cmi.session_time' : 'cmi.core.session_time', sessionTime());
    // Always suspend, even when finished, so a learner who comes back to review still sees their checkmarks.
    set(v2004 ? 'cmi.exit' : 'cmi.core.exit', 'suspend');
    lms.commit();
    lms.finish();
  }
  addEventListener('pagehide', end);
  addEventListener('beforeunload', end);

  /* ---------- the interface book pages use ---------- */
  window.PapermorphSCORM = {
    live,
    progressKey: CFG.progressKey,   // the contents page's own key, when the book sets one
    // A copy of {done, last}, in the shape the book's own progress() works on.
    progress: () => ({ done: S.done.slice(), last: S.last }),
    // The book changed its progress (opened or finished a chapter).
    save(p) {
      S.done = [...new Set((p.done || []).filter(known))].sort((a, b) => a - b);
      if (Number.isInteger(p.last)) S.last = p.last;
      report();
    },
    // A chapter's finish card appeared; [right, total] are its first-try answers. Keep the best attempt.
    finished(n, right, total) {
      if (known(n) && !S.done.includes(n)) S.done = [...S.done, n].sort((a, b) => a - b);
      const old = S.s[n];
      if (total > 0 && (!old || right / total > old[0] / old[1])) S.s[n] = [right, total];
      report();
    },
    // A question (or one of its rows) was graded for the first time. entry: { rows: [{key, type, ok,
    // response, correct}, ...] }, from engine.js's reportAnswer. Locked in forever: a question already in
    // S.q is never reported again, so answering it differently after a restart or in a later session can
    // never change what the LMS already has, and reopening the module never writes a duplicate for it.
    answered(chapterN, qid, entry, description, latencySec) {
      if (!known(chapterN)) return;
      const base = fitId('ch' + pad(chapterN) + '.' + qid);
      if (Object.hasOwn(S.q, base)) return;
      const rows = (entry.rows && entry.rows.length ? entry.rows : [{ key: null, type: 'choice', ok: entry.total > 0 && entry.right === entry.total, response: '', correct: '' }])
        .map(r => ({ k: r.key || null, t: r.type || 'choice', ok: !!r.ok, r: clip(r.response, 255), c: clip(r.correct, 255) }));
      S.q[base] = { d: clip(description, 250), rows };
      writeInteractionsFor(base, S.q[base], latencySec);
      report();
    },
    start(frame) {
      // Every launch opens on the cover; its Continue button uses the saved last chapter.
      frame.src = 'book/index.html';
    },
  };
})();
