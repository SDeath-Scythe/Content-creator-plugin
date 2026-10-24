#!/usr/bin/env python3
"""Generate the graduation-report reel's reel.html (row reorder keyframes are computed here)."""
import sys
DUR = 15.0
ROW = 104  # px per row
# chapter, title, page, slot timeline [(time, slot)], settle time, write order
ROWS = [
    ("1", "Introduction",       "1",  [(0,0),(3.0,2),(5.5,3),(8.0,4),(10.5,5)], 11.0, "5"),
    ("2", "Literature Review",  "6",  [(0,1),(3.0,3),(5.5,4),(8.0,3)],          8.5,  "4"),
    ("3", "Methodology",        "19", [(0,2),(3.0,0)],                          3.5,  "1"),
    ("4", "Implementation",     "31", [(0,3),(3.0,1)],                          3.5,  "1"),
    ("5", "Results & Testing",  "52", [(0,4),(5.5,2)],                          6.0,  "2"),
    ("6", "Conclusion",         "67", [(0,5),(10.5,4)],                         11.0, "4"),
]
# Write-order labels: Methodology+Implementation both "1st", Results 2nd, Lit 3rd, Conclusion 4th, Intro last
ORDER = {"Introduction":"LAST","Literature Review":"3rd","Methodology":"1st","Implementation":"1st","Results & Testing":"2nd","Conclusion":"4th"}
MOVE = 0.5
JITTER = [(-3, -18), (2.5, 14), (-2, -10), (3, 20), (-2.5, -14), (2, 10)]  # rotate deg, x px during the break

def pct(t): return f"{t / DUR * 100:.3f}%"

def keyframes(i, row):
    _, title, _, steps, settle, _ = row
    orig = steps[0][1]
    rot, dx = JITTER[i]
    frames = []
    def add(t, slot, r=0, x=0):
        frames.append(f"  {pct(t)} {{ transform: translate({x}px, {(slot - orig) * ROW}px) rotate({r}deg); }}")
    slot = orig
    add(0, slot)
    add(2.30, slot)
    add(2.45, slot, rot, dx)            # the list breaks when the stamp lands
    add(2.95, slot, rot * 0.7, dx * 0.7)
    if not any(t == 3.0 for t, _ in steps[1:]):
        add(3.0 + MOVE, slot)           # settle back from the break even if this row doesn't move at 3 s
    for t, s in steps[1:]:
        add(t, slot, *( (rot*0.7, dx*0.7) if t == 3.0 else (0, 0) ))
        add(t + MOVE, s)
        slot = s
    add(DUR, slot)
    frames.sort(key=lambda f: float(f.split('%')[0]))
    return f"@keyframes row{i} {{\n" + "\n".join(frames) + "\n}"

def highlight(i, row):
    steps = row[3]
    moves = [t for t, _ in steps[1:]]
    # highlighted while it is the row being moved into place (its final move)
    t = moves[-1]
    return (f"@keyframes hl{i} {{ 0%, {pct(t - 0.01)} {{ background: transparent; }} "
            f"{pct(t)}, {pct(t + 1.6)} {{ background: var(--hl); }} {pct(t + 2.2)}, 100% {{ background: transparent; }} }}")

rows_css = "\n".join(keyframes(i, r) + "\n" + highlight(i, r) + f"\n.row:nth-child({i+1}) {{ animation: row{i} {DUR}s linear both, hl{i} {DUR}s linear both; }}"
                     f"\n.row:nth-child({i+1}) .tag {{ animation-delay: {r[4]}s; }}" for i, r in enumerate(ROWS))
rows_html = "\n".join(
    f'          <li class="row"><span class="ch" style="--k: {int(ch) - 1}">{ch}</span><span class="title">{title}</span><span class="dots"></span>'
    f'<span class="pg">{pg}</span><span class="tag">{ORDER[title]}</span></li>' for ch, title, pg, *_ in ROWS)

html = open(sys.argv[1]).read().replace("/*ROWS_CSS*/", rows_css).replace("<!--ROWS_HTML-->", rows_html)
open(sys.argv[2], "w").write(html)
