# Examples

Output from test runs of content-creator, on made-up pages. Nothing here was posted, and the reels are silent because no one recorded a voice for them.

| Example | Page | What it shows |
| --- | --- | --- |
| [grad-projects](grad-projects/creator) | Helping students build their graduation project, and write the report | Two 15 s English reels taken through the reel pipeline: [project plan](grad-projects/creator/reels/2026-10-24-project-plan) (the main topic) and [report order](grad-projects/creator/reels/2026-10-24-report-order). Each folder has the plan (goal, 3 hooks on the 8-point check, script, captions, approval card), the build and the rendered MP4 + cover |
| [freelance-pricing](freelance-pricing/creator) | Pricing for freelance designers in the Gulf (Arabic) | A full dry run by a separate Claude session: page-setup's files, a scored idea bank, and a 29 s Arabic reel through to the approval card |

To re-render a reel from its build folder:

```bash
node skills/render-reel/scripts/render.mjs examples/grad-projects/creator/reels/2026-10-24-project-plan/build/reel.html out.mp4 --cover cover.jpg
```

The grad-projects reels compute their row animations with `build/gen.py`: edit `reel.src.html` or the rows in `gen.py`, then `python3 gen.py reel.src.html reel.html`.
