# Reel: stop writing your report in this order

Status: built and checked; not posted. Needs the owner's voiceover before approval. This is the page's secondary topic (the report); the project-plan reel is the lead.

## 1. Goal
**Leads**, through **saves**. The emotion: relief. "I don't have to start with the introduction."
Serves the page goal: comment REPORT for the chapter-by-chapter template.

## 2. Hooks (each checked against the virality 8-point list)

| # | Hook | Frames 0 to 3 s | Pattern | Check |
| --- | --- | --- | --- | --- |
| A | **Stop writing your report in this order.** | 0 s: the report's table of contents slams in. 0.35 to 1.6 s: chapter numbers tick red 1 to 6. 1.0 to 1.6 s: claim lands. 2.3 s: "WRONG ORDER" stamp, rows break apart | contrarian | 8/8 (point 6 once the voice starts on "Stop") |
| B | Your graduation report is 80 pages. Here's the shortcut. | 0 s: page counter races 0 → 80 and locks | number-race | 7/8: "shortcut" over-promises (banned-adjacent). Dropped |
| C | Never start with Chapter 1. | 0 s: a blank page titled "Chapter 1: Introduction" with a blinking cursor | warning | 7/8: a blank page is a weak frame 0 (point 3: little moves) |

**Picked A.**

## 3. Script (15 s)

| Time | Spoken (voiceover to record) | On screen | Visual |
| --- | --- | --- | --- |
| 0 to 3 | "Stop writing your graduation report in this order." | Stop writing your report in this order. | Contents: Introduction, Literature Review, Methodology, Implementation, Results & Testing, Conclusion. WRONG ORDER stamp |
| 3 to 5.5 | "Write what you built first: methodology and implementation." | 1. Write what you built | Methodology and Implementation jump to the top, tagged 1st |
| 5.5 to 8 | "Then your results, while they're fresh." | 2. Then your results | Results & Testing moves to 3rd place, tagged 2nd |
| 8 to 10.5 | "Now the literature review. You finally know what to search for." | 3. Now the literature review | Literature Review settles, tagged 3rd |
| 10.5 to 12.5 | "Introduction goes last." | 4. Introduction goes last | Conclusion up, Introduction to the bottom, tagged LAST |
| 12.5 to 15 | "Comment REPORT for the template." | Comment REPORT | RIGHT ORDER stamp |

## 4. Production plan

Faceless, built in code (render-reel, built-in engine). The owner records the voice; captions are timed to it. No music, or a licensed bed. Cover: hook over the contents page with the stamp.

## 5. Build

- `build/reel.src.html` + `build/gen.py` → `build/reel.html`; rendered with `render.mjs` (47 s).
- Spec check (`out/spec.json`): **ok**. 15.0 s, 1080×1920, 30 fps, H.264 + AAC (silent), 3.2 MB.
- Frames in `out/frames.png`. Still to do: voice and captions.

## 6. Captions

**Instagram**
```
Stop writing your graduation report in this order 👇

Write it in the order you know it:
1. Methodology + implementation: what you built
2. Results: tests, screenshots, numbers
3. Literature review: now you know what to search for
4. Introduction + abstract: last

Comment REPORT and I'll send you the chapter-by-chapter template.

#graduationproject #finalyearproject #thesiswriting #universitytips #studytips
```

**YouTube Shorts title:** `Stop writing your graduation report in this order`

## 7. Approval card

Same as the project-plan reel: `out/reel.mp4`, 15.0 s, 1080×1920, 3.2 MB, cover `out/cover.jpg`, manual route. **Not ready to post** until the voice is in.
