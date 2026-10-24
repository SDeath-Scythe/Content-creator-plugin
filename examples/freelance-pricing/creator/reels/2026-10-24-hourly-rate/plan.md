# Reel plan: your hourly rate is wrong (idea 20261024-1)

Page: @test.pricing.design · Instagram only · Arabic (Gulf) · test run, owner approval given at every gate (recommended option taken).

Stages: 1 Goal [done] · 2 Hooks [done] · 3 Script [done] · 4 Production plan [done] · 5 Build [see Build] · 6 Captions [see Captions] · 7 Approval card [see creator/reels/2026-10-24-hourly-rate/approval-card.md]

## 1. Goal

- **Goal: LEAD** (page goal is leads; CTA keyword PRICE).
- **Emotion:** terminal curiosity plus a little indignation: "my price has been half of what it should be, and I did the maths myself". Mechanic: show the value (the two-line calculation), withhold the tool (the calculator) behind PRICE.
- Page goal served: free calculator delivered by DM. The DM must really deliver the Google Sheet (open question in page.md: share setting and who sends the DM).
- Idea evidence: hypothesis only (audience.md). All numbers on screen are an illustrative example, labelled "مثال".

## 2. Hooks

Frame plans are described from frame 0. Hooks run 3 to 6 Arabic words so the claim lands at 1.2 to 1.6 s.

| # | Hook (Arabic) | Frames 0 to 3 s | Pattern | Checklist |
| --- | --- | --- | --- | --- |
| A | ساعاتك المدفوعة مو 8 | 0.0 giant yellow "8" already slamming in over an 8-block work-day bar, blocks filling; 0.5 bar full, "8" settles; 1.2 claim lands word by word: ساعاتك / المدفوعة / مو / 8; 1.8 four of the eight blocks go dark and drop; 2.4 "4" replaces the "8", pulsing; 3.0 cut to body | Contrarian + something breaks | 1 to 8 pass (see below) |
| B | سعر ساعتك: 50؟ الصح 100 | 0.0 price tag "50 ريال / ساعة" shaking, yellow; 0.5 counter starts climbing; 1.2 claim words; 2.0 number locks at 100; 3.0 cut | Number races and locks (result first) | passes but the claim is long (7 words), lands after 1.6 s in Arabic |
| C | ليش تسعّر على 8 ساعات؟ | 0.0 empty invoice line "8 × ساعتك" ticking; 1.2 claim; 2.0 question mark slams | Question | weaker: point 4 (nothing extraordinary) thin; point 6 filler start |

Checklist for A, frame by frame: 1 frame 0 already moving (slam + filling blocks) ✓ · 2 recognisable: the designer's own work-day and rate unit (a day bar with hours) ✓ · 3 the "8" owns about 40% of the frame and moves from frame 1 ✓ · 4 four blocks collapse before 3 s ✓ · 5 claim lands 1.2 s word by word ✓ · 6 first spoken word "ساعاتك" at 0.0 to 0.3 s (voice not yet recorded; captions carry it in this test) ✓ · 7 works on mute: the claim and the visual are both on screen ✓ · 8 about the viewer's own hours ✓.

`hook-wins.csv` is empty (0 rows), so no past-winner structure offered.

**Picked (owner gate, recommended): A.** Not a trial reel (no data yet; owner can switch it on in the app).

## 3. Script (A). Target length 29 s

Voice: owner will record later; this test renders **without voice or music**, captions timed to the script lines.
Digits: Western (0 to 9). Currency: ريال (SAR), written the same way each time. Both are assumptions to confirm (open questions in page.md).

| Time | Spoken line (Gulf) | On-screen text | Visual |
| --- | --- | --- | --- |
| 0.0 to 3.0 | ساعاتك المدفوعة مو 8 | Claim: ساعاتك المدفوعة مو 8 | Giant "8" slams in; 8-block day bar fills; at 1.8 s four blocks go dark and fall |
| 3.0 to 8.0 | تقعد 8 ساعات. بس المدفوع منها 4 | مثال: 4 ساعات مدفوعة · tags on dark blocks: رسائل، عروض أسعار، تعديلات، بحث | Day bar: four lit blocks, four dark blocks with tags rising on each |
| 8.0 to 14.0 | مثال: تبغى 8,800 ريال بالشهر | 8,800 ريال / الشهر · 22 يوم × 8 ساعات = 176 · 8,800 ÷ 176 = 50 | Calculation builds line by line; the 50 pops in yellow |
| 14.0 to 21.0 | بس المدفوع 4 ساعات باليوم | 22 يوم × 4 ساعات = 88 · 8,800 ÷ 88 = 100 | Previous 50 strikes through, new line builds, number races 50 to 100 and locks |
| 21.0 to 25.0 | يعني حسبت نص سعرك | 50 ← نص السعر · 100 | 50 shrinks next to 100 (half bar versus full bar) |
| 25.0 to 29.0 | اكتب PRICE وأرسل لك الحاسبة مجاناً | اكتب PRICE · الحاسبة مجاناً | CTA pops; keyword in its own LTR span; small "الأرقام أمثلة مو وعد" line |

- CTA: comment PRICE; DM delivers the free pricing calculator (Google Sheet). Serves goal LEAD. Per arabic.md, whoever sends the DM should accept "PRICE" and "سعر".
- Reason to comment (not bait): the example is a hypothesis for their own hours; the caption asks them to count their own paid hours, and PRICE gets the sheet that does it.
- Voice file check: no banned words (ثراء، مضمون، سر، خيالي، أسهل طريقة), no income promise, no other designers named, all numbers labelled as an example.
- Muted version first: every line is on screen as caption text.

## 4. Production plan

| Choice | Decision |
| --- | --- |
| Picture | Faceless, built in code (render-reel, built-in engine, forced by the owner for this test) |
| Voice | None in this test. Real voice (owner records later, preferred) will replace caption timing |
| Sound | No music, silent AAC track added by the renderer. Trending sound can be added in the app by hand |
| On-camera edit | Not used |
| Cover | Designed JPEG: "ساعاتك المدفوعة مو 8", big 8 in yellow, small yellow bar |
| Assets to supply | None. Fonts come from the plugin |

Confirmed by owner (test). Fully code-built.

## Build

- **Engine:** built-in (Playwright + ffmpeg), chosen by the owner for this test. Node 22.22, ffmpeg 6.1.1, Playwright found on NODE_PATH, no npm install.
- **Files:** `out/reel.mp4` (29 s, 1080×1920, 30 fps, 5.0 MB, H.264 + silent AAC), `out/cover.jpg` (1080×1920 JPEG, 61 KB), review frames in `out/frames/`.
- **Render time:** 95.6 s wall clock for 870 frames (about 3.3 s per second of video).
- **Spec check (instagram):** `ok: true`, `fails: []`, `warnings: []`.
- **Design pass:** impeccable was available but its launcher, detector and sub-agent flow were blocked by permission prompts in this non-interactive run. The design review was done inline on the stills (degraded run). Fixes applied: frame-0 bar made solid, CTA text no longer duplicates the caption, scene 2 opens with content visible.
- **Captions:** timed to the script lines (no voice yet), not to a voice transcript.
- **Still to do by the owner:** record the voice (script lines above) and re-time the captions to it, or post as a text-led reel; confirm digits and currency; confirm the sheet share link and who sends the DM; add a trending sound in the app if wanted.
- **Frames:** 0 s solid 8 mid-slam over a filling 8-block day bar; 1.5 s claim "ساعاتك المدفوعة مو" with "8" about to land; 3.0 s scene 2 starting ("مثال", "4 ساعات مدفوعة", 4 lit and 4 dimmed blocks, caption "تقعد 8 ساعات").

## Captions

Instagram only (page.md lists no other platform). Keyword in the first line, one CTA (PRICE), 4 hashtags, no income promise, numbers labelled as an example.

**Instagram caption:**

```
Freelance designer hourly rate: you do not bill 8 hours a day
سعر ساعتك كمصمم حر غلط إذا حسبته على 8 ساعات.
مثال: 8,800 ريال بالشهر ÷ 176 ساعة = 50 ريال بالساعة.
بس إذا المدفوع 4 ساعات باليوم: 8,800 ÷ 88 = 100 ريال.
الرسائل والتعديلات والبحث ما أحد يدفع لك عنها، فلازم تدخل بسعرك.
الأرقام أمثلة مو وعد.
اكتب PRICE وأرسل لك حاسبة التسعير مجاناً.
#تسعير_التصميم #مصمم_حر #فريلانسر_الخليج #freelancedesigner
```

- DM keyword: accept PRICE and سعر.
- No first comment.
- Alt/search keywords on screen and in the first spoken line: ساعتك، سعر، مصمم حر.
