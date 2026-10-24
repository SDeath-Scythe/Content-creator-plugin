# content-creator

A Claude Code plugin for running a short-form video page on Instagram, TikTok and YouTube Shorts. It turns a daily session into ideas, hooks, a script, a rendered reel and a caption, and nothing is posted until you approve the exact video and caption.

## Install

In Claude Code:

```text
/plugin marketplace add SDeath-Scythe/content-creator-plugin
/plugin install content-creator@content-creator
```

Installing also pulls in three video and design plugins as dependencies:

| Plugin | What it does here |
| --- | --- |
| [HyperFrames](https://github.com/heygen-com/hyperframes) (HeyGen) | Default video engine: reels written as HTML and rendered to MP4, which keeps Arabic and right-to-left text reliable |
| [Remotion](https://github.com/remotion-dev/claude-code-plugin) | Second engine for data-driven reels and word-by-word captions |
| [Impeccable](https://github.com/pbakaus/impeccable) | Design pass on reel frames, covers and carousels before rendering |

Remotion is free for individuals and companies of up to 3 people. Larger companies need a [Remotion company licence](https://www.remotion.dev/license).

On your machine you also need **Node.js 22+** and **ffmpeg** for rendering, and **yt-dlp** for studying other reels. Without Node 22 the plugin falls back to its own renderer (Node 18+ with the `playwright` package).

## How you use it

| When | Run | What happens |
| --- | --- | --- |
| Once | `page-setup` | Interview, goal first. Writes your page files into `creator/`, fixes your bio and pinned reels, checks your tools |
| Weekly | `weekly-research` | Finds reels beating their creator's normal in your niche (Apify, about $0.65 a week), tears down the top 4, refills the idea bank |
| Every session | `daily-ideas` | 5 to 7 scored ideas for today, tied to your pillars and goal |
| Per reel | `reel-pipeline` | Goal → 3 hooks checked against the 8-point first-3-seconds rule → script → production plan → `render-reel` → captions per platform → `publish` |
| Weekly | `weekly-review` | Reads your Insights, finds what worked, moves your winning hooks into the rules for next week |

Each step stops for your yes before moving on. `publish` shows a final card with the exact file, cover, captions and platforms, and posts only after you approve it. Instagram posts made through the API can't be deleted through the API.

Your page's files live in a `creator/` folder in your project, so they carry over between sessions: page settings, brand profile, voice, pillars, idea bank, post log, your winning hooks, research notes and one folder per reel.

## Connectors

| Connector | Needed for | Setup |
| --- | --- | --- |
| ElevenLabs | Voiceover, Arabic dubbing, sound effects, music beds | Ships with the plugin. Run `/mcp` once and sign in. Free tier: 10,000 credits a month |
| Composio | Posting to Instagram, TikTok and YouTube | Add your Composio MCP server in Claude Code. Without it you post by hand |
| Apify | Weekly niche research | Add the Apify connector. Without it you paste reel links yourself |
| Descript (optional) | Editing your own on-camera footage | `claude mcp add --transport http descript https://api.descript.com/v2/mcp`, then `/mcp` to sign in. Needs a paid Descript plan |

Posting to Instagram through an API needs a **Business or Creator** account. TikTok makes posts from unaudited apps private, so check your first TikTok post's visibility.

## Where things run

- **Claude Code on your machine:** everything, including rendering, downloading reels to study and posting.
- **Chat on claude.ai:** ideas, hooks, scripts and approval. Cloud sessions can't reach Instagram, and may not render video.

## What's inside

**Our skills:** page-setup, daily-ideas, reel-pipeline, render-reel, publish, weekly-research, weekly-review.

**Bundled skills (23):** 19 from [social-media-skills](https://github.com/social-media-skills/skills), virality, going-viral and hook-mining from [Ootto](https://github.com/Ootto-AI/claude-content-skills), and [ootto-watch](https://github.com/Ootto-AI/ootto-watch) as watch-reel. All MIT; see [NOTICE.md](NOTICE.md) for credits and what was changed.

**Arabic:** IBM Plex Sans Arabic and Noto Kufi Arabic (OFL) ship in `assets/fonts/`, and the reel templates are right-to-left by default.

## Maintaining

- `scripts/vendor.sh` re-pulls the bundled skills at the commits pinned in it.
- `scripts/pin-companions.py` moves Remotion, HyperFrames and Impeccable to their latest commits in the marketplace.
- `claude plugin validate .` checks the manifests and skills.

## Privacy

The plugin itself collects nothing. The connectors you choose to sign in to (ElevenLabs, Composio, Apify, Descript) receive what you send them under their own privacy policies; see [ElevenLabs' privacy policy](https://elevenlabs.io/privacy-policy).

## Licence

MIT, see [LICENSE](LICENSE). Bundled projects, fonts and dependencies keep their own licences; see [NOTICE.md](NOTICE.md).
