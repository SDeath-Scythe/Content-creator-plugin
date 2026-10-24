---
name: reel-pipeline
description: >-
  Take one chosen idea all the way to an approved reel: goal, 3 hooks checked against the 8-point
  first-3-seconds rule, script with a visual for every line, production plan, build, captions per
  platform, then the approval card. Use after daily-ideas, or when the user says "make this reel",
  "script this", "build the reel" or gives an idea to turn into a video.
argument-hint: "[idea id from the bank, or the idea in a sentence]"
---

# Reel pipeline

One idea in, one approved reel out. Each stage ends at a gate: show the result, get a yes or a change, then move on. Never skip a gate to save time; a weak hook found at stage 2 is cheap, found after rendering it is not.

Keep everything for this reel in `creator/reels/YYYY-MM-DD-<slug>/`, with the decisions in `plan.md` there. Create it at stage 1. If a `plan.md` already exists for this idea, resume from the first stage not marked done.

Before starting, read `creator/page.md`, `creator/brand-profile.md`, `creator/voice.md` and `creator/hook-wins.csv`. If the idea came from the bank, load its row. If the page is in Arabic, follow [references/arabic.md](references/arabic.md) at every stage.

## Stage 1 — Goal

Use `going-viral` step 1: pick ONE goal for this reel (saves, shares, follows or leads) and the emotion that drives it. It must serve the page goal in `page.md`. Write both at the top of `plan.md`.

**Gate:** the user confirms the goal.

## Stage 2 — Hooks

1. Run `hook-writer` to draft hooks from the idea's strongest element, in the voice from `voice.md`.
2. Take the best **three** and run each through the `virality` checklist: describe frame 0 and every half second up to 3 seconds, and mark all eight points. In this plugin, read point 2 as "something this audience recognises instantly" and point 8 as "about the viewer's own situation", whatever the niche. A faceless page has no logo to show: point 2 is met by the audience's problem made concrete on screen (an invoice, a client's message, a price tag, the app they use), never by abstract shapes.
3. Rewrite any hook that fails a point until it passes all eight. If `creator/hook-wins.csv` has 5 or more rows, also offer one hook that keeps the structure of a past winner with new words (`hook-mining`'s rule: psychology fixed, words swapped).
4. Show the three as a table: hook text, frames 0 to 3 s, the pattern it uses, checklist result.

**Gate:** the user picks one. If they plan to test it, note "trial reel" in `plan.md`; the publish skill can post it to non-followers first.

## Stage 3 — Script

Run `reels-script` (Instagram) for the full script. For a page that posts mostly to TikTok or Shorts, `short-form-video-script` instead. The script must have:

- every spoken line next to what is on screen at that moment (`virality` rule 3: shown, never just said);
- a target length, between 5 and 90 seconds, that fits the idea rather than filling time;
- the CTA from `page.md`, serving this reel's goal. A comment keyword only if the DM delivers something real;
- a reason to comment (`virality` rule 4) that isn't bait.

Write the script into `plan.md` as a table: time, spoken line, on-screen text, visual.

**Gate:** the user approves the script, or edits lines.

## Stage 4 — Production plan

Decide how the reel gets made, and write it into `plan.md`:

| Choice | Options |
| --- | --- |
| Picture | **Faceless, built in code** (render-reel) · **on camera** (the user films; give a shot list with framing and the first frame described exactly) · **mixed** (on-camera footage under code-built text and graphics) |
| Voice | The user records it (preferred: real voice) · ElevenLabs voiceover, only if the user asks and `page.md` lists it · no voice, text-led |
| Sound | **Posted through the API:** no Instagram music library, so either a licensed bed (ElevenLabs music, or a library the user has rights to) or no music. **Needs a trending sound:** export without music; the user adds the sound in the app and posts by hand. Never use a track without a licence. Every file gets an audio track; render-reel adds a silent one when there's no sound |
| On-camera edit | If the user films, they can clean it in Descript (filler words, Studio Sound, captions) when the Descript connector is set up, and export the file |
| Cover | A designed cover (JPEG): the hook in a few words, readable at grid size. Never a random frame |

Ask for anything the user must supply (recordings, footage, screenshots as proof) and where they will put it, usually `creator/reels/<this reel>/assets/`.

**Gate:** the user confirms the plan and has supplied the assets, or chooses fully code-built.

## Stage 5 — Build

Run `render-reel` with this reel's folder. It builds 1080×1920 at 30 fps, keeps text inside the safe area away from Instagram's buttons and caption, makes the cover, renders, and runs the spec check.

render-reel's spec check covers the hard limits (Instagram API: 3 s to 15 min, under 300 MB, H.264 + AAC, 23 to 60 fps). Then use `platform-specs-and-validation` for anything platform-specific it doesn't cover. Over 90 s is allowed but gets flagged: most short-form winners are shorter.

Look at the rendered frames at 0, 0.5, 1, 1.5, 2, 3 seconds and at the end. Check them against the hook's frame plan from stage 2. If frame 0 isn't already moving, or the claim lands after 3 s, fix and re-render before showing the user.

**Gate:** the user watches the file and approves it, or gives changes.

## Stage 6 — Captions per platform

For each platform in `page.md`:

- **Instagram:** `caption-writer` in the page voice, then `instagram-seo` for keywords in the first line and 3 to 5 relevant hashtags. Optional first comment.
- **TikTok:** its own caption with search keywords; no Instagram hashtag block.
- **YouTube Shorts:** a title under 100 characters written for search, and a short description.

Use `cross-platform-repurposing` so each platform gets its own clean file and words, never the same file with another platform's watermark.

Write all captions into `plan.md`.

## Stage 7 — Approval, then publish

Hand off to `publish` with this reel's folder. It shows the final approval card and posts only on an explicit yes.

After posting, set the idea's `status` to `posted` in `creator/idea-bank.csv` (or `made` if it was rendered but held back).

## Rules

- Hooks, scripts and captions follow `voice.md` and never use anything in Banned claims.
- No fabricated numbers, testimonials or results on screen or in captions. Proof shown must be real and supplied by the user.
- No AI avatar or AI-generated person presented as real. If the user insists, the post carries Instagram's AI label.
- Model other creators' mechanisms, never their footage, audio or script.
