---
name: weekly-review
description: >-
  Weekly review of the page's own posts: fill the post log from Insights (screenshots, numbers
  the user gives, or Composio if it exposes them), find what worked by watch time, skip rate,
  shares and saves, move winning hooks into creator/hook-wins.csv, and set next week's mix. Use
  once a week, or when the user says "review my week", "how did my posts do" or sends Insights
  screenshots.
---

# Weekly review

Close the loop: our own results decide next week, and over time our winners replace the bundled examples as the hook rules.

Read `creator/page.md`, `creator/post-log.csv`, `creator/hook-wins.csv` and the last research file.

## 1. Get the numbers

For every post in `creator/post-log.csv` from the last 7 to 14 days with empty number columns:

- If Composio exposes Instagram insights for the account, read them: views, reach, average watch time, skip rate (or 3-second views), shares, saves, comments, follows from the post.
- Otherwise ask the user for Insights screenshots of each post (the reel's Insights page, scrolled to show retention and interactions), and read the numbers from the images.

Write them into the log. Leave a cell empty when the number isn't shown. **Never estimate or invent a metric.** If most numbers are missing, say what's missing and review only what's there.

Use `views_7d` for comparisons; posts younger than 7 days get a note and are compared again next week.

## 2. Find what worked

Run `analytics-and-reporting` on the log, with these signals in this order (vanity counts like likes and follower totals come last):

1. **Hook:** skip rate, or 3-second views ÷ views. This judges the first 3 seconds.
2. **Hold:** average watch time ÷ duration.
3. **Spread:** shares ÷ reach, saves ÷ reach.
4. **Goal:** follows, comments with the keyword, link clicks or DMs, whichever matches the page goal.

Compare each post to the page's own median for the last 30 posts (or all posts, if fewer). Show one table, best first: post, hook, format, pillar, and each signal against the median (e.g. "1.8× median shares").

Then 3 to 5 findings, each with its evidence: which hooks held, which pillars or formats beat the median, what the losers share. With fewer than 10 posts, say the findings are early.

## 3. Feed the winners back

- Posts in the top 20% by shares + saves per reach, or with a hook score clearly above median: append their hook to `creator/hook-wins.csv` (`hook,views,shares,saves,pattern,platform,date,source=own`).
- From 20 rows on, run `hook-mining` on `creator/hook-wins.csv` (and `creator/research/niche-hooks.csv` if it exists) and note the top patterns in `page.md` under "What works for us". `reel-pipeline` uses them.
- For each top post, suggest a follow-up with `content-recycling`: a part 2, the same mechanism on another pillar, or a carousel version.

## 4. Set next week

Using `instagram-growth` as the lens, propose next week's plan in a few lines: how many reels and carousels (within the cadence the user can sustain), which pillars, which hook patterns to repeat, one experiment (a new format or a trial-reel hook test). Mark the ideas this makes urgent in the bank.

## 5. Monthly checks

On the first review of each month, also:

- Ask the user to open Instagram's **Account Status** and confirm there's no originality or recommendation warning. Instagram stops recommending accounts whose posts are mostly not their own.
- Revisit `voice.md` if it was provisional and there are now 10 or more posts.
- Check `page.md`: is the goal still right, is the cadence realistic?

## Rules

- Numbers come only from Insights, Composio or the user.
- One week of data is noise. Name a pattern only when 3 or more posts show it.
- Recommend changes, don't make them: the user approves next week's plan.
