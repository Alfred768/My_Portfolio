# Design QA — Sac Editorial Portfolio

- Source visual truth: `/tmp/sac-ai-reference/editorial-manifesto/reference/01-hero.png` and `/tmp/sac-ai-reference/editorial-manifesto/reference/02-about.png`
- Implementation: `http://127.0.0.1:5175/`
- Desktop viewport: `1672 × 941`
- Mobile viewport: `390 × 844`
- State: English, initial hero; About anchor; mobile navigation open
- Full-view comparison evidence: `tmp/qa/hero-comparison-pass1.png`, `tmp/qa/about-comparison.png`
- Focused comparison evidence: `tmp/qa/hero-focused-comparison.png`
- Responsive evidence: `tmp/qa/implementation-mobile-v2.png`

## Findings

- No actionable P0, P1, or P2 issues remain.
- [P3] The source uses a high-contrast orange/black manga illustration, while the portfolio intentionally uses Gaoyi Wu's transparent photographic cutout. The replacement preserves the same right-heavy subject composition, oversized serif wordmark, cream paper field, orange accent, registration marks, and editorial rhythm while keeping the candidate recognizable.
- [P3] The About section carries more evidence and education content than the source social-platform roster, so it extends beyond one viewport on shorter displays. This is an intentional content adaptation for recruiting rather than a structural drift.

## Required Fidelity Surfaces

- Fonts and typography: Playfair Display provides the high-contrast editorial serif; Inter and Noto Sans SC cover UI and bilingual copy. Display scale, tight tracking, small uppercase navigation, and mono metadata follow the source hierarchy without clipping.
- Spacing and layout rhythm: Desktop hero and About retain the source's two-column composition, fixed header, left registration rail, thin rules, large negative space, and full-height sections. Mobile has no horizontal overflow.
- Colors and visual tokens: Warm cream paper, near-black ink, muted rules, and restrained orange accents closely track the source palette.
- Image quality and asset fidelity: The portrait is a real RGBA cutout with intact hair and clean transparent edges. It is rendered without stretching; its circular technical field and registration marks match the source art direction.
- Copy and content: Source labels are replaced with resume-backed recruiting content, measurable outcomes, publications, experience, role targets, and direct contact paths.

## Patches Made During QA

- Reduced mobile portrait height from `29rem` to `19rem`.
- Reduced mobile portrait width and wordmark scale so name, role, specialization, and summary appear in the opening viewport.
- Confirmed the mobile menu exposes all five navigation links and changes to an expanded close state.

## Verification

- Desktop console errors/warnings: none.
- Mobile console errors/warnings: none.
- Mobile horizontal overflow: none.
- Focused interaction: mobile navigation opens and exposes About, Research, Experience, Projects, and Contact.

final result: passed
