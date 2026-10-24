# Reel (Arabic): خطة مشروع تخرجك مقلوبة

Status: built and checked; not posted. The Arabic version of [the project-plan reel](../2026-10-24-project-plan/plan.md): same goal, hook mechanic and structure. Needs the owner's voiceover before approval.

## Language decisions
- On-screen text in simple standard Arabic, so it reads the same in every country (`skills/reel-pipeline/references/arabic.md`). The voiceover can be in the owner's own dialect.
- Western digits. Week ranges sit in a left-to-right `<bdi>` so they read 1–4, never 4–1.
- No letter-spacing, line height 1.3 or more, Noto Kufi Arabic for headings and IBM Plex Sans Arabic for text.
- Comment keyword: مشروع, and accept PROJECT too.

## Hook
**خطة مشروع تخرجك مقلوبة.** Four words, landing word by word from 1.0 to about 1.5 s. Frame 0: the semester plan (مشروع التخرج / خطتي للفصل الدراسي) slams in, already moving. The week pills tick red one by one, and the «ترتيب غلط» stamp slams down at 2.3 s. Same 8/8 check as the English hook.

## Script (15 s)

| Time | Voiceover (to record, in the owner's dialect) | On screen | Visual |
| --- | --- | --- | --- |
| 0 to 3 | خطة مشروع تخرجك مقلوبة. | خطة مشروع تخرجك مقلوبة. | Plan: learn everything (weeks 1–4), design (5–7), build (8–12), test (13), the 80-page report (14–15, in red). «ترتيب غلط» stamp |
| 3 to 6 | ابنِ نسخة صغيرة أولاً: ميزة وحدة تشتغل من البداية للنهاية. | 1. ابنِ نسخة صغيرة أولاً | «أبني كل شيء» jumps to the top as «أبني نسخة صغيرة» (weeks 1–3), tagged أولاً |
| 6 to 9 | تعلّم بس اللي تحتاجه للميزة الجاية. | 2. تعلّم فقط ما تحتاجه الآن | «أتعلم كل التقنيات» becomes «أتعلم أثناء البناء» (حسب الحاجة), tagged ثانياً |
| 9 to 12 | واكتب التقرير وأنت تبني. كل ميزة تخلصها قسم جاهز. | 3. اكتب التقرير وأنت تبني | The red report row leaves week 14 and moves up as «أكتب التقرير» (كل أسبوع), tagged ثالثاً |
| 12 to 15 | اكتب «مشروع» بالتعليقات وأرسل لك الخطة. | اكتب مشروع في التعليقات | «الترتيب الصح» stamp |

The voiceover lines are only a starting point: read them aloud and change any word that doesn't sound like you.

## Build
- Engine: built-in. `build/reel.src.html` + `build/gen.py` → `build/reel.html`.
- Spec check (`out/spec.json`): **ok**. 15.0 s, 1080×1920, 30 fps, H.264 + AAC (silent), 2.9 MB.
- Frames: `out/frames.png`. Still to do: voice and captions.

## Instagram caption
```
خطة مشروع تخرجك مقلوبة 👇

أغلب الطلاب يخططون كذا: يتعلمون كل التقنيات ← يصممون كل شيء ← يبنون كل شيء ← يختبرون ← ويكتبون التقرير في آخر أسبوعين.

اقلبها:
1. ابنِ نسخة صغيرة أولاً: ميزة واحدة تعمل من البداية للنهاية
2. تعلّم فقط ما تحتاجه للميزة التالية
3. اكتب التقرير وأنت تبني: كل ميزة تنهيها قسم جاهز

اكتب «مشروع» في التعليقات وأرسل لك الخطة أسبوعاً بأسبوع + قالب التقرير.

#مشروع_تخرج #مشاريع_تخرج #طلاب_الجامعة #هندسة_برمجيات #graduationproject
```

## Approval card
`out/reel.mp4`, 15.0 s, 1080×1920, 2.9 MB, cover `out/cover.jpg`, manual route, trial reel recommended. **Not ready to post** until the voice is in.
