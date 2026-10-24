# content-creator

A Claude Code plugin for running a short-form video page on Instagram, TikTok and YouTube Shorts. It turns a daily session into ideas, hooks, a script, a rendered reel and a caption, and nothing is posted until you approve the exact video and caption.

> **Status: 0.1.0, in progress.** The bundled skills and the video plugins are in place. The workflow skills (`page-setup`, `daily-ideas`, `reel-pipeline`, `weekly-research`, `weekly-review`, `publish`, `render-reel`) are being built next.

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

## Connectors

| Connector | Needed for | Setup |
| --- | --- | --- |
| ElevenLabs | Voiceover, Arabic dubbing, sound effects, music beds | Ships with the plugin. Run `/mcp` once and sign in. Free tier: 10,000 credits a month |
| Composio | Posting to Instagram, TikTok and YouTube | Add your Composio MCP server in Claude Code. Without it you post by hand |
| Apify | Weekly niche research (outlier reels, transcripts) | Add the Apify connector. Without it you paste reel links yourself |
| Descript (optional) | Editing your own on-camera footage | `claude mcp add --transport http descript https://api.descript.com/v2/mcp`, then `/mcp` to sign in. Needs a paid Descript plan |

Posting to Instagram through an API needs a **Business or Creator** account.

## Where things run

- **Claude Code on your machine:** everything, including rendering, downloading reels to study and posting.
- **Chat on claude.ai:** ideas, hooks, scripts and approval. Cloud sessions can't reach Instagram or render video.

Your page's files (brand profile, voice, pillars, idea bank, post log) live in a `creator/` folder in your project, so they carry over between sessions.

## What's inside

- **Our workflow skills** (in progress): the daily loop from idea to approved post, weekly research and review.
- **23 bundled skills** from [social-media-skills](https://github.com/social-media-skills/skills), [Ootto](https://github.com/Ootto-AI/claude-content-skills) and [ootto-watch](https://github.com/Ootto-AI/ootto-watch), all MIT. See [NOTICE.md](NOTICE.md) for credits and what was changed.

## Maintaining

- `scripts/vendor.sh` re-pulls the bundled skills at the commits pinned in it.
- `scripts/pin-companions.py` moves Remotion, HyperFrames and Impeccable to their latest commits in the marketplace.
- `claude plugin validate .` checks the manifests and skills.

## Privacy

The plugin itself collects nothing. The connectors you choose to sign in to (ElevenLabs, Composio, Apify, Descript) receive what you send them under their own privacy policies; see [ElevenLabs' privacy policy](https://elevenlabs.io/privacy-policy).

## Licence

MIT, see [LICENSE](LICENSE). Bundled and dependent projects keep their own licences; see [NOTICE.md](NOTICE.md).
