# Design QA

## Comparison Setup

- Source visual truth: `/Users/wugaoyi/Learning/求职/Portfolio/tmp/design-qa/source-editorial-dossier.png`
- Implementation URL: `http://127.0.0.1:5173/`
- Primary implementation screenshot: `/Users/wugaoyi/Learning/求职/Portfolio/tmp/design-qa/portfolio-desktop-final-v3.png`
- Full-view comparison: `/Users/wugaoyi/Learning/求职/Portfolio/tmp/design-qa/desktop-side-by-side-final.png`
- Focused research evidence: `/Users/wugaoyi/Learning/求职/Portfolio/tmp/design-qa/portfolio-research-final.png`
- Mobile Chinese evidence: `/Users/wugaoyi/Learning/求职/Portfolio/tmp/design-qa/portfolio-mobile-zh.png`
- Desktop viewport: 1280 × 720
- Mobile viewport: 390 × 844
- State: English default hero and research; Chinese mobile hero

## Findings

No actionable P0, P1, or P2 findings remain.

### Fonts and Typography

- The implementation uses Bodoni Moda for display typography and Inter / Noto Sans SC for body copy.
- The large name, role, research titles, metrics, and small technical labels reproduce the selected editorial hierarchy.
- English and Chinese headings wrap without clipping. Optical weight and spacing remain legible at desktop and mobile sizes.

### Spacing and Layout Rhythm

- The final desktop pass places identity, role, portrait, calls to action, and all four proof metrics inside the first viewport.
- Thin rules, open paper space, and alternating research spreads reproduce the reference rhythm without copying its exact composition.
- The mobile layout becomes a single reading column with no horizontal overflow.

### Colors and Visual Tokens

- Warm ivory paper, near-black ink, muted graphite, and restrained burnt orange closely match the selected direction.
- The background uses a real generated paper texture asset instead of a CSS noise approximation.
- Text and controls retain clear contrast and visible focus treatment.

### Image Quality and Asset Fidelity

- The implementation uses Gaoyi's real portrait and generated project-specific iSeal and WebWeaver editorial illustrations.
- Research assets share the paper, ink, stippling, and orange spot-color treatment of the source.
- The portrait uses a rectangular editorial crop instead of the source mock's cutout treatment. This is an intentional identity-preservation choice and does not reduce hierarchy or usability.

### Copy and Content

- The visible content is resume-backed and prioritizes AI Algorithm Engineer positioning.
- iSeal, WebWeaver, Intellisys Lab, and DHL Express claims use verified metrics and real publication destinations.
- English and Chinese content switch together and preserve the same hierarchy.

### Interaction and Accessibility

- Header navigation targets existing sections.
- The language switch exposes selected state and persists locally.
- Research methodology controls expose `aria-expanded` and reveal real secondary content.
- Mobile navigation, reduced-motion behavior, keyboard focus, external links, and image fallback behavior are implemented.
- Browser console review found no warnings or errors.

## Patches Made During QA

- Reduced hero height and tightened display typography so the proof strip appears above the fold.
- Rebalanced hero spacing and metric density against the selected source.
- Corrected research-image aspect ratios to preserve the complete generated diagrams.
- Added minimum-width and wrap protections for editorial grid copy.
- Shortened the visible mobile navigation label while preserving the localized accessible name.
- Verified Chinese hero and research layouts at mobile width.

## Focused Region Review

The research section received a focused review because its display typography, diagram crop, metadata line, and multi-column spacing were too small to judge from the hero comparison. The final research screenshot shows the section heading, iSeal metadata, and generated illustration aligned to the same editorial system with no clipping or placeholder assets.

## Follow-up Polish

- P3: A professionally produced transparent portrait cutout could move the hero even closer to the source mock, but the current real-photo crop is sharper and safer for identity fidelity.

final result: passed
