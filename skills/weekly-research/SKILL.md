---
name: weekly-research
description: >-
  Weekly niche research that refills the idea bank: keyword reel searches and competitor pulls
  through Apify (about $0.65 a week, on the free tier), outliers scored against each creator's
  median, transcripts and teardowns of the top few, saved to creator/research/. Works from
  pasted links without Apify. Use once a week, or when the user says "research", "what's working
  in my niche", "find outliers" or "study this competitor".
---

# Weekly research

Once a week, find what is beating its creator's normal in the niche, understand why, and turn the mechanisms into ideas for the bank. Daily sessions then cost nothing.

Read `creator/page.md`, `creator/content-pillars.md` and the last research file in `creator/research/`. Keep a list of keywords and competitor handles at the bottom of `page.md` under "Research"; ask for them the first time (3 to 6 keywords in the language the audience searches in, 3 to 5 competitors of similar or slightly bigger size).

## 1. Plan and confirm the cost

Pick this week's 2 keywords (rotate through the list, favour pillars that are due) and 2 to 4 competitors. Show the plan with the cost estimate from [references/apify.md](references/apify.md). Run only after the user agrees. Skip this confirmation in later weeks if the user said to.

## 2. Collect

**With Apify** (its tools are available in this session):

1. Run the keyword search for each keyword.
2. Rank all results by `play_count`. Take the creators of the top 10 reels plus this week's competitors; pull the last 30 reels of up to 4 of them to get each creator's median views.
3. Score every reel from those creators with the outlier formula in the reference file. Keep reels at 3× or more, newest first, up to 8.
4. Get transcripts for the top 4.

**Without Apify:** ask the user to paste 4 to 8 reel links they noticed doing well, with the views and the creator's usual views if they know them. In Claude Code, `watch-reel` can download, sample frames and transcribe each one for free.

Never browse Instagram with the user's own logged-in account to scrape: it breaks Instagram's terms and can get the page flagged. If the user wants to browse, they use a second account.

## 3. Tear down the top 4

For each top outlier, run `viral-reverse-engineering`, using the transcript and, where available, frames from `watch-reel`:

- the hook, and what happens in frames 0 to 3 s (the `virality` checklist as the lens);
- the structure, pacing and the moment that drives shares or saves;
- the mechanism in one line: the reusable part;
- what was luck or circumstance (a trend, an existing big audience, a collab) and can't be copied.

Never reuse their footage, audio or script. Only the mechanism moves into our ideas.

## 4. Write the research file

Save `creator/research/YYYY-Www.md` (ISO week):

1. **What's working this week:** 3 to 5 bullets, each a mechanism with its evidence (outlier score, link).
2. **Outliers:** a table of reel link, creator, views, creator median, outlier score, hook (first line), format, length.
3. **Teardowns:** the four from step 3.
4. **Niche hooks:** the first spoken or on-screen line of every outlier. Also append them to `creator/research/niche-hooks.csv` (`hook,views,outlier,creator,url,date`) so `hook-mining` can use them.
5. **Cost:** what this run spent.

## 5. Refill the bank

Turn each mechanism into 2 or 3 ideas for our pillars, angled to our audience and voice (`idea-generation-and-ideation`'s angle step). Score them as `daily-ideas` does and append to `creator/idea-bank.csv` with `source` = this research file and `evidence` = the outlier link and score. Aim for 10 to 20 new ideas.

Finish with a short summary: the top 3 mechanisms, how many ideas were added, and the cost.

## Rules

- Report numbers exactly as the data gives them. If a field is missing, say so; never estimate views or medians.
- A huge raw view count is not an outlier on its own. The score against the creator's median is what counts.
- Public data only.
