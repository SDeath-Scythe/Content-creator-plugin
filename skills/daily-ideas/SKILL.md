---
name: daily-ideas
description: >-
  Open a content session with 5 to 7 scored ideas for today, drawn from the idea bank, this
  week's research and anything breaking in the niche, each tied to a pillar, a goal and a format.
  Use at the start of every session, or when the user says "what should I post", "ideas for
  today", "daily ideas" or "open the session".
---

# Daily ideas

The session's opener. It costs nothing to run: ideas come from the bank, the page files and the skills, never from a paid research call.

## 1. Load the page

Read `creator/page.md`, `creator/content-pillars.md`, `creator/idea-bank.csv` and the last 14 days of `creator/post-log.csv`. Read the newest file in `creator/research/` if it is less than 8 days old.

If `creator/page.md` is missing or its Goal is empty, stop and run `page-setup` first.

## 2. Work out what today needs

From the post log and `page.md`:

- **What's due:** how many reels and carousels are left this week against the cadence in `page.md`. If the week is on track, say so: fewer, better posts beat filler.
- **Pillar balance:** which pillars haven't had a post in the last 7 days. Lean today's list toward them.
- **Format balance:** if the last 3 posts were reels, offer at least one carousel idea (`carousel-writer`), since carousels earn saves and shares.
- **Build day:** if today is the build day in `page.md`, favour ideas already marked `picked` so the batch gets made.

## 3. Gather candidates

Pull from three places, in this order:

1. **The bank:** the highest-scored `new` ideas, plus any `picked` idea not yet made.
2. **This week's research:** outlier mechanisms from the research file not yet turned into ideas.
3. **What's breaking:** if the user mentions a trend, or the research file flags one, run `trend-jacking` and keep it only if it fits a pillar and the goal. Don't go looking for trends unprompted.

If the bank has fewer than 10 `new` ideas, run `idea-generation-and-ideation` to expand real signals (comments, questions, research outliers, the user's own experience) into angled ideas, then score them and add them to the bank. Never pad the bank with generic ideas that any page in the niche could post.

## 4. Score

Score each candidate 1 to 5 on four things and add them up (max 20):

| Criterion | 5 means |
| --- | --- |
| Pillar fit | Squarely in a pillar, and in one that's due |
| Audience evidence | Real people asked for it, or it beat a creator's median in research |
| Goal | Moves a viewer toward the goal in `page.md` |
| Effort | Can be built and posted today with the tools in `page.md` |

On a new page with no research yet, nothing has audience evidence: score it 1 or 2, write "hypothesis" in `evidence`, and suggest running `weekly-research` first so tomorrow's list stands on real signals.

## 5. Show the list

Show 5 to 7 ideas as one table, highest score first:

| # | Idea (one line) | Pillar | Format | Goal it serves | Why now | Score |
| --- | --- | --- | --- | --- | --- | --- |

Under the table, one line naming your recommendation and why. Then ask which one to make.

## 6. Update the bank and hand off

- Add new ideas to `creator/idea-bank.csv`: `id` as `YYYYMMDD-n`, `source` (bank, research file name, trend, comments, own), `evidence` (a link or a short fact), `score`, `status` = `new`.
- Mark the chosen idea `picked`. Mark ideas the user rejects outright `dropped`, with the reason in `notes`.
- Hand off: a reel goes to `reel-pipeline` with the idea's id; a carousel goes to `carousel-writer`, then `caption-writer` and `publish`.

## Rules

- Every idea names its pillar and the goal it serves. An idea that serves neither doesn't make the list.
- Model the mechanism of other people's winners, never their content. Instagram stops recommending accounts whose posts are mostly not their own.
- Don't claim an idea "will go viral". Say what evidence it has.
