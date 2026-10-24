// content-creator reel runtime. Makes the page seekable so render.mjs can draw any frame exactly.
//
// - Elements with data-start / data-end (seconds) are visible only inside that window,
//   and their CSS animations start at data-start.
// - Captions come from <script type="application/json" id="captions-data">[{start, end, text}]</script>.
// - ?mode=cover shows the .cover element instead of the video. ?guides=1 shades unsafe areas.
// - ?t=1.5 freezes the page at that time, for previews in a normal browser.
(() => {
  const params = new URLSearchParams(location.search);
  const meta = (name, fallback) => document.querySelector(`meta[name="${name}"]`)?.content ?? fallback;
  const REEL = (window.REEL = {
    duration: Number(meta("reel-duration", 20)),
    fps: Number(meta("reel-fps", 30)),
    mode: params.get("mode") || "video",
  });

  const root = document.documentElement;
  if (params.has("guides")) root.classList.add("guides");
  if (REEL.mode === "cover") root.classList.add("cover-mode");

  const captions = JSON.parse(document.getElementById("captions-data")?.textContent || "[]");
  const captionEl = document.getElementById("captions");

  // Index each word of a .words claim so the stagger works without hand-written delays
  for (const claim of document.querySelectorAll(".words")) {
    const words = claim.textContent.trim().split(/\s+/);
    claim.textContent = "";
    words.forEach((w, i) => {
      const span = document.createElement("span");
      span.textContent = w;
      span.style.setProperty("--i", i);
      claim.append(span, " ");
    });
  }

  const startOf = (el) => Number(el.closest("[data-start]")?.dataset.start ?? 0);
  const isActive = (el, t) => {
    for (let node = el.closest("[data-start]"); node; node = node.parentElement?.closest("[data-start]")) {
      const s = Number(node.dataset.start);
      const e = node.dataset.end === undefined ? Infinity : Number(node.dataset.end);
      if (t < s || t >= e) return false;
    }
    return true;
  };

  window.seek = (t) => {
    for (const el of document.querySelectorAll("[data-start]")) {
      el.style.visibility = isActive(el, t) ? "visible" : "hidden";
    }
    for (const anim of document.getAnimations()) {
      anim.pause();
      const target = anim.effect?.target;
      anim.currentTime = Math.max(0, (t - (target ? startOf(target) : 0)) * 1000);
    }
    if (captionEl) {
      const cue = captions.find((c) => t >= c.start && t < c.end);
      captionEl.innerHTML = cue ? cue.text : "";
    }
  };

  window.reelReady = document.fonts.ready.then(() => window.seek(Number(params.get("t") ?? 0)));
})();
