---
name: publish
description: >-
  Show the final approval card for a finished reel or carousel (file, duration, ratio, size,
  cover, caption per platform, trial or not, time) and post it through Composio only after an
  explicit yes; otherwise hand over everything for a manual post. Logs every post. Use when a
  reel or carousel is ready, or when the user says "post it", "publish" or "schedule this".
argument-hint: "[path to the reel folder in creator/reels/]"
---

# Publish

Nothing goes out without the user's yes on the exact file and words. Instagram posts made through the API can't be deleted through the API, so the card must show everything that will be posted.

## 1. Build the approval card

Read `plan.md` and the rendered files in the reel's folder, and `creator/page.md`. Measure the file yourself; don't copy numbers from `plan.md`:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/render-reel/scripts/check_spec.py <file> --platforms <platforms from page.md>
```

Show one card:

| | |
| --- | --- |
| File | path, per platform if they differ |
| Duration | seconds (Instagram API: 3 s to 15 min; flag over 90 s) |
| Size and ratio | width×height, 9:16 or not; MB (Instagram API: under 300) |
| Cover | path to the cover JPEG (Instagram requires JPEG); show it |
| Platforms | Instagram, TikTok, YouTube, as chosen |
| Caption | the full text per platform, exactly as it will post |
| Trial reel | yes or no (Instagram only: shown to non-followers first) |
| When | now, or the posting hour from `page.md`; confirm the user can reply to comments for 30 to 60 minutes after |
| Route | Composio, or manual, per platform |

Flag anything out of spec in the card itself. Don't post an out-of-spec file.

Then ask: "Post exactly this?" Only a clear yes (yes, post it, go) counts. If anything changes after the card (a word in a caption, a re-render), show a new card and ask again.

## 2. Pick the route per platform

**Composio** if its tools for that platform are available in this session and the account is connected. Otherwise **manual**.

Some cases are always manual:

- The reel needs a trending sound from Instagram's library (the API can't add it).
- It's a story.
- The user would rather post it themselves.

## 3. Post through Composio

Composio's tool names and parameters change, so look them up from the tools available rather than assuming them. Read each tool's input schema before calling it.

**Instagram (reel):**

1. Instagram fetches the video from a **public HTTPS link**. If the Composio tool takes a local file and uploads it, use that. If it needs a URL, ask the user where to host the file (a public bucket or file host they control). If neither works, switch to manual. Never upload the user's video to a host they haven't chosen.
2. Create the media container (reel type, video URL, caption, cover; trial reel settings if chosen and offered by the tool).
3. Poll the container's status until it's finished. Stop and report if it errors or takes over 10 minutes.
4. Publish the container. Get the post's permalink.

**TikTok:** posts from apps that TikTok hasn't audited come out **private**. After the first TikTok post, ask the user to check its visibility. If it's private, note in `page.md` that TikTok is manual from now on.

**YouTube Shorts:** upload with the title and description from `plan.md`, vertical, under 3 minutes. After the first upload, ask the user to check it is public and listed as a Short.

If any step fails, stop and show the error. Don't retry a publish step blindly: a duplicate post can't be removed through the API.

## 4. Manual route

Give the user, per platform:

- the file path to upload, and the cover path;
- the caption in a code block, ready to copy;
- the sound to add in the app, if any;
- what to tap: for Instagram, the trial reel switch if chosen, and the cover.

Ask them to paste the post's link back when it's live.

## 5. Log it

For each platform posted, add a row to `creator/post-log.csv`: `date`, `platform`, `idea_id`, `reel_dir`, `hook`, `format`, `duration_s`, `url`, `trial`. Leave the number columns empty; `weekly-review` fills them.

Then remind the user: reply to comments for the next 30 to 60 minutes, since the first hour decides reach. If the post used a comment keyword, the DM must deliver what was promised.

## Rules

- No post without a yes to the exact card.
- Never post the same file to several platforms with another platform's watermark on it.
- Never store or print the user's tokens or keys.
