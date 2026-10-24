# Reel: your graduation project plan is backwards

Status: built and checked; not posted. Needs the owner's voiceover before approval.

## 1. Goal
**Leads**, through **saves**. The emotion: relief. "I've been planning it the hard way, and there's a simpler order."
Serves the page goal: comment PROJECT for the week-by-week plan.

## 2. Hooks (each checked against the virality 8-point list)

| # | Hook | Frames 0 to 3 s | Pattern | Check |
| --- | --- | --- | --- | --- |
| A | **Your graduation project plan is backwards.** | 0 s: a student's semester plan slams in, already moving. 0.35 to 1.5 s: the week pills tick red one by one. 1.0 to 1.6 s: claim lands word by word. 2.3 s: "WRONG ORDER" stamp slams down and the rows break apart | contrarian | 8/8 (point 6 once the voice starts on "Your") |
| B | 90% of graduation projects fail in week 1. | 0 s: a calendar on week 1; the number races 0 → 90% and locks | number-race | 6/8: the 90% isn't a real statistic (banned). Dropped |
| C | Don't learn React for your graduation project. | 0 s: a React logo cracks | contrarian | 7/8: point 8 fails for non-web projects. Too narrow |

**Picked A.** Frame 0 is something every final-year student recognises (their own plan), it's about the viewer's situation, and the stamp is the "extraordinary event" before 3 s. Candidate for a trial reel.

## 3. Script (15 s)

| Time | Spoken (voiceover to record) | On screen | Visual |
| --- | --- | --- | --- |
| 0 to 3 | "Your graduation project plan is backwards." | Your graduation project plan is backwards. | Plan: learn every technology (W1–4), design all screens (W5–7), build everything (W8–12), test (W13), write the 80-page report (W14–15, in red). WRONG ORDER stamp |
| 3 to 6 | "Build a tiny version first: one feature, working end to end." | 1. Build a tiny version first | "Build everything" jumps to the top and becomes "Build a tiny version" (W1–3), tagged 1st |
| 6 to 9 | "Learn only what that next feature needs." | 2. Learn only what you need next | "Learn every technology" becomes "Learn as you go", tagged 2nd |
| 9 to 12 | "And write the report as you build. Every feature you finish is a section done." | 3. Write the report as you build | The red report row leaves week 14 and moves up as "Write the report", weekly, tagged 3rd |
| 12 to 15 | "Comment PROJECT and I'll send you the week-by-week plan." | Comment PROJECT | RIGHT ORDER stamp |

CTA: comment PROJECT; the DM sends the week-by-week plan and the report template.

## 4. Production plan

| Choice | Decision |
| --- | --- |
| Picture | Faceless, built in code (render-reel, built-in engine) |
| Voice | Owner records the script above; captions re-timed to it |
| Sound | Posted through the API: no music, or a licensed bed under the voice |
| Cover | Hook over the plan, with the WRONG ORDER stamp |

## 5. Build

- Engine: built-in (Playwright + ffmpeg). `build/reel.src.html` + `build/gen.py` → `build/reel.html` (gen.py computes the rows' moves).
- Render: `node skills/render-reel/scripts/render.mjs build/reel.html out/reel.mp4 --cover out/cover.jpg` (47 s).
- Spec check (`out/spec.json`): **ok**. 15.0 s, 1080×1920, 30 fps, H.264 + AAC (silent), 3.0 MB, moov first. No fails, no warnings.
- Frames (`out/frames.png`, at 0, 0.8, 1.6, 2.5, 4, 7, 10, 13.5 s and the cover): frame 0 moving and readable, claim complete by 1.6 s, stamp at 2.5 s, everything inside the safe area.
- Still to do: record the voice, add captions timed to it.

## 6. Captions

**Instagram**
```
Your graduation project plan is backwards 👇

Most final-year plans go: learn every technology → design everything → build everything → test → write the report in the last two weeks.

Flip it:
1. Build a tiny version first: one feature, working end to end
2. Learn only what the next feature needs
3. Write the report as you build: every finished feature is a section

Comment PROJECT and I'll send you the week-by-week plan + report template.

#graduationproject #finalyearproject #computerscience #engineeringstudent #studytips
```

**TikTok:** `Graduation project plan, done right: build small first, learn as you go, write the report weekly. Comment PROJECT for the plan. #graduationproject #finalyearproject #studentlife`

**YouTube Shorts title:** `Your graduation project plan is backwards (do this instead)`

## 7. Approval card

| | |
| --- | --- |
| File | `out/reel.mp4` |
| Duration | 15.0 s |
| Size and ratio | 1080×1920, 9:16, 3.0 MB |
| Cover | `out/cover.jpg` (JPEG) |
| Platforms | Instagram, TikTok, YouTube Shorts |
| Caption | as in section 6 |
| Trial reel | Yes: test hook A on non-followers first |
| When | An evening slot when the owner can reply for 30 to 60 minutes |
| Route | Manual (no Composio in this example) |

**Not ready to post:** no voice yet. Record it, re-time the captions, re-render, then approve.
