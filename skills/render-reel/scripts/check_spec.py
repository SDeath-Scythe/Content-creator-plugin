#!/usr/bin/env python3
"""Check a rendered reel against each platform's upload limits and pull review frames.

  python3 check_spec.py out.mp4 [--platforms instagram,tiktok,youtube] [--frames frames/]

Exits 1 if any hard limit fails. Warnings don't fail the check but belong on the approval card.
Limits: Meta's IG User Media reference for REELS (3 s to 15 min, 300 MB, H.264/HEVC, AAC,
23 to 60 fps, moov atom first). The 90-second line is our reach guideline, not an API limit.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

LIMITS = {
    "instagram": {"min_s": 3, "max_s": 900, "max_mb": 300, "warn_over_s": 90},
    "tiktok": {"min_s": 3, "max_s": 600, "max_mb": 4000, "warn_over_s": 60},
    "youtube": {"min_s": 1, "max_s": 180, "max_mb": 256000, "warn_over_s": 60},
}
REVIEW_TIMES = [0, 0.5, 1.0, 1.5, 2.0, 3.0]


def probe(path):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(path)],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        sys.exit(f"ffprobe couldn't read {path}: {result.stderr.strip()}")
    return json.loads(result.stdout)


def moov_first(path):
    """True if the moov atom comes before mdat (needed for streaming uploads)."""
    with open(path, "rb") as f:
        offset = 0
        while True:
            f.seek(offset)
            header = f.read(16)
            if len(header) < 8:
                return False
            size = int.from_bytes(header[:4], "big")
            kind = header[4:8]
            if size == 1:
                size = int.from_bytes(header[8:16], "big")
            if kind == b"moov":
                return True
            if kind == b"mdat" or size == 0:
                return False
            offset += size


def check(path, platforms):
    info = probe(path)
    video = next((s for s in info["streams"] if s["codec_type"] == "video"), None)
    audio = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    duration = float(info["format"]["duration"])
    size_mb = int(info["format"]["size"]) / 1_000_000
    num, den = (video["avg_frame_rate"].split("/") + ["1"])[:2] if video else ("0", "1")
    fps = float(num) / float(den or 1)
    w, h = (video["width"], video["height"]) if video else (0, 0)

    summary = {
        "file": str(path), "duration_s": round(duration, 2), "size_mb": round(size_mb, 2),
        "width": w, "height": h, "fps": round(fps, 2),
        "video_codec": video and video["codec_name"], "audio_codec": audio and audio["codec_name"],
        "moov_first": moov_first(path),
    }
    fails, warns = [], []

    if not video:
        fails.append("no video stream")
    else:
        if video["codec_name"] not in ("h264", "hevc"):
            fails.append(f"video codec {video['codec_name']}: use H.264")
        if video.get("pix_fmt") not in ("yuv420p", "yuvj420p"):
            warns.append(f"pixel format {video.get('pix_fmt')}: yuv420p plays everywhere")
        if (w, h) != (1080, 1920):
            (warns if abs(w / h - 9 / 16) < 0.01 else fails).append(f"{w}x{h}: reels should be 1080x1920 (9:16)")
        if not 23 <= fps <= 60:
            fails.append(f"{fps:.2f} fps: must be 23 to 60")
    if not audio:
        warns.append("no audio track: add voice, a licensed bed, or a silent track")
    elif audio["codec_name"] != "aac":
        fails.append(f"audio codec {audio['codec_name']}: use AAC")
    if not summary["moov_first"]:
        fails.append("moov atom not at the front: re-encode with -movflags +faststart")

    for name in platforms:
        lim = LIMITS[name]
        if not lim["min_s"] <= duration <= lim["max_s"]:
            fails.append(f"{name}: {duration:.1f}s is outside {lim['min_s']} to {lim['max_s']}s")
        elif duration > lim["warn_over_s"]:
            warns.append(f"{name}: {duration:.0f}s is long for short-form; aim for under {lim['warn_over_s']}s unless the idea needs it")
        if size_mb > lim["max_mb"]:
            fails.append(f"{name}: {size_mb:.0f} MB is over {lim['max_mb']} MB")

    return summary, fails, warns


def extract_frames(path, out_dir, duration):
    out_dir.mkdir(parents=True, exist_ok=True)
    times = [t for t in REVIEW_TIMES if t < duration] + [max(0, duration - 0.1)]
    written = []
    for t in times:
        target = out_dir / f"t{t:06.2f}.png"
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", str(path), "-frames:v", "1", str(target)],
            check=True,
        )
        written.append(str(target))
    return written


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("video", type=Path)
    parser.add_argument("--platforms", default="instagram")
    parser.add_argument("--frames", type=Path, help="write review frames (0 to 3 s and the end) here")
    args = parser.parse_args()

    platforms = [p.strip() for p in args.platforms.split(",") if p.strip()]
    unknown = set(platforms) - LIMITS.keys()
    if unknown:
        sys.exit(f"unknown platform(s): {', '.join(sorted(unknown))}")

    summary, fails, warns = check(args.video, platforms)
    if args.frames:
        summary["frames"] = extract_frames(args.video, args.frames, summary["duration_s"])
    summary.update(platforms=platforms, ok=not fails, fails=fails, warnings=warns)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
