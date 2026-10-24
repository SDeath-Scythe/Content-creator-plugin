#!/usr/bin/env python3
"""Generate the graduation-project reel's reel.html: plan rows that move and change text on a 15 s timeline."""
import sys
DUR, ROW, MOVE = 15.0, 124, 0.5
# key, (pill, text) before, (pill, text) after or None, swap time, slot timeline, tag, tag time
ROWS = [
    ("learn",  ("W1–4", "Learn every technology"), ("as needed", "Learn as you go"), 6.0, [(0, 0), (3.0, 1)], "2nd", 6.4),
    ("design", ("W5–7", "Design all the screens"), None, None, [(0, 1), (3.0, 2), (9.0, 3)], "", 0),
    ("build",  ("W8–12", "Build everything"), ("W1–3", "Build a tiny version"), 3.0, [(0, 2), (3.0, 0)], "1st", 3.5),
    ("test",   ("W13", "Test it"), None, None, [(0, 3), (9.0, 4)], "", 0),
    ("report", ("W14–15", "Write the 80-page report"), ("weekly", "Write the report"), 9.0, [(0, 4), (9.0, 2)], "3rd", 9.5),
]
JITTER = [(-3, -16), (2.5, 14), (-2, -12), (3, 18), (-2.5, -14)]

def pct(t): return f"{t / DUR * 100:.3f}%"

def move_keyframes(i, steps):
    orig = steps[0][1]
    rot, dx = JITTER[i]
    frames = {}
    def add(t, slot, r=0.0, x=0.0):
        frames[round(t, 3)] = f"transform: translate({x:.1f}px, {(slot - orig) * ROW}px) rotate({r:.2f}deg);"
    add(0, orig); add(2.30, orig); add(2.45, orig, rot, dx); add(2.95, orig, rot * .7, dx * .7)
    if not any(t == 3.0 for t, _ in steps[1:]):
        add(3.0 + MOVE, orig)
    slot = orig
    for t, s in steps[1:]:
        add(t, slot, *((rot * .7, dx * .7) if t == 3.0 else (0, 0)))
        add(t + MOVE, s)
        slot = s
    add(DUR, slot)
    body = "\n".join(f"  {pct(t)} {{ {v} }}" for t, v in sorted(frames.items()))
    return f"@keyframes mv{i} {{\n{body}\n}}"

def highlight(i, t):
    return (f"@keyframes hl{i} {{ 0%, {pct(t - .01)} {{ background: transparent; }} {pct(t)}, {pct(t + 2.0)} {{ background: var(--hl); }} "
            f"{pct(t + 2.5)}, 100% {{ background: transparent; }} }}")

css, html = [], []
for i, (key, before, after, swap, steps, tag, tag_t) in enumerate(ROWS):
    anims = [f"mv{i} {DUR}s linear both"]
    css.append(move_keyframes(i, steps))
    if swap is not None:
        css.append(highlight(i, swap))
        anims.append(f"hl{i} {DUR}s linear both")
        css.append(f".row:nth-child({i+1}) .before {{ animation-delay: {swap}s; }} .row:nth-child({i+1}) .after {{ animation-delay: {swap}s; }}")
    if tag:
        css.append(f".row:nth-child({i+1}) .tag {{ animation-delay: {tag_t}s; }}")
    css.append(f".row:nth-child({i+1}) {{ animation: {', '.join(anims)}; }}")
    def content(cls, pill, text):
        return f'<span class="{cls}"><span class="pill">{pill}</span><span class="text">{text}</span></span>'
    inner = content("before" if after else "only", *before) + (content("after", *after) if after else "")
    html.append(f'          <li class="row {key}" style="--k: {i}">{inner}<span class="tag">{tag}</span></li>')

src = open(sys.argv[1]).read()
open(sys.argv[2], "w").write(src.replace("/*ROWS_CSS*/", "\n".join(css)).replace("<!--ROWS_HTML-->", "\n".join(html)))
