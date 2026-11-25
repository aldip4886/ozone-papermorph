// Connects a Papermorph book page to the SCORM host in launch.html. scripts/scorm.py adds it to every page:
// in the contents page's <head>, and in each chapter right after lib/engine.js (before the chapter calls boot()).
// Outside the package wrapper it does nothing, so the book still works as a plain web book.
'use strict';
(function () {
  let host = null;
  try { host = parent !== window && parent.PapermorphSCORM; } catch {}
  if (!host) return;

  // 1. Seed the book's own progress store from the LMS, so the contents page and the chapter
  //    see the learner's saved checkmarks. This file sits in the book folder, the same folder the default key names;
  //    in a chapter, the engine's own key (BOOK_PROGRESS_KEY, which honours lib/book.css --progress-key) wins;
  //    on the contents page, the progressKey the page passes to Contents.book(), which scorm.py reads at build time.
  const KEY = typeof BOOK_PROGRESS_KEY === 'string' ? BOOK_PROGRESS_KEY
    : host.progressKey || 'animebook:progress:' + new URL('.', document.currentScript.src).pathname;
  try { localStorage.setItem(KEY, JSON.stringify(host.progress())); } catch {}

  // 2. In a chapter, every progress change and every finish goes to the host as well.
  //    engine.js's top-level functions and constants are shared globals, so they can be wrapped here.
  if (typeof progress === 'function' && typeof finishCard === 'function') {
    const own = progress;
    progress = function (f) {
      const p = host.progress();
      f(p);
      host.save(p);
      own(f);                                  // keep the page's localStorage copy in step
    };
    const card = finishCard;
    finishCard = function () {
      // Score the chapter and tell the host BEFORE rendering the card: the card's own progress()
      // call (below, via card.apply) triggers an immediate report() too, and that report must never
      // fire while S.s[chapter] is still empty -- it would briefly commit "failed" with no score,
      // just before this function's real score arrives a moment later.
      let right = 0, total = 0;
      for (const v of Object.values(typeof SCORE === 'object' ? SCORE : {})) { right += v.right; total += v.total; }
      host.finished(CHAPTER.number, right, total);
      card.apply(this, arguments);
    };
  } else if (/\/ch\d\d\/[^/]*$/.test(location.pathname)) {
    console.error('[scorm] This chapter has no progress()/finishCard() to hook; the Papermorph engine may have changed. Completion will not reach the LMS.');
  }

  // 2b. In a chapter, every question's or row's first-ever grading goes to the host as a cmi.interactions
  //     record. engine.js calls window.onInteraction itself (it doesn't know SCORM exists), so this is the
  //     only wiring a chapter page needs; a plain web book just never sets the hook.
  //     This file runs right after lib/engine.js -- before the chapter's own inline script has declared
  //     CHAPTER -- so the gate here is typeof finishCard, the same engine-is-a-chapter-page check block 2
  //     already uses, never typeof CHAPTER (which doesn't exist yet at this point in page load). CHAPTER is
  //     read only inside the callback, once a question has actually been answered.
  if (typeof finishCard === 'function') {
    window.onInteraction = (qid, entry, description, latencySec) => {
      try {
        if (typeof CHAPTER !== 'object' || !CHAPTER) return console.error('[scorm] CHAPTER missing; interaction not reported:', qid);
        host.answered(CHAPTER.number, qid, entry, description, latencySec);
      } catch (e) { console.error('[scorm] answered() failed:', e); }
    };
  }

  // 3. LMS file servers often don't serve a folder's index.html for a folder URL like "ch02/",
  //    so point every same-site folder link at its index.html.
  const fix = href => href.replace(/^([^?#:]*\/)(?=[?#]|$)/, '$1index.html');
  const sameSite = href => { try { return new URL(href, location.href).origin === location.origin; } catch { return false; } };
  const fixLink = a => {
    const href = a.getAttribute('href');
    if (href && sameSite(href)) { const f = fix(href); if (f !== href) a.setAttribute('href', f); }
  };
  document.addEventListener('click', e => { const a = e.target.closest?.('a[href]'); if (a) fixLink(a); }, true);
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('a[href]').forEach(fixLink);
    if (typeof CHAPTER === 'object' && CHAPTER?.next && sameSite(CHAPTER.next)) CHAPTER.next = fix(CHAPTER.next);
    // A chapter page that still has no onInteraction hook by now means a question's first answer will
    // silently never reach the LMS -- that must never fail quietly.
    if (/\/ch\d\d\/[^/]*$/.test(location.pathname) && typeof window.onInteraction !== 'function') {
      console.error('[scorm] This chapter never got a window.onInteraction hook (finishCard missing at bridge load?); answers will not be reported to the LMS.');
    }
  });
})();
