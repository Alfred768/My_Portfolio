# Sac Editorial Portfolio Redesign

Date: 2026-06-30
Status: Approved design brief
Primary reference: `Sac-Y/sac-ai.com` at commit `86473fc`
Target project: Gaoyi Wu AI Algorithm Engineer portfolio

## 1. Objective

Rebuild the portfolio as a faithful, responsive interpretation of the actual
`sac-ai.com` Editorial Manifesto site. Preserve the reference site's page
rhythm, typographic hierarchy, paper-like visual system, fixed navigation,
editorial grids, reveal motion, and mobile reflow while replacing Sac's
creator content with Gaoyi Wu's job-search narrative.

The result must prioritize AI Algorithm Engineer, Applied AI/ML, LLM security,
and multi-agent systems roles. It must remain bilingual and keep every
recruiter-facing action functional.

## 2. Source of Truth

Visual and interaction decisions follow the reference repository rather than
the earlier single-screen dossier screenshot.

Reference characteristics to reproduce:

- warm cream paper canvas with subtle grain;
- near-black ink, muted brown-gray metadata, and saturated orange accent;
- Playfair-style display serif paired with restrained sans and mono metadata;
- fixed top navigation with thin separators and compact uppercase labels;
- left rhythm rail, fine rules, targets, crosses, and technical annotations;
- oversized hero wordmark balanced against a transparent cutout portrait;
- viewport-scale sections with generous editorial whitespace;
- thin-rule archives, asymmetric grids, understated hover transitions, and
  scroll reveal;
- dedicated mobile composition rather than a scaled-down desktop page.

The implementation will reproduce the system and composition in React without
copying the reference site's content.

## 3. Content Mapping

### Navigation

- Brand: Gaoyi Wu
- About
- Research
- Experience
- Projects
- Education
- Contact
- Language control: EN / 中文
- Resume action

### Hero

- Oversized wordmark: `GAOYI WU`
- Kicker: `AI Algorithm Engineer`
- Positioning statement:
  `LLM Security × Multi-Agent Systems × Applied ML`
- Short job-search value proposition
- Primary action: resume
- Secondary action: contact
- Right-side transparent natural-color cutout from
  `public/assets/gaoyi-wu-portrait-studio.jpg`
- Reference-style registration marks and restrained technical metadata

### About / Research Profile

The reference About section becomes a compact professional profile:

- left: “About me,” short research-and-delivery narrative, and a technical
  blueprint-style profile panel;
- right: three research workflow nodes and a signal table containing evidence
  such as AAAI 2026, two publications, 100+ edge devices, and the 61% to 94%
  accuracy gain;
- skills and education appear as concise archive metadata rather than large
  independent marketing cards.

### Research

The reference Writing section becomes Selected Research:

- featured entry: iSeal;
- supporting entry: WebWeaver;
- real paper links and publication metadata;
- editorial thumbnails using existing project artwork;
- titles, contribution summaries, methods, and measurable results;
- hover and focus behavior modeled after the reference feature/archive rows.

### Experience and Projects

The reference Work archive becomes Applied ML Experience:

- Intellisys Lab;
- DHL Express;
- selected technical projects where verified content exists;
- index, date, role, concise impact summary, thumbnail/logo, and directional
  arrow;
- rows remain scannable for recruiters and keyboard accessible.

### Contact

- oversized “Let’s work together” treatment;
- availability indicator for AI Algorithm and Applied AI/ML roles;
- email, LinkedIn, GitHub, location, and resume actions;
- scrolling keyword rail adapted to the candidate's technical focus;
- compact footer with copyright, location, and back-to-top action.

## 4. Portrait Asset

Create `public/assets/gaoyi-wu-cutout.png` from the existing studio portrait.

Requirements:

- remove the blue-gray background completely;
- preserve fine hair edges, ears, arms, shirt silhouette, and clothing detail;
- keep the subject in natural color;
- do not redraw, beautify, restyle, or synthesize facial details;
- export with true transparency and enough resolution for a desktop hero;
- position the cutout as a free-standing subject, not inside a card or
  rectangular image frame.

The portrait may sit over reference-style halftone and technical marks, but
those decorations must remain separate from the person asset.

## 5. Visual Tokens

Approximate tokens will be calibrated against repository screenshots:

- paper: warm off-white around `#f4efe6`;
- ink: near-black brown around `#1a1714`;
- ink-soft: muted brown-gray;
- accent: vivid editorial orange around `#f0652e`;
- line: low-contrast warm gray;
- display serif: Playfair Display or the closest freely available match;
- sans: Inter;
- CJK serif/sans: Noto Serif SC and Noto Sans SC;
- metadata mono: a restrained system monospace stack.

No gradients, glossy cards, large rounded containers, or generic SaaS styling
will be introduced. Borders stay mostly one-pixel rules. Corner rounding is
reserved for controls where the reference uses it.

## 6. Responsive Behavior

### Desktop

- fixed navigation;
- two-column hero with the cutout occupying the right half;
- viewport-scale sections;
- asymmetric editorial grids and archive rows;
- large display typography with controlled overlap and whitespace.

### Tablet

- hero becomes vertically staged while retaining the portrait as a major
  visual;
- two-column sections collapse selectively;
- evidence and archive rows preserve hierarchy without horizontal overflow.

### Mobile

- dedicated compact navigation and menu;
- portrait appears before or tightly beside the hero copy, following the
  reference mobile rhythm;
- wordmark scales independently from body content;
- archive rows reduce metadata and thumbnails without losing links;
- all controls remain at least 44px tall;
- no horizontal scrolling.

## 7. Interaction Model

- smooth anchor navigation with fixed-header offset;
- active or hovered navigation state;
- working EN / 中文 switch with persisted preference;
- reveal-on-scroll transitions following the repository's timing;
- row and image hover treatments;
- functioning resume, contact, paper, GitHub, and LinkedIn links;
- mobile navigation open/close behavior;
- back-to-top action;
- `prefers-reduced-motion` disables nonessential motion;
- focus-visible styles match the orange/ink system.

## 8. Component Architecture

Keep portfolio content in the existing typed bilingual data layer.

Proposed components:

- `EditorialHeader`
- `EditorialRail`
- `EditorialHero`
- `EditorialAbout`
- `ResearchFeature`
- `ResearchArchive`
- `ExperienceArchive`
- `EditorialContact`
- shared `Crosshair`, `ArchiveRow`, `Reveal`, and `LanguageControl`

`PortfolioMainPage` remains the composition boundary. Each section receives
typed content and owns only its presentation and local interaction state.

## 9. Error and Fallback Behavior

- missing local-storage access falls back to English without blocking render;
- missing images retain meaningful alt text and stable dimensions;
- external links use safe new-tab attributes;
- the navigation remains usable without JavaScript-powered reveal motion;
- unsupported intersection observation shows content immediately;
- the page remains readable when custom web fonts fail.

## 10. Testing

Automated checks:

- app renders the new editorial page directly;
- language preference initializes and persists;
- navigation, resume, paper, and contact links point to expected targets;
- research and experience content appears in both languages;
- mobile menu opens and closes;
- reduced-motion behavior avoids hidden content;
- `npm test -- --run`;
- `npm run build`.

Visual checks:

- compare desktop implementation against the repository's hero, about,
  research/work, and contact reference captures;
- compare at matched viewport sizes;
- verify portrait transparency and hair edges on the paper background;
- verify mobile navigation and hero composition;
- inspect console errors and broken assets;
- repeat until `design-qa.md` reports `final result: passed`.

## 11. Scope Boundaries

Included:

- full homepage redesign;
- transparent portrait asset;
- bilingual content;
- responsive interaction and visual QA;
- local runnable handoff.

Excluded unless requested later:

- a CMS;
- analytics or tracking;
- new backend services;
- fabricated projects, publications, metrics, or employers;
- automatic production deployment.
