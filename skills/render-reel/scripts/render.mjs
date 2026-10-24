#!/usr/bin/env node
// Built-in reel renderer: draws an HTML reel (see ../template) frame by frame with Playwright,
// then encodes it with ffmpeg as H.264 + AAC, 1080x1920, moov atom first.
//
//   node render.mjs reel.html out.mp4 [--voice voice.wav] [--music bed.mp3] [--music-volume 0.15]
//                                      [--cover cover.jpg] [--draft]
//   node render.mjs reel.html stills/ --stills 0,0.5,1.3,2,3 [--guides]   (PNG frames only, for quick review;
//                                      --guides shades the areas Instagram covers)
//
// The page must define window.seek(t) and window.reelReady (reel.js does). The page is served from a
// local server: any file it asks for that isn't next to it (reel.css, reel.js, fonts/…) comes from
// this plugin's template and fonts, so a build folder only needs its own reel.html and assets.
// Needs: Node 18+, ffmpeg on PATH, and the playwright package with Chromium
// (`npm i -g playwright && npx playwright install chromium` if it's missing).

import { spawn } from "node:child_process";
import { createReadStream, existsSync, mkdirSync, statSync } from "node:fs";
import { createServer } from "node:http";
import { createRequire } from "node:module";
import { basename, dirname, extname, join, normalize, resolve, sep } from "node:path";
import { fileURLToPath } from "node:url";

const require = createRequire(import.meta.url);
const HERE = dirname(fileURLToPath(import.meta.url));
const TEMPLATE_DIR = resolve(HERE, "../template");
const FONTS_DIR = resolve(HERE, "../../../assets/fonts");
const TYPES = {
  ".html": "text/html", ".css": "text/css", ".js": "text/javascript", ".json": "application/json",
  ".ttf": "font/ttf", ".otf": "font/otf", ".woff": "font/woff", ".woff2": "font/woff2",
  ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".svg": "image/svg+xml", ".webp": "image/webp",
  ".mp4": "video/mp4", ".webm": "video/webm", ".mp3": "audio/mpeg", ".wav": "audio/wav",
};

// Serve the reel's folder, falling back to the plugin's template and fonts for files it doesn't have.
function serve(root) {
  const server = createServer((req, res) => {
    const rel = normalize(decodeURIComponent(new URL(req.url, "http://x").pathname)).replace(/^[/\\]+/, "");
    const candidates = [join(root, rel)];
    if (rel.startsWith(`fonts${sep}`)) candidates.push(join(FONTS_DIR, rel.slice(6)));
    else candidates.push(join(TEMPLATE_DIR, rel));
    const file = candidates.find((f) => (f.startsWith(root + sep) || f.startsWith(TEMPLATE_DIR) || f.startsWith(FONTS_DIR)) && existsSync(f) && statSync(f).isFile());
    if (!file) {
      res.writeHead(404).end();
      return;
    }
    res.writeHead(200, { "content-type": TYPES[extname(file).toLowerCase()] || "application/octet-stream" });
    createReadStream(file).pipe(res);
  });
  return new Promise((ok) => server.listen(0, "127.0.0.1", () => ok(server)));
}

function parseArgs(argv) {
  const opts = { musicVolume: 0.15, draft: false, positional: [] };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--voice") opts.voice = argv[++i];
    else if (a === "--music") opts.music = argv[++i];
    else if (a === "--music-volume") opts.musicVolume = Number(argv[++i]);
    else if (a === "--cover") opts.cover = argv[++i];
    else if (a === "--draft") opts.draft = true;
    else if (a === "--stills") opts.stills = argv[++i].split(",").map(Number);
    else if (a === "--guides") opts.guides = true;
    else opts.positional.push(a);
  }
  if (opts.positional.length !== 2) {
    console.error("usage: node render.mjs reel.html out.mp4 [--voice f] [--music f] [--music-volume 0.15] [--cover cover.jpg] [--draft]\n" +
      "       node render.mjs reel.html out-dir/ --stills 0,0.5,1.3 [--guides]");
    process.exit(2);
  }
  [opts.html, opts.out] = opts.positional.map((p) => resolve(p));
  for (const file of [opts.html, opts.voice, opts.music].filter(Boolean)) {
    if (!existsSync(file)) {
      console.error(`not found: ${file}`);
      process.exit(2);
    }
  }
  return opts;
}

function loadPlaywright() {
  for (const name of ["playwright", "playwright-core"]) {
    try {
      return require(name);
    } catch {}
  }
  const globalRoot = process.env.npm_config_prefix || "/usr/local";
  try {
    return require(`${globalRoot}/lib/node_modules/playwright`);
  } catch {}
  console.error("Playwright not found. Install it with: npm i -g playwright && npx playwright install chromium");
  process.exit(3);
}

function ffmpegArgs({ fps, duration, voice, music, musicVolume, out, draft }) {
  const args = ["-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(fps), "-i", "-"];
  if (voice) args.push("-i", voice);
  if (music) args.push("-stream_loop", "-1", "-i", music);

  // No sound given: a silent track, so every platform gets the AAC stream it expects
  if (!voice && !music) args.push("-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo");

  // Every audio path ends at exactly `duration`, so a looped bed can't keep ffmpeg running
  const end = `atrim=0:${duration},asetpts=N/SR/TB`;
  let filter;
  if (voice && music) {
    // Music sits under the voice and ducks while the voice speaks
    filter =
      `[1:a]aresample=48000,apad,${end},asplit=2[voice][key];` +
      `[2:a]aresample=48000,volume=${musicVolume},${end}[bed];` +
      `[bed][key]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[ducked];` +
      `[voice][ducked]amix=inputs=2:duration=first:normalize=0[mix]`;
  } else if (voice) {
    filter = `[1:a]aresample=48000,apad,${end}[mix]`;
  } else if (music) {
    filter = `[1:a]aresample=48000,volume=${musicVolume * 4},${end}[mix]`;
  } else {
    filter = `[1:a]${end}[mix]`;
  }

  return [
    ...args,
    "-filter_complex", filter,
    "-map", "0:v", "-map", "[mix]",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", String(fps),
    "-preset", draft ? "veryfast" : "slow", "-crf", draft ? "28" : "18",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    "-t", String(duration), "-movflags", "+faststart", out,
  ];
}

async function openPage(browser, url) {
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  const errors = [];
  page.on("pageerror", (e) => errors.push(e.message));
  page.on("requestfailed", (r) => errors.push(`failed to load ${r.url()}`));
  await page.goto(url, { waitUntil: "load" });
  await page.evaluate(() => window.reelReady);
  if (errors.length) console.warn(`page warnings:\n  ${errors.join("\n  ")}`);
  return page;
}

async function main() {
  const opts = parseArgs(process.argv.slice(2));
  const { chromium } = loadPlaywright();
  const browser = await chromium.launch();
  const server = await serve(dirname(opts.html));
  const url = `http://127.0.0.1:${server.address().port}/${encodeURIComponent(basename(opts.html))}`;

  try {
    const page = await openPage(browser, opts.stills && opts.guides ? `${url}?guides=1` : url);
    if (opts.stills) {
      mkdirSync(opts.out, { recursive: true });
      for (const t of opts.stills) {
        await page.evaluate((t) => window.seek(t), t);
        const path = resolve(opts.out, `t${t.toFixed(2).padStart(5, "0")}.png`);
        await page.screenshot({ path, type: "png" });
        console.log(`wrote ${path}`);
      }
      return;
    }
    const { duration, fps } = await page.evaluate(() => ({ duration: window.REEL.duration, fps: window.REEL.fps }));
    const frames = Math.round(duration * fps);
    console.log(`rendering ${frames} frames (${duration}s at ${fps} fps) from ${opts.html}`);

    mkdirSync(dirname(opts.out), { recursive: true });
    const ff = spawn("ffmpeg", ffmpegArgs({ ...opts, fps, duration }), { stdio: ["pipe", "inherit", "inherit"] });
    const done = new Promise((ok, fail) => ff.on("close", (code) => (code === 0 ? ok() : fail(new Error(`ffmpeg exited ${code}`)))));
    done.catch(() => {}); // awaited below; this stops an early ffmpeg failure from crashing the loop
    let ffClosed = false;
    ff.stdin.on("error", () => (ffClosed = true));
    ff.on("close", () => (ffClosed = true));

    for (let i = 0; i < frames && !ffClosed; i++) {
      await page.evaluate((t) => window.seek(t), i / fps);
      const frame = await page.screenshot({ type: "jpeg", quality: 95 }); // JPEG 95 is visually lossless before H.264 and ~3x faster than PNG
      if (!ff.stdin.write(frame) && !ffClosed) {
        // Wait for ffmpeg to catch up, or stop waiting if it has died (it may already have)
        await new Promise((r) => {
          const poll = setInterval(() => ffClosed && (clearInterval(poll), r()), 100);
          ff.stdin.once("drain", () => (clearInterval(poll), r()));
        });
      }
      if (i % (fps * 5) === 0) console.log(`  ${(i / fps).toFixed(0)}s`);
    }
    ff.stdin.end();
    await done;
    console.log(`wrote ${opts.out}`);

    if (opts.cover) {
      mkdirSync(dirname(resolve(opts.cover)), { recursive: true });
      const coverPage = await openPage(browser, `${url}?mode=cover`);
      await coverPage.screenshot({ path: resolve(opts.cover), type: "jpeg", quality: 92 });
      console.log(`wrote ${resolve(opts.cover)}`);
    }
  } finally {
    await browser.close();
    server.close();
  }
}

main().catch((e) => {
  console.error(e.message);
  process.exit(1);
});
