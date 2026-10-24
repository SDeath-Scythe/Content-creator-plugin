#!/usr/bin/env bash
# Re-pull the bundled upstream skills at their pinned commits.
#
# Every bundled SKILL.md is copied unchanged, except for a short note inserted
# right after its frontmatter (and, for ootto-watch, the skill name). To update
# a library: change its *_REF below, run this script, review the diff, commit.
#
# Usage: scripts/vendor.sh

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS="$ROOT/skills"
THIRD_PARTY="$ROOT/third_party"

SMS_REPO=https://github.com/social-media-skills/skills
SMS_REF=f28cef2b7067ec64e79c9d85421c022c06659e03
SMS_VERSION=1.0.1
SMS_SKILLS=(
  brand-profile voice-builder audience-research content-pillars profile-optimization
  idea-generation-and-ideation trend-jacking viral-reverse-engineering
  hook-writer reels-script short-form-video-script carousel-writer
  caption-writer instagram-seo instagram-growth analytics-and-reporting
  content-recycling platform-specs-and-validation cross-platform-repurposing
)

OOTTO_REPO=https://github.com/Ootto-AI/claude-content-skills
OOTTO_REF=c79c330a27c9b191d9b78839beebf43ae10a500d
OOTTO_SKILLS=(virality going-viral hook-mining)

WATCH_REPO=https://github.com/Ootto-AI/ootto-watch
WATCH_REF=275e3a7d133b42a573a7f6ea9814f95456cc9ca4

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

fetch() { # fetch <repo> <ref> <dir>
  git init -q "$3"
  git -C "$3" fetch -q --depth 1 "$1" "$2"
  git -C "$3" checkout -q FETCH_HEAD
}

# Insert the note (from stdin) after the closing '---' of the frontmatter.
add_note() { # add_note <SKILL.md>
  local note
  note="$(cat)"
  NOTE="$note" awk '
    { print }
    /^---$/ && ++n == 2 { print ""; print ENVIRON["NOTE"] }
  ' "$1" > "$1.tmp"
  mv "$1.tmp" "$1"
}

copy_skill() { # copy_skill <src dir> <dest name>
  rm -rf "$SKILLS/$2"
  mkdir -p "$SKILLS/$2"
  (cd "$1" && tar --exclude=./evals --exclude=./.git -cf - .) | (cd "$SKILLS/$2" && tar -xf -)
}

fetch "$SMS_REPO" "$SMS_REF" "$TMP/sms"
fetch "$OOTTO_REPO" "$OOTTO_REF" "$TMP/ootto"
fetch "$WATCH_REPO" "$WATCH_REF" "$TMP/watch"

for s in "${SMS_SKILLS[@]}"; do
  copy_skill "$TMP/sms/skills/$s" "$s"
  add_note "$SKILLS/$s/SKILL.md" <<EOF
> **Bundled in content-creator** from [social-media-skills](${SMS_REPO}) v${SMS_VERSION} (MIT, Frank Heijdenrijk). The text below this note is unchanged. In this plugin:
> - **Publishing** goes through the \`publish\` skill (Composio, or a manual post), not WoopSocial. Read every WoopSocial mention as that step.
> - **Files** such as \`brand-profile.md\`, \`voice.md\`, \`audience.md\` and \`content-pillars.md\` live in the \`creator/\` folder of the user's project.
> - **Other skills** named below that this plugin doesn't bundle are optional: use them if installed, otherwise skip that step. Links to \`tools/integrations/\` point at the upstream repo.
EOF
done

for s in "${OOTTO_SKILLS[@]}"; do
  copy_skill "$TMP/ootto/skills/$s" "$s"
  add_note "$SKILLS/$s/SKILL.md" <<EOF
> **Bundled in content-creator** from [Ootto claude-content-skills](${OOTTO_REPO}) (MIT, Ootto). The text below this note is unchanged. Its examples come from one English account in the AI niche: keep the rules, but prefer the user's own winners in \`creator/hook-wins.csv\` as examples. Ootto skills named below that this plugin doesn't bundle are optional.
EOF
done

copy_skill "$TMP/watch" watch-reel
rm -f "$SKILLS/watch-reel/LICENSE" "$SKILLS/watch-reel/README.md"
sed -i '0,/^name: watch-video$/s//name: watch-reel/' "$SKILLS/watch-reel/SKILL.md"
add_note "$SKILLS/watch-reel/SKILL.md" <<EOF
> **Bundled in content-creator** from [ootto-watch](${WATCH_REPO}) (MIT, Ootto-AI), renamed from \`watch-video\`; otherwise unchanged. Needs \`yt-dlp\` and \`ffmpeg\` on the user's machine. Instagram may block downloads without a login: if it does, ask the user to attach the reel file instead.
EOF

mkdir -p "$THIRD_PARTY"/{social-media-skills,ootto-claude-content-skills,ootto-watch}
cp "$TMP/sms/LICENSE" "$THIRD_PARTY/social-media-skills/LICENSE"
cp "$TMP/ootto/LICENSE" "$THIRD_PARTY/ootto-claude-content-skills/LICENSE"
cp "$TMP/watch/LICENSE" "$THIRD_PARTY/ootto-watch/LICENSE"

echo "Vendored ${#SMS_SKILLS[@]} social-media-skills, ${#OOTTO_SKILLS[@]} Ootto skills and watch-reel."
