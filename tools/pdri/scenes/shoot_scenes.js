const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1.5 });
  const errs = [];
  pg.on('pageerror', e => errs.push(e.message));
  pg.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  fs.mkdirSync(process.argv[2] + '/png', { recursive: true });
  for (const f of fs.readdirSync(process.argv[2] + '/html').filter(f => f.endsWith('.html')).sort()) {
    errs.length = 0;
    await pg.goto('file://' + path.resolve(process.argv[2] + '/html', f) + '?beat=0&t=999');
    await pg.waitForTimeout(1500);
    await pg.evaluate(() => document.fonts.ready);
    const st = await pg.$('#stage');
    await st.screenshot({ path: process.argv[2] + '/png/' + f.replace('.html', '.png') });
    console.log(f, errs.length ? errs.join(' | ') : 'ok');
  }
  await b.close();
})();
