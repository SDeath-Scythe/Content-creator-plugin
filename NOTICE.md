# Notices

content-creator is MIT-licensed (see [LICENSE](LICENSE)). It bundles skills from three other MIT-licensed projects and depends on three plugins that install separately.

## Bundled

These files are copied into `skills/` by [`scripts/vendor.sh`](scripts/vendor.sh) at the commits pinned there. Each bundled `SKILL.md` gets a short note after its frontmatter; the rest of its text is unchanged. Each project's licence is kept in [`third_party/`](third_party).

| Project | Skills | Licence | Changes |
| --- | --- | --- | --- |
| [social-media-skills](https://github.com/social-media-skills/skills) v1.0.1, © 2026 Frank Heijdenrijk | brand-profile, voice-builder, audience-research, content-pillars, profile-optimization, idea-generation-and-ideation, trend-jacking, viral-reverse-engineering, hook-writer, reels-script, short-form-video-script, carousel-writer, caption-writer, instagram-seo, instagram-growth, analytics-and-reporting, content-recycling, platform-specs-and-validation, cross-platform-repurposing | [MIT](third_party/social-media-skills/LICENSE) | Note added; `evals/` left out |
| [claude-content-skills](https://github.com/Ootto-AI/claude-content-skills), © 2026 Ootto | virality, going-viral, hook-mining | [MIT](third_party/ootto-claude-content-skills/LICENSE) | Note added |
| [ootto-watch](https://github.com/Ootto-AI/ootto-watch), © 2026 Ootto-AI | watch-reel | [MIT](third_party/ootto-watch/LICENSE) | Renamed from `watch-video`; note added |

## Dependencies (installed separately, not bundled)

Listed in this repo's marketplace at pinned commits ([`scripts/pin-companions.py`](scripts/pin-companions.py) updates them). Their code stays in their own repositories under their own licences.

| Plugin | Licence |
| --- | --- |
| [Remotion Claude Code plugin](https://github.com/remotion-dev/claude-code-plugin) | MIT. Remotion itself is free for individuals and companies of up to 3 people; larger companies need a [Remotion company licence](https://www.remotion.dev/license). |
| [HyperFrames](https://github.com/heygen-com/hyperframes) by HeyGen | Apache-2.0 |
| [Impeccable](https://github.com/pbakaus/impeccable) by Paul Bakaus | Apache-2.0 |
