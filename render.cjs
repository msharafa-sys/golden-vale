const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const [,, mode, src, out, w, h] = process.argv;
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }).catch(async () => chromium.launch());
  const p = await b.newPage({ viewport: { width: +w || 1920, height: +h || 1080 } });
  await p.goto('file://' + src, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  if (mode === 'pdf') await p.pdf({ path: out, width: (+w||1920)+'px', height: (+h||1080)+'px', printBackground: true, preferCSSPageSize: true });
  else await p.screenshot({ path: out, fullPage: true });
  await b.close();
})();
