---
name: render-reel
description: >-
  Build and render a reel from its plan in creator/reels/<reel>/: picks HyperFrames, Remotion or
  the built-in Playwright + ffmpeg renderer, applies the brand look, safe areas and Arabic or
  English type, adds voice, music and captions, runs a design pass, renders 1080x1920 MP4 plus a
  JPEG cover, and checks platform specs. Use from reel-pipeline stage 5, or when the user says
  "render", "build the video" or "make the cover".
argument-hint: "[path to the reel folder]"
---

# Render reel

Turn an approved script into a finished file. Read the reel's `plan.md` (hook frame plan, script table, production plan), `creator/page.md` (look, language, platforms) and the files in the reel's `assets/`. Everything this skill writes goes into the reel's folder; final files go into its `out/`.

## 1. Pick the engine

| Engine | Use when | Needs |
| --- | --- | --- |
| **HyperFrames** (default) | Most reels: text-led, motion graphics, screen recordings, the user's footage with overlays. HTML, so Arabic and right-to-left text render as in a browser | Node.js 22+, ffmpeg; the HyperFrames skills (installed with this plugin) |
| **Remotion** | Data-driven reels (charts, counters from a table), or the user asks for it | Node.js, ffmpeg; the Remotion skills. Free for individuals and companies of up to 3 people; bigger companies need a Remotion company licence |
| **Built-in** | Neither works (no Node 22, no npm, a cloud session), or a quick draft | Node.js 18+, ffmpeg, the `playwright` package with Chromium |

Check what's there (`node --version`, `ffmpeg -version`) before choosing. Say which engine you're using and why in one line. If the first choice fails to install or run, fall to the next one rather than stopping.

## 2. The spec every engine follows

- **Canvas:** 1080×1920, 30 fps, H.264 `yuv420p`, AAC 48 kHz, moov atom first (`-movflags +faststart`).
- **Length:** what the script needs. Over 90 s gets flagged on the approval card.
- **Safe area:** keep all text and key visuals inside x 60 to 930, y 250 to 1500. Instagram's top bar, caption block and buttons cover the rest (the buttons are on the right in every language). For a TikTok-first reel, keep text above y 1440 and left of x 910.
- **Frame 0 moves**, and shows the thing the hook's frame plan says, readable at once. The claim lands around 1.2 to 1.6 s. Read the hook plan in `plan.md` and match it.
- **Type:** big. Hook 120 px or more, body 70 px or more, captions 54 px or more. High contrast (WCAG AA at least) against everything moving behind it.
- **Look:** colours and fonts from `page.md`. For Arabic, use the fonts in `${CLAUDE_PLUGIN_ROOT}/assets/fonts/` (Noto Kufi Arabic for display, IBM Plex Sans Arabic for text; both also cover Latin) and follow [the Arabic rules](../reel-pipeline/references/arabic.md).
- **Cover:** a 1080×1920 **JPEG** (Instagram requires JPEG, under 8 MB). The hook in 3 to 6 words, big, inside the safe area and inside the 3:4 grid crop (y 240 to 1680), so it reads on the profile grid.
- **No borrowed media:** no clips, audio or footage from other creators, and no watermarks.

## 3. Sound and captions

- **Voice:** the user's recording in `assets/` (ask for it if missing). ElevenLabs only if `plan.md` says so: generate with the ElevenLabs tools, save to `assets/voice.mp3`, and tell the user it's AI voice. Trim leading silence so the first word lands within 0.5 s.
- **Music:** only a bed the user has rights to, or ElevenLabs music (commercial use needs a paid ElevenLabs plan). Under the voice and ducked while it speaks. If `plan.md` says "trending sound, add in app", render with no music.
- **Captions:** time them to the voice, not to the script. Get word or line timings from a transcript: HyperFrames' `transcribe`, ElevenLabs speech to text, or local `faster-whisper`. If none works, time them by ear from the waveform and say so. Captions go in the safe area, never over the hook's claim.

## 4. Build

**HyperFrames:** use the `hyperframes` skill to build the composition in `<reel>/hyperframes/`. Give it the spec above, the script table, the look, the fonts path and the audio files. Follow its own loop: lint, `check --json` until clean, `snapshot` and look at the frames. Render with `--quality delivery` to `out/reel.mp4`. Make the cover as a still of a cover composition, saved as JPEG.

**Remotion:** use the `remotion-best-practices` skill and the others it routes to (create, captions, render). Same spec. Render to `out/reel.mp4`; export the cover still as JPEG.

**Built-in:**

1. Copy `${CLAUDE_SKILL_DIR}/template/` into `<reel>/build/` (`reel.html` for Arabic, `reel-en.html` for English, plus `reel.css` and `reel.js`), and copy `${CLAUDE_PLUGIN_ROOT}/assets/fonts/` to `<reel>/build/fonts/`.
2. Set the look in `reel.css`'s `:root`, the duration in the `reel-duration` meta tag, and write one `.scene` per beat of the script with `data-start` and `data-end`. Use the motion presets (`slam` for the frame-0 element, `words` for a claim landing word by word, `rise`, `pop`). Put the caption timings in `#captions-data`.
3. Check stills before rendering (fast):
   `node ${CLAUDE_SKILL_DIR}/scripts/render.mjs <reel>/build/reel.html <reel>/build/stills --stills 0,0.5,1,1.5,2,3`
   Open `reel.html?guides=1&t=1.5` in a browser to see the safe area shaded, if the user wants to look.
4. Render:
   `node ${CLAUDE_SKILL_DIR}/scripts/render.mjs <reel>/build/reel.html <reel>/out/reel.mp4 --voice <voice> --music <bed> --cover <reel>/out/cover.jpg`
   Add `--draft` for a fast low-quality pass while iterating. About 4 seconds of render time per second of video.

## 5. Design pass

Before the final render, run the `impeccable` skill's critique on the composition source (the HTML/CSS, or the Remotion components) and its rendered stills, with this context: a 9:16 short-form video watched on a phone, often on mute, judged in the first 3 seconds. Apply its findings on hierarchy, type, colour and contrast. Ignore anything that only makes sense for a web page (navigation, hover states, responsive layouts).

## 6. Check

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/check_spec.py <reel>/out/reel.mp4 --platforms instagram,tiktok,youtube --frames <reel>/out/frames
```

Use the platforms from `page.md`. It fails on hard limits (codec, frame rate, length, size, moov atom) and writes frames at 0, 0.5, 1, 1.5, 2, 3 s and the end. Look at those frames against the hook plan: frame 0 moving and readable, claim by 1.6 s, nothing outside the safe area, captions in sync. Fix and re-render until the check passes and the frames match.

If a platform needs different framing (TikTok-first safe area) or a different end card, render a separate file per platform: `out/instagram.mp4`, `out/tiktok.mp4`. Otherwise one `out/reel.mp4` serves all.

## 7. Record

Add a "Build" section to `plan.md`: engine, output files, the spec check result (paste its `ok`, `fails`, `warnings`), and anything the user still has to do (add a sound in the app, record a better take). Then hand back to `reel-pipeline` stage 5's gate: the user watches the file.
