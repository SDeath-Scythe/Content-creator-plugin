# Apify actors for weekly research

Checked October 2026 on the Apify free tier. Actors change: before each run, read the actor's current input schema with Apify's actor-details tool, and if a name below no longer exists, search the Apify Store for a replacement with the same job.

| Job | Actor | Input | Free-tier price | Fields used |
| --- | --- | --- | --- | --- |
| Keyword search | `data-slayer/instagram-search-reels` | `{"query": "<keyword>", "maxPages": 4}` | $0.0025 a result + $0.002 a start | `code` (reel URL is `https://www.instagram.com/reel/<code>/`), `play_count`, `like_count`, `comment_count`, `share_count`, `video_duration`, `taken_at`, `caption.text`, `user.username` |
| Creator's recent reels (median) | `apify/instagram-reel-scraper` | `{"username": ["<handle>"], "resultsLimit": 30, "skipPinnedPosts": true}` | $0.0026 a reel + $0.001 a start | views, date, caption, URL (check names in the output) |
| Transcript | `steadyfetch/instagram-reel-transcript-scraper` | `{"reelUrls": ["<url>", "..."]}` | $0.015 a reel | transcript, first-3-second hook, language |

`maxPages` doesn't map to a fixed result count. After the first run, note how many results one page gave and set `maxPages` so a search returns about 50.

## Budget for one weekly batch

| Step | Count | Cost |
| --- | --- | --- |
| Keyword searches | 2 × ~50 reels | ~$0.26 |
| Creator medians | 4 creators × 30 reels | ~$0.32 |
| Transcripts | 4 reels | ~$0.06 |
| **Total** | | **~$0.65** |

That is about $2.60 a month against Apify's $5 free monthly credit. Cut creator pulls to 2 to halve that step. Always state the estimate before running, and stop if the account's remaining credit is lower.

## Outlier score

```
outlier = reel views ÷ median views of that creator's last 30 reels (pinned excluded)
```

- 3× or more: a real outlier, worth a teardown.
- 1.5× to 3×: above normal; note the mechanism, lower priority.
- Under 1.5×: ignore, even if the raw view count is huge. Big accounts get big numbers on average posts.

A reel in the first 48 hours after posting hasn't settled; mark it "early" and don't rank it yet.
