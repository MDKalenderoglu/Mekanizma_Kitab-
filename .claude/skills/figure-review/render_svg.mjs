// figure-review renderer: SVG → PNG, en-boy oranını koruyarak.
// Kullanım: node render_svg.mjs <girdi.svg> <çıktı.png> [genişlik=1600]
// Bağımlılık: sharp (bkz. package.json). Kontrollü kontrol: sharp yoksa net hata
// verir ve durur — sessiz/rastgele bir fallback renderer'a düşmez.
import { readFileSync } from 'node:fs';

const [, , inPath, outPath, widthArg] = process.argv;
if (!inPath || !outPath) {
  console.error('Kullanım: node render_svg.mjs <girdi.svg> <çıktı.png> [genişlik]');
  process.exit(2);
}
const width = parseInt(widthArg || '1600', 10);

let sharp;
try {
  sharp = (await import('sharp')).default;
} catch (err) {
  console.error(
    "HATA: 'sharp' bulunamadı. figure-review render'ı sharp gerektirir.\n" +
    "  Çözüm: cd .claude/skills/figure-review && npm install\n" +
    "  (rsvg-convert/cairosvg kuruluysa onları elle da kullanabilirsin; " +
    "ama bu betik sessiz bir fallback KULLANMAZ.)"
  );
  process.exit(1);
}

const svg = readFileSync(inPath);
await sharp(svg, { density: 200 })
  .resize({ width, withoutEnlargement: false })
  .flatten({ background: '#ffffff' })
  .png()
  .toFile(outPath);

const meta = await sharp(outPath).metadata();
console.log(`rendered ${outPath}: ${meta.width}x${meta.height}`);

// Kırpılma guard'ı: geniş şekiller (viewBox ~1200x780) kareye kırpılmamalı.
// Çıktı oranı ~1.3–1.7 aralığında beklenir; kare (~1.0) ise render kusurludur.
const ratio = meta.width / meta.height;
if (ratio < 1.15) {
  console.warn(
    `UYARI: çıktı en-boy oranı ${ratio.toFixed(2)} — beklenenden dar/kare. ` +
    'Şekil kırpılmış olabilir; renderer ayarını kontrol et.'
  );
}
