#!/usr/bin/env python3
"""Build the reel's soundtrack: the narration cut at its pauses with gaps opened, plus synthesized sound effects.

  python3 audio.py voice.mp3 mix.wav

Every effect is generated here (no samples), so nothing needs a licence.
"""
import subprocess
import sys
import wave

import numpy as np

SR = 48000
DUR = 21.2
rng = np.random.default_rng(7)

# Narration chunks (seconds in the original file) and where they start in the reel.
# Cuts sit in the middle of the voice's own pauses.
CHUNKS = [
    ((0.00, 3.08), 0.00),   # مشروع تخرجك… ياخذ منك فصل كامل؟
    ((3.08, 4.31), 3.58),   # خلّيه علينا               (+0.5 s: room for the stamp)
    ((4.31, 8.16), 5.41),   # نبني مشروعك كامل… برمجة، تصميم، واختبار   (+0.6 s: screens fly in)
    ((8.16, 14.41), 9.66),  # ونكتب التقرير… ونجهّزك للمناقشة… نشرح لك كل جزء   (+0.4 s)
    ((14.41, 18.29), 16.51),  # اكتب «مشروع» بالتعليقات وانطيك التفاصيل والسعر   (+0.6 s: riser into the CTA)
]


def load_voice(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                         check=True, capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def env(n, attack=0.005, release=None, curve=6.0):
    t = np.linspace(0, 1, n)
    e = np.exp(-curve * t) if release is None else np.ones(n)
    a = max(1, int(attack * SR))
    e[:a] *= np.linspace(0, 1, a)
    return e


def sine_sweep(f0, f1, dur):
    n = int(dur * SR)
    f = np.geomspace(f0, f1, n)
    return np.sin(2 * np.pi * np.cumsum(f) / SR)


def lowpass(x, cutoff):
    # one-pole low-pass, enough for shaping noise
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i, v in enumerate(x):
        acc = (1 - a) * v + a * acc
        y[i] = acc
    return y


def noise(dur):
    return rng.standard_normal(int(dur * SR))


# --- the effects -------------------------------------------------------------------------------
def thud(dur=0.45, big=False):
    body = sine_sweep(140 if big else 180, 45, dur) * env(int(dur * SR), curve=7)
    hit = lowpass(noise(0.08), 1800) * env(int(0.08 * SR), curve=18) * (1.6 if big else 0.8)
    out = np.zeros(int(dur * SR))
    out += body * (1.0 if big else 0.55)
    out[: len(hit)] += hit
    return out


def whoosh(dur=0.5, rise=False):
    n = int(dur * SR)
    t = np.linspace(0, 1, n)
    shape = t ** 2 if rise else np.sin(np.pi * t) ** 1.5
    x = lowpass(noise(dur), 900) * 2.2 + lowpass(noise(dur), 3500) * 0.6
    return x * shape * 0.5


def pop(f0=900, f1=260, dur=0.09, level=0.5):
    return sine_sweep(f0, f1, dur) * env(int(dur * SR), curve=9) * level


def tick(f=2600, level=0.18):
    return sine_sweep(f, f * 0.8, 0.03) * env(int(0.03 * SR), curve=14) * level


def riser(dur=0.75):
    n = int(dur * SR)
    t = np.linspace(0, 1, n)
    tone = sine_sweep(180, 1400, dur) * 0.18 + sine_sweep(270, 2100, dur) * 0.08
    return (tone + lowpass(noise(dur), 2500) * 0.25) * t ** 2


def paper(dur=0.35):
    x = noise(dur)
    hp = x - lowpass(x, 1200)
    flutter = 0.6 + 0.4 * np.sin(2 * np.pi * 22 * np.linspace(0, dur, int(dur * SR)))
    return hp * flutter * np.sin(np.pi * np.linspace(0, 1, int(dur * SR))) * 0.22


def marker(dur=0.42):
    x = noise(dur)
    band = lowpass(x, 5000) - lowpass(x, 1800)
    return band * np.sin(np.pi * np.linspace(0, 1, int(dur * SR))) ** 0.6 * 0.35


def ding():
    dur = 1.1
    t = np.linspace(0, dur, int(dur * SR))
    tone = np.sin(2 * np.pi * 1318.5 * t) + 0.55 * np.sin(2 * np.pi * 1975.5 * t) + 0.25 * np.sin(2 * np.pi * 2637 * t)
    return tone * np.exp(-4.2 * t) * 0.22


def sparkle():
    out = np.zeros(int(0.9 * SR))
    for k in range(9):
        at = int(rng.uniform(0, 0.7) * SR)
        b = pop(rng.uniform(2400, 4200), rng.uniform(1800, 3000), 0.05, 0.12)
        out[at:at + len(b)] += b
    return out


# --- the timeline (seconds in the reel) ----------------------------------------------------------
SFX = [
    (0.00, thud()),                                   # the plan slams in
    *[(0.35 + k * 0.22, tick()) for k in range(5)],   # the week pills tick red
    (3.05, whoosh(0.55, rise=True)),                  # wind-up to the stamp
    (3.60, thud(0.7, big=True)),                      # «خلّيه علينا» stamp
    (4.85, whoosh(0.45)),                             # into step 1
    (5.05, whoosh(0.35)), (5.28, pop(700, 220, 0.12, 0.45)),   # IDE window slams in
    (5.65, pop(1100, 380, 0.1, 0.4)),                 # phone pops in
    (6.92, whoosh(0.4)),                              # screens fly out
    (7.05, pop(600, 300)), (7.25, pop(700, 350)), (7.85, pop(800, 400)), (8.45, pop(900, 450)),  # rows flip
    (9.22, whoosh(0.45)),                             # into step 2
    (9.90, pop(950, 420, 0.1, 0.5)),                  # report row flips
    (10.30, paper()),                                 # the real report slides in
    (10.85, marker()),                                # highlighter sweep
    (12.55, whoosh(0.35)),                            # report out
    (12.80, pop(800, 380)), (13.10, pop(1200, 500, 0.1, 0.35)),   # defence row, slide card
    (15.45, whoosh(0.35)),                            # slide out
    (15.75, riser(0.75)),                             # build-up to the CTA
    (16.50, thud(0.6, big=True)),                     # CTA hits
    (17.10, pop(1300, 600, 0.1, 0.4)),                # «مشروع» chip pulses
    (20.15, thud(0.5)), (20.15, ding()), (20.20, sparkle()),   # «جاهز ✓» + confetti
]


def place(track, at, clip, gain=1.0):
    i = int(at * SR)
    j = min(len(track), i + len(clip))
    track[i:j] += clip[: j - i] * gain


def main(voice_path, out_path):
    voice = load_voice(voice_path)
    vtrack = np.zeros(int(DUR * SR))
    for (a, b), at in CHUNKS:
        place(vtrack, at, voice[int(a * SR):int(b * SR)])
    sfx = np.zeros_like(vtrack)
    for at, clip in SFX:
        place(sfx, at, clip.astype(np.float32))
    mix = vtrack + sfx * 0.55
    mix /= max(1.0, np.abs(mix).max() / 0.95)
    with wave.open(out_path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((mix * 32767).astype(np.int16).tobytes())
    for (a, b), at in CHUNKS:
        print(f"voice {a:5.2f}-{b:5.2f}  ->  {at:5.2f}-{at + b - a:5.2f}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
