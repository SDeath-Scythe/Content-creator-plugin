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

## 3. Script (15 s)

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

## 5. Build
- Voice: `assets/voice.mp3`, generated in ElevenLabs (Iraqi Arabic voice, with emotion tags), 18.3 s. The reel was stretched from 15 s to 18.4 s to fit it instead of speeding the voice up.
- Timing comes from the voice's pauses: the hook words appear as they're spoken (0 to 2.5 s), the «خلّيه علينا» stamp lands at 3.3 s on those words, the build rows flip on «نبني» 4.6, «برمجة» 6.15, «تصميم» 6.85, «اختبار» 7.45, the report row on «ونكتب التقرير» 8.4, defence prep slides in on «ونجهّزك» 11.3, and the CTA runs 14.5 to 18.4.
- `build/reel.html` (hand-written; rows flip rather than move). Render: `node skills/render-reel/scripts/render.mjs build/reel.html out/reel.mp4 --voice assets/voice.mp3 --cover out/cover.jpg`.
- Spec check (`out/spec.json`): **ok**. 18.4 s, 1080×1920, 30 fps, H.264 + AAC, 3.4 MB, moov first.
- Frames: `out/frames.png` at 0.3, 1.6, 2.6, 3.5, 4.9, 6.5, 7.8, 8.9, 11.7, 16.8 s and the cover.
- No burned-in captions: the on-screen steps already carry each line, so the reel works on mute.

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
`out/reel.mp4`, 18.4 s, 1080×1920, 3.4 MB, cover `out/cover.jpg`, manual route, trial reel recommended. Ready for the owner's yes. The voice is AI-generated: generate it on a paid ElevenLabs plan for commercial use.

## Note on the offer
Universities treat submitting work someone else did as misconduct, and some countries have laws against "contract cheating" services. The reel only promises what the page delivers: no grade guarantees, no claims about passing. Defence prep is part of the offer because the student still has to present and defend the project.
