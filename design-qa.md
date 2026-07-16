# Design QA — Xiaoyang Hu portfolio adaptation

> Historical note: the prior Sac Editorial Portfolio QA record is retained below for continuity; the active validation for this task starts at **Xiaoyang Hu portfolio adaptation**.

## Prior QA record — Sac Editorial Portfolio

- Source visual truth: `/tmp/sac-ai-reference/editorial-manifesto/reference/01-hero.png` and `/tmp/sac-ai-reference/editorial-manifesto/reference/02-about.png`
- Implementation: `http://127.0.0.1:5175/`
- Desktop viewport: `1672 × 941`
- Mobile viewport: `390 × 844`
- State: English, initial hero; About anchor; mobile navigation open
- Full-view comparison evidence: `tmp/qa/hero-comparison-pass1.png`, `tmp/qa/about-comparison.png`
- Focused comparison evidence: `tmp/qa/hero-focused-comparison.png`
- Responsive evidence: `tmp/qa/implementation-mobile-v2.png`

- No actionable P0, P1, or P2 issues remained.
- [P3] The source used a high-contrast orange/black manga illustration, while that portfolio intentionally used Gaoyi Wu's transparent photographic cutout.
- [P3] The About section carried more recruiting evidence than the source social-platform roster.

---

## Evidence

- Source (desktop, top-of-page idle state): `.codex-artifacts/xiaoyanghu-check/source-desktop-current.png`
- Implementation (desktop, same state): `.codex-artifacts/xiaoyanghu-check/local-desktop-current.png`
- Side-by-side comparison: `.codex-artifacts/xiaoyanghu-check/desktop-comparison-current.png`
- Source and implementation mobile captures: `.codex-artifacts/xiaoyanghu-check/source-home-mobile.png` and `.codex-artifacts/xiaoyanghu-check/local-home-mobile.png`
- Route captures: `.codex-artifacts/xiaoyanghu-check/local-akool-desktop.png` and `.codex-artifacts/xiaoyanghu-check/local-siemens-desktop.png`

## Scope and states checked

- Desktop homepage at 1440 px: hero, sidebar, project heading, first project card, typography, borders, spacing, source visual assets, and custom XClaw artwork.
- Mobile layout at approximately 390 px: stacked hero, compact navigation, project heading, and desktop-only notice.
- Project routes: `/xclaw/` and `/iseal/` resolve and expose their expected case-study headings.
- Browser console: no error-level messages in the local prototype.

## Comparison history

1. Initial static export left Framer hydration scripts active, so their client runtime could replace personalized text with the original source content.
2. The generator now removes that runtime/hydration layer and preserves the SSR visual state, including elements that would otherwise remain invisible after animation initialization.
3. Re-generated all three routes, rechecked stale source copy, and compared the desktop source and prototype at the identical idle state.

## Findings

- No P0, P1, or P2 visual defects remain in the checked surfaces.
- The original layout, locally copied source assets, visual treatment, and responsive structure are retained; only approved portfolio copy and selected project imagery are personalized.
- The original site's Framer-driven decorative motion is intentionally delivered as a static visual state in this local artifact. Primary project routes remain functional.

## Verification

- `python3 scripts/personalize_clone.py` completed and found no stale checked source strings in `index.html`, `xclaw/index.html`, or `iseal/index.html`.
- `npm run build` passed without warnings.
- Direct route verification passed for `http://localhost:4173/xclaw/` and `http://localhost:4173/iseal/`.

## Final result

final result: passed
