#!/usr/bin/env python3
"""Build the reel's soundtrack: the narration cut at its pauses with gaps opened, three synthesized sound effects
and an original music bed that ducks under the voice.

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
    (3.60, thud(0.7, big=True)),     # «خلّيه علينا» stamp
    (16.50, thud(0.5)),              # the CTA appears
    (20.15, ding()),                 # «جاهز ✓»
]


def place(track, at, clip, gain=1.0):
    i = int(at * SR)
    j = min(len(track), i + len(clip))
    track[i:j] += clip[: j - i] * gain


# --- the music bed (composed here, so it's original) -------------------------------------------
BPM = 100
BAR = 4 * 60 / BPM          # 2.4 s
# A minor, warm and hopeful: Am F C G, twice, then C to land on the ding (E6) at 20.15 s
CHORDS = [("A", "C", "E"), ("F", "A", "C"), ("C", "E", "G"), ("G", "B", "D")] * 2 + [("C", "E", "G")]
NOTE = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}


def hz(name, octave):
    return 440.0 * 2 ** ((NOTE[name] + 12 * (octave + 1) - 69) / 12)


def soft_tone(f, dur, harmonics=((1, 1.0), (2, .25), (3, .08)), detune=0.0):
    t = np.arange(int(dur * SR)) / SR
    out = np.zeros_like(t)
    for k, a in harmonics:
        for d in ((-detune, detune) if detune else (0,)):
            out += a * np.sin(2 * np.pi * f * k * (1 + d) * t)
    return out


def pad_chord(chord, dur):
    n = int(dur * SR)
    out = np.zeros(n)
    for i, name in enumerate(chord):
        out += soft_tone(hz(name, 3 if i == 0 else 4), dur, detune=0.0025) * (0.5 if i == 0 else 0.35)
    a, r = int(0.5 * SR), int(0.7 * SR)
    env_ = np.ones(n)
    env_[:a] = np.linspace(0, 1, a)
    env_[-r:] = np.linspace(1, 0, r)
    return out * env_


def pluck(f, dur=0.6):
    t = np.arange(int(dur * SR)) / SR
    tone = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 2 * f * t) + 0.08 * np.sin(2 * np.pi * 3 * f * t)
    return tone * np.exp(-6 * t) * np.minimum(1, t / 0.004)


def kick(dur=0.3):
    return sine_sweep(110, 45, dur) * env(int(dur * SR), curve=9)


def music():
    track = np.zeros(int(DUR * SR))
    step = BAR / 8                                   # eighth notes
    for b, chord in enumerate(CHORDS):
        t0 = b * BAR
        dur = BAR + 0.7 if b < len(CHORDS) - 1 else DUR - t0
        place(track, t0, pad_chord(chord, dur), 0.22)
        # arpeggio joins at step 1 (4.85 s)
        notes = [hz(chord[0], 4), hz(chord[1], 4), hz(chord[2], 4), hz(chord[0], 5)]
        for i, f in enumerate([notes[j] for j in (0, 1, 2, 3, 2, 1, 2, 3)]):
            at = t0 + i * step
            if 4.8 <= at < 20.0:
                place(track, at, pluck(f), 0.16)
        # soft kick on beats 1 and 3 from step 2 (9.6 s); the last chord rings out
        for beat in (0, 2):
            at = t0 + beat * BAR / 4
            if 9.6 <= at < 19.2:
                place(track, at, kick(), 0.35)
    fade = int(1.2 * SR)
    track[-fade:] *= np.linspace(1, 0, fade)
    track[: int(0.3 * SR)] *= np.linspace(0, 1, int(0.3 * SR))
    return track


def duck(music_track, voice_track, depth=0.55):
    """Lower the music while the voice speaks (smoothed voice level as the key)."""
    win = int(0.05 * SR)
    level = np.sqrt(np.convolve(voice_track ** 2, np.ones(win) / win, mode="same"))
    level /= max(level.max(), 1e-9)
    smooth = int(0.25 * SR)
    level = np.convolve(level, np.ones(smooth) / smooth, mode="same")
    level = np.clip(level * 3, 0, 1)
    return music_track * (1 - depth * level)


def main(voice_path, out_path):
    voice = load_voice(voice_path)
    vtrack = np.zeros(int(DUR * SR))
    for (a, b), at in CHUNKS:
        place(vtrack, at, voice[int(a * SR):int(b * SR)])
    sfx = np.zeros_like(vtrack)
    for at, clip in SFX:
        place(sfx, at, clip.astype(np.float32))
    bed = duck(music(), vtrack)
    bed *= 0.16 * np.sqrt(np.mean(vtrack ** 2)) / max(np.sqrt(np.mean(bed ** 2)), 1e-9)  # bed sits about 16 dB under the voice
    mix = vtrack + sfx * 0.4 + bed
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
