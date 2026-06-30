# Sac Editorial Portfolio Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild Gaoyi Wu's bilingual portfolio as a faithful React implementation of the `Sac-Y/sac-ai.com` Editorial Manifesto site, including a transparent natural-color portrait, responsive interactions, and recruiter-focused content.

**Architecture:** Preserve the current typed bilingual content layer and replace the page composition with focused editorial sections. Shared structural components own navigation, crosshair decoration, archive rows, and reveal behavior; section components receive typed data and remain presentation-focused. CSS recreates the reference repository's token system and responsive rhythm without copying its content.

**Tech Stack:** React 19, TypeScript 6, Vite 8, Vitest, Testing Library, CSS, ImageGen-assisted asset editing with transparent-mask post-processing.

---

## File Map

**Create**

- `public/assets/gaoyi-wu-cutout.png` — transparent natural-color hero portrait.
- `src/components/editorial/Crosshair.tsx` — reusable technical registration mark.
- `src/components/editorial/Reveal.tsx` — accessible intersection-based reveal wrapper.
- `src/components/editorial/ArchiveRow.tsx` — shared recruiter-scannable archive row.
- `src/components/sections/EditorialHeader.tsx` — fixed desktop and mobile navigation.
- `src/components/sections/EditorialHero.tsx` — oversized wordmark and portrait hero.
- `src/components/sections/EditorialAbout.tsx` — profile blueprint and evidence signals.
- `src/components/sections/EditorialResearch.tsx` — publication feature/archive layout.
- `src/components/sections/EditorialExperience.tsx` — experience and project archive.
- `src/components/sections/EditorialContact.tsx` — contact marquee, links, and footer.
- focused test files beside the new sections.

**Modify**

- `src/types/portfolio.ts` — add optional editorial labels and archive metadata only if current fields cannot represent the approved design.
- `src/data/portfolio.ts` — add bilingual editorial labels while preserving verified resume facts.
- `src/data/portfolio.test.ts` — verify both languages and critical links/metrics.
- `src/components/sections/PortfolioMainPage.tsx` — compose the editorial page.
- `src/App.test.tsx` — assert direct render, language persistence, and main actions.
- `src/index.css` — replace current page styling with the Sac-derived editorial system.
- `design-qa.md` — record matched-viewport comparison and final gate.

## Chunk 1: Assets and Data Contracts

### Task 1: Produce the transparent portrait asset

**Files:**

- Source: `public/assets/gaoyi-wu-portrait-studio.jpg`
- Create: `public/assets/gaoyi-wu-cutout.png`

- [ ] **Step 1: Record source dimensions and visual requirements**

Run:

```bash
sips -g pixelWidth -g pixelHeight public/assets/gaoyi-wu-portrait-studio.jpg
```

Expected: `1920 × 1280`.

- [ ] **Step 2: Use ImageGen to isolate the exact source subject**

Edit the source image with this constraint: preserve the person's face, hair,
skin, white shirt, dark jeans, body proportions, and pose; remove only the
blue-gray background; place the unchanged subject against a flat removable
background for mask extraction.

- [ ] **Step 3: Post-process to true alpha transparency**

Use an edge-aware foreground mask. Keep enough transparent padding for the
hero crop and export a lossless PNG. Do not synthesize or repaint face details.

- [ ] **Step 4: Inspect the result**

Open the PNG against light and dark backgrounds. Expected: no rectangular
background, no blue halo, intact hair tips, natural shirt edge.

- [ ] **Step 5: Commit**

```bash
git add public/assets/gaoyi-wu-cutout.png
git commit -m "feat: add transparent portfolio portrait"
```

### Task 2: Lock the bilingual editorial content contract

**Files:**

- Modify: `src/types/portfolio.ts`
- Modify: `src/data/portfolio.ts`
- Modify: `src/data/portfolio.test.ts`

- [ ] **Step 1: Write failing data tests**

Add expectations that both languages expose:

```ts
expect(content.hero.portraitSrc).toBe('/assets/gaoyi-wu-cutout.png')
expect(content.navigation.map((item) => item.href)).toEqual(
  expect.arrayContaining(['#about', '#research', '#experience', '#contact']),
)
expect(content.research.map((item) => item.title)).toEqual(
  expect.arrayContaining(['iSeal', 'WebWeaver']),
)
```

Also verify resume, paper, GitHub, LinkedIn, email, AAAI 2026, 100+ devices,
and 61% to 94% claims are present and identical in meaning across languages.

- [ ] **Step 2: Run the data test and verify RED**

Run:

```bash
npm test -- --run src/data/portfolio.test.ts
```

Expected: FAIL because the portrait path and editorial labels are not yet
present.

- [ ] **Step 3: Add the minimal typed content**

Prefer existing fields. Add only fields required for reference-faithful labels,
archive metadata, or contact marquee content.

- [ ] **Step 4: Run the data test and verify GREEN**

Run:

```bash
npm test -- --run src/data/portfolio.test.ts
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/types/portfolio.ts src/data/portfolio.ts src/data/portfolio.test.ts
git commit -m "feat: add editorial portfolio content"
```

## Chunk 2: Structure and Interaction

### Task 3: Build shared editorial primitives and fixed navigation

**Files:**

- Create: `src/components/editorial/Crosshair.tsx`
- Create: `src/components/editorial/Reveal.tsx`
- Create: `src/components/editorial/ArchiveRow.tsx`
- Create: `src/components/sections/EditorialHeader.tsx`
- Create: `src/components/sections/EditorialHeader.test.tsx`

- [ ] **Step 1: Write failing header and reveal tests**

Tests must assert:

- brand and section links render;
- EN / 中文 buttons expose pressed state;
- mobile menu opens and closes;
- resume link is reachable;
- `Reveal` renders visible content when intersection observation is unavailable
  or reduced motion is requested.

- [ ] **Step 2: Run focused tests and verify RED**

```bash
npm test -- --run src/components/sections/EditorialHeader.test.tsx
```

Expected: FAIL because components do not exist.

- [ ] **Step 3: Implement minimal accessible primitives**

Use semantic anchors/buttons, `aria-expanded`, `aria-controls`, and
`aria-pressed`. Avoid drawing icons with CSS or handcrafted SVG; use text labels
and existing arrow glyphs only where the reference visibly uses typographic
arrows.

- [ ] **Step 4: Run focused tests and verify GREEN**

```bash
npm test -- --run src/components/sections/EditorialHeader.test.tsx
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/components/editorial src/components/sections/EditorialHeader.tsx src/components/sections/EditorialHeader.test.tsx
git commit -m "feat: add editorial navigation primitives"
```

### Task 4: Build the hero and about/profile sections

**Files:**

- Create: `src/components/sections/EditorialHero.tsx`
- Create: `src/components/sections/EditorialHero.test.tsx`
- Create: `src/components/sections/EditorialAbout.tsx`
- Create: `src/components/sections/EditorialAbout.test.tsx`

- [ ] **Step 1: Write failing section tests**

Hero expectations:

```ts
expect(screen.getByRole('heading', { level: 1, name: /Gaoyi Wu/i })).toBeVisible()
expect(screen.getByAltText(/Portrait of Gaoyi Wu/i)).toHaveAttribute(
  'src',
  '/assets/gaoyi-wu-cutout.png',
)
expect(screen.getByRole('link', { name: /resume/i })).toBeVisible()
```

About expectations cover AAAI 2026, two papers, 100+ devices, and accuracy
improvement.

- [ ] **Step 2: Run focused tests and verify RED**

```bash
npm test -- --run src/components/sections/EditorialHero.test.tsx src/components/sections/EditorialAbout.test.tsx
```

Expected: FAIL because components do not exist.

- [ ] **Step 3: Implement the sections**

Match the reference composition:

- hero uses a two-column viewport-scale layout;
- wordmark remains text, not an image;
- cutout stays free-standing;
- about uses a blueprint archive on the left and three-node/evidence signals on
  the right;
- all decoration is aria-hidden.

- [ ] **Step 4: Run focused tests and verify GREEN**

Run the same command. Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/components/sections/EditorialHero* src/components/sections/EditorialAbout*
git commit -m "feat: add editorial hero and profile"
```

### Task 5: Build research, experience, and contact sections

**Files:**

- Create: `src/components/sections/EditorialResearch.tsx`
- Create: `src/components/sections/EditorialResearch.test.tsx`
- Create: `src/components/sections/EditorialExperience.tsx`
- Create: `src/components/sections/EditorialExperience.test.tsx`
- Create: `src/components/sections/EditorialContact.tsx`
- Create: `src/components/sections/EditorialContact.test.tsx`

- [ ] **Step 1: Write failing section tests**

Verify iSeal and WebWeaver paper links, Intellisys and DHL archive rows, email,
LinkedIn, GitHub, location, resume, availability status, and back-to-top.

- [ ] **Step 2: Run focused tests and verify RED**

```bash
npm test -- --run src/components/sections/EditorialResearch.test.tsx src/components/sections/EditorialExperience.test.tsx src/components/sections/EditorialContact.test.tsx
```

Expected: FAIL because components do not exist.

- [ ] **Step 3: Implement the sections**

Map Research to the reference Writing feature/archive pattern, Experience to
the Work archive rows, and Contact to the full-height reference contact
composition. Keep all real recruiter actions functional.

- [ ] **Step 4: Run focused tests and verify GREEN**

Run the same command. Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/components/sections/EditorialResearch* src/components/sections/EditorialExperience* src/components/sections/EditorialContact*
git commit -m "feat: add editorial portfolio sections"
```

## Chunk 3: Composition, Styling, and QA

### Task 6: Compose the page and recreate the reference visual system

**Files:**

- Modify: `src/components/sections/PortfolioMainPage.tsx`
- Modify: `src/App.test.tsx`
- Modify: `src/index.css`

- [ ] **Step 1: Write failing app integration tests**

Assert the page composes the new header, hero, about, research, experience, and
contact landmarks; language preference persists; no intro gate returns.

- [ ] **Step 2: Run the app test and verify RED**

```bash
npm test -- --run src/App.test.tsx
```

Expected: FAIL because the old section composition remains.

- [ ] **Step 3: Compose the new sections**

Replace old section imports in `PortfolioMainPage`. Preserve the existing
language state in `App`.

- [ ] **Step 4: Implement reference-calibrated CSS**

Recreate:

- paper, ink, accent, line, serif/sans/mono token variables;
- fixed header and rhythm rail;
- hero geometry and transparent portrait positioning;
- full-height editorial sections and archive grids;
- reveal, hover, focus-visible, and reduced-motion states;
- tablet and mobile layouts at approximately 860px and 600px;
- stable image dimensions and no horizontal overflow.

- [ ] **Step 5: Run all automated checks**

```bash
npm test -- --run
npm run build
```

Expected: all tests pass and Vite production build exits 0.

- [ ] **Step 6: Commit**

```bash
git add src/components/sections/PortfolioMainPage.tsx src/App.test.tsx src/index.css
git commit -m "feat: compose Sac editorial portfolio"
```

### Task 7: Run matched-viewport visual QA

**Files:**

- Modify: `design-qa.md`

- [ ] **Step 1: Start the local app**

```bash
npm run dev -- --host 127.0.0.1 --port 5173
```

- [ ] **Step 2: Capture matched desktop and mobile states**

Use the user's in-app browser. Compare the local hero, about, research/work,
and contact views to:

- `/tmp/sac-ai-reference/editorial-manifesto/reference/01-hero.png`
- `/tmp/sac-ai-reference/editorial-manifesto/reference/02-about.png`
- `/tmp/sac-ai-reference/editorial-manifesto/reference/writing.png`
- `/tmp/sac-ai-reference/editorial-manifesto/reference/build.png`
- `/tmp/sac-ai-reference/editorial-manifesto/reference/04-contact.png`

- [ ] **Step 3: Write the blocking QA report**

Record P0–P3 discrepancies in `design-qa.md`. The first line must remain
`final result: blocked` until all P0/P1/P2 items are fixed.

- [ ] **Step 4: Fix and recapture**

Repeat matched-state comparison. Verify portrait edges, font scale, whitespace,
rules, rail/crosshairs, mobile menu, links, and console logs.

- [ ] **Step 5: Mark QA passed**

Set:

```md
final result: passed
```

only after matched-viewport comparison has no remaining P0/P1/P2 issues.

- [ ] **Step 6: Run final verification**

```bash
npm test -- --run
npm run build
git diff --check
```

Expected: all commands exit 0.

- [ ] **Step 7: Commit**

```bash
git add design-qa.md
git commit -m "docs: verify Sac editorial redesign"
```
