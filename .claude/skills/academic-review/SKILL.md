---
name: academic-review
description: Mekanizma Kitabı'nda bir bölümü veya bölüm parçasını bağımsız kıdemli bilimsel/editöryal incelemeden geçirir. Claude ana yazar, Codex (resmi openai/codex-plugin-cc eklentisi) salt-okunur bağımsız editördür. Kullanıcı "Codex'e kontrol ettir", "editör kontrolü yap", "bu bölümü bitir", "academic-review", "bilimsel inceleme yaptır" dediğinde veya bir bölüm/alt bölüm tamamlandığında (kullanıcı aksini söylemedikçe) kullan.
---

# Skill: academic-review

`CLAUDE.md`'deki **Claude = Principal Author / Codex = Senior Scientific Editor** iş bölümünü uygular. Codex, `openai/codex-plugin-cc` resmi eklentisi üzerinden çağrılır (kurulu: marketplace `openai-codex`, plugin `codex@openai-codex`). **Codex hiçbir manuscript dosyasını değiştirmez, oluşturmaz, silmez, yeniden adlandırmaz, patch uygulamaz.** Yalnızca stdout'a yapılandırılmış editör raporu üretir; kararı ve uygulamayı **Claude** yapar.

## Doğrulanmış delegation yolu (smoke test edildi 2026-09-27)

- Codex, plugin'in rescue mekanizması üzerinden çağrılır: `node "$CLAUDE_PLUGIN_ROOT/scripts/codex-companion.mjs" task --fresh --wait <prompt>` (interaktif oturumda karşılığı `/codex:rescue --fresh`). Plugin bu yolu **`sandbox: read-only`** ile çalıştırır (`--write` verilmedikçe) — bu OS düzeyinde gerçek bir yazma-engeli, yalnız prompt değil.
- **`/codex:review` KULLANMA:** özel akademik focus alamaz, git/kod diff'i için tasarlanmıştır.
- **`/codex:adversarial-review` yalnız ikinci, isteğe bağlı pressure-test** olarak; özellikle manuscript değişiklikleri working-tree/branch diff içindeyse (§4).
- Read-only garantisi smoke test ile doğrulandı: inceleme öncesi/sonrası manuscript hash'i ve `git diff` birebir aynı kaldı.

## Ne zaman çalışır

- "Codex'e kontrol ettir", "editör kontrolü yap", "bu bölümü bitir", "academic-review [Bölüm N]".
- Bir bölüm/alt bölüm/paket tamamlandığında, kullanıcı aksini söylemedikçe.

## Adım adım iş akışı

### 1. Kapsamı belirle
İncelenecek bölüm/dosya(lar)? Belirtilmediyse en son çalışılan bölümü varsay ve teyit et. Kaynak dosyayı, ilgili kaynak kütüğü satırlarını (`Bölüm_00` §2) ve `git log --oneline -- <dosya>` geçmişini not al.

### 2. Claude self-review
Codex'ten önce bölümü CLAUDE.md §2, Dogrulama_Protokolu T1–T5 ve Stil_Rehberi'ne göre kendi gözünle oku. Bariz şeyleri Codex'e devretme; hedef bağımsız gözün bulacağı sorunlar.

### 3. Kapsam durumunu belirle → doğru komutu seç
- **Bitmiş/commit edilmiş bölüm** (working tree'de o dosyada değişiklik yok) → §3A (`task --fresh`).
- **Bu oturumda değişmiş / commit edilmemiş manuscript** → önce §3A ile bütünsel inceleme; istenirse §4 ile diff-temelli ikinci tur.

### 3A. Codex'i çağır — salt-okunur editör raporu (`task --fresh`)

**Zorunlu kurallar:**
- **Her review `--fresh`** — önceki Codex thread'ini ASLA resume etme (thread izolasyonu; §"Thread izolasyonu").
- Prompt **tam olarak** şu cümleyle başlar: `READ-ONLY SCIENTIFIC EDITORIAL REVIEW. DO NOT MODIFY, CREATE, DELETE, RENAME OR PATCH ANY FILE.`
- Codex'ten **yalnızca stdout'a editör raporu** iste; hiçbir dosyaya çıktı yazdırma (`-o`, output dosyası, "kaydet" vb. YOK).
- Codex'e verilen görev metninde **write-fiili kullanma:** `fix`, `apply`, `edit`, `rewrite`, `implement`, `update`, `patch`, `düzelt`, `uygula`, `yeniden yaz` gibi Codex'i write-task'a çeviren fiiller yasak. Yalnız `review`, `assess`, `report`, `identify`, `incele`, `değerlendir`, `raporla`, `işaretle` kullan.

Komut:
```bash
node "$CLAUDE_PLUGIN_ROOT/scripts/codex-companion.mjs" task --fresh --wait "READ-ONLY SCIENTIFIC EDITORIAL REVIEW. DO NOT MODIFY, CREATE, DELETE, RENAME OR PATCH ANY FILE. Return only an editorial report to stdout; write to no file.

CONTEXT: <proje> — Türkçe akademik tıbbi genetik ders kitabı. Review ONLY <bölüm/section> of file: <Bölüm_NN_*.md> in the current working directory. Read that file yourself. Çekirdek pedagoji: mekanizma → varyant tipi → hücresel sonuç → klinik fenotip → tanısal test → varyant yorumu (ACMG/ClinGen).

Assess these axes; report EACH finding exactly as:
SEVERITY (BLOCKER/MAJOR/MINOR/SUGGESTION) | LOCATION (dosya+satır) | ISSUE | WHY IT MATTERS | PROPOSED ACTION | CONFIDENCE (high/moderate/low)

1. FACTUAL ACCURACY — moleküler/hücresel/biyokimyasal/gelişimsel/genetik mekanizma hataları
2. MECHANISTIC CAUSALITY — atlanan basamak, ters nedensellik, aşırı basitleştirme, kanıtlanmamış bağlantı
3. TERMINOLOGY — gen/protein/kompleks/domain/pathway/hastalık/varyant terimleri doğru ve kitap geneliyle tutarlı mı
4. CLAIM-EVIDENCE ALIGNMENT — metin kanıttan güçlü mü konuşuyor; association/mechanism/causation/hypothesis/established fact ayrımı
5. MISSING MECHANISMS — anlaşılırlık için gereken ama eksik ara süreç
6. INTERNAL CONSISTENCY — bu bölüm veya önceki bölümlerle çelişen ifade
7. PEDAGOGICAL QUALITY — anlatım mekanizmayı öğretiyor mu; gereksiz tekrar, bilgi sıçraması, açıklanmadan kullanılan kavram
8. FIGURE OPPORTUNITIES — hangi kısım şema/diyagram/tabloyla daha iyi anlatılır (yalnız fırsatı işaretle; görsel doğruluğu ayrı figure-review skill'inde)
9. REDUNDANCY & STRUCTURE — tekrar eden/yanlış yerde/başka başlık altında olması gereken içerik
10. STRUCTURE — standart 10 başlık formatı (CLAUDE.md §4) eksiksiz ve sıralı mı

Bulgu yoksa 'bulgu yok' de; bulgu uydurma. Report only; change nothing."
```
- Uzun/çok bölümlü inceleme için `--wait` yerine `--background` kullanılabilir; sonra `/codex:status` → `/codex:result`.

### 4. (Opsiyonel) İkinci tur — diff pressure-test
Manuscript değişiklikleri working-tree/branch diff içindeyse ve tasarım/varsayım sorgulaması isteniyorsa:
```
/codex:adversarial-review --base <son commit sha>
<yukarıdaki READ-ONLY başlangıç + 10 başlık, focus text olarak>
```
Steerable ve salt-okunurdur; yalnız ikinci, isteğe bağlı pressure-test.

### 5. Claude adjudication (ZORUNLU)
**Codex'in hiçbir bulgusunu otomatik kabul etme.** Her bulguyu kaynağa/metne bakarak doğrula:
- Yanlış/gereksiz bulguları **reddet**, nedenini kullanıcı raporunda göster (sessizce atma).
- Kabul edilenleri **Claude uygular** — Codex'e patch yaptırma.
- Kitabın bilinçli editöryal kararıysa (T5 pedagojik sentez, onaylı esneklik kuralı) → **YANLIŞ POZİTİF**; `Editor_Degerlendirme_Formu_Tur2.md` / `Dogrulama_Kutugu.md`'ye bak.
- BLOCKER/MAJOR kalırsa düzeltme sonrası ikinci Codex turu açılabilir. **En fazla 2 tur** — sonsuz döngü yok.

### 6. Kullanıcıya rapor
Kaç bulgu / kaç kabul-red (kısa gerekçe) · uygulanan diff özeti · kalan açık nokta (BEKLİYOR / insan uzmanı) · stage/commit/push için **ayrı onay iste** (CLAUDE.md §1C).

## Model seçimi
Codex'in **mevcut varsayılan modelini** kullan; komuta model bayrağı (`--model`, `-m`, `-c model=…`) ekleme. Model ancak **kullanıcı açıkça istediğinde** override edilir; aksi hâlde Codex kendi varsayılanıyla çalışır.

## Thread izolasyonu
Her bağımsız bölüm review'ü **`--fresh`**. Önceki Codex rescue thread'lerini resume etme — Codex önceki Claude/Codex tartışmasından etkilenmeden bağımsız editör gibi davransın.

## Sınır
Codex ortak yazar değildir; yalnız eleştirir, boşluk bulur, kalite kontrol yapar. Nihai metin ve akademik ses **Claude'undur**. Bu skill bağımsız insan uzman incelemesinin yerine geçmez (Dogrulama_Protokolu §6).
