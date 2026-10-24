# Reel (Arabic): مشروع تخرجك ياخذ منك فصل كامل؟

Status: built with the ElevenLabs narration and checked; not posted. The page's lead reel: it sells the service (we build the project and write the report).

## 1. Goal
**Leads.** The emotion: relief. "A whole semester of work, and someone else can carry it."
Serves the page goal: comment «مشروع» to get the details and the price.

## 2. Hooks (each checked against the virality 8-point list)

| # | Hook | Frames 0 to 3 s | Pattern | Check |
| --- | --- | --- | --- | --- |
| A | **مشروع تخرجك ياخذ منك فصل كامل؟** | 0 s: the student's semester plan slams in (learn everything, design, build, test, an 80-page report in red). 0.35 to 1.5 s: the week pills tick red one by one. 1.0 to 1.6 s: the question lands. 2.3 s: a green «خلّيه علينا» stamp slams down | question + relief | 8/8 (point 6 once the voice starts on «مشروع») |
| B | 80 صفحة تقرير؟ ولا صفحة عليك. | 0 s: a page counter races to 80 and locks | number-race | 7/8: point 2 is weaker; a counter alone isn't instantly "my project" |
| C | آخر أسبوع قبل التسليم وما بديت؟ | 0 s: a calendar with the deadline circled | fear | 7/8: works, but leads with panic rather than relief; keep for a later reel |

**Picked A.** Frame 0 is the student's own workload; the stamp is the "extraordinary event", and it lands the offer before 3 s.

## 3. Script (first cut 15 s; final 21.2 s with the narration and effects, see section 5)

| Time | Voiceover (to record, in the owner's dialect) | On screen | Visual |
| --- | --- | --- | --- |
| 0 to 3 | مشروع تخرجك ياخذ منك فصل كامل؟ خلّيه علينا. | مشروع تخرجك ياخذ منك فصل كامل؟ | The plan, then the «خلّيه علينا» stamp |
| 3 to 6 | نبني مشروعك كامل: برمجة، تصميم، واختبار. | 1. نبني مشروعك كامل | The four build rows flip to «علينا» one by one (3.2 to 4.4 s) |
| 6 to 9 | ونكتب التقرير كامل، بتنسيق جامعتك. | 2. ونكتب التقرير كامل | The red 80-page report row flips to «علينا · التقرير كامل» |
| 9 to 12 | ونجهّزك للمناقشة، نشرح لك كل جزء. | 3. ونجهّزك للمناقشة | A sixth row slides in: «علينا · تجهيزك للمناقشة» |
| 12 to 15 | اكتب «مشروع» بالتعليقات وانطيك التفاصيل والسعر. | اكتب مشروع بالتعليقات | «جاهز ✓» stamp |

Read the voiceover aloud and change any word that doesn't sound like you. On-screen text uses light colloquial Arabic that reads across countries.

## 4. Production plan

Faceless, built in code (built-in engine). Voice: the owner. Sound: no music, or a licensed bed under the voice. Cover: the hook over the plan with the «خلّيه علينا» stamp.

## 5. Build (v2: motion, sound effects, real report)

**Soundtrack** (`build/audio.py`): the narration (`assets/voice.mp3`, 18.3 s) is cut at its own pauses and gaps are opened at the key moments, then mixed with sound effects that are synthesized in the script (no samples, nothing to license), and normalised for Instagram. Result: 21.2 s.

| Reel time | Voice | Picture | Sound |
| --- | --- | --- | --- |
| 0 to 3.1 | مشروع تخرجك… ياخذ منك فصل كامل؟ | Plan slams in; week pills tick red; words appear as spoken; punch zoom on «كامل؟» | Thud, five ticks |
| 3.1 to 4.85 | خلّيه علينا (3.8) | Stamp at 3.6 with a flash and camera shake | Rising whoosh into a heavy stamp |
| 4.85 to 9.2 | نبني مشروعك كامل… برمجة، تصميم، واختبار | Step 1 slides in; a browser IDE and a mobile app fly over the plan (5.05 to 7.0, labelled «مشاريع نبنيها»); then the rows flip on their words (7.05, 7.25, 7.85, 8.45) | Whooshes, pops rising in pitch |
| 9.2 to 12.7 | ونكتب التقرير كامل، بتنسيق جامعتك | Report row flips (9.9); the real report's contents page slides up over half the plan, labelled «من شغلنا»; a highlighter sweeps "Chapter One" (10.85) | Pop, paper, marker |
| 12.7 to 15.75 | ونجهّزك للمناقشة… نشرح لك كل جزء | Defence row slides in (12.8); a defence slide deck flies in (13.05 to 15.5) | Pops, whoosh |
| 15.75 to 21.2 | اكتب «مشروع» بالتعليقات… وانطيك التفاصيل والسعر | Riser, then the CTA hits at 16.5 with a flash and shake; «مشروع» pulses (17.1); «جاهز ✓» stamp and confetti (20.15) | Riser, big hit, pop, ding + sparkles |

- The app screens are built in code (`build/reel.html`), not copied from the internet: original, so nothing to license, and they match the kind of project in the report. Swap in screenshots of the page's real past projects when there are some.
- The report page (`build/assets/report-toc.jpg`) is the owner's own work.
- Render: `python3 build/audio.py assets/voice.mp3 mix_raw.wav`, then `ffmpeg -i mix_raw.wav -af loudnorm=I=-14:TP=-1.5:LRA=11 mix.wav`, then `node skills/render-reel/scripts/render.mjs build/reel.html out/reel.mp4 --voice mix.wav --cover out/cover.jpg` (about 2 minutes).
- Spec check (`out/spec.json`): **ok**. 21.2 s, 1080×1920, 30 fps, H.264 + AAC, 7.8 MB, about -15.7 LUFS. Frames: `out/frames.png`.

## 6. Instagram caption
```
مشروع تخرجك ياخذ منك فصل كامل؟ خلّيه علينا 👇

✓ نبني المشروع كامل: برمجة، تصميم، واختبار
✓ نكتب التقرير كامل بتنسيق جامعتك ومع المراجع
✓ نجهّزك للمناقشة ونشرح لك كل جزء

اكتب «مشروع» بالتعليقات ونرسل لك التفاصيل والسعر.

#مشروع_تخرج #مشاريع_تخرج #تقرير_تخرج #طلاب_الجامعة #graduationproject
```

## 7. Approval card
`out/reel.mp4`, 21.2 s, 1080×1920, 7.8 MB, cover `out/cover.jpg`, manual route, trial reel recommended. Ready for the owner's yes. The voice is AI-generated: generate it on a paid ElevenLabs plan for commercial use.

## Note on the offer
Universities treat submitting work someone else did as misconduct, and some countries have laws against "contract cheating" services. The reel only promises what the page delivers: no grade guarantees, no claims about passing. Defence prep is part of the offer because the student still has to present and defend the project.
