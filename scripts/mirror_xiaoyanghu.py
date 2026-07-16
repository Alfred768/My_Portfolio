#!/usr/bin/env python3

from __future__ import annotations

import argparse
import concurrent.futures
import re
import sys
from collections import deque
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


SOURCE_URL = "https://xiaoyanghu.com/"
ROOT = Path(__file__).resolve().parent.parent
PUBLIC_DIR = ROOT / "public"
TEMPLATE_ROOT = ROOT / "templates" / "source"
SOURCE_HOST = urlparse(SOURCE_URL).netloc
MIRROR_HOSTS = {"framerusercontent.com", "fonts.gstatic.com"}
TRACKING_PREFIXES = (
    "https://t.contentsquare.net/",
    "https://www.googletagmanager.com/",
    "https://events.framer.com/script",
)
TRACKING_SNIPPETS = (
    "gtag(",
    "contentsquare",
    "__framer_force_showing_editorbar_since",
)
URL_PATTERN = re.compile(r"https://[^\s\"'<>\\)]+")
CONTROL_CHARS = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F]")
ASSET_SUFFIXES = (
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".gif",
    ".svg",
    ".mp4",
    ".mp3",
    ".wav",
    ".pdf",
    ".woff2",
    ".woff",
    ".ttf",
    ".otf",
    ".css",
    ".js",
    ".mjs",
    ".json",
)
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0.0.0 Safari/537.36"
)


def fetch_text(url: str) -> str:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8")


def fetch_bytes(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=60) as response:
        return response.read()


def strip_tracking(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    for tag in list(soup.find_all("script")):
        src = tag.get("src", "")
        text = tag.string or tag.get_text()

        if any(src.startswith(prefix) for prefix in TRACKING_PREFIXES):
            tag.decompose()
            continue

        if any(snippet in text for snippet in TRACKING_SNIPPETS):
            tag.decompose()

    for tag in list(soup.find_all("link", rel="preconnect")):
        href = tag.get("href", "")
        if href.startswith("https://fonts.gstatic.com"):
            tag.decompose()

    return str(soup)


def collect_urls(html: str) -> list[str]:
    urls = set(URL_PATTERN.findall(html))
    mirrored = set()

    for url in urls:
        parsed = urlparse(url)
        if parsed.netloc in MIRROR_HOSTS:
            mirrored.add(f"{parsed.scheme}://{parsed.netloc}{parsed.path}")

    return sorted(mirrored)


def collect_internal_routes(html: str, page_url: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    routes = set()

    for tag in soup.find_all("a"):
        href = tag.get("href", "").strip()

        if not href or href.startswith(("#", "mailto:", "tel:")):
            continue

        resolved = urlparse(urljoin(page_url, href))
        if resolved.netloc and resolved.netloc != SOURCE_HOST:
            continue
        if resolved.path.startswith("/framerusercontent.com/"):
            continue
        if resolved.path.lower().endswith(ASSET_SUFFIXES):
            continue

        path = resolved.path or "/"
        if path != "/" and path.endswith("/"):
            path = path[:-1]
        routes.add(path)

    return sorted(routes)


def local_path_for(url: str) -> Path:
    parsed = urlparse(url)
    relative = parsed.netloc + parsed.path
    return PUBLIC_DIR / relative


def download_one(url: str, force: bool = False) -> tuple[str, str]:
    output_path = local_path_for(url)

    if output_path.exists() and not force:
        return url, "cached"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(fetch_bytes(url))
    return url, "downloaded"


def rewrite_urls(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup.find_all("a"):
        href = tag.get("href", "").strip()

        if not href or href.startswith(("#", "mailto:", "tel:")):
            continue

        resolved = urlparse(urljoin(SOURCE_URL, href))
        if resolved.netloc and resolved.netloc != SOURCE_HOST:
            continue
        if resolved.path.lower().endswith(ASSET_SUFFIXES):
            continue
        if resolved.path.startswith("/framerusercontent.com/"):
            continue

        path = resolved.path or "/"
        if path == "/":
            tag["href"] = "/"
        else:
            tag["href"] = f"{path.rstrip('/')}/"

    rewritten = str(soup)
    rewritten = rewritten.replace("https://framerusercontent.com/", "/framerusercontent.com/")
    rewritten = rewritten.replace("https://fonts.gstatic.com/", "/fonts.gstatic.com/")
    return CONTROL_CHARS.sub("", rewritten)


def output_path_for_route(route: str) -> Path:
    if route == "/":
        return TEMPLATE_ROOT / "index.html"

    return TEMPLATE_ROOT / route.lstrip("/") / "index.html"


def crawl_site() -> tuple[dict[str, str], list[str]]:
    pages: dict[str, str] = {}
    mirrored_assets: set[str] = set()
    queue = deque(["/"])
    visited = set()

    while queue:
        route = queue.popleft()
        if route in visited:
            continue

        visited.add(route)
        page_url = urljoin(SOURCE_URL, route.lstrip("/"))
        cleaned_html = strip_tracking(fetch_text(page_url))
        pages[route] = cleaned_html
        mirrored_assets.update(collect_urls(cleaned_html))

        for internal_route in collect_internal_routes(cleaned_html, page_url):
            if internal_route not in visited:
                queue.append(internal_route)

    return pages, sorted(mirrored_assets)


def mirror(force: bool = False, workers: int = 12) -> None:
    pages, mirrored_urls = crawl_site()

    print(
        f"Found {len(pages)} mirrored pages and {len(mirrored_urls)} mirrored assets.",
        file=sys.stderr,
    )

    downloaded = 0
    cached = 0
    failures: list[tuple[str, Exception]] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(download_one, url, force): url for url in mirrored_urls
        }

        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            try:
                _, status = future.result()
                if status == "downloaded":
                    downloaded += 1
                else:
                    cached += 1
            except Exception as error:  # pragma: no cover - best effort mirror
                failures.append((url, error))

    if failures:
        for url, error in failures:
            print(f"Failed to mirror {url}: {error}", file=sys.stderr)
        raise SystemExit(1)

    written_pages = []

    for route, html in pages.items():
        output_path = output_path_for_route(route)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rewrite_urls(html), encoding="utf-8")
        written_pages.append(str(output_path))

    print(
        "Wrote mirrored pages:\n- " + "\n- ".join(written_pages),
        file=sys.stderr,
    )
    print(
        f"Asset mirror summary: {downloaded} downloaded, {cached} cached.",
        file=sys.stderr,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Mirror https://xiaoyanghu.com/ into the local Vite project."
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Redownload mirrored assets even if they already exist locally.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=12,
        help="Number of concurrent asset downloads.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    mirror(force=args.force, workers=max(1, args.workers))


if __name__ == "__main__":
    main()
