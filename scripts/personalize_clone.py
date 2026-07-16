#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parent.parent
SOURCE_ROOT = ROOT / "templates" / "source"
RUNTIME_ROOT = ROOT / "public" / "framerusercontent.com" / "sites" / "5kT83MbRe9g6EXugCPEmVS"
RUNTIME_TEMPLATE_ROOT = SOURCE_ROOT / "runtime"

PORTFOLIO_POST_LINK = "https://github.com/Alfred768/portfolio"
XRAY_LINK = "https://arxiv.org/abs/2511.02280"
WEBWEAVER_LINK = "https://arxiv.org/abs/2603.11132"
LINKEDIN_LINK = "https://www.linkedin.com/in/gaoyiwu/"
GITHUB_LINK = "https://github.com/Alfred768"
SCHOLAR_LINK = "https://scholar.google.com/citations?user=mvtCDxQA&user=mvtCDxQAAAAJ"
CONTROL_CHARS = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F-\x9F]")

PROFILE_URL_REWRITES = [
    ("mailto:mshuxy@gmail.com", "mailto:criswu20010728@gmail.com"),
    ("mshuxy@gmail.com", "criswu20010728@gmail.com"),
    (
        "https://drive.google.com/file/d/1Mru8H1SZOt1-31eJhhlMEmqCMK6kx-2_/view?usp=sharing",
        "/resume/gaoyi-wu-resume.pdf",
    ),
    ("https://www.linkedin.com/in/xiaoyang-hu-elena/", LINKEDIN_LINK),
    ("https://github.com/Xiaoyang-Hu-96", GITHUB_LINK),
    ("https://x.com/elenahuxy", GITHUB_LINK),
]


def replace_strings(html: str, replacements: list[tuple[str, str]]) -> str:
    """Replace visible copy without mutating Framer asset URLs or runtime data."""
    soup = BeautifulSoup(html, "html.parser")

    for node in soup.find_all(string=True):
        if node.parent and node.parent.name in {"script", "style"}:
            continue

        value = str(node)
        for old, new in replacements:
            value = value.replace(old, new)

        if value != node:
            node.replace_with(value)

    for tag in soup.find_all(True):
        for attribute in ("alt", "aria-label", "content", "title", "href"):
            value = tag.get(attribute)
            if not isinstance(value, str):
                continue
            for old, new in replacements:
                value = value.replace(old, new)
            tag[attribute] = value

    return str(soup)


def replace_images(html: str, image_map: dict[str, str]) -> str:
    soup = BeautifulSoup(html, "html.parser")

    for img in soup.find_all("img"):
        src = img.get("src", "")
        basename = Path(urlparse(src).path).name

        if basename not in image_map:
            continue

        new_src = image_map[basename]
        img["src"] = new_src
        img["srcset"] = new_src

    # Framer also stores some image sources inside serialized component props,
    # not only on <img> tags. Apply the same URL replacement to those props.
    return replace_runtime_images(str(soup), image_map)


def preserve_framer_runtime(html: str) -> str:
    """Keep Framer's preload, hydration, and appear scripts intact.

    The generated page deliberately keeps the original initial motion states.
    Framer resolves them once it hydrates, which is what restores entrance
    animation, scroll behavior, hover states, and route transitions.
    """
    return html


def inject_gaoyi_footer_artwork(html: str) -> str:
    """Keep the shared footer's animated seal personalized after hydration."""
    style = """
<style data-gaoyi-footer-artwork>
.framer-dsmh78-container:has(> video[src*="hKQxNSjOTY53ZlJXaLDmO8bUzg"]) {
  background: url("/assets/style-kit/frames/gaoyi-wu-wax-seal.svg") center / 98% no-repeat;
  animation: gaoyi-wax-seal-breathe 3.6s ease-in-out infinite;
}
.framer-dsmh78-container > video[src*="hKQxNSjOTY53ZlJXaLDmO8bUzg"] { opacity: 0 !important; }
.framer-4znru > [data-framer-name="1"],
.framer-4znru > [data-framer-name="2"],
.framer-4znru > [data-framer-name="3"],
.framer-4znru > [data-framer-name="4"],
.framer-4znru > [data-framer-name="5"] { pointer-events: none; }
@keyframes gaoyi-wax-seal-breathe {
  0%, 100% { background-size: 96%; }
  50% { background-size: 104%; }
}
@media (prefers-reduced-motion: reduce) {
  .framer-dsmh78-container:has(> video[src*="hKQxNSjOTY53ZlJXaLDmO8bUzg"]) { animation: none; }
}
</style>
"""
    return html.replace("</head>", style + "</head>")


def inject_gaoyi_name_story(html: str) -> str:
    """Replace the hydrated wax-seal postcard with Gaoyi's own name story."""
    style_and_script = """
<style data-gaoyi-name-story>
[data-framer-name="A5 postcard"].gaoyi-name-story-ready
  > :not(.framer-df8r03):not(.gaoyi-name-story) {
  display: none !important;
}

.gaoyi-name-story {
  box-sizing: border-box;
  color: #0c131b;
  container-type: inline-size;
  font-family: "Mynerve", "Comic Sans MS", cursive;
  pointer-events: none;
  position: absolute;
  transform-origin: 50% 50%;
  z-index: 3;
}

.gaoyi-name-story *,
.gaoyi-name-story *::before,
.gaoyi-name-story *::after {
  box-sizing: border-box;
}

.gaoyi-name-story-frame {
  background: #fbfcfe;
  border: 1.5px dashed #79a8ed;
  border-radius: 10px;
  display: grid;
  grid-template-columns: minmax(0, 1.42fr) minmax(0, 0.92fr);
  inset: 12px;
  overflow: hidden;
  position: absolute;
}

.gaoyi-name-story-left {
  border-right: 1px solid #5a9eff;
  display: flex;
  flex-direction: column;
  min-width: 0;
  padding: 17px 17px 15px 20px;
}

.gaoyi-name-story-kicker {
  color: #3e6190;
  font-size: clamp(12px, 2.45cqw, 15px);
  line-height: 1.15;
  margin: 0;
}

.gaoyi-name-story-kicker strong {
  color: #204773;
  font-family: "Songti SC", "STSong", "Noto Serif CJK SC", serif;
  font-size: 1.14em;
  font-weight: 600;
}

.gaoyi-name-characters {
  display: grid;
  gap: 11px;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  margin-top: 13px;
}

.gaoyi-name-character {
  align-items: center;
  border-bottom: 1px solid rgba(62, 97, 144, 0.32);
  display: grid;
  gap: 7px;
  grid-template-columns: auto minmax(0, 1fr);
  min-width: 0;
  padding: 0 2px 8px;
}

.gaoyi-name-character-glyph {
  color: #174f39;
  font-family: "Songti SC", "STSong", "Noto Serif CJK SC", serif;
  font-size: clamp(32px, 7.3cqw, 44px);
  font-weight: 600;
  line-height: 1;
}

.gaoyi-name-character-copy {
  min-width: 0;
}

.gaoyi-name-character-copy strong,
.gaoyi-name-character-copy span {
  display: block;
}

.gaoyi-name-character-copy strong {
  color: #3e6190;
  font-family: "Montserrat Alternates", sans-serif;
  font-size: clamp(7px, 1.55cqw, 9px);
  letter-spacing: 0;
  line-height: 1.2;
}

.gaoyi-name-character-copy span {
  color: rgba(62, 97, 144, 0.8);
  font-size: clamp(8px, 1.7cqw, 10px);
  line-height: 1.2;
  margin-top: 3px;
}

.gaoyi-name-process {
  align-items: center;
  display: grid;
  gap: 6px;
  grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr) auto 68px;
  margin-top: 13px;
}

.gaoyi-name-process-step {
  color: #3e6190;
  font-size: clamp(9px, 1.95cqw, 12px);
  line-height: 1.25;
}

.gaoyi-name-process-step strong {
  color: #174f39;
  display: block;
  font-family: "Montserrat Alternates", sans-serif;
  font-size: clamp(7px, 1.35cqw, 8px);
  margin-bottom: 4px;
}

.gaoyi-name-process-arrow {
  color: #4e895d;
  font-family: sans-serif;
  font-size: clamp(16px, 3.2cqw, 20px);
}

.gaoyi-name-seal-result {
  align-items: center;
  display: flex;
  flex-direction: column;
  gap: 2px;
  justify-content: center;
}

.gaoyi-name-seal-result img {
  display: block;
  height: 58px;
  object-fit: contain;
  width: 58px;
}

.gaoyi-name-seal-result span {
  color: rgba(62, 97, 144, 0.82);
  font-size: clamp(7px, 1.35cqw, 8px);
  line-height: 1.1;
  text-align: center;
}

.gaoyi-name-interpretation {
  border-top: 1px dashed rgba(62, 97, 144, 0.38);
  margin-top: auto;
  padding-top: 12px;
}

.gaoyi-name-interpretation strong {
  color: #174f39;
  display: block;
  font-family: "Montserrat Alternates", sans-serif;
  font-size: clamp(7px, 1.35cqw, 8px);
  margin-bottom: 5px;
}

.gaoyi-name-interpretation p {
  color: #3e6190;
  font-size: clamp(10px, 2.15cqw, 13px);
  line-height: 1.35;
  margin: 0;
  max-width: 31ch;
}

.gaoyi-name-story-right {
  display: flex;
  flex-direction: column;
  min-width: 0;
  padding: 14px 15px 14px 17px;
  position: relative;
}

.gaoyi-name-stamp-row {
  align-items: flex-start;
  display: flex;
  justify-content: flex-end;
  min-height: 105px;
  position: relative;
}

.gaoyi-name-postmark {
  border-bottom: 2px solid #4e895d;
  border-top: 2px solid #4e895d;
  height: 18px;
  left: 0;
  opacity: 0.88;
  position: absolute;
  top: 42px;
  transform: rotate(8deg);
  width: 80px;
}

.gaoyi-name-postmark::before,
.gaoyi-name-postmark::after {
  border-bottom: 1px solid #4e895d;
  content: "";
  left: 0;
  position: absolute;
  width: 100%;
}

.gaoyi-name-postmark::before { top: 4px; }
.gaoyi-name-postmark::after { bottom: 4px; }

.gaoyi-name-stamp {
  background: #5a9eff;
  border: 4px dotted #fbfcfe;
  box-shadow: 0 0 0 5px #5a9eff;
  height: 94px;
  padding: 6px;
  position: relative;
  width: 76px;
}

.gaoyi-name-stamp-inner {
  background: #f8fafc;
  height: 100%;
  overflow: hidden;
  position: relative;
}

.gaoyi-name-stamp-inner img {
  display: block;
  height: 100%;
  object-fit: cover;
  object-position: center 17%;
  width: 100%;
}

.gaoyi-name-stamp-inner span {
  background: rgba(248, 250, 252, 0.9);
  bottom: 0;
  color: #f06832;
  font-family: "Montserrat Alternates", sans-serif;
  font-size: 6px;
  font-weight: 700;
  left: 0;
  padding: 2px 1px;
  position: absolute;
  right: 0;
  text-align: center;
}

.gaoyi-name-recipient {
  display: grid;
  font-size: clamp(9px, 1.8cqw, 11px);
  gap: 5px;
  grid-template-columns: 34px minmax(0, 1fr);
  margin-top: 7px;
}

.gaoyi-name-recipient b {
  color: #3e6190;
  font-family: "Montserrat Alternates", sans-serif;
  font-size: clamp(8px, 1.55cqw, 9px);
}

.gaoyi-name-recipient span {
  border-bottom: 1px solid rgba(62, 97, 144, 0.55);
  min-width: 0;
  padding: 0 2px 2px;
}

.gaoyi-name-message {
  background-image: repeating-linear-gradient(
    to bottom,
    transparent 0,
    transparent 20px,
    rgba(62, 97, 144, 0.42) 20px,
    rgba(62, 97, 144, 0.42) 21px
  );
  color: #0c131b;
  font-size: clamp(9px, 1.85cqw, 11px);
  line-height: 21px;
  margin: 9px 0 0;
  min-height: 106px;
}

.gaoyi-name-signature {
  align-self: flex-end;
  display: block;
  height: 31px;
  margin-top: auto;
  object-fit: contain;
  opacity: 0.8;
  width: 92px;
}

@media (prefers-reduced-motion: reduce) {
  .gaoyi-name-story { transition: none !important; }
}
</style>
<script data-gaoyi-name-story>
(() => {
  const install = () => document
    .querySelectorAll('[data-framer-name="A5 postcard"]')
    .forEach((card) => {
      if (card.dataset.gaoyiNameStoryReady) return;
      const base = card.querySelector('[data-framer-name="Rectangle 1"]');
      if (!base) return;

      card.dataset.gaoyiNameStoryReady = "true";
      card.classList.add("gaoyi-name-story-ready");
      card.setAttribute("role", "dialog");
      card.setAttribute("aria-modal", "true");
      card.setAttribute("aria-label", "The story behind the name Gaoyi Wu");

      const story = document.createElement("div");
      story.className = "gaoyi-name-story";
      story.innerHTML = `
        <div class="gaoyi-name-story-frame">
          <section class="gaoyi-name-story-left" aria-label="Chinese name meaning">
            <p class="gaoyi-name-story-kicker">From my Chinese name, <strong>吴高艺</strong></p>
            <div class="gaoyi-name-characters">
              <div class="gaoyi-name-character">
                <span class="gaoyi-name-character-glyph">吴</span>
                <span class="gaoyi-name-character-copy"><strong>WU</strong><span>my family name</span></span>
              </div>
              <div class="gaoyi-name-character">
                <span class="gaoyi-name-character-glyph">高</span>
                <span class="gaoyi-name-character-copy"><strong>GAO</strong><span>high, aspiring upward</span></span>
              </div>
              <div class="gaoyi-name-character">
                <span class="gaoyi-name-character-glyph">艺</span>
                <span class="gaoyi-name-character-copy"><strong>YI</strong><span>art, craft, skill</span></span>
              </div>
            </div>
            <div class="gaoyi-name-process" aria-label="How the seal mark was formed">
              <div class="gaoyi-name-process-step"><strong>COMPOSE</strong>Stack the three characters into a compact seal.</div>
              <span class="gaoyi-name-process-arrow" aria-hidden="true">→</span>
              <div class="gaoyi-name-process-step"><strong>REFINE</strong>Simplify the strokes into one balanced mark.</div>
              <span class="gaoyi-name-process-arrow" aria-hidden="true">→</span>
              <div class="gaoyi-name-seal-result">
                <img src="/assets/style-kit/frames/gaoyi-wu-wax-seal.svg" alt="Gaoyi Wu silver wax seal">
                <span>finished in silver wax</span>
              </div>
            </div>
            <div class="gaoyi-name-interpretation">
              <strong>WHAT IT MEANS TO ME</strong>
              <p>Stay rooted. Keep aiming higher. Treat every AI system as a craft built with care.</p>
            </div>
          </section>
          <section class="gaoyi-name-story-right" aria-label="A note from Gaoyi Wu">
            <div class="gaoyi-name-stamp-row">
              <span class="gaoyi-name-postmark" aria-hidden="true"></span>
              <div class="gaoyi-name-stamp">
                <div class="gaoyi-name-stamp-inner">
                  <img src="/assets/gaoyi-wu-portrait-red.png" alt="Portrait of Gaoyi Wu">
                  <span>HOBOKEN, NJ</span>
                </div>
              </div>
            </div>
            <div class="gaoyi-name-recipient">
              <b>From:</b><span>Gaoyi Wu / 吴高艺</span>
              <b>To:</b><span>Curious Reader</span>
            </div>
            <p class="gaoyi-name-message">I'm an AI/ML engineer building secure, measurable systems from research ideas. My name reminds me to stay grounded, aim higher, and respect the craft.</p>
            <img class="gaoyi-name-signature" src="/assets/style-kit/frames/gaoyi-wu-signature.svg" alt="Gaoyi Wu signature">
          </section>
        </div>`;

      const syncGeometry = () => {
        story.style.left = `${base.offsetLeft}px`;
        story.style.top = `${base.offsetTop}px`;
        story.style.width = `${base.offsetWidth}px`;
        story.style.height = `${base.offsetHeight}px`;
        story.style.transform = base.style.transform || "rotate(90deg)";
      };

      syncGeometry();
      card.append(story);
      requestAnimationFrame(syncGeometry);
      window.setTimeout(syncGeometry, 250);
      window.setTimeout(syncGeometry, 700);
    });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", install, { once: true });
  } else {
    install();
  }
  new MutationObserver(install).observe(document.documentElement, {
    childList: true,
    subtree: true,
  });
})();
</script>
"""
    return html.replace("</head>", style_and_script + "</head>")


def inject_polaroid_repair(html: str) -> str:
    """Replace Framer's unstable Polaroid photo layer with a durable local one."""
    style_and_script = """
<style data-gaoyi-polaroid-repair>
[data-framer-name="Polaroid 📸"] [data-framer-name^="Picture"] {
  visibility: hidden !important;
  pointer-events: none !important;
}
[data-framer-name="Polaroid 📸"] [data-framer-name="Polaroid Camera"] {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
  overflow: visible !important;
}
[data-framer-name="Polaroid 📸"] [data-framer-name="Polaroid Camera"] > [data-framer-background-image-wrapper] {
  display: none !important;
}
[data-framer-name="Polaroid 📸"] [data-framer-name="Turn on sound"] {
  display: none !important;
}
[data-framer-name="Polaroid 📸"] [data-framer-name="polaroid_shadow"] {
  display: none !important;
}
.gaoyi-polaroid-camera-cutout {
  display: block;
  width: 125%;
  height: 125%;
  max-width: none;
  object-fit: contain;
  clip-path: inset(0 0 31% 0);
  -webkit-mask-image: linear-gradient(to bottom, #000 0 62%, transparent 69%);
  mask-image: linear-gradient(to bottom, #000 0 62%, transparent 69%);
  pointer-events: none;
  user-select: none;
  position: absolute;
  inset: -12.5%;
  z-index: 1;
}
.gaoyi-polaroid-photo {
  --drag-x: 0px;
  --drag-y: 0px;
  --rotation: 0deg;
  position: absolute;
  width: 112px;
  padding: 6px 6px 24px;
  background: #fff;
  box-shadow: 0 7px 16px rgba(12, 19, 27, 0.22);
  cursor: grab;
  opacity: 0;
  pointer-events: none;
  transform: translate(var(--drag-x), calc(var(--drag-y) - 12px)) rotate(var(--rotation));
  transition: opacity 260ms ease, transform 360ms cubic-bezier(.2, .8, .2, 1);
  user-select: none;
  z-index: 6;
}
.gaoyi-polaroid-photo.is-visible {
  opacity: 1;
  pointer-events: auto;
  transform: translate(var(--drag-x), var(--drag-y)) rotate(var(--rotation));
}
.gaoyi-polaroid-photo:active { cursor: grabbing; }
.gaoyi-polaroid-photo img {
  display: block;
  width: 100%;
  aspect-ratio: 1 / 1;
  object-fit: cover;
}
.gaoyi-polaroid-photo-1 { left: -76px; top: 120px; --rotation: -9deg; }
.gaoyi-polaroid-photo-2 { left: 63px; top: 132px; --rotation: 7deg; }
.gaoyi-polaroid-photo-3 { left: -7px; top: 204px; --rotation: 2deg; }
.gaoyi-polaroid-photo-2 img { object-position: center 62%; }
</style>
<script data-gaoyi-polaroid-repair>
(() => {
  const photoSources = [
    "/assets/gaoyi-wu-portrait-studio.jpg",
    "/assets/gaoyi-wu-highline.jpg",
    "/assets/gaoyi-wu-portrait-red.png",
  ];
  const install = () => document.querySelectorAll('[data-framer-name="Polaroid 📸"]').forEach((root) => {
    if (root.dataset.gaoyiPolaroidReady) return;
    root.dataset.gaoyiPolaroidReady = "true";
    const camera = root.querySelector('[data-framer-name="Polaroid Camera"]');
    if (camera) {
      const cameraImage = document.createElement("img");
      cameraImage.className = "gaoyi-polaroid-camera-cutout";
      cameraImage.src = "/assets/gaoyi-polaroid-camera-cutout.png";
      cameraImage.alt = "Polaroid camera";
      camera.append(cameraImage);
    }
    const photos = Array.from({ length: 3 }, (_, index) => {
      const photo = document.createElement("div");
      photo.className = `gaoyi-polaroid-photo gaoyi-polaroid-photo-${index + 1}`;
      const image = document.createElement("img");
      image.src = photoSources[index];
      image.alt = `Gaoyi Wu photo ${index + 1}`;
      photo.append(image);
      root.append(photo);
      let startX = 0;
      let startY = 0;
      let offsetX = 0;
      let offsetY = 0;
      photo.addEventListener("pointerdown", (event) => {
        startX = event.clientX;
        startY = event.clientY;
        photo.setPointerCapture(event.pointerId);
      });
      photo.addEventListener("pointermove", (event) => {
        if (!photo.hasPointerCapture(event.pointerId)) return;
        photo.style.setProperty("--drag-x", `${offsetX + event.clientX - startX}px`);
        photo.style.setProperty("--drag-y", `${offsetY + event.clientY - startY}px`);
      });
      photo.addEventListener("pointerup", (event) => {
        if (!photo.hasPointerCapture(event.pointerId)) return;
        offsetX += event.clientX - startX;
        offsetY += event.clientY - startY;
        photo.releasePointerCapture(event.pointerId);
      });
      return photo;
    });
    let revealed = 0;
    root.addEventListener("click", (event) => {
      if (event.target.closest(".gaoyi-polaroid-photo") || revealed >= photos.length) return;
      photos[revealed++].classList.add("is-visible");
    });
  });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", install, { once: true });
  else install();
  new MutationObserver(install).observe(document.documentElement, { childList: true, subtree: true });
})();
</script>
"""
    return html.replace("</head>", style_and_script + "</head>")


def inject_about_camera_portrait(html: str) -> str:
    """Replace the baked-in camera LCD photo with Gaoyi's portrait."""
    style_and_script = """
<style data-gaoyi-about-camera-portrait>
.framer-t5xm7h .framer-cs9esv { isolation: isolate; }
/* Remove the separate tilted portrait beneath the camera. */
.framer-t5xm7h > .framer-ma6zvg { display: none !important; }
.gaoyi-camera-screen-portrait {
  position: absolute;
  left: 16.2%;
  top: 40%;
  width: 43%;
  height: 32.4%;
  background: #d6dfec;
  border-radius: 1px;
  display: block;
  object-fit: cover;
  object-position: center 22%;
  opacity: 1 !important;
  pointer-events: none;
  z-index: 3;
}
</style>
<script data-gaoyi-about-camera-portrait>
(() => {
  const install = () => document.querySelectorAll(".framer-t5xm7h").forEach((cameraMount) => {
    if (cameraMount.querySelector(".gaoyi-camera-screen-portrait")) return;
    const cameraImage = cameraMount.querySelector(".framer-cs9esv");
    if (!cameraImage) return;
    const portrait = document.createElement("img");
    portrait.className = "gaoyi-camera-screen-portrait";
    portrait.src = "/assets/gaoyi-wu-portrait-red.png";
    portrait.alt = "Gaoyi Wu";
    cameraImage.append(portrait);
  });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", install, { once: true });
  else install();
  new MutationObserver(install).observe(document.documentElement, { childList: true, subtree: true });
})();
</script>
"""
    return html.replace("</head>", style_and_script + "</head>")


def inject_hero_anime_greeting(html: str) -> str:
    """Play Gaoyi's greeting inside the iMac screen on hover."""
    style_and_script = """
<style data-gaoyi-hero-anime-greeting>
video[src*="f8ZstgA2nyWGgUD7VIBQvCcdI"],
video[src*="f8ZstgA2nyWGgUD7VIBQvCcdI"] + img { opacity: 0 !important; }
.framer-gpno9v-container > [data-gaoyi-anime-greeting-ready="true"] {
  background: transparent !important;
}
.framer-LdH77 .framer-nsa3d0,
.framer-LdH77 .framer-1o5ndwv {
  overflow: visible !important;
}
.gaoyi-anime-greeting {
  background: transparent;
  cursor: pointer;
  display: block;
  inset: 0;
  overflow: hidden;
  pointer-events: auto;
  position: absolute;
  z-index: 3;
}
@media (min-width: 1200px) {
  [data-gaoyi-hero-media] {
    translate: clamp(32px, 3vw, 48px) 0;
  }
}
.gaoyi-imac-shell {
  display: block;
  height: 100%;
  object-fit: cover;
  pointer-events: none;
  position: absolute;
  width: 100%;
}
.gaoyi-anime-screen {
  background: #171717 url("/assets/gaoyi-wu-hero-wave-poster.jpg") center / cover no-repeat;
  border-radius: 3.5% 3.5% 3% 3%;
  inset: 15.8% 33.8% 45% 30.4%;
  overflow: hidden;
  position: absolute;
  transform: translateZ(0);
  z-index: 1;
}
.gaoyi-anime-screen::after {
  background: rgba(235, 250, 255, 0.9);
  content: "";
  inset: 0;
  opacity: 0;
  pointer-events: none;
  position: absolute;
  z-index: 2;
}
.gaoyi-anime-screen .gaoyi-anime-poster {
  display: block;
  height: 100%;
  object-fit: cover;
  object-position: center;
  opacity: 1;
  position: absolute;
  transition: opacity 160ms ease;
  width: 100%;
}
.gaoyi-anime-screen video {
  display: block;
  filter: blur(0);
  height: 100%;
  object-fit: cover;
  object-position: center;
  opacity: 0;
  transition: opacity 160ms ease;
  pointer-events: none;
  transform: scale(1);
  width: 100%;
}
.gaoyi-anime-greeting.is-playing .gaoyi-anime-screen .gaoyi-anime-poster {
  opacity: 0;
}
.gaoyi-anime-greeting.is-playing .gaoyi-anime-screen video {
  opacity: 1;
}
.gaoyi-anime-greeting.is-booting .gaoyi-anime-screen::after {
  animation: gaoyi-screen-flash 460ms cubic-bezier(.18, .78, .25, 1) both;
}
.gaoyi-anime-greeting.is-booting .gaoyi-anime-screen video {
  animation: gaoyi-screen-resolve 620ms cubic-bezier(.18, .78, .25, 1) both;
}
@keyframes gaoyi-screen-flash {
  0% { opacity: 0; }
  30% { opacity: .88; }
  100% { opacity: 0; }
}
@keyframes gaoyi-screen-resolve {
  0% { filter: blur(12px) brightness(1.35); transform: scale(1.08); }
  48% { filter: blur(4px) brightness(1.14); }
  100% { filter: blur(0); transform: scale(1); }
}
@media (prefers-reduced-motion: reduce) {
  .gaoyi-anime-greeting.is-booting .gaoyi-anime-screen::after,
  .gaoyi-anime-greeting.is-booting .gaoyi-anime-screen video { animation: none; }
}
</style>
<script data-gaoyi-hero-anime-greeting>
(() => {
  const videoId = "f8ZstgA2nyWGgUD7VIBQvCcdI";
  const install = () => document.querySelectorAll(`video[src*="${videoId}"]`).forEach((video) => {
    const mount = video.parentElement;
    if (!mount || mount.dataset.gaoyiAnimeGreetingReady) return;
    mount.dataset.gaoyiAnimeGreetingReady = "true";
    if (mount.parentElement) mount.parentElement.dataset.gaoyiHeroMedia = "true";
    const greeting = document.createElement("div");
    greeting.className = "gaoyi-anime-greeting";
    const shell = document.createElement("img");
    shell.className = "gaoyi-imac-shell";
    shell.src = "/assets/imac-g3-frame-cutout.png";
    shell.alt = "";
    const screen = document.createElement("div");
    screen.className = "gaoyi-anime-screen";
    const poster = document.createElement("img");
    poster.className = "gaoyi-anime-poster";
    poster.src = "/assets/gaoyi-wu-hero-wave-poster.jpg";
    poster.alt = "";
    const greetingVideo = document.createElement("video");
    greetingVideo.src = "/assets/gaoyi-wu-hero-wave.mp4";
    greetingVideo.poster = "/assets/gaoyi-wu-hero-wave-poster.jpg";
    greetingVideo.muted = true;
    greetingVideo.defaultMuted = true;
    greetingVideo.autoplay = false;
    greetingVideo.removeAttribute("autoplay");
    greetingVideo.loop = true;
    greetingVideo.playsInline = true;
    greetingVideo.preload = "auto";
    greetingVideo.setAttribute("aria-label", "Gaoyi Wu waving");
    screen.append(poster, greetingVideo);
    greeting.append(shell, screen);
    const startGreeting = () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
      if (greeting.classList.contains("is-playing")) return;
      greeting.classList.remove("is-booting");
      greetingVideo.currentTime = 0;
      requestAnimationFrame(() => greeting.classList.add("is-booting"));
      greetingVideo.play().catch(() => {});
    };
    const stopGreeting = () => {
      greeting.classList.remove("is-playing");
      greeting.classList.remove("is-booting");
      greetingVideo.pause();
      greetingVideo.currentTime = 0;
    };
    greetingVideo.addEventListener("playing", () => greeting.classList.add("is-playing"));
    greeting.addEventListener("pointerenter", startGreeting);
    greeting.addEventListener("pointerover", startGreeting);
    greeting.addEventListener("mouseenter", startGreeting);
    greeting.addEventListener("pointerleave", stopGreeting);
    greeting.addEventListener("focusin", startGreeting);
    greeting.addEventListener("focusout", stopGreeting);
    mount.append(greeting);
  });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", install, { once: true });
  else install();
  new MutationObserver(install).observe(document.documentElement, { childList: true, subtree: true });
})();
</script>
"""
    return html.replace("</head>", style_and_script + "</head>")


def inject_hero_previous_logos_cleanup(html: str) -> str:
    """Keep the hero's selected previous-work logos clean and legible."""
    style_and_script = """
<style data-gaoyi-hero-previous-logos>
/* The former Museum of Flight mark is not part of Gaoyi's experience. */
.framer-LdH77 .framer-1ebljle > a.framer-95ddia.framer-lux5qc {
  display: none !important;
}
.framer-LdH77 .framer-1ebljle > .framer-1e8z3a0 {
  display: none !important;
}

.framer-LdH77 .framer-1ebljle {
  gap: 20px !important;
  justify-content: flex-start !important;
  white-space: nowrap !important;
}
.framer-LdH77 .framer-1ebljle > a.framer-1i4obf4.framer-lux5qc,
.framer-LdH77 .framer-1ebljle > .framer-woez5z {
  margin-right: 0 !important;
}
.framer-LdH77 .framer-1ebljle > a.framer-1i4obf4.framer-lux5qc img,
.framer-LdH77 .framer-1ebljle > a.framer-1c478o.framer-lux5qc img {
  object-fit: contain !important;
  object-position: center !important;
}

@media (max-width: 809.98px) {
  .framer-LdH77 .framer-1ebljle {
    gap: 6px !important;
  }
}
</style>
<script data-gaoyi-hero-previous-logo-links>
(() => {
  const destinations = {
    ".framer-1i4obf4.framer-lux5qc": "https://intellisys.haow.us/",
    ".framer-1c478o.framer-lux5qc": "https://www.dhl.com/us-en/home/express.html#fs-step=connectors",
  };
  const bindLinks = () => document.querySelectorAll(".framer-LdH77 .framer-1ebljle > a").forEach((anchor) => {
    const destination = Object.entries(destinations)
      .find(([selector]) => anchor.matches(selector))?.[1];
    if (!destination) return;
    anchor.href = destination;
    anchor.target = "_blank";
    anchor.rel = "noopener";
  });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", bindLinks, { once: true });
  else bindLinks();
  new MutationObserver(bindLinks).observe(document.documentElement, { childList: true, subtree: true });
})();
</script>
"""
    return html.replace("</head>", style_and_script + "</head>")


def remove_applied_ai_notes_links(html: str) -> str:
    """Keep the Applied AI Notes collage presentation-only in the initial HTML."""
    soup = BeautifulSoup(html, "html.parser")
    section = soup.find("section", attrs={"data-framer-name": "ai Section"})
    if not section:
        return html

    for anchor in section.find_all("a"):
        for attribute in ("href", "target", "rel", "as"):
            anchor.attrs.pop(attribute, None)
        anchor["aria-disabled"] = "true"

    for image in section.find_all("img"):
        source = image.get("src", "")
        if "9PiMNrI5x9DO4A1LiMz6f6BAK2c.png" not in source:
            continue
        image["src"] = "/assets/projects/prediction-router-search-v2.webp"
        image["alt"] = "Mantis prediction-market search workspace"
        image.attrs.pop("srcset", None)
        image.attrs.pop("sizes", None)
    return str(soup)


def inject_project_preview_image_repair(html: str) -> str:
    """Keep Framer's hover-only project previews backed by local assets."""
    style_and_script = """
<script data-gaoyi-project-preview-images>
(() => {
  const sourceFallbacks = {
    "rnSNcUt7AARtRxfQlOMi5CdyF2M.png": "/assets/projects/xclaw-dashboard.webp",
    "yYHAJfe5mnD3HJq2JUhf8foM5g.png": "/assets/about/xclaw-account.webp",
    "ipvYobD6R5gwDM75HADMY4uXqIU.png": "/assets/projects/iseal-pipeline.webp",
    "UHIhF5z0rCwMx3ofY9ZhMuKAQ.png": "/assets/projects/iseal-results.webp",
    "F88Oars6dEz3rF4fRVs49pXXZ0A.png": "/assets/about/iseal-resistance.webp",
    "YUrWrQt3EBxwiGpWsUxWaKcc6f0.png": "/assets/about/iseal-sensitivity.webp",
    "1a9rvLhWMUC8kGTkDqBieE6uy4.png": "/assets/projects/webweaver-topology.webp",
    "xiKhH2uMtRLq6aJ7o5lTKyc3I.png": "/assets/projects/webweaver-robustness.webp",
    "KaHyfkp6ALRteyeSGid06gOCEzU.png": "/assets/projects/webweaver-reconstruction.webp",
  };
  const cardFallback = (image) => {
    const cardText = image.closest('[data-framer-name="Work 1"]')?.textContent || "";
    if (cardText.includes("XClaw")) return "/assets/projects/xclaw-dashboard.webp";
    if (cardText.includes("iSeal")) return "/assets/projects/iseal-pipeline.webp";
    if (cardText.includes("WebWeaver")) return "/assets/projects/webweaver-topology.webp";
    return null;
  };
  const repairProjectPreviews = () => document
    .querySelectorAll('[data-framer-name="Work section"] img')
    .forEach((image) => {
      image.loading = "eager";
      if (image.dataset.gaoyiProjectPreviewReady) return;
      image.dataset.gaoyiProjectPreviewReady = "true";
      image.addEventListener("error", () => {
        const source = image.getAttribute("src") || "";
        const fallback = Object.entries(sourceFallbacks)
          .find(([filename]) => source.includes(filename))?.[1] || cardFallback(image);
        if (!fallback || image.dataset.gaoyiProjectFallback === fallback) return;
        image.dataset.gaoyiProjectFallback = fallback;
        image.removeAttribute("srcset");
        image.src = fallback;
      });
    });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", repairProjectPreviews, { once: true });
  else repairProjectPreviews();
  new MutationObserver(repairProjectPreviews).observe(document.documentElement, { childList: true, subtree: true });
})();
</script>
"""
    return html.replace("</head>", style_and_script + "</head>")


def inject_xclaw_project_art(html: str) -> str:
    """Turn the XClaw card into a product-led, editorial screenshot collage."""
    style_and_script = """
<style data-gaoyi-xclaw-project-art>
[data-gaoyi-xclaw-card] {
  cursor: pointer !important;
  isolation: isolate;
  overflow: hidden !important;
  background: #e9edef !important;
}

[data-gaoyi-xclaw-card] > [data-gaoyi-xclaw-content] {
  position: absolute !important;
  inset: 0 !important;
  z-index: 5 !important;
  display: block !important;
  width: 100% !important;
  height: 100% !important;
  padding: 34px 38px !important;
  pointer-events: none !important;
  box-sizing: border-box !important;
  opacity: 0 !important;
  visibility: hidden !important;
  transform: none !important;
}

[data-gaoyi-xclaw-card] [data-gaoyi-xclaw-legacy-art] {
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
}

[data-gaoyi-xclaw-card] [data-gaoyi-xclaw-title] {
  position: relative !important;
  z-index: 6 !important;
  width: 38% !important;
  max-width: 300px !important;
  height: auto !important;
  margin: 0 !important;
}

[data-gaoyi-xclaw-card] [data-gaoyi-xclaw-title] h1,
[data-gaoyi-xclaw-card] [data-gaoyi-xclaw-title] h2,
[data-gaoyi-xclaw-card] [data-gaoyi-xclaw-title] h3 {
  margin: 0 !important;
  font-size: 30px !important;
  line-height: 1.08 !important;
  text-align: left !important;
  color: #111820 !important;
}

[data-gaoyi-xclaw-card] [data-gaoyi-xclaw-subtitle] {
  position: relative !important;
  z-index: 6 !important;
  width: 36% !important;
  max-width: 286px !important;
  height: auto !important;
  margin: 13px 0 0 !important;
}

[data-gaoyi-xclaw-card] [data-gaoyi-xclaw-subtitle] p {
  margin: 0 !important;
  font-size: 15px !important;
  line-height: 1.45 !important;
  text-align: left !important;
  color: rgba(17, 24, 32, 0.62) !important;
}

[data-gaoyi-xclaw-card] [data-gaoyi-xclaw-meta] {
  display: none !important;
}

.gaoyi-xclaw-copy {
  position: absolute;
  top: 34px;
  left: 38px;
  z-index: 6;
  width: 292px;
  pointer-events: none;
}

.gaoyi-xclaw-copy h3 {
  margin: 0;
  color: #111820;
  font-family: "Inter Display", "Inter", sans-serif;
  font-size: 30px;
  font-weight: 500;
  line-height: 1.08;
  text-align: left;
}

.gaoyi-xclaw-copy p {
  margin: 13px 0 0;
  color: rgba(17, 24, 32, 0.62);
  font-family: "Inter", sans-serif;
  font-size: 15px;
  line-height: 1.45;
  text-align: left;
  white-space: normal;
}

.gaoyi-xclaw-card-art {
  position: absolute;
  inset: 0;
  z-index: 1;
  width: 100%;
  height: 100%;
  overflow: hidden;
  border-radius: inherit;
  pointer-events: none;
}

.gaoyi-xclaw-card-art::before {
  content: "";
  position: absolute;
  right: -7%;
  bottom: -26%;
  width: 78%;
  height: 94%;
  border: 1px solid rgba(255, 255, 255, 0.92);
  border-radius: 12px;
  background: #f5f6f5;
  box-shadow: 0 22px 55px rgba(38, 48, 56, 0.1);
  transform: rotate(-3.5deg);
}

.gaoyi-xclaw-paper {
  position: absolute;
  overflow: visible;
  padding: 8px 8px 22px;
  border: 1px solid rgba(24, 34, 43, 0.1);
  border-radius: 7px;
  background: #fbfbfa;
  box-shadow:
    0 18px 38px rgba(32, 44, 53, 0.17),
    0 3px 8px rgba(32, 44, 53, 0.08);
  box-sizing: border-box;
  transition:
    transform 760ms cubic-bezier(0.22, 1, 0.36, 1),
    box-shadow 760ms cubic-bezier(0.22, 1, 0.36, 1);
}

.gaoyi-xclaw-paper::before {
  content: "";
  position: absolute;
  top: -10px;
  left: 50%;
  z-index: 3;
  width: 54px;
  height: 18px;
  border: 1px solid rgba(156, 132, 76, 0.1);
  background: rgba(238, 222, 178, 0.82);
  box-shadow: 0 2px 4px rgba(76, 68, 48, 0.08);
  transform: translateX(-50%) rotate(-2deg);
}

.gaoyi-xclaw-paper--dashboard {
  right: 18%;
  bottom: -13%;
  z-index: 1;
  width: 59%;
  height: 75%;
  transform: rotate(-2.8deg);
}

.gaoyi-xclaw-paper--chat {
  right: -2.5%;
  bottom: -9%;
  z-index: 2;
  width: 37%;
  height: 68%;
  transform: rotate(3.6deg);
}

.gaoyi-xclaw-paper--chat::before {
  left: 58%;
  background: rgba(205, 224, 227, 0.86);
  transform: translateX(-50%) rotate(4deg);
}

.gaoyi-xclaw-paper img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top left;
  border: 1px solid rgba(24, 34, 43, 0.08);
  border-radius: 3px;
  background: #f8fafb;
  box-sizing: border-box;
}

[data-gaoyi-xclaw-card]:hover .gaoyi-xclaw-paper--dashboard,
[data-gaoyi-xclaw-card]:focus-within .gaoyi-xclaw-paper--dashboard {
  transform: translate(-8px, -13px) rotate(-1.4deg);
  box-shadow:
    0 24px 48px rgba(32, 44, 53, 0.2),
    0 4px 10px rgba(32, 44, 53, 0.08);
}

[data-gaoyi-xclaw-card]:hover .gaoyi-xclaw-paper--chat,
[data-gaoyi-xclaw-card]:focus-within .gaoyi-xclaw-paper--chat {
  transform: translate(-6px, -18px) rotate(2.1deg);
  box-shadow:
    0 26px 52px rgba(32, 44, 53, 0.22),
    0 4px 10px rgba(32, 44, 53, 0.08);
}

[data-gaoyi-xclaw-card] > [data-gaoyi-xclaw-marker] {
  position: absolute;
  z-index: 7;
  opacity: 0;
  filter: blur(4px);
  scale: 0.82;
  translate: 0 12px;
  pointer-events: none;
  transition:
    opacity 320ms ease calc(var(--gaoyi-xclaw-marker-index, 0) * 70ms),
    filter 500ms ease calc(var(--gaoyi-xclaw-marker-index, 0) * 70ms),
    scale 620ms cubic-bezier(0.22, 1, 0.36, 1) calc(var(--gaoyi-xclaw-marker-index, 0) * 70ms),
    translate 620ms cubic-bezier(0.22, 1, 0.36, 1) calc(var(--gaoyi-xclaw-marker-index, 0) * 70ms);
}

[data-gaoyi-xclaw-card]:hover > [data-gaoyi-xclaw-marker],
[data-gaoyi-xclaw-card]:focus-within > [data-gaoyi-xclaw-marker] {
  opacity: 1;
  filter: blur(0);
  scale: 1;
  translate: 0 0;
}

.gaoyi-xclaw-marker--sticker {
  width: 72px;
  height: 72px;
  transform: rotate(var(--gaoyi-xclaw-sticker-rotation, 0deg));
}

.gaoyi-xclaw-marker--sticker img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: contain;
  filter: drop-shadow(0 8px 10px rgba(32, 44, 53, 0.14));
}

.gaoyi-xclaw-marker--orchestration {
  top: 24px;
  left: 50%;
  --gaoyi-xclaw-sticker-rotation: -6deg;
}

.gaoyi-xclaw-marker--tool-calling {
  top: 126px;
  left: 35%;
  width: 68px;
  height: 68px;
  --gaoyi-xclaw-sticker-rotation: 5deg;
}

.gaoyi-xclaw-marker--model-routing {
  top: 88px;
  right: 19%;
  width: 76px;
  height: 76px;
  --gaoyi-xclaw-sticker-rotation: 7deg;
}

.gaoyi-xclaw-marker--channels {
  bottom: 20px;
  left: 43%;
  width: 84px;
  height: 84px;
  --gaoyi-xclaw-sticker-rotation: -4deg;
}

.gaoyi-xclaw-marker--cron {
  top: 126px;
  right: 3.5%;
  width: 70px;
  height: 70px;
  --gaoyi-xclaw-sticker-rotation: 5deg;
}

.gaoyi-xclaw-marker--desktop {
  right: 3%;
  bottom: 18px;
  width: 88px;
  height: 88px;
  --gaoyi-xclaw-sticker-rotation: -3deg;
}

.gaoyi-xclaw-marker--brand {
  top: 25px;
  right: 30px;
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 7px 10px 7px 8px;
  border: 1px solid rgba(24, 34, 43, 0.16);
  border-radius: 4px;
  background: #fffefd;
  box-shadow: 0 10px 20px rgba(32, 44, 53, 0.14);
  transform: rotate(5deg);
  color: #171d22;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 12px;
  font-weight: 700;
}

.gaoyi-xclaw-marker--brand img {
  display: block;
  width: 28px;
  height: 28px;
  object-fit: contain;
}

.gaoyi-xclaw-marker--note {
  bottom: 20px;
  left: 26px;
  padding: 9px 13px;
  background: #fff9d9;
  box-shadow: 0 10px 20px rgba(32, 44, 53, 0.13);
  clip-path: polygon(2% 9%, 98% 0, 100% 88%, 3% 100%);
  transform: rotate(-4deg);
  color: rgba(17, 24, 32, 0.74);
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 11px;
  line-height: 1.2;
}

@media (max-width: 809.98px) {
  [data-gaoyi-xclaw-card] > [data-gaoyi-xclaw-content] {
    padding: 24px 24px !important;
  }

  [data-gaoyi-xclaw-card] [data-gaoyi-xclaw-title],
  [data-gaoyi-xclaw-card] [data-gaoyi-xclaw-subtitle] {
    width: 100% !important;
    max-width: 310px !important;
  }

  [data-gaoyi-xclaw-card] [data-gaoyi-xclaw-title] h1,
  [data-gaoyi-xclaw-card] [data-gaoyi-xclaw-title] h2,
  [data-gaoyi-xclaw-card] [data-gaoyi-xclaw-title] h3 {
    font-size: 25px !important;
  }

  [data-gaoyi-xclaw-card] [data-gaoyi-xclaw-subtitle] p {
    font-size: 14px !important;
  }

  .gaoyi-xclaw-copy {
    top: 24px;
    left: 24px;
    width: 300px;
    max-width: calc(100% - 48px);
  }

  .gaoyi-xclaw-copy h3 {
    font-size: 25px;
  }

  .gaoyi-xclaw-copy p {
    margin-top: 10px;
    font-size: 14px;
  }

  .gaoyi-xclaw-card-art::before {
    right: -18%;
    bottom: -20%;
    width: 102%;
    height: 73%;
  }

  .gaoyi-xclaw-paper--dashboard {
    right: 19%;
    bottom: -8%;
    width: 72%;
    height: 56%;
  }

  .gaoyi-xclaw-paper--chat {
    right: -9%;
    bottom: -5%;
    width: 47%;
    height: 51%;
  }

  .gaoyi-xclaw-marker--brand {
    top: auto;
    right: 18px;
    bottom: 18px;
  }

  .gaoyi-xclaw-marker--note {
    display: none;
  }

  .gaoyi-xclaw-marker--sticker {
    width: 58px;
    height: 58px;
  }

  .gaoyi-xclaw-marker--orchestration {
    top: 118px;
    left: 24px;
  }

  .gaoyi-xclaw-marker--model-routing {
    top: 112px;
    right: 20px;
  }

  .gaoyi-xclaw-marker--channels {
    bottom: 16px;
    left: 24px;
  }

  .gaoyi-xclaw-marker--desktop {
    right: 18px;
    bottom: 15px;
    width: 64px;
    height: 64px;
  }

  .gaoyi-xclaw-marker--tool-calling,
  .gaoyi-xclaw-marker--cron {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gaoyi-xclaw-paper,
  [data-gaoyi-xclaw-card] > [data-gaoyi-xclaw-marker] {
    transition: none !important;
  }
}
</style>
<script data-gaoyi-xclaw-project-art>
(() => {
  const screenshotSources = [
    ["/assets/projects/xclaw-dashboard.webp", "XClaw dashboard showing gateway, skills, channels, and quick actions", "dashboard"],
    ["/assets/projects/xclaw-chat.webp", "XClaw desktop chat workspace", "chat"],
  ];

    const personalize = () => {
    const heading = Array.from(document.querySelectorAll("h1, h2, h3"))
      .find((node) => node.textContent?.trim() === "XClaw" && node.closest('[data-framer-name="Thumbnail"]'));
    const card = heading?.closest('[data-framer-name="Thumbnail"]');
    if (!heading || !card) return;

    const cardLink = card.closest("a[href]") || card.querySelector("a[href]");
    if (cardLink && cardLink.getAttribute("href") !== "https://www.x-claw.shop/") {
      cardLink.setAttribute("href", "https://www.x-claw.shop/");
    }
    if (cardLink) cardLink.setAttribute("aria-label", "View the XClaw project");

    if (!card.dataset.gaoyiXclawNavigationBound) {
      const openXclaw = (event) => {
        if (event.type === "click" && event.button !== 0) return;
        event.preventDefault();
        event.stopPropagation();
        event.stopImmediatePropagation();
        if (event.metaKey || event.ctrlKey) window.open("https://www.x-claw.shop/", "_blank", "noopener");
        else window.location.assign("https://www.x-claw.shop/");
      };
      card.addEventListener("click", openXclaw, true);
      card.addEventListener("keydown", (event) => {
        if (event.key !== "Enter" && event.key !== " ") return;
        openXclaw(event);
      }, true);
      card.dataset.gaoyiXclawNavigationBound = "true";
    }

    let content = heading;
    while (content.parentElement && content.parentElement !== card) content = content.parentElement;
    if (content.parentElement !== card) return;

    const contentChildren = Array.from(content.children);
    const titleBlock = contentChildren.find((child) => child.contains(heading));
    if (titleBlock) titleBlock.dataset.gaoyiXclawTitle = "true";

    const subtitle = Array.from(content.querySelectorAll("p"))
      .find((node) => node.textContent?.includes("A desktop workspace for coordinating"));
    if (subtitle) {
      let subtitleBlock = subtitle;
      while (subtitleBlock.parentElement && subtitleBlock.parentElement !== content) {
        subtitleBlock = subtitleBlock.parentElement;
      }
      if (subtitleBlock.parentElement === content) subtitleBlock.dataset.gaoyiXclawSubtitle = "true";
    }

    const metaBlock = contentChildren.find((child) => child.textContent?.includes("Agent Workflows"));
    if (metaBlock) metaBlock.dataset.gaoyiXclawMeta = "true";

    if (card.dataset.gaoyiXclawReady) return;

    card.dataset.gaoyiXclawReady = "true";
    card.dataset.gaoyiXclawCard = "true";
    content.dataset.gaoyiXclawContent = "true";

    Array.from(content.querySelectorAll("img"))
      .filter((image) => {
        const source = image.getAttribute("src") || "";
        return source.includes("xclaw-account") || source.includes("xclaw-dashboard");
      })
      .forEach((image) => {
        const legacyArt = image.closest("[data-framer-name]");
        if (legacyArt && content.contains(legacyArt)) legacyArt.dataset.gaoyiXclawLegacyArt = "true";
      });

    Array.from(card.children)
      .filter((child) => child !== content)
      .forEach((child) => child.dataset.gaoyiXclawLegacyArt = "true");

    const art = document.createElement("div");
    art.className = "gaoyi-xclaw-card-art";
    screenshotSources.forEach(([source, alt, name]) => {
      const paper = document.createElement("div");
      paper.className = `gaoyi-xclaw-paper gaoyi-xclaw-paper--${name}`;
      const image = document.createElement("img");
      image.src = source;
      image.alt = alt;
      image.loading = "eager";
      image.decoding = "async";
      paper.appendChild(image);
      art.appendChild(paper);
    });
    card.appendChild(art);

    content.setAttribute("aria-hidden", "true");
    const copy = document.createElement("div");
    copy.className = "gaoyi-xclaw-copy";
    const copyTitle = document.createElement("h3");
    copyTitle.textContent = "XClaw";
    const copyDescription = document.createElement("p");
    copyDescription.textContent = "A desktop workspace for coordinating agents, tools, models, and channels.";
    copy.append(copyTitle, copyDescription);
    card.appendChild(copy);

    const brand = document.createElement("div");
    brand.className = "gaoyi-xclaw-marker--brand";
    brand.dataset.gaoyiXclawMarker = "true";
    brand.style.setProperty("--gaoyi-xclaw-marker-index", "0");
    const brandIcon = document.createElement("img");
    brandIcon.src = "/assets/logos/xclaw-lobster.png";
    brandIcon.alt = "";
    brandIcon.setAttribute("aria-hidden", "true");
    const brandName = document.createElement("span");
    brandName.textContent = "XCLAW";
    brand.append(brandIcon, brandName);
    card.appendChild(brand);

    const note = document.createElement("div");
    note.className = "gaoyi-xclaw-marker--note";
    note.dataset.gaoyiXclawMarker = "true";
    note.style.setProperty("--gaoyi-xclaw-marker-index", "1");
    note.textContent = "agents  /  tools  /  channels";
    card.appendChild(note);

    const stickers = [
      ["/assets/projects/xclaw-stickers-generated/xclaw-sticker-agent-orchestration.png", "Agent orchestration", "orchestration"],
      ["/assets/projects/xclaw-stickers-generated/xclaw-sticker-tool-calling.png", "Tool calling", "tool-calling"],
      ["/assets/projects/xclaw-stickers-generated/xclaw-sticker-model-routing-v2.png", "Model routing", "model-routing"],
      ["/assets/projects/xclaw-stickers-generated/xclaw-sticker-channels-v2.png", "Communication channels", "channels"],
      ["/assets/projects/xclaw-stickers-generated/xclaw-sticker-cron-tasks.png", "Scheduled tasks", "cron"],
      ["/assets/projects/xclaw-stickers-generated/xclaw-sticker-desktop-automation.png", "Desktop automation", "desktop"],
    ];
    stickers.forEach(([source, alt, name], index) => {
      const sticker = document.createElement("div");
      sticker.className = `gaoyi-xclaw-marker--sticker gaoyi-xclaw-marker--${name}`;
      sticker.dataset.gaoyiXclawMarker = "true";
      sticker.style.setProperty("--gaoyi-xclaw-marker-index", String(index + 2));
      const image = document.createElement("img");
      image.src = source;
      image.alt = alt;
      image.loading = "eager";
      image.decoding = "async";
      sticker.appendChild(image);
      card.appendChild(sticker);
    });
  };

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", personalize, { once: true });
  else personalize();
  new MutationObserver(personalize).observe(document.documentElement, {
    childList: true,
    subtree: true,
    attributes: true,
    attributeFilter: ["href"],
  });
})();
</script>
"""
    return html.replace("</head>", style_and_script + "</head>")


def inject_webweaver_project_art(html: str) -> str:
    """Replace the inherited Museum collage with WebWeaver artwork and stickers."""
    style_and_script = f"""
<style data-gaoyi-webweaver-project-art>
[data-gaoyi-webweaver-card] {{
  cursor: pointer !important;
}}

[data-gaoyi-webweaver-card]:focus-visible {{
  outline: 3px solid rgba(47, 99, 224, 0.72) !important;
  outline-offset: 4px !important;
}}

[data-gaoyi-webweaver-card] > [data-gaoyi-webweaver-content] {{
  position: relative !important;
  z-index: 3 !important;
}}

[data-gaoyi-webweaver-card] [data-gaoyi-webweaver-legacy-art] {{
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
}}

[data-gaoyi-webweaver-card] > [data-gaoyi-webweaver-sticker] img {{
  object-fit: contain !important;
  object-position: center !important;
}}

[data-gaoyi-webweaver-card] > [data-gaoyi-webweaver-sticker] {{
  z-index: 2 !important;
  opacity: 0 !important;
  filter: blur(4px);
  scale: 0.8;
  translate: 0 14px;
  pointer-events: none !important;
  transition:
    opacity 360ms ease calc(var(--gaoyi-sticker-index, 0) * 55ms),
    filter 520ms ease calc(var(--gaoyi-sticker-index, 0) * 55ms),
    scale 620ms cubic-bezier(0.22, 1, 0.36, 1) calc(var(--gaoyi-sticker-index, 0) * 55ms),
    translate 620ms cubic-bezier(0.22, 1, 0.36, 1) calc(var(--gaoyi-sticker-index, 0) * 55ms) !important;
}}

[data-gaoyi-webweaver-card]:hover > [data-gaoyi-webweaver-sticker],
[data-gaoyi-webweaver-card]:focus-visible > [data-gaoyi-webweaver-sticker] {{
  opacity: 1 !important;
  filter: blur(0);
  scale: 1;
  translate: 0 0;
}}

.gaoyi-webweaver-card-art {{
  position: absolute;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1;
  height: 65%;
  overflow: hidden;
  border-radius: 0 0 24px 24px;
  pointer-events: none;
}}

.gaoyi-webweaver-card-art::before {{
  content: "";
  position: absolute;
  inset: 0;
  z-index: 1;
  background: linear-gradient(to bottom, rgba(245, 247, 255, 0.84) 0%, rgba(245, 247, 255, 0) 20%);
  pointer-events: none;
}}

.gaoyi-webweaver-card-art img {{
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 52%;
  transform: scale(1.015);
  transition: transform 700ms cubic-bezier(0.22, 1, 0.36, 1);
}}

[data-gaoyi-webweaver-card]:hover .gaoyi-webweaver-card-art img,
[data-gaoyi-webweaver-card]:focus-visible .gaoyi-webweaver-card-art img {{
  transform: scale(1.055) translateY(-2px);
}}

@media (max-width: 809.98px) {{
  .gaoyi-webweaver-card-art {{
    height: 61%;
    border-radius: 0 0 20px 20px;
  }}

  .gaoyi-webweaver-card-art img {{
    object-position: center 50%;
  }}
}}

@media (prefers-reduced-motion: reduce) {{
  .gaoyi-webweaver-card-art img,
  [data-gaoyi-webweaver-card] > [data-gaoyi-webweaver-sticker] {{
    transition: none !important;
  }}
}}
</style>
<script data-gaoyi-webweaver-project-art>
(() => {{
  const destination = "{WEBWEAVER_LINK}";
  const artSource = "/assets/projects/webweaver-card-collage.webp";
  const stickerSources = [
    ["/assets/projects/webweaver-sticker-traces.png", "WebWeaver communication traces"],
    ["/assets/projects/webweaver-sticker-magnifier.png", "WebWeaver topology inspection"],
    ["/assets/projects/webweaver-sticker-shield.png", "WebWeaver graph security"],
    ["/assets/projects/webweaver-sticker-reconstruction.png", "WebWeaver topology reconstruction"],
  ];

  const openPaper = () => window.open(destination, "_blank", "noopener,noreferrer");

  const personalize = () => {{
    const heading = Array.from(document.querySelectorAll("h1, h2, h3"))
      .find((node) => node.textContent?.includes("Built WebWeaver"));
    const card = heading?.closest('[data-framer-name="Thumbnail"]');
    if (!heading || !card || card.dataset.gaoyiWebweaverReady) return;

    let content = heading;
    while (content.parentElement && content.parentElement !== card) content = content.parentElement;
    if (content.parentElement !== card) return;

    card.dataset.gaoyiWebweaverReady = "true";
    card.dataset.gaoyiWebweaverCard = "true";
    card.setAttribute("role", "link");
    card.setAttribute("tabindex", "0");
    card.setAttribute("aria-label", "Read the WebWeaver paper on arXiv");
    content.dataset.gaoyiWebweaverContent = "true";

    const projectImages = Array.from(content.querySelectorAll("img"))
      .filter((image) => (image.getAttribute("src") || "").includes("webweaver-"));
    projectImages.forEach((image) => {{
      let legacyArt = image;
      while (legacyArt.parentElement && legacyArt.parentElement !== content) legacyArt = legacyArt.parentElement;
      if (legacyArt.parentElement === content) legacyArt.dataset.gaoyiWebweaverLegacyArt = "true";
    }});

    const stickers = Array.from(card.children).filter((child) => child !== content);
    stickers.slice(0, stickerSources.length).forEach((sticker, index) => {{
      const image = sticker.querySelector("img");
      if (!image) return;
      const [source, alt] = stickerSources[index];
      sticker.dataset.gaoyiWebweaverSticker = "true";
      sticker.style.setProperty("--gaoyi-sticker-index", String(index));
      image.removeAttribute("srcset");
      image.src = source;
      image.alt = alt;
    }});

    const art = document.createElement("div");
    art.className = "gaoyi-webweaver-card-art";
    const image = document.createElement("img");
    image.src = artSource;
    image.alt = "WebWeaver multi-agent topology inference collage";
    image.loading = "eager";
    image.decoding = "async";
    art.appendChild(image);
    card.appendChild(art);

    card.addEventListener("click", openPaper);
    card.addEventListener("keydown", (event) => {{
      if (event.key !== "Enter" && event.key !== " ") return;
      event.preventDefault();
      openPaper();
    }});
  }};

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", personalize, {{ once: true }});
  else personalize();
  new MutationObserver(personalize).observe(document.documentElement, {{ childList: true, subtree: true }});
}})();
</script>
"""
    return html.replace("</head>", style_and_script + "</head>")


def inject_iseal_project_art(html: str) -> str:
    """Turn the iSeal card into an editorial collage of real paper figures."""
    style_and_script = """
<style data-gaoyi-iseal-project-art>
[data-gaoyi-iseal-card] {
  cursor: pointer !important;
  isolation: isolate;
  overflow: hidden !important;
  background: #e8edea !important;
}

[data-gaoyi-iseal-card] > [data-gaoyi-iseal-content] {
  position: absolute !important;
  inset: 0 !important;
  z-index: 5 !important;
  width: 100% !important;
  height: 100% !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
}

[data-gaoyi-iseal-card] > [data-gaoyi-iseal-legacy-art] {
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
}

.gaoyi-iseal-copy {
  position: absolute;
  top: 34px;
  left: 38px;
  z-index: 6;
  width: 292px;
  pointer-events: none;
}

.gaoyi-iseal-copy h3 {
  margin: 0;
  color: #101b2d;
  font-family: "Inter Display", "Inter", sans-serif;
  font-size: 30px;
  font-weight: 500;
  line-height: 1.08;
  text-align: left;
}

.gaoyi-iseal-copy p {
  margin: 13px 0 0;
  color: rgba(16, 27, 45, 0.64);
  font-family: "Inter", sans-serif;
  font-size: 15px;
  line-height: 1.45;
  text-align: left;
  white-space: normal;
}

.gaoyi-iseal-card-art {
  position: absolute;
  inset: 0;
  z-index: 1;
  width: 100%;
  height: 100%;
  overflow: hidden;
  border-radius: inherit;
  pointer-events: none;
}

.gaoyi-iseal-card-art::before {
  content: "";
  position: absolute;
  right: -8%;
  bottom: -30%;
  width: 79%;
  height: 94%;
  border: 1px solid rgba(16, 27, 45, 0.09);
  border-radius: 8px;
  background: #f5f7f4;
  box-shadow: 0 22px 54px rgba(35, 53, 47, 0.1);
  transform: rotate(2.4deg);
}

.gaoyi-iseal-paper {
  position: absolute;
  padding: 9px 9px 25px;
  border: 1px solid rgba(16, 27, 45, 0.12);
  border-radius: 7px;
  background: #fffefd;
  box-shadow:
    0 18px 38px rgba(35, 53, 47, 0.16),
    0 3px 8px rgba(35, 53, 47, 0.08);
  box-sizing: border-box;
  transition:
    transform 760ms cubic-bezier(0.22, 1, 0.36, 1),
    box-shadow 760ms cubic-bezier(0.22, 1, 0.36, 1);
}

.gaoyi-iseal-paper::before {
  content: "";
  position: absolute;
  top: -10px;
  left: 50%;
  z-index: 3;
  width: 58px;
  height: 18px;
  border: 1px solid rgba(118, 105, 70, 0.1);
  background: rgba(232, 218, 174, 0.84);
  box-shadow: 0 2px 4px rgba(64, 72, 60, 0.08);
  transform: translateX(-50%) rotate(-2deg);
}

.gaoyi-iseal-paper--pipeline {
  right: -2.5%;
  bottom: -7%;
  z-index: 1;
  width: 70%;
  height: 70%;
  transform: rotate(2.5deg);
}

.gaoyi-iseal-paper--results {
  right: 35%;
  bottom: 3.5%;
  z-index: 2;
  width: 41%;
  height: 31%;
  padding-bottom: 18px;
  transform: rotate(-5deg);
}

.gaoyi-iseal-paper--results::before {
  left: 36%;
  background: rgba(203, 222, 218, 0.88);
  transform: translateX(-50%) rotate(4deg);
}

.gaoyi-iseal-paper img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: contain;
  object-position: center;
  border: 1px solid rgba(16, 27, 45, 0.08);
  border-radius: 3px;
  background: #ffffff;
  box-sizing: border-box;
}

[data-gaoyi-iseal-card]:hover .gaoyi-iseal-paper--pipeline,
[data-gaoyi-iseal-card][data-gaoyi-iseal-hovered] .gaoyi-iseal-paper--pipeline,
[data-gaoyi-iseal-card]:focus-within .gaoyi-iseal-paper--pipeline {
  transform: translate(-9px, -15px) rotate(1.2deg);
  box-shadow:
    0 25px 48px rgba(35, 53, 47, 0.2),
    0 4px 10px rgba(35, 53, 47, 0.08);
}

[data-gaoyi-iseal-card]:hover .gaoyi-iseal-paper--results,
[data-gaoyi-iseal-card][data-gaoyi-iseal-hovered] .gaoyi-iseal-paper--results,
[data-gaoyi-iseal-card]:focus-within .gaoyi-iseal-paper--results {
  transform: translate(-8px, -21px) rotate(-3deg);
  box-shadow:
    0 25px 48px rgba(35, 53, 47, 0.2),
    0 4px 10px rgba(35, 53, 47, 0.08);
}

[data-gaoyi-iseal-card] > [data-gaoyi-iseal-marker] {
  position: absolute;
  z-index: 7;
  opacity: 0;
  filter: blur(4px);
  scale: 0.82;
  translate: 0 12px;
  pointer-events: none;
  transition:
    opacity 320ms ease calc(var(--gaoyi-iseal-marker-index, 0) * 70ms),
    filter 500ms ease calc(var(--gaoyi-iseal-marker-index, 0) * 70ms),
    scale 620ms cubic-bezier(0.22, 1, 0.36, 1) calc(var(--gaoyi-iseal-marker-index, 0) * 70ms),
    translate 620ms cubic-bezier(0.22, 1, 0.36, 1) calc(var(--gaoyi-iseal-marker-index, 0) * 70ms);
}

[data-gaoyi-iseal-card]:hover > [data-gaoyi-iseal-marker],
[data-gaoyi-iseal-card][data-gaoyi-iseal-hovered] > [data-gaoyi-iseal-marker],
[data-gaoyi-iseal-card]:focus-within > [data-gaoyi-iseal-marker] {
  opacity: 1;
  filter: blur(0);
  scale: 1;
  translate: 0 0;
}

.gaoyi-iseal-marker--sticker {
  width: 72px;
  height: 72px;
  transform: rotate(var(--gaoyi-iseal-sticker-rotation, 0deg));
}

.gaoyi-iseal-marker--sticker img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: contain;
  filter: drop-shadow(0 8px 10px rgba(35, 53, 47, 0.14));
}

.gaoyi-iseal-marker--private-key {
  top: 24px;
  left: 50%;
  --gaoyi-iseal-sticker-rotation: -5deg;
}

.gaoyi-iseal-marker--fingerprint-embed {
  top: 126px;
  left: 35%;
  width: 66px;
  height: 66px;
  --gaoyi-iseal-sticker-rotation: 5deg;
}

.gaoyi-iseal-marker--black-box {
  top: 88px;
  right: 19%;
  width: 76px;
  height: 76px;
  --gaoyi-iseal-sticker-rotation: 6deg;
}

.gaoyi-iseal-marker--ownership {
  bottom: 20px;
  left: 43%;
  width: 84px;
  height: 84px;
  --gaoyi-iseal-sticker-rotation: -4deg;
}

.gaoyi-iseal-marker--theft-resistance {
  top: 126px;
  right: 3.5%;
  width: 70px;
  height: 70px;
  --gaoyi-iseal-sticker-rotation: 4deg;
}

.gaoyi-iseal-marker--robustness {
  right: 3%;
  bottom: 18px;
  width: 88px;
  height: 88px;
  --gaoyi-iseal-sticker-rotation: -3deg;
}

.gaoyi-iseal-marker--venue {
  top: 25px;
  right: 30px;
  display: grid;
  place-items: center;
  width: 68px;
  height: 68px;
  border: 1px solid rgba(16, 27, 45, 0.18);
  border-radius: 5px;
  background: #fffefd;
  box-shadow: 0 10px 20px rgba(35, 53, 47, 0.14);
  transform: rotate(6deg);
  color: #101b2d;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 12px;
  font-weight: 700;
  line-height: 1.15;
  text-align: center;
}

.gaoyi-iseal-marker--note {
  bottom: 19px;
  left: 25px;
  padding: 9px 13px;
  background: #fff7cb;
  box-shadow: 0 10px 20px rgba(35, 53, 47, 0.13);
  clip-path: polygon(2% 9%, 98% 0, 100% 88%, 3% 100%);
  transform: rotate(-4deg);
  color: rgba(16, 27, 45, 0.76);
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 11px;
  line-height: 1.2;
}

@media (max-width: 809.98px) {
  .gaoyi-iseal-copy {
    top: 24px;
    left: 24px;
    width: 300px;
    max-width: calc(100% - 48px);
  }

  .gaoyi-iseal-copy h3 {
    font-size: 25px;
  }

  .gaoyi-iseal-copy p {
    margin-top: 10px;
    font-size: 14px;
  }

  .gaoyi-iseal-card-art::before {
    right: -20%;
    bottom: -18%;
    width: 112%;
    height: 69%;
  }

  .gaoyi-iseal-paper--pipeline {
    right: -13%;
    bottom: -4%;
    width: 92%;
    height: 54%;
  }

  .gaoyi-iseal-paper--results {
    right: 43%;
    bottom: 4%;
    width: 59%;
    height: 25%;
  }

  .gaoyi-iseal-marker--venue,
  .gaoyi-iseal-marker--note {
    display: none;
  }

  .gaoyi-iseal-marker--sticker {
    width: 58px;
    height: 58px;
  }

  .gaoyi-iseal-marker--private-key {
    top: 118px;
    left: 24px;
  }

  .gaoyi-iseal-marker--black-box {
    top: 112px;
    right: 20px;
  }

  .gaoyi-iseal-marker--ownership {
    bottom: 16px;
    left: 24px;
  }

  .gaoyi-iseal-marker--robustness {
    right: 18px;
    bottom: 15px;
    width: 64px;
    height: 64px;
  }

  .gaoyi-iseal-marker--fingerprint-embed,
  .gaoyi-iseal-marker--theft-resistance {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gaoyi-iseal-paper,
  [data-gaoyi-iseal-card] > [data-gaoyi-iseal-marker] {
    transition: none !important;
  }
}
</style>
<script data-gaoyi-iseal-project-art>
(() => {
  const paperUrl = "https://arxiv.org/abs/2511.08905";
  const figureSources = [
    ["/assets/projects/iseal-pipeline.webp", "iSeal model registration, fingerprint injection, and ownership verification pipeline", "pipeline"],
    ["/assets/projects/iseal-results.webp", "iSeal fingerprint effectiveness across ten language models", "results"],
  ];

  const personalize = () => {
    const heading = Array.from(document.querySelectorAll("h1, h2, h3"))
      .find((node) => node.textContent?.trim() === "iSeal" || node.textContent?.includes("Published iSeal"));
    const card = heading?.closest('[data-framer-name="Thumbnail"]');
    if (!heading || !card) return;

    const cardLink = card.closest("a[href]") || card.querySelector("a[href]");
    if (cardLink) {
      if (cardLink.getAttribute("href") !== paperUrl) {
        cardLink.setAttribute("href", paperUrl);
      }
      cardLink.setAttribute("target", "_blank");
      cardLink.setAttribute("rel", "noopener noreferrer");
      cardLink.setAttribute("aria-label", "Read the iSeal paper on arXiv");
    }

    if (!card.dataset.gaoyiIsealNavigationBound) {
      const openIseal = (event) => {
        if (event.type === "click" && event.button !== 0) return;
        event.preventDefault();
        event.stopPropagation();
        event.stopImmediatePropagation();
        window.open(paperUrl, "_blank", "noopener");
      };
      card.addEventListener("click", openIseal, true);
      card.addEventListener("keydown", (event) => {
        if (event.key !== "Enter" && event.key !== " ") return;
        openIseal(event);
      }, true);
      card.dataset.gaoyiIsealNavigationBound = "true";
    }

    if (!card.dataset.gaoyiIsealHoverBound) {
      const showHoverArt = () => card.dataset.gaoyiIsealHovered = "true";
      const hideHoverArt = () => delete card.dataset.gaoyiIsealHovered;
      let restingHeight = card.getBoundingClientRect().height;
      card.addEventListener("pointerenter", showHoverArt);
      card.addEventListener("pointerleave", hideHoverArt);
      card.addEventListener("focusin", showHoverArt);
      card.addEventListener("focusout", (event) => {
        if (!card.contains(event.relatedTarget)) hideHoverArt();
      });
      document.addEventListener("mousemove", (event) => {
        const rect = card.getBoundingClientRect();
        const isInside =
          event.clientX >= rect.left &&
          event.clientX <= rect.right &&
          event.clientY >= rect.top &&
          event.clientY <= rect.bottom;
        if (isInside) showHoverArt();
        else hideHoverArt();
      }, { capture: true, passive: true });
      const resizeObserver = new ResizeObserver(([entry]) => {
        const height = entry.contentRect.height;
        if (height > restingHeight + 24) showHoverArt();
        else if (height <= restingHeight + 8) {
          restingHeight = height;
          hideHoverArt();
        }
      });
      resizeObserver.observe(card);
      card.dataset.gaoyiIsealHoverBound = "true";
    }

    let content = heading;
    while (content.parentElement && content.parentElement !== card) content = content.parentElement;
    if (content.parentElement !== card) return;

    card.dataset.gaoyiIsealCard = "true";
    content.dataset.gaoyiIsealContent = "true";

    Array.from(card.children)
      .filter((child) =>
        child !== content &&
        !child.classList.contains("gaoyi-iseal-card-art") &&
        !child.classList.contains("gaoyi-iseal-copy") &&
        !child.hasAttribute("data-gaoyi-iseal-marker")
      )
      .forEach((child) => child.dataset.gaoyiIsealLegacyArt = "true");

    if (card.dataset.gaoyiIsealReady) return;
    card.dataset.gaoyiIsealReady = "true";

    const art = document.createElement("div");
    art.className = "gaoyi-iseal-card-art";
    figureSources.forEach(([source, alt, name]) => {
      const paper = document.createElement("div");
      paper.className = `gaoyi-iseal-paper gaoyi-iseal-paper--${name}`;
      const image = document.createElement("img");
      image.src = source;
      image.alt = alt;
      image.loading = "eager";
      image.decoding = "async";
      paper.appendChild(image);
      art.appendChild(paper);
    });
    card.appendChild(art);

    content.setAttribute("aria-hidden", "true");
    const copy = document.createElement("div");
    copy.className = "gaoyi-iseal-copy";
    const copyTitle = document.createElement("h3");
    copyTitle.textContent = "iSeal";
    const copyDescription = document.createElement("p");
    copyDescription.textContent = "Encrypted model fingerprinting for verifiable black-box LLM ownership.";
    copy.append(copyTitle, copyDescription);
    card.appendChild(copy);

    const venue = document.createElement("div");
    venue.className = "gaoyi-iseal-marker--venue";
    venue.dataset.gaoyiIsealMarker = "true";
    venue.style.setProperty("--gaoyi-iseal-marker-index", "0");
    venue.innerHTML = "AAAI<br>2026";
    card.appendChild(venue);

    const note = document.createElement("div");
    note.className = "gaoyi-iseal-marker--note";
    note.dataset.gaoyiIsealMarker = "true";
    note.style.setProperty("--gaoyi-iseal-marker-index", "1");
    note.textContent = "embed / query / verify";
    card.appendChild(note);

    const stickers = [
      ["/assets/projects/iseal-stickers-generated/iseal-sticker-private-key.png", "Private key generation", "private-key"],
      ["/assets/projects/iseal-stickers-generated/iseal-sticker-fingerprint-embed.png", "Fingerprint embedding", "fingerprint-embed"],
      ["/assets/projects/iseal-stickers-generated/iseal-sticker-black-box-query.png", "Black-box model query", "black-box"],
      ["/assets/projects/iseal-stickers-generated/iseal-sticker-ownership-verify.png", "Ownership verification", "ownership"],
      ["/assets/projects/iseal-stickers-generated/iseal-sticker-theft-resistance.png", "Model theft resistance", "theft-resistance"],
      ["/assets/projects/iseal-stickers-generated/iseal-sticker-model-robustness.png", "Cross-model robustness", "robustness"],
    ];
    stickers.forEach(([source, alt, name], index) => {
      const sticker = document.createElement("div");
      sticker.className = `gaoyi-iseal-marker--sticker gaoyi-iseal-marker--${name}`;
      sticker.dataset.gaoyiIsealMarker = "true";
      sticker.style.setProperty("--gaoyi-iseal-marker-index", String(index + 2));
      const image = document.createElement("img");
      image.src = source;
      image.alt = alt;
      image.loading = "eager";
      image.decoding = "async";
      sticker.appendChild(image);
      card.appendChild(sticker);
    });
  };

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", personalize, { once: true });
  else personalize();
  new MutationObserver(personalize).observe(document.documentElement, {
    childList: true,
    subtree: true,
    attributes: true,
    attributeFilter: ["href"],
  });
})();
</script>
"""
    return html.replace("</head>", style_and_script + "</head>")


def inject_applied_ai_notes_cleanup(html: str) -> str:
    """Preserve the original collage while preventing hydrated external navigation."""
    style_and_script = """
<style data-gaoyi-applied-ai-notes-cleanup>
section[data-framer-name="ai Section"] a[aria-disabled="true"] {
  cursor: default !important;
  /* Keep Framer's hover handlers active while suppressing navigation in JS. */
  pointer-events: auto !important;
  overflow: visible !important;
}

section[data-framer-name="ai Section"] img[src*="/assets/projects/prediction-router-search-v2.webp"]:not(a img),
section[data-framer-name="ai Section"] img[data-gaoyi-mantis-duplicate="true"] {
  display: none !important;
  visibility: hidden !important;
}
</style>
<script data-gaoyi-applied-ai-notes-cleanup>
(() => {
  const imageFallbacks = {
    "9PiMNrI5x9DO4A1LiMz6f6BAK2c.png": "/assets/projects/prediction-router-search-v2.webp",
    "mantis-live-desktop.webp": "/assets/projects/prediction-router-search-v2.webp",
    "prediction-router-search-v2.webp": "/assets/projects/prediction-router-search-v2.webp",
    "xxRBOkPDrW19Prpbbj1s7ap0DFw.png": "/assets/xiaoyanghu-homepage-original/images/xxRBOkPDrW19Prpbbj1s7ap0DFw.png",
    "EglDn1eZzU5OOKALS6lK7Rpog.png": "/assets/xiaoyanghu-homepage-original/images/EglDn1eZzU5OOKALS6lK7Rpog.png",
    "k4vxzwpdUysWRPsx59yscP95iEY.png": "/assets/xiaoyanghu-homepage-original/images/k4vxzwpdUysWRPsx59yscP95iEY.png",
    "ACK99otcO4GzOG2TrAifm8QHcqM.png": "/assets/xiaoyanghu-homepage-original/images/ACK99otcO4GzOG2TrAifm8QHcqM.png",
    "nvVmqesHhAViGJmCGehX1vCBf0.png": "/assets/xiaoyanghu-homepage-original/images/nvVmqesHhAViGJmCGehX1vCBf0.png",
    "A6YF39xOIevjXuP8wveAae5C2TQ.png": "/framerusercontent.com/images/A6YF39xOIevjXuP8wveAae5C2TQ.png",
    "guSHFivuwQ7O8MMrtDFxQC9NQW0.png": "/framerusercontent.com/images/guSHFivuwQ7O8MMrtDFxQC9NQW0.png",
    "Zm7rxCNckbHeaiNzgT55kw1AAEs.png": "/framerusercontent.com/images/Zm7rxCNckbHeaiNzgT55kw1AAEs.png",
  };
  const repairImages = () => document
    .querySelectorAll('section[data-framer-name="ai Section"] img')
    .forEach((image) => {
      const source = image.getAttribute("src") || "";
      const replacement = Object.entries(imageFallbacks)
        .find(([filename]) => source.includes(filename))?.[1];
      if (!replacement) return;
      image.dataset.gaoyiImageSource = replacement;
      if (replacement === "/assets/projects/prediction-router-search-v2.webp") {
        const anchor = image.closest("a");
        const isDuplicate = !anchor;
        image.toggleAttribute("data-gaoyi-mantis-duplicate", isDuplicate);
        image.toggleAttribute("aria-hidden", isDuplicate);
        image.alt = anchor && anchor.querySelector("img") === image
          ? "Mantis prediction-market search workspace"
          : "";
      }
      image.loading = "eager";
      image.removeAttribute("srcset");
      image.removeAttribute("sizes");
      if (image.getAttribute("src") === replacement) return;
      image.src = replacement;
    });
  const disableLinks = () => document
    .querySelectorAll('section[data-framer-name="ai Section"] a')
    .forEach((anchor) => {
      anchor.removeAttribute("href");
      anchor.removeAttribute("target");
      anchor.removeAttribute("rel");
      anchor.setAttribute("aria-disabled", "true");
      if (anchor.dataset.gaoyiNavigationBlocked) return;
      anchor.dataset.gaoyiNavigationBlocked = "true";
      anchor.addEventListener("click", (event) => {
        event.preventDefault();
        event.stopPropagation();
      }, true);
    });
  const syncNoteHover = (event) => document
    .querySelectorAll('section[data-framer-name="ai Section"] a[aria-disabled="true"]')
    .forEach((anchor) => {
      const rect = anchor.getBoundingClientRect();
      const isInside =
        event.clientX >= rect.left &&
        event.clientX <= rect.right &&
        event.clientY >= rect.top &&
        event.clientY <= rect.bottom;
      anchor.toggleAttribute("data-gaoyi-note-hovered", isInside);
    });
  const install = () => {
    repairImages();
    disableLinks();
    if (!document.documentElement.dataset.gaoyiNoteHoverBound) {
      document.addEventListener("mousemove", syncNoteHover, { capture: true, passive: true });
      document.documentElement.dataset.gaoyiNoteHoverBound = "true";
    }
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", install, { once: true });
  else install();
  new MutationObserver(install).observe(document.documentElement, {
    childList: true,
    subtree: true,
    attributes: true,
    attributeFilter: ["src", "srcset"],
  });
})();
</script>
"""
    return html.replace("</head>", style_and_script + "</head>")


def apply_profile_footer_links(html: str) -> str:
    """Give every footer button a concrete Gaoyi profile destination."""
    destinations = {
        "email": "mailto:criswu20010728@gmail.com",
        "cv": "/resume/gaoyi-wu-resume.pdf",
        "Linkedin": LINKEDIN_LINK,
        "LinkedIn": LINKEDIN_LINK,
        "scholar": SCHOLAR_LINK,
        "github": GITHUB_LINK,
    }
    soup = BeautifulSoup(html, "html.parser")
    scholar_icon = """
<div aria-hidden="true" class="gaoyi-google-scholar-icon">
  <svg fill="none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <path d="M2.4 9.2 12 4l9.6 5.2L12 14.4 2.4 9.2Z" fill="currentColor"/>
    <path d="M6.2 11.1v4.1c0 1.8 2.6 3.2 5.8 3.2s5.8-1.4 5.8-3.2v-4.1L12 14.3l-5.8-3.2Z" fill="currentColor" opacity=".78"/>
    <path d="M21.6 9.5v5.3" stroke="currentColor" stroke-linecap="round" stroke-width="1.6"/>
  </svg>
</div>
"""
    for anchor in soup.select('footer a[data-framer-name="x"]'):
        anchor["data-framer-name"] = "scholar"
        anchor["name"] = "Google Scholar"
        anchor["aria-label"] = "Google Scholar"
        anchor["href"] = SCHOLAR_LINK
        anchor["target"] = "_blank"
        anchor["rel"] = "noopener"
        anchor.clear()
        anchor.append(BeautifulSoup(scholar_icon, "html.parser"))
    for name, href in destinations.items():
        for anchor in soup.select(f'footer a[data-framer-name="{name}"]'):
            anchor["href"] = href
    return str(soup)


def inject_profile_footer_link_binding(html: str) -> str:
    """Reapply footer destinations if Framer replaces the hydrated nodes."""
    destinations = json.dumps(
        {
            "email": "mailto:criswu20010728@gmail.com",
            "cv": "/resume/gaoyi-wu-resume.pdf",
            "Linkedin": LINKEDIN_LINK,
            "LinkedIn": LINKEDIN_LINK,
            "scholar": SCHOLAR_LINK,
            "github": GITHUB_LINK,
        }
    )
    script = f"""
<style data-gaoyi-profile-footer-presentation>
/* Never show the legacy X control while Framer is hydrating the footer. */
footer a[data-framer-name="x"] {{ display: none !important; }}
footer a[data-framer-name="email"] .framer-14p36o2-container {{ z-index: 1 !important; }}
footer a[data-framer-name="email"] .framer-1o6iv6c {{ left: 39px !important; right: auto !important; }}
footer a[data-framer-name="email"] .framer-1o6iv6c p {{ font-size: 11px !important; letter-spacing: 0 !important; }}
footer a[data-framer-name="scholar"],
footer a[data-framer-name="scholar"] * {{ cursor: pointer !important; }}
.gaoyi-google-scholar-icon {{
  align-items: center;
  color: var(--token-8056d279-4388-496c-b0ab-8ec93edb0b33, rgb(12, 19, 27));
  display: flex;
  inset: 0;
  justify-content: center;
  position: absolute;
}}
.gaoyi-google-scholar-icon svg {{ display: block; height: 23px; width: 23px; }}
</style>
<script data-gaoyi-profile-links>
(() => {{
  const destinations = {destinations};
  const scholarIcon = `<div aria-hidden="true" class="gaoyi-google-scholar-icon"><svg fill="none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M2.4 9.2 12 4l9.6 5.2L12 14.4 2.4 9.2Z" fill="currentColor"/><path d="M6.2 11.1v4.1c0 1.8 2.6 3.2 5.8 3.2s5.8-1.4 5.8-3.2v-4.1L12 14.3l-5.8-3.2Z" fill="currentColor" opacity=".78"/><path d="M21.6 9.5v5.3" stroke="currentColor" stroke-linecap="round" stroke-width="1.6"/></svg></div>`;
  const applyLinks = () => document.querySelectorAll("footer a[data-framer-name]").forEach((anchor) => {{
    if (anchor.dataset.framerName === "x") {{
      anchor.dataset.framerName = "scholar";
      anchor.setAttribute("name", "Google Scholar");
      anchor.setAttribute("aria-label", "Google Scholar");
      anchor.innerHTML = scholarIcon;
    }}
    const href = destinations[anchor.dataset.framerName];
    if (href) anchor.setAttribute("href", href);
    if (anchor.dataset.framerName === "scholar") {{
      anchor.setAttribute("target", "_blank");
      anchor.setAttribute("rel", "noopener");
    }}
  }});
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", applyLinks, {{ once: true }});
  else applyLinks();
  new MutationObserver(applyLinks).observe(document.documentElement, {{ childList: true, subtree: true }});
}})();
</script>
"""
    return html.replace("</head>", script + "</head>")


def prune_retired_experience_cards(html: str) -> str:
    """Remove source experience cards that do not belong to Gaoyi's history."""
    soup = BeautifulSoup(html, "html.parser")
    for label in ("Lanma.ai", "Mobile Now"):
        for text in soup.find_all(string=lambda value: value and value.strip() == label):
            # Framer emits Default, larger-card, and mobile versions of each
            # experience row. They all share the card root class.
            card = text.find_parent(
                "div",
                class_=lambda classes: classes and "framer-E2tnR" in classes,
            )
            if card and card.parent:
                card.parent.decompose()
    return str(soup)


def repair_xclaw_experience_copy(html: str) -> str:
    """Give XClaw its own role and dates without changing other experience cards."""
    soup = BeautifulSoup(html, "html.parser")
    replacements = {
        "Research Assistant": "Individual Contributor (IC)",
        "May 2024 - Aug 2024": "Sep 2025 - Nov 2025",
        "Research": "IC",
    }
    for card in soup.select(".framer-E2tnR"):
        if "XClaw" not in card.get_text(" ", strip=True):
            continue
        for text in card.find_all(string=True):
            replacement = replacements.get(text.strip())
            if replacement:
                text.replace_with(replacement)
    return str(soup)


def repair_shenzhen_experience_copy(html: str) -> str:
    """Keep Shenzhen University's undergraduate dates accurate."""
    soup = BeautifulSoup(html, "html.parser")
    for card in soup.select(".framer-E2tnR"):
        if "Shenzhen University" not in card.get_text(" ", strip=True):
            continue
        for text in card.find_all(string=True):
            if text.strip() == "Sep 2020 - Jul 2024":
                text.replace_with("Sep 2019 - Jul 2023")
    return str(soup)


def inject_experience_personalization(html: str) -> str:
    """Keep the hydrated Experience section aligned with Gaoyi's CV."""
    style_and_script = """
<style data-gaoyi-experience-presentation>
/* Normalize visual weight across the mixed square and horizontal marks. */
.framer-1bi44tx img[src*="/assets/logos/intellisys-lab.svg"] {
  box-sizing: border-box !important;
  object-fit: contain !important;
  padding: 18px 4px !important;
}
.framer-1bi44tx img[src*="/assets/logos/dhl-express.svg"],
.framer-1bi44tx img[src*="/assets/logos/xclaw-lobster.png"] {
  box-sizing: border-box !important;
  object-fit: contain !important;
  padding: 7px !important;
}
.framer-1bi44tx img[src*="/assets/logos/stevens.svg"] {
  box-sizing: border-box !important;
  object-fit: contain !important;
  padding: 15px 4px !important;
}
.framer-1bi44tx img[src*="/assets/logos/shenzhen-university.png"] {
  box-sizing: border-box !important;
  object-fit: contain !important;
  padding: 10px !important;
}
/* The wide Experience layout positions these marks independently from the card text. */
.framer-E2tnR img[data-gaoyi-experience-logo="true"] {
  box-sizing: border-box !important;
  object-fit: contain !important;
}
/* Back-face textures must be ready before a visitor flips an Experience card. */
.framer-E2tnR [data-framer-name="Back"] img[data-gaoyi-experience-backdrop="true"] {
  display: block !important;
  object-fit: cover !important;
}
.framer-E2tnR [data-framer-name="Back"] {
  isolation: isolate;
  overflow: visible !important;
}
.framer-E2tnR [data-framer-name="Back"] [data-framer-name="BG"] {
  z-index: 0 !important;
}
.framer-E2tnR [data-framer-name="Back"] [data-framer-name="Row 1"] {
  position: relative !important;
  z-index: 1 !important;
}
.framer-E2tnR [data-framer-name="Back"] [data-gaoyi-experience-badge="true"] {
  overflow: visible !important;
  transform: rotate(-7deg) !important;
  z-index: 2;
}
.framer-E2tnR [data-framer-name="Back"] [data-gaoyi-experience-badge="true"] > div {
  overflow: visible !important;
}
.framer-E2tnR [data-framer-name="Back"] [data-gaoyi-experience-badge="true"] img {
  display: block !important;
  filter: drop-shadow(0 2px 2px rgba(12, 19, 27, 0.16));
  height: 100% !important;
  object-fit: contain !important;
  width: 100% !important;
}
.framer-E2tnR [data-framer-name="Back"][data-gaoyi-experience-fallback="true"] [data-framer-name="Row 1"] {
  box-sizing: border-box !important;
  padding-right: 104px !important;
}
.gaoyi-experience-badge {
  height: 94px;
  position: absolute;
  right: 6px;
  top: 50%;
  transform: translateY(-50%) rotate(-7deg);
  width: 94px;
  z-index: 2;
}
.gaoyi-experience-badge img {
  display: block !important;
  filter: drop-shadow(0 2px 2px rgba(12, 19, 27, 0.16));
  height: 100% !important;
  object-fit: contain !important;
  width: 100% !important;
}
</style>
<script data-gaoyi-experience-cleanup>
(() => {
  const experienceLogos = {
    "Intellisys Lab": "/assets/logos/intellisys-lab.svg",
    "DHL Express": "/assets/logos/dhl-express.svg",
    "XClaw": "/assets/logos/xclaw-lobster.png",
    "Stevens Institute": "/assets/logos/stevens.svg",
    "Shenzhen University": "/assets/logos/shenzhen-university.png",
  };
  const experienceBackdrops = [
    "/assets/experience/experience-blue-texture.jpg",
    "/assets/experience/experience-paper-texture.jpg",
    "/assets/experience/experience-mint-texture.jpg",
  ];
  const experienceBadges = {
    "Intellisys Lab": "/assets/experience/badges/intellisys-lab.png",
    "DHL Express": "/assets/experience/badges/dhl-express.png",
    "XClaw": "/assets/experience/badges/xclaw.png",
    "Stevens Institute of Technology": "/assets/experience/badges/stevens.png",
    "Shenzhen University": "/assets/experience/badges/shenzhen-university.png",
  };
  const retired = new Set([
    "Lanma.ai",
    "Mobile Now",
    "__gaoyi_retired_lanma__",
    "__gaoyi_retired_mobile_now__",
  ]);
  const removeRetiredRows = () => document.querySelectorAll(".framer-text").forEach((node) => {
    if (!retired.has(node.textContent.trim())) return;
    const card = node.closest(".framer-E2tnR");
    const row = card && card.parentElement;
    if (row) row.remove();
  });
  const repairXClawCopy = () => document.querySelectorAll(".framer-E2tnR").forEach((card) => {
    if (!card.textContent.includes("XClaw")) return;
    card.querySelectorAll(".framer-text").forEach((node) => {
      const replacement = {
        "Research Assistant": "Individual Contributor (IC)",
        "May 2024 - Aug 2024": "Sep 2025 - Nov 2025",
        "Research": "IC",
      }[node.textContent.trim()];
      if (replacement) node.textContent = replacement;
    });
  });
  const repairShenzhenCopy = () => document.querySelectorAll(".framer-E2tnR").forEach((card) => {
    if (!card.textContent.includes("Shenzhen University")) return;
    card.querySelectorAll(".framer-text").forEach((node) => {
      if (node.textContent.trim() === "Sep 2020 - Jul 2024") {
        node.textContent = "Sep 2019 - Jul 2023";
      }
    });
  });
  const repairExperienceLogos = () => document.querySelectorAll(".framer-E2tnR").forEach((card) => {
    const replacement = Object.entries(experienceLogos)
      .find(([label]) => card.textContent.includes(label))?.[1];
    if (!replacement) return;
    const image = card.querySelector('[data-framer-name="Image"] img') || card.querySelector("img");
    if (!image || (image.dataset.gaoyiExperienceLogoSrc === replacement && image.getAttribute("src") === replacement)) return;
    image.dataset.gaoyiExperienceLogo = "true";
    image.dataset.gaoyiExperienceLogoSrc = replacement;
    image.loading = "eager";
    image.removeAttribute("srcset");
    image.src = replacement;
  });
  const repairExperienceBackdrops = () => document
    .querySelectorAll('.framer-E2tnR [data-framer-name="Back"] img')
    .forEach((image) => {
      const existingSource = image.getAttribute("src") || image.currentSrc || "";
      const replacement = experienceBackdrops.find((path) => existingSource.includes(path));
      if (!replacement || (image.dataset.gaoyiExperienceBackdropSrc === replacement && image.getAttribute("src") === replacement)) return;
      image.dataset.gaoyiExperienceBackdrop = "true";
      image.dataset.gaoyiExperienceBackdropSrc = replacement;
      image.loading = "eager";
      image.decoding = "async";
      image.removeAttribute("srcset");
      image.removeAttribute("sizes");
      image.src = replacement;
    });
  const repairExperienceBadges = () => document.querySelectorAll(".framer-E2tnR").forEach((card) => {
    const match = Object.entries(experienceBadges)
      .find(([label]) => card.textContent.includes(label));
    const back = card.querySelector('[data-framer-name="Back"]');
    if (!match || !back) return;
    const [label, src] = match;
    const badge = back.querySelector('[data-framer-name="Row 1"] [data-framer-name="Image"]');
    let fallback = back.querySelector(':scope > .gaoyi-experience-badge');
    if (!badge) {
      back.dataset.gaoyiExperienceFallback = "true";
      if (!fallback) {
        fallback = document.createElement("div");
        fallback.className = "gaoyi-experience-badge";
        fallback.setAttribute("role", "img");
        fallback.append(document.createElement("img"));
        back.append(fallback);
      }
      fallback.setAttribute("aria-label", `${label} badge`);
      const fallbackImage = fallback.querySelector("img");
      if (fallbackImage) {
        fallbackImage.alt = "";
        fallbackImage.loading = "eager";
        fallbackImage.decoding = "async";
        fallbackImage.removeAttribute("srcset");
        fallbackImage.removeAttribute("sizes");
        if (fallbackImage.getAttribute("src") !== src) fallbackImage.src = src;
      }
      return;
    }
    delete back.dataset.gaoyiExperienceFallback;
    if (fallback) fallback.remove();
    badge.dataset.gaoyiExperienceBadge = "true";
    badge.setAttribute("role", "img");
    badge.setAttribute("aria-label", `${label} badge`);
    const image = badge.querySelector("img");
    if (!image) return;
    image.alt = "";
    image.loading = "eager";
    image.decoding = "async";
    image.removeAttribute("srcset");
    image.removeAttribute("sizes");
    if (image.getAttribute("src") !== src) image.src = src;
    badge.querySelectorAll(".gaoyi-experience-badge-name").forEach((name) => name.remove());
  });
  const install = () => {
    removeRetiredRows();
    repairXClawCopy();
    repairShenzhenCopy();
    repairExperienceLogos();
    repairExperienceBackdrops();
    repairExperienceBadges();
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", install, { once: true });
  else install();
  new MutationObserver(install).observe(document.documentElement, { childList: true, subtree: true });
})();
</script>
"""
    return html.replace("</head>", style_and_script + "</head>")


def write_text(path: Path, html: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(CONTROL_CHARS.sub("", html), encoding="utf-8")


HOME_REPLACEMENTS = [
    ("Xiaoyang Hu Design Portfolio", "Gaoyi Wu AI Portfolio"),
    (
        "Seeking 26NG positions. Product Designer specializing in GenAI, complex workflows, and intuitive multi-platform UX. Crafting AI-native systems with clarity, empathy, and play.",
        "Applied AI engineer building practical ML systems, secure LLM workflows, and production-ready AI products.",
    ),
    ("Xiaoyang Hu", "Gaoyi Wu"),
    ("Designs", "Builds"),
    ("and cross-platform ", "and ML "),
    ("products, making complex challenges", "systems, turning research ideas"),
    ("feel intuitive across", "into practical products across"),
    ("B2B & B2C", "infra & apps"),
    ("B2B &amp; B2C", "infra &amp; apps"),
    ("worlds.", "layers."),
    ("Featured Projects", "Selected Projects"),
    (
        "End-to-End Designer of AKOOL's AI Image Generator 2.0",
        "XClaw",
    ),
    (
        "Driving +16% creations on a 7M-user GenAI platform through UX iteration",
        "A desktop workspace for coordinating agents, tools, models, and channels.",
    ),
    ("GenAI", "secure AI"),
    ("AI-Native Startup", "Applied AI Product"),
    ("B2C Product", "Agent Workflows"),
    ("Internship Project", "Desktop Build"),
    (
        "Sole Designer of Siemens XData Hub ETL",
        "iSeal",
    ),
    (
        "Turning SME Data Challenges into an MVP in 8 Weeks",
        "Encrypted model fingerprinting for verifiable black-box LLM ownership.",
    ),
    ("0→1 Product Design", "LLM Security"),
    ("Data Engineering (ETL)", "Fingerprinting"),
    ("Platform Internship Project", "Research System"),
    (
        "Lead Designer For the Museum of Flight's App Easy MoF",
        "Built WebWeaver, topology inference for LLM multi-agent systems",
    ),
    (
        "Empowering elderly visitors with AI-assisted design, improving navigation by 40%",
        "Recovering hidden multi-agent communication graphs from contextual traces",
    ),
    (
        "Enhancing accessibility and navigation efficiency through AI powered Features",
        "Recovering hidden multi-agent communication graphs from contextual traces",
    ),
    (
        "Empowering elderly visitors with AI-assisted design, improving navigation score by 40%",
        "Recovering hidden multi-agent communication graphs from contextual traces",
    ),
    ("Accessibility Design", "AI Security"),
    ("Mobile UX&UI", "Topology Inference"),
    ("Mobile UX&amp;UI", "Topology Inference"),
    ("Practicum Project", "arXiv 2026"),
    ("Coming Soon", "Read Paper"),
    ("Vibe Coding", "Applied AI Notes"),
    ("field notes", "build notes"),
    ("from config'26", "from applied AI systems"),
    ("from config’26", "from applied AI systems"),
    ("Chritmas tree made of rejection emails", "Prediction Router live routing interface"),
    ("Chritmas tree made of", "Prediction Router live"),
    ("rejection emails", "routing interface"),
    ("Open claw inspired Agent Oversight Dashboard ", "Mantis desktop routing workspace "),
    ("Open claw inspired", "Mantis desktop"),
    ("Agent Oversight Dashboard", "routing workspace"),
    ("AKOOL", "XClaw"),
    ("My Design Toolkit", "System Toolkit"),
    ("Building Design System", "LLM Systems"),
    ("Crafting Graceful UI", "ML Infrastructure"),
    ("Simplifying Complex SaaS", "Research to Product"),
    ("My Design Journey", "Experience"),
    ("From Spaces to Systems", "From Models to Reliable Systems"),
    (
        "I studied architecture before stepping into digital product design.",
        "I work on applied AI at the intersection of ML research, LLM security, and systems engineering.",
    ),
    (
        "That training taught me to think in systems : how people move, feel, and make decisions within a space. The scale changed from city blocks to pixels, but the core remained constant: Human-centered scale, System orchestration, Context-driven storytelling……",
        "Across ownership verification, adversarial evaluation, and multi-agent topology inference, I treat every model as an operational system: define the threat model, measure what matters, and design for deployment.",
    ),
    (
        "Today, I apply the same thinking to digital products, transforming abstract operations into intuitive, human-friendly digital environments.",
        "Today, I turn research ideas into reliable AI infrastructure and products, making complex model behavior measurable, secure, and useful.",
    ),
    ("Siemens", "Intellisys Lab"),
    ("Product Design Intern", "Research Assistant"),
    ("Jul 2025 -Sep 2025", "Sep 2024 - Present"),
    ("Full time", "Research"),
    (
        "As the sole designer, I built an enterprise data platform (X-DataHub) from 0 to 1—my largest-scope project to date. I learned to use design to abstract complexity, visualize logic, and support decision-making in a highly technical system, while taking on 40% of PM responsibilities.",
        "I build secure and measurable AI systems, from federated LLM workflows to adversarial evaluation pipelines and production-minded research infrastructure.",
    ),
    ("The Museum of Flight", "DHL Express"),
    ("Product Designer", "AI/ML Engineer Intern"),
    ("Mar 2025 - Jul 2025", "May 2024 - Aug 2024"),
    ("Practium Sponsor", "Production Systems"),
    ("University of Washington", "Stevens Institute of Technology"),
    ("MS in Digital Media", "Master of Science, Computer Science"),
    ("Sep 2024 - Mar 2026", "Sep 2024 - Present"),
    ("Tongji University", "Shenzhen University"),
    ("BEng in Landscape Architecture", "Bachelor, Logistics Management"),
    ("Practicum Sponsor", "Production Systems"),
    (
        "At the Museum of Flight, I designed an accessible museum app with an AI-powered voice assistant for elderly visitors. I learned how accessibility goes beyond visuals and WCAG. Collaborating with museum staff helped me understand how to design AI features that can address genuine challenges.",
        "At DHL Express, I worked on churn prediction, sentiment analysis, retraining workflows, and ML delivery paths that connected model quality to production operations.",
    ),
    (
        "At Akool, things moved fast (“new feature every other morning” fast). I learned to listen to users, test ideas quickly, and find clarity in chaos. Despite limited startup resources, I worked closely with PMs and developers to advocate for design value and push UX improvements.",
        "In applied AI environments, things move fast. I learned to test ideas quickly, work closely with PMs and engineers, and keep product decisions grounded in real user constraints.",
    ),
    (
        "Coming to the US and studying at UW has been one of the best decisions I’ve made. I fell in love with Seattle’s energy and UW’s beautiful campus. Transitioning from architecture, I’ve been able to systematically learn UI & UX and gained a broader perspective through interdisciplinary projects that connect design and marketing.",
        "At Stevens Institute of Technology, I strengthened my computer science foundation through systems, machine learning, and AI research. Studying in Hoboken also placed me close to New York's engineering community and helped me connect research decisions with production constraints.",
    ),
    (
        "Studying at Tongji’s world-top architecture school was where I first realized design was more than a skill, instead it was my way of seeing the world. In studio after studio, I found joy in solving problems with a design mindset. Many of those architectural instincts naturally evolved into the way I now design digital products.",
        "At Shenzhen University, I built a foundation in logistics management, data analysis, and operational systems. That training taught me to trace how information, people, and resources move through complex organizations, a perspective I now apply to AI and ML systems.",
    ),
    ("Beyond Design", "Beyond the Work"),
    (
        "I’m an avid theatre lover and reviewer, writing about plays, musicals, and dance on Chinese social media. I also explore street photography, capturing stories and moments worth remembering on ",
        "Outside of building AI systems, I keep a running archive of photos, textures, and references that sharpen how I think about interfaces, storytelling, and product taste. You can browse a few more notes and builds on ",
    ),
    ("my dedicated Instagram account", "my GitHub"),
    ("Thank you for Visiting", "Thanks for Visiting"),
    ("Eat. Sleep. Design. Repeat.", "Build. Ship. Iterate. Repeat."),
    ("Hi, I'm Xiaoyang :)", "Hi, I'm Gaoyi :)"),
    (
        "I'm a product designer specializing in transforming complex enterprise data and AI workflows into intuitive, scalable B2B solutions.",
        "I'm an applied AI engineer focused on turning research ideas into practical ML systems, trustworthy LLM workflows, and production-ready AI products.",
    ),
    (
        "My approach is deeply informed by product strategy. I've often been recognized for my strong product sense, allowing me to look beyond pixels and effectively bridge the gap between user needs, business goals, and technical feasibility.",
        "My approach stays grounded in measurable outcomes, system ownership, and clear communication across research and product.",
    ),
    ("Design Philosophy", "Working Style"),
    ("mshuxy@gmail.com", "criswu20010728@gmail.com"),
    ("https://www.linkedin.com/in/xiaoyang-hu-elena/", "https://www.linkedin.com/in/gaoyiwu/"),
    ("https://github.com/Xiaoyang-Hu-96", "https://github.com/Alfred768"),
    ("https://x.com/elenahuxy", "https://github.com/Alfred768"),
    (
        "https://drive.google.com/file/d/1Mru8H1SZOt1-31eJhhlMEmqCMK6kx-2_/view?usp=sharing",
        "/resume/gaoyi-wu-resume.pdf",
    ),
]


HOME_IMAGE_MAP = {
    "36lfHPWTDJQOcFpigFNLZzI6Y.png": "/assets/logos/intellisys-lab.svg",
    "1aYKsDxmhTb3CAheqTo9RyIPGIs.png": "/assets/logos/dhl-express.svg",
    "ACAqekk053rsrb6xBmwXfFpU8A.jpg": "/assets/logos/xclaw-lobster.png",
    "o1MNcuY3XV6ONgKCzLe0bKg0A.png": "/assets/logos/stevens.svg",
    "qBTebIavoC4ZhrO0NpUfAHb0.png": "/assets/logos/shenzhen-university.png",
    "Isu4lpHAQKdkzaMiG6sflRK7Ow.jpg": "/assets/experience/experience-blue-texture.jpg",
    "03M7mtRJeSkIESdVbKwbWAAyj0s.jpg": "/assets/experience/experience-paper-texture.jpg",
    "EUjfTkhUJCaXcK9t3KM8K6wQ2ks.jpg": "/assets/experience/experience-mint-texture.jpg",
    "A0XixKFvjxxQJ8sgnzGXtNOqDHY.png": "/assets/logos/intellisys-lab.svg",
    "To57oBa2ocWjVytjkOui11T34mw.png": "/assets/logos/dhl-express.svg",
    "rnSNcUt7AARtRxfQlOMi5CdyF2M.png": "/assets/projects/xclaw-dashboard.webp",
    "yYHAJfe5mnD3HJq2JUhf8foM5g.png": "/assets/about/xclaw-account.webp",
    "tYMeKa1vpUZTjR7sxgn2Y1M6o.png": "/assets/style-kit/stickers/robot-3d.png",
    "I5XJ7YWLit19wYZ01Z4xo2T31o.png": "/assets/style-kit/stickers/desktop-computer-3d.png",
    "uzlQLN9YQT1zhfi1XhNFOeGCHE8.png": "/assets/style-kit/stickers/puzzle-piece-3d.png",
    "xnUg8RExk6YNQ5qMsbAcLOnpcxs.png": "/assets/style-kit/stickers/light-bulb-3d.png",
    "ipvYobD6R5gwDM75HADMY4uXqIU.png": "/assets/projects/iseal-pipeline.webp",
    "UHIhF5z0rCwMx3ofY9ZhMuKAQ.png": "/assets/projects/iseal-results.webp",
    "uyvQS3H8LhnvBbVBcNK4tbvxE.png": "/assets/style-kit/stickers/file-folder-3d.png",
    "F88Oars6dEz3rF4fRVs49pXXZ0A.png": "/assets/about/iseal-resistance.webp",
    "YUrWrQt3EBxwiGpWsUxWaKcc6f0.png": "/assets/about/iseal-sensitivity.webp",
    "Ow88kijPgLbHUvOTO888dkjs.png": "/assets/style-kit/stickers/stevens-s-sticker.svg",
    "Hc4JLMsg7E5n5Unk9Lu6LIF9UM.png": "/assets/style-kit/stickers/gaoyi-ai-ml-engineer-sticker.svg",
    "kM4sBpfrA0ZFYO4Dkc9cdmtIMUw.png": "/assets/gaoyi-wu-portrait-studio.jpg",
    "QRGZyGRAf0QwAYbVddHt4wxGkA.webp": "/assets/style-kit/photos/instant-camera-supercolor.jpg",
    "dkZK6b5c2v3jSliE5F86C9i7Z0.webp": "/assets/style-kit/photos/instant-camera-supercolor.jpg",
    "lkY8vh8k5IL5jaN7tBaRZWMD4k.webp": "/assets/gaoyi-wu-portrait-studio.jpg",
    "kw8vfuk4bb5yDcVGQ7M5C97c.png": "/assets/style-kit/frames/gaoyi-wu-wax-seal.svg",
    "BLq9oAT9HrWdp5D2W0NTqzKTM.png": "/assets/style-kit/frames/gaoyi-wu-wax-seal.svg",
    "mtYxVS1lgU4Cxmxi9tFTZMy7p8.png": "/assets/style-kit/frames/gaoyi-wu-signature.svg",
    "1a9rvLhWMUC8kGTkDqBieE6uy4.png": "/assets/projects/webweaver-topology.webp",
    "xiKhH2uMtRLq6aJ7o5lTKyc3I.png": "/assets/projects/webweaver-robustness.webp",
    "KaHyfkp6ALRteyeSGid06gOCEzU.png": "/assets/projects/webweaver-reconstruction.webp",
    "Snm10XuSyGSplwqU9IfOxnyAT4.png": "/assets/projects/prediction-router-search-v2.webp",
    "RiqLKfUeOnAkCdZNYWVN54MMxFA.png": "/assets/projects/mantis-live-desktop.webp",
    "tzmhndHCyCO4Eo7oRYdxmIVKiTg.jpg": "/assets/gaoyi-wu-highline.jpg",
    "yzXkZuukRrIZqunGcSe3B3L45lQ.jpg": "/assets/style-kit/photos/theatre-stage.jpg",
    "M6Qqd3B0kTEyFG5F9hjmFxlols.jpg": "/assets/style-kit/photos/seattle-pike-street-bw.jpg",
    "5OUPML1Rmh2K1mPi5xEfMF8QNOI.jpg": "/assets/style-kit/photos/architecture-model.jpg",
    "UiTg5bttx0MkY2ApPU479YROs.jpg": "/assets/style-kit/photos/retro-computer-hp250.jpg",
}


# Footer art lives in a shared Framer module loaded by every route.
FOOTER_ARTIFACT_MAP = {
    "BLq9oAT9HrWdp5D2W0NTqzKTM.png": "/assets/style-kit/frames/gaoyi-wu-wax-seal.svg",
    "mtYxVS1lgU4Cxmxi9tFTZMy7p8.png": "/assets/style-kit/frames/gaoyi-wu-signature.svg",
}


XCLAW_REPLACEMENTS = [
    ("AKOOL Case Study | Xiaoyang Hu Design Portfolio", "XClaw Case Study | Gaoyi Wu AI Portfolio"),
    (
        "AKOOL AI Image Generator 2.0 | Redesigning AKOOL's core creator workflow to unlock growth, scalability, and seamless cross-tool conversion",
        "XClaw | A desktop workspace for orchestrating AI agents, tool use, and multi-model automation",
    ),
    ("Xiaoyang Hu Design Portfolio", "Gaoyi Wu AI Portfolio"),
    ("Xiaoyang Hu", "Gaoyi Wu"),
    ("AKOOL AI Image Generator 2.0", "XClaw"),
    (
        "Redesigning AKOOL's core creator workflow to unlock growth, scalability, and seamless cross-tool conversion",
        "Designing a desktop workspace for AI agents, tool use, and multi-model automation",
    ),
    ("Sole Designer", "Builder / Designer"),
    ("AI Creation Tool Redesign", "Applied AI Product"),
    ("End-to-End Design", "Agent Workspace"),
    ("Internship", "Self-Directed Build"),
    ("Visit Site", "Live Site"),
    ("+26%", "Desktop"),
    ("Page Traffic", "Agent Hub"),
    ("+18%", "Multi-model"),
    ("Daily Creations", "Workflows"),
    ("3x", "Tool"),
    ("Cross-tool conversions", "Calling"),
    ("Background", "Project Overview"),
    ("1.1 About AKOOL", "1.1 About XClaw"),
    (
        "Akool is one of the fastest-growing AI creative companies in the US.",
        "XClaw is a desktop interface for orchestrating AI agents, model access, and multi-channel workflows in one place.",
    ),
    ("7M+", "Electron"),
    ("Users", "Desktop App"),
    ("73K", "React"),
    ("Companies Using", "Frontend"),
    ("#1", "Agent"),
    ("on Inc. 5000", "Workflows"),
    (
        "By early 2025, Image-to-Video went viral and tripled daily generations, bringing a large wave of new creators.",
        "It started from a simple question: what if model routing, tool use, and channel automation lived in a single operator workspace?",
    ),
    (
        "This sudden growth exposed critical gaps in the aging Image Generator 1.0, which had never been updated since launch.",
        "From that question, I designed a product shell that keeps power-user flows legible instead of scattering them across isolated demos and scripts.",
    ),
    ("1.2 Owning the End-to-End Redesign", "1.2 Owning the End-to-End Build"),
    ("I was the sole designer responsible for this redesign.", "I built the product shell, interaction model, and visual system for XClaw."),
    ("For Image Generator 2.0, I independently drove:", "For XClaw, I independently drove:"),
    ("🔍 UX research", "🔍 Workflow framing"),
    ("🧩 IA (Information Architecture) redesign", "🧩 Agent workflow modeling"),
    ("🎨 Design system updates", "🎨 Visual system and component patterns"),
    ("🔗 Cross-product alignment", "🔗 Tool and model integration planning"),
    ("📱 Responsive and mobile design", "💻 Desktop interaction design"),
    ("🛠️ Developer handoff and QA", "🛠️ Build, iteration, and QA"),
    (
        "I collaborated primarily with 2 engineers and 1 PM, and delivered the full redesign in two month .",
        "I used XClaw to explore how applied AI products can feel operational, legible, and genuinely usable beyond isolated demos.",
    ),
    (
        "Here’s a quick look at the product before and after the redesign.",
        "Here is a quick look at the workspace, routing surfaces, and interaction patterns that shaped the build.",
    ),
    ("Why Redesign", "Why Build It"),
    (
        "Before diving into the redesign, it’s important to understand why the old system could no longer support Akool’s growth.",
        "Before diving into the interface, it helps to understand why an AI agent workspace needs more than a handful of disconnected chat windows.",
    ),
    (
        "Designed for a simple “upload → generate” workflow , IG 1.0 lacked the architecture needed for Akool’s fast expansion into a multi-model, multi-tool ecosystem.",
        "Most AI tooling still treats model access, tool use, and channel automation as separate surfaces, even when users need them to work as one system.",
    ),
    (
        "Akool’s fast expansion into a multi-model, multi-tool ecosystem.",
        "AI tooling's shift toward multi-model, multi-tool ecosystems.",
    ),
    ("From the old experience, three systemic problems emerged.", "From that gap, three product problems emerged."),
    ("A single-purpose IA couldn’t scale", "Agent workflows lived in separate silos"),
    ("No normalization layer across models", "Model and tool actions lacked a shared control surface"),
    ("The Preview UX broke the workflow", "Outputs were hard to inspect, route, and reuse"),
    ("How these problems appeared in the product:", "How those problems appeared in the product:"),
    ("We needed a system that could scale .", "I needed a workspace that could coordinate complex AI workflows without hiding how the system works."),
    ("Design Strategy", "Product Strategy"),
    (
        "In a fast-moving startup, design is often pulled into short-term fires.",
        "In applied AI products, it is easy to optimize for short demos instead of durable operator workflows.",
    ),
    (
        "Instead of letting urgency dictate the direction, I intentionally balanced immediate velocity with system-level decisions to prevent future UX debt and support scalable growth .",
        "I focused on a system that could stay extensible as tools, models, and channels expand, while still feeling understandable for day-to-day use.",
    ),
    ("Shifting to a Two-Pane IA", "Separating orchestration from execution"),
    ("Linear IA tied to a single-purpose workflow", "A narrow workflow could not support real agent operations"),
    ("A linear IA that forces users down a single path, blocking iteration and new feature growth.", "A single linear flow makes it hard to compare outputs, route work, or move between models without losing context."),
    ("Modular IA enabling a flexible, scalable creator workspace", "A modular workspace for routing, inspection, and reuse"),
    ("A modular IA that decouples interaction from workflow steps, supporting iteration, branching, and future tools.", "The workspace separates command, execution, and result management so advanced workflows stay legible instead of collapsing into a chat log."),
    (
        "Adopting a two-pane IA required additional engineering effort and refactoring several core components.",
        "Separating orchestration from execution adds complexity up front, but it makes future tools and channels far easier to integrate cleanly.",
    ),
    (
        "The redesigned IA became a platform pattern reused across other tools such as Image-to-Video, reducing long-term design and engineering alignment cost.",
        "That structure gives XClaw a reusable product pattern for model routing, tool invocation, and output handling as the system grows.",
    ),
    ("Thank you for Visiting", "Thanks for Visiting"),
    ("Eat. Sleep. Design. Repeat.", "Build. Ship. Iterate. Repeat."),
    ("Turning Preview into a Platform-Level Module", "Making tool actions reusable across channels"),
    (
        "Preview inconsistencies across tools revealed a deeper issue: each product had evolved its own logic and workflows, making iteration and cross-tool usage increasingly difficult.",
        "Tool-specific actions often fragment AI products. I wanted the same interaction model to handle inspection, follow-up actions, and routing regardless of channel.",
    ),
    (
        "The unified Preview model now scales consistently across image, video, and audio products.",
        "The result is a unified action surface that stays consistent as XClaw coordinates more models, tools, and delivery paths.",
    ),
    ("1️⃣ A unified Preview architecture that supports consistent actions across tools", "1️⃣ A shared action surface for models, tools, and channels"),
    ("2️⃣ A clear action model: Edit / Send to Tools / Modify", "2️⃣ Clear separation between inspect, route, and act"),
    ("2️⃣ Clear grouping: Edit / Send to Tools / Actions", "3️⃣ Grouped controls that reduce hidden state"),
    ("3️⃣ A media-agnostic structure enabling reuse across image, video, and audio products", "4️⃣ A reusable layout pattern for future AI workflow modules"),
    (
        "A reusable preview module with consistent actions, clearer hierarchies, and seamless cross-tool conversion.",
        "A reusable operator surface with clearer hierarchy and smoother movement between model outputs and downstream actions.",
    ),
    (
        "Now adopted across 9 products and forming a core part of our platform design system.",
        "It became the clearest demonstration of how I think about AI products: make complexity visible, structured, and operable.",
    ),
    ("mshuxy@gmail.com", "criswu20010728@gmail.com"),
    ("https://www.linkedin.com/in/xiaoyang-hu-elena/", "https://www.linkedin.com/in/gaoyiwu/"),
    ("https://github.com/Xiaoyang-Hu-96", "https://github.com/Alfred768"),
    ("https://x.com/elenahuxy", "https://github.com/Alfred768"),
    ("©Xiaoyang Hu 2025", "©Gaoyi Wu 2026"),
]


XCLAW_IMAGE_MAP = {
    "96dmDMZfX9q1dkoi20t38DssV0I.png": "/assets/projects/xclaw-dashboard.webp",
    "tkV8YMxwQ9jcicXmqJTNj7ezPA.png": "/assets/projects/xclaw-chat.webp",
    "5nT4bTw5GICfIsdqHiKUsOZtc.png": "/assets/style-kit/stickers/desktop-computer-3d.png",
    "Qn5DT663azgSlJ2UrrISjQhGA.png": "/assets/style-kit/stickers/robot-3d.png",
    "589XgGvfL1bYnQbHTbNwnx7c.png": "/assets/style-kit/stickers/light-bulb-3d.png",
    "fGf5OlxxIBnzF2SGsf6aoMQW4.png": "/assets/about/xclaw-briefing.webp",
    "iHkpjGuD4OqMB00qSVBM0cnjebM.png": "/assets/about/xclaw-account.webp",
    "IozwJ8q2qibohX5zrP6gkBSoK3s.png": "/assets/about/xclaw-subscription.webp",
    "KpAq2EoBHPwJTHlTmvq99KRQVBM.png": "/assets/about/xclaw-setting.webp",
    "Zxf8OLyndywjsbD4UA7wGyx8iRo.png": "/assets/about/xclaw-channel.webp",
    "mF4D7hozCvee3ALX2s02xIHcnn0.png": "/assets/toolkit/xclaw-mission.webp",
    "f6LAbutaOUk8yEFJhzcs8pLdYI.png": "/assets/toolkit/xclaw-skill.webp",
    "lmORIhu9V9o9UbOttQeoA12M34.png": "/assets/toolkit/xclaw-usage.webp",
    "mVQBlKdwbrEWSYmjhXU10gtERI.png": "/assets/xclaw-editorial-crop-v2.webp",
    "XvszxNrcKtJ74pDP1j1VG53yY.png": "/assets/about/xclaw-todo.webp",
    "zgoEfd5VdlQK3rWWwU85QdJ5HHU.png": "/assets/projects/xclaw-dashboard.webp",
    "GrokZjm4uY9g7ysl6ghyakvnxx0.jpg": "/assets/gaoyi-wu-portrait-studio.jpg",
}


ISEAL_REPLACEMENTS = [
    ("SIEMENS Case Study | Xiaoyang Hu Design Portfolio", "iSeal Case Study | Gaoyi Wu AI Portfolio"),
    (
        "Siemens X Data Hub ETL | Designing a lightweight 0→1 data platform for SMBs to unlock industrial data without heavy engineering overhead",
        "iSeal | Encrypted fingerprinting for reliable black-box LLM ownership verification",
    ),
    ("Xiaoyang Hu Design Portfolio", "Gaoyi Wu AI Portfolio"),
    ("Xiaoyang Hu", "Gaoyi Wu"),
    ("Siemens X Data Hub ETL", "iSeal"),
    (
        "Designing a lightweight 0→1 data platform for SMBs to unlock industrial data without heavy engineering overhead",
        "Encrypted fingerprinting for reliable black-box LLM ownership verification",
    ),
    ("Sole Designer", "Research Lead"),
    ("B2B SaaS", "LLM Security"),
    ("0→1 Product Design", "Ownership Verification"),
    ("Design System", "Adversarial Evaluation"),
    ("Internship", "Research"),
    ("Overview", "Overview"),
    (
        "X Data Hub ETL is a lightweight data platform designed for small and medium-sized businesses (SMBs) to model, integrate, and serve industrial data across IT and OT systems.",
        "iSeal is a cryptographic fingerprinting system for black-box LLM ownership verification, designed to stay reliable even when a model thief controls the inference interface.",
    ),
    (
        "Note: This project is still in development. Due to confidentiality and launch constraints, only high-level design thinking and selected abstractions are shared here ：）",
        "The project combines key-bound encoding, similarity-aware verification, and adversarial testing to separate genuine ownership evidence from harmless model variation.",
    ),
    ("My Role", "My Role"),
    (
        "I worked as the sole product designer on this project, collaborating closely with a product manager and data engineering team.",
        "I led the research and implementation of the ownership-verification pipeline, including method design, LoRA training, attack evaluation, and benchmark analysis.",
    ),
    (
        "I was the sole designer responsible for this redesign.",
        "My work focused on turning a theoretical ownership problem into a measurable and reproducible security system.",
    ),
    ("My responsibilities included:", "Key contributions included:"),
    ("🔍 Defining the product structure from 0→1", "🔍 Designing the key-bound fingerprinting method"),
    ("🧩 Translating data engineering concepts into usable product abstractions", "🧩 Building the verification logic and evaluation pipeline"),
    ("🎨 Designing core workflows and interaction patterns", "🎨 Stress-testing the method under adaptation, quantization, and adversarial attacks"),
    ("🛠️ Establishing a scalable design system for a complex B2B platform", "🛠️ Comparing the method against prior watermarking and ownership baselines"),
    ("The Challenge", "Research Challenge"),
    ("Designing an ETL platform for SMBs presented some unique challenges:", "Reliable ownership verification for black-box LLMs is difficult because the model owner does not control downstream inference behavior."),
    ("Challenge 1", "Challenge 1"),
    ("Flexibility", "Black-box constraints"),
    ("Support diverse data sources and evolving schemas without hard-coded pipelines.", "Verification must work without access to model weights or hidden activations."),
    ("Challenge 2", "Challenge 2"),
    ("Control", "Adversarial adaptation"),
    ("Ensure predictable, transparent workflows instead of opaque automation.", "A model thief can fine-tune, quantize, or manipulate outputs to weaken ownership signals."),
    ("Challenge 3", "Challenge 3"),
    ("Lightweight", "Efficiency"),
    ("Reduce engineering overhead while retaining core ETL capabilities.", "The method needs to be practical enough to train and test across many model scales."),
    (
        "Balancing these constraints required careful product-level design judgment rather than surface-level UI optimization.",
        "Balancing these constraints required a method that was robust, measurable, and efficient enough to evaluate at scale.",
    ),
    ("Design Focus", "Method Focus"),
    (
        "Given the early stage of the product, my design work focused on establishing a strong foundation rather than polishing individual screens.",
        "The research centered on three foundations rather than a single benchmark win.",
    ),
    ("Key areas of focus included:", "Core areas of focus included:"),
    ("Defining clear boundaries between data sources, models, pipelines, and services", "Binding the verification key directly to the model-side encoder"),
    ("Designing configuration-driven workflows that scale without becoming chaotic", "Separating ownership evidence from normal model variation with Bayesian thresholds"),
    ("Creating shared interaction patterns that could be reused across multiple modules", "Testing the method against collusion-based unlearning, response manipulation, and quantization"),
    ("Building a design system that supports rapid iteration and future expansion", "Keeping LoRA-based training efficient enough for broad comparative experiments"),
    ("Outcome (So Far)", "Results"),
    ("Although the product has not yet launched, the design work helped:", "The resulting system showed strong performance across models and attacks:"),
    ("🧠", "⚡"),
    ("Align product, design, and engineering teams around shared mental models", "46× faster key-bound encoder training than the WLM baseline on A100"),
    ("📈", "🔒"),
    ("Create a scalable structure for future feature development", "100% fingerprint success rate across 12 LLMs from 125M to 13B parameters"),
    ("✨", "🧪"),
    ("Reduce design and engineering rework as requirements evolved", "Reliable verification under 10+ attacks, Alpaca fine-tuning, and 8/16-bit quantization"),
    (
        "This project marked a shift in my practice, from designing individual interfaces to designing systems and constraints that enable long-term product growth.",
        "The project sharpened how I approach AI security: combine theory, evaluation discipline, and systems thinking so the method holds up under real deployment pressure.",
    ),
    ("What’s Next", "Why It Matters"),
    ("As the product continues to evolve, future work will focus on:", "iSeal matters because model ownership is increasingly valuable, and verification systems must stay reliable even when the attacker controls the interface."),
    ("Improving onboarding for first-time users", "It is a step toward security methods that work in realistic black-box settings rather than only in idealized lab conditions."),
    ("Progressive disclosure for advanced configuration", "It also shows how efficient LoRA-based security tooling can make large comparative studies more practical."),
    ("Better visibility into system states and data flow health", "Future work can extend the approach to broader model families and stronger adaptive attacks."),
    ("Thanks for taking the time to read this case study ;D", "Thanks for reading this case study."),
    ("If the work resonates or sparks your curiosity, I’d love to chat.", "If this work resonates, I would be glad to talk more about LLM security and applied AI systems."),
    ("Thank you for Visiting", "Thanks for Visiting"),
    ("Eat. Sleep. Design. Repeat.", "Build. Evaluate. Improve. Repeat."),
    ("mshuxy@gmail.com", "criswu20010728@gmail.com"),
    ("https://www.linkedin.com/in/xiaoyang-hu-elena/", "https://www.linkedin.com/in/gaoyiwu/"),
    ("https://github.com/Xiaoyang-Hu-96", "https://github.com/Alfred768"),
    ("https://x.com/elenahuxy", "https://github.com/Alfred768"),
    ("©Xiaoyang Hu 2025", "©Gaoyi Wu 2026"),
]


ISEAL_IMAGE_MAP = {
    "553tLjwoxAzzc8aZAVIwU4IQ.png": "/assets/iseal-editorial-diagram.webp",
    "tdJhc7cvihqN8vgVq5p6lzPGVT0.png": "/assets/projects/iseal-pipeline.webp",
    "VVAWYlcaqJzMHNIxAJvUYAo4Ib8.jpeg": "/assets/projects/iseal-results.webp",
}


COMMON_RUNTIME_REPLACEMENTS = [
    ("Xiaoyang Hu Design Portfolio", "Gaoyi Wu AI Portfolio"),
    ("Xiaoyang Hu", "Gaoyi Wu"),
    ("mshuxy@gmail.com", "criswu20010728@gmail.com"),
    ("https://www.linkedin.com/in/xiaoyang-hu-elena/", "https://www.linkedin.com/in/gaoyiwu/"),
    ("https://github.com/Xiaoyang-Hu-96", "https://github.com/Alfred768"),
    ("https://x.com/elenahuxy", "https://github.com/Alfred768"),
    ("©Xiaoyang Hu 2025", "©Gaoyi Wu 2026"),
]

HOME_RUNTIME_REWRITES = [
    ("Lanma.ai", "__gaoyi_retired_lanma__"),
    ("Mobile Now", "__gaoyi_retired_mobile_now__"),
    ("href:`/akool/`", "href:`/xclaw/`"),
    ("href:`/siemens/`", "href:`/iseal/`"),
    ("https://www.museumofflight.org/", WEBWEAVER_LINK),
    ("Coming Soon", "Read Paper"),
    ("https://configpins.xiaoyanghu.com/", "https://github.com/Alfred768"),
    ("https://lobster-watch-landing.netlify.app/", "https://github.com/Alfred768"),
    ("https://www.instagram.com/eyes.of.elena/", "https://github.com/Alfred768"),
]

XCLAW_RUNTIME_REWRITES = [("https://akool.com/", "https://www.x-claw.shop/")]
ISEAL_RUNTIME_REWRITES = [("https://www.siemens.com/us/en.html", "https://arxiv.org/abs/2511.08905")]

SEARCH_INDEX_REWRITES = [
    ('"url":"/akool"', '"url":"/xclaw"'),
    ('"url":"/siemens"', '"url":"/iseal"'),
]


def replace_runtime_images(code: str, image_map: dict[str, str]) -> str:
    """Replace Framer's responsive image URLs with the downloaded local assets."""
    for basename, local_path in image_map.items():
        # Framer emits local and absolute responsive paths inside template
        # literals. Replace the stable asset prefix first so every src/srcSet
        # entry survives regardless of the following query-string syntax.
        code = code.replace(
            f"/framerusercontent.com/images/{basename}",
            local_path,
        ).replace(
            f"https://framerusercontent.com/images/{basename}",
            local_path,
        )
        code = re.sub(
            rf"(?:https://framerusercontent\\.com|/framerusercontent\\.com)/images/{re.escape(basename)}(?:\\?[^`\\\"']*)?",
            local_path,
            code,
        )
    return code


def localize_runtime_urls(code: str) -> str:
    """Make every runtime asset resolve through Vite rather than the live site."""
    return (
        code.replace("https://framerusercontent.com/", "/framerusercontent.com/")
        .replace("https://fonts.gstatic.com/", "/fonts.gstatic.com/")
        # Image props in Framer modules normalize replacement paths as URLs.
        # Keep personalized files on this site's public /assets route.
        .replace("https://assets/", "/assets/")
    )


def smooth_beyond_work_photo_motion(code: str) -> str:
    """Replace the abrupt stock photo-stack animation with a gentler interaction."""
    replacements = {
        "Dp.fromTo(g.current,{scale:0},{scale:1,stagger:b,ease:y,delay:l,duration:x})": (
            "Dp.fromTo(g.current,{scale:.9,opacity:0,y:18},"
            "{scale:1,opacity:1,y:0,stagger:.11,ease:`power3.out`,delay:l+.08,duration:.82})"
        ),
        "if(n===e){let e=T(i);Dp.to(r,{transform:e,duration:.4,ease:`back.out(1.4)`,overwrite:`auto`})}else{let t=E(i,n<e?-160:160),a=Math.abs(e-n)*.05;Dp.to(r,{transform:t,duration:.4,ease:`back.out(1.4)`,delay:a,overwrite:`auto`})}": (
            "if(n===e){Dp.to(r,{y:-16,scale:1.035,duration:.62,ease:`power3.out`,overwrite:`auto`})}"
            "else{let t=E(i,n<e?-42:42),a=Math.abs(e-n)*.035;"
            "Dp.to(r,{transform:t,scale:.985,duration:.62,ease:`power3.out`,delay:a,overwrite:`auto`})}"
        ),
        "Dp.to(n,{transform:r,duration:.4,ease:`back.out(1.4)`,overwrite:`auto`})": (
            "Dp.to(n,{transform:r,y:0,scale:1,duration:.68,ease:`power3.inOut`,overwrite:`auto`})"
        ),
    }

    for original, replacement in replacements.items():
        if original not in code:
            raise RuntimeError("Could not find the expected Beyond the Work photo-stack animation.")
        code = code.replace(original, replacement, 1)

    return code


def replace_runtime_copy(code: str, replacements: list[tuple[str, str]]) -> str:
    """Apply long copy changes before their shorter constituent phrases."""
    for old, new in sorted(replacements, key=lambda pair: len(pair[0]), reverse=True):
        code = code.replace(old, new)
    return code


def ensure_runtime_templates() -> None:
    """Snapshot the downloaded Framer runtime once, before producing variants."""
    if RUNTIME_TEMPLATE_ROOT.exists():
        return
    shutil.copytree(RUNTIME_ROOT, RUNTIME_TEMPLATE_ROOT)


def build_runtime() -> None:
    """Personalize the same modules Framer reads during client hydration."""
    ensure_runtime_templates()

    home_module = "oJu-iJ5QXN-FJjJoTqU4JzEbkfZsASp8LUvNHBo-EKg.BYm9xDs6.mjs"
    home_metadata = "4yxpiHDAJFNiLrcsOOmjQnEH7_FozzjTKbUUwVZPs94.D1AHhbS0.mjs"
    xclaw_module = "b-oDM3tLJwW1NSyYu6julwLYrbJPzannbSjSdD9h3vg.V_NpFb6U.mjs"
    xclaw_metadata = "8UD7uZfC7n3_RBT9yF7Pp_793RlkFPXVcwyUNlG_gz4.BzMyPGmK.mjs"
    iseal_module = "agW-M-ChECQkQiVR-0Q1O8656H9wYKCy4nXH3AQ6VHM.aqzt6pSg.mjs"
    iseal_metadata = "LDDGfAxFH-F6LocDYhpp7am8uuGTxvgTeMjW-N8shbA.aTyrxSDD.mjs"

    for template_path in RUNTIME_TEMPLATE_ROOT.rglob("*.mjs"):
        code = template_path.read_text(encoding="utf-8")
        name = template_path.name

        if name in {home_module, home_metadata}:
            code = replace_runtime_copy(code, HOME_REPLACEMENTS + HOME_RUNTIME_REWRITES)
            code = replace_runtime_images(code, HOME_IMAGE_MAP)
            if name == home_module:
                code = smooth_beyond_work_photo_motion(code)
        elif name in {xclaw_module, xclaw_metadata}:
            code = replace_runtime_copy(code, XCLAW_REPLACEMENTS + XCLAW_RUNTIME_REWRITES)
            code = replace_runtime_images(code, XCLAW_IMAGE_MAP)
        elif name in {iseal_module, iseal_metadata}:
            code = replace_runtime_copy(code, ISEAL_REPLACEMENTS + ISEAL_RUNTIME_REWRITES)
            code = replace_runtime_images(code, ISEAL_IMAGE_MAP)
        else:
            code = replace_runtime_copy(code, COMMON_RUNTIME_REPLACEMENTS)

        code = replace_runtime_copy(code, PROFILE_URL_REWRITES)
        code = replace_runtime_images(code, FOOTER_ARTIFACT_MAP)

        output_path = RUNTIME_ROOT / template_path.relative_to(RUNTIME_TEMPLATE_ROOT)
        output_path.write_text(localize_runtime_urls(code), encoding="utf-8")


def build_search_indexes() -> None:
    """Keep client search results aligned with the personalized page copy."""
    for template_path in RUNTIME_TEMPLATE_ROOT.glob("searchIndex-*.json"):
        content = template_path.read_text(encoding="utf-8")
        content = replace_runtime_copy(
            content,
            HOME_REPLACEMENTS
            + XCLAW_REPLACEMENTS
            + ISEAL_REPLACEMENTS
            + COMMON_RUNTIME_REPLACEMENTS
            + SEARCH_INDEX_REWRITES,
        )
        output_path = RUNTIME_ROOT / template_path.relative_to(RUNTIME_TEMPLATE_ROOT)
        output_path.write_text(localize_runtime_urls(content), encoding="utf-8")


def build_home() -> None:
    html = (SOURCE_ROOT / "index.html").read_text(encoding="utf-8")
    html = replace_strings(html, HOME_REPLACEMENTS)
    html = replace_runtime_copy(html, PROFILE_URL_REWRITES)
    html = html.replace('data-framer-name="Instagram" name="Instagram"', 'data-framer-name="LinkedIn" name="LinkedIn"')
    html = html.replace('name="Instagram"', 'name="LinkedIn"')
    html = html.replace('href="/akool/"', 'href="/xclaw/"')
    html = html.replace(
        'href="/siemens/"',
        'aria-label="Read the iSeal paper on arXiv" '
        'href="https://arxiv.org/abs/2511.08905" rel="noopener noreferrer" target="_blank"',
    )
    html = html.replace("https://www.siemens.com/us/en.html", LINKEDIN_LINK)
    html = html.replace("https://akool.com/", GITHUB_LINK)
    html = html.replace("https://www.museumofflight.org/", WEBWEAVER_LINK)
    html = html.replace(
        '<link href="https://xiaoyanghu.com/" rel="canonical"/><meta content="https://xiaoyanghu.com/" property="og:url"/>',
        "",
    )
    html = html.replace(
        '<link href="/" rel="canonical"/><meta content="/" property="og:url"/>',
        "",
    )
    html = html.replace("https://configpins.xiaoyanghu.com/", "https://github.com/Alfred768")
    html = html.replace("https://lobster-watch-landing.netlify.app/", "https://github.com/Alfred768")
    html = html.replace(
        "https://www.linkedin.com/posts/xiaoyang-hu-elena_people-kept-asking-how-i-built-my-portfolio-activity-7442971154572533760-QtAZ?utm_source=share&amp;utm_medium=member_desktop&amp;rcm=ACoAAEcv5iUB4EAJDUA_lCMCTIQx6D4EPoaoekc",
        PORTFOLIO_POST_LINK,
    )
    html = html.replace(
        "https://www.linkedin.com/posts/xiaoyang-hu-elena_creativecoding-vibecoding-interactiondesign-activity-7408990860836794368-vfqa?utm_source=share&amp;utm_medium=member_desktop&amp;rcm=ACoAAEcv5iUB4EAJDUA_lCMCTIQx6D4EPoaoekc",
        XRAY_LINK,
    )
    html = html.replace("https://www.instagram.com/eyes.of.elena/", "https://github.com/Alfred768")
    html = replace_images(html, HOME_IMAGE_MAP)
    html = prune_retired_experience_cards(html)
    html = repair_xclaw_experience_copy(html)
    html = repair_shenzhen_experience_copy(html)
    html = remove_applied_ai_notes_links(html)
    html = apply_profile_footer_links(html)
    html = inject_gaoyi_footer_artwork(html)
    html = inject_gaoyi_name_story(html)
    html = inject_polaroid_repair(html)
    html = inject_about_camera_portrait(html)
    html = inject_hero_anime_greeting(html)
    html = inject_hero_previous_logos_cleanup(html)
    html = inject_project_preview_image_repair(html)
    html = inject_xclaw_project_art(html)
    html = inject_iseal_project_art(html)
    html = inject_webweaver_project_art(html)
    html = inject_applied_ai_notes_cleanup(html)
    html = inject_experience_personalization(html)
    html = inject_profile_footer_link_binding(html)
    html = preserve_framer_runtime(html)
    write_text(ROOT / "index.html", html)


def build_xclaw() -> None:
    html = (ROOT / "templates/xclaw-case-study.html").read_text(encoding="utf-8")
    write_text(ROOT / "xclaw/index.html", html)


def build_iseal() -> None:
    html = (SOURCE_ROOT / "siemens/index.html").read_text(encoding="utf-8")
    html = replace_strings(html, ISEAL_REPLACEMENTS)
    html = replace_runtime_copy(html, PROFILE_URL_REWRITES)
    html = html.replace('data-framer-name="Instagram" name="Instagram"', 'data-framer-name="LinkedIn" name="LinkedIn"')
    html = html.replace('name="Instagram"', 'name="LinkedIn"')
    html = html.replace(
        '<link href="https://xiaoyanghu.com/siemens" rel="canonical"/><meta content="https://xiaoyanghu.com/siemens" property="og:url"/>',
        "",
    )
    html = html.replace(
        '<link href="/iseal/" rel="canonical"/><meta content="/iseal/" property="og:url"/>',
        "",
    )
    html = html.replace("https://www.siemens.com/us/en.html", "https://arxiv.org/abs/2511.08905")
    html = replace_images(html, ISEAL_IMAGE_MAP)
    html = apply_profile_footer_links(html)
    html = inject_profile_footer_link_binding(html)
    html = preserve_framer_runtime(html)
    write_text(ROOT / "iseal/index.html", html)


def main() -> None:
    build_runtime()
    build_search_indexes()
    build_home()
    build_xclaw()
    build_iseal()


if __name__ == "__main__":
    main()
