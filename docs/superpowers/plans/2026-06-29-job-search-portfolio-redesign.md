# Job-Search Portfolio Redesign Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the intro-gated portfolio with a bilingual, recruiter-first Editorial Research Dossier that positions Gaoyi Wu as an AI Algorithm Engineer.

**Architecture:** Keep the React, TypeScript, Vite, and Tailwind stack. Introduce a typed localized content model selected by `App`, compose the page from focused sections, and keep research disclosure state local to the research section. Existing unreferenced intro-era components may remain temporarily so the redesign does not destroy unrelated work.

**Tech Stack:** React 19, TypeScript 6, Vite 8, Tailwind CSS 4, Vitest, Testing Library.

---

## Chunk 1: Content, State, and Direct Entry

### Task 1: Define the bilingual portfolio content model

**Files:**
- Modify: `src/types/portfolio.ts`
- Modify: `src/data/portfolio.ts`
- Modify: `src/data/portfolio.test.ts`

- [ ] **Step 1: Write failing data tests**

Add assertions that:

- English and Chinese content both exist.
- The English role is `AI Algorithm Engineer`.
- Hero proof values are `AAAI 2026`, `2 Published Papers`, `100+ Edge Devices`, and `61% → 94% Accuracy`.
- Research items are ordered `iSeal`, then `WebWeaver`.
- Experience is ordered `Intellisys Lab`, then `DHL Express`.
- Skill groups match the latest resume.

- [ ] **Step 2: Run the data test and confirm failure**

Run:

```bash
npm test -- --run src/data/portfolio.test.ts
```

Expected: FAIL because the localized content model and latest-resume evidence do not exist.

- [ ] **Step 3: Add focused localized types**

Add:

```ts
export type Language = 'en' | 'zh'

export type PortfolioContent = {
  navigation: ...
  hero: ...
  proof: ...
  research: ...
  experience: ...
  skills: ...
  education: ...
  contact: ...
}
```

Keep legacy types required by unreferenced existing components until those files are intentionally removed.

- [ ] **Step 4: Replace stale homepage data**

Export:

```ts
export const portfolioByLanguage: Record<Language, PortfolioContent> = {
  en: { ... },
  zh: { ... },
}
```

Use only claims supported by the latest resume. Keep official company, publication, and technology names unchanged across languages where appropriate.

- [ ] **Step 5: Run the data test**

Run:

```bash
npm test -- --run src/data/portfolio.test.ts
```

Expected: PASS.

### Task 2: Remove the intro gate and add persisted language state

**Files:**
- Modify: `src/App.tsx`
- Modify: `src/App.test.tsx`
- Modify: `src/test/setup.ts` if local-storage cleanup is not already available

- [ ] **Step 1: Write failing application tests**

Cover:

- The homepage immediately renders `AI Algorithm Engineer`.
- Intro copy is absent.
- English is the default.
- Clicking `中文` switches representative hero and contact copy.
- The language choice is stored under `portfolio-language`.

- [ ] **Step 2: Run the application test and confirm failure**

Run:

```bash
npm test -- --run src/App.test.tsx
```

Expected: FAIL because the current app renders the intro sequence first.

- [ ] **Step 3: Implement direct entry and language state**

`App` should:

- Read `portfolio-language` safely.
- Default to `en`.
- Select `portfolioByLanguage[language]`.
- Persist language changes.
- Set `document.documentElement.lang`.
- Render `PortfolioMainPage` directly.

- [ ] **Step 4: Run the application test**

Run:

```bash
npm test -- --run src/App.test.tsx
```

Expected: PASS.

---

## Chunk 2: Recruiter-First Page Composition

### Task 3: Build the editorial header, hero, and proof strip

**Files:**
- Modify: `src/components/sections/PortfolioMainPage.tsx`
- Modify: `src/components/sections/MainHeader.tsx`
- Modify: `src/components/sections/HeroSection.tsx`
- Create: `src/components/sections/EvidenceStrip.tsx`
- Modify: `src/components/sections/HeroSection.test.tsx`
- Create: `src/components/sections/MainHeader.test.tsx`

- [ ] **Step 1: Write failing section tests**

Cover:

- Header anchors target Research, Experience, Skills, Education, and Contact.
- Language controls expose selected state.
- Hero renders name, primary role, positioning line, portrait, Resume, and Contact.
- Proof values and qualifiers render.

- [ ] **Step 2: Run the section tests and confirm failure**

Run:

```bash
npm test -- --run src/components/sections/HeroSection.test.tsx src/components/sections/MainHeader.test.tsx
```

Expected: FAIL against the current Figma-hybrid hero.

- [ ] **Step 3: Implement the new header**

Create a slim editorial header with:

- `GW / GAOYI WU` identity.
- Anchored navigation.
- Resume link.
- `EN / 中文` language controls.
- Compact mobile navigation that does not create horizontal overflow.

- [ ] **Step 4: Implement the new hero**

Use:

- Oversized editorial name.
- Primary role and supporting specialization line.
- Brief value proposition.
- Resume and Contact actions.
- Real portrait with decorative halftone/annotation treatment.
- Semantic heading and link structure.

- [ ] **Step 5: Implement the evidence strip**

Render the four proof signals with short qualifiers. Keep the component data-driven and independent of language selection.

- [ ] **Step 6: Run the section tests**

Run the command from Step 2.

Expected: PASS.

### Task 4: Build accessible research case studies

**Files:**
- Create: `src/components/sections/ResearchSection.tsx`
- Create: `src/components/sections/ResearchSection.test.tsx`
- Modify: `src/components/ui/Icons.tsx` only if a needed existing icon is unavailable

- [ ] **Step 1: Write failing research tests**

Cover:

- iSeal precedes WebWeaver.
- Each case shows venue, summary, contribution, benchmark, and a paper action.
- Optional code actions render only when a verified URL exists.
- Details controls update `aria-expanded` and reveal secondary content.

- [ ] **Step 2: Run the research test and confirm failure**

Run:

```bash
npm test -- --run src/components/sections/ResearchSection.test.tsx
```

Expected: FAIL because the component does not exist.

- [ ] **Step 3: Implement the research section**

Use alternating editorial spreads:

- Numbered publication label.
- Large publication title.
- Compact abstract.
- Contribution bullets.
- Large benchmark treatment.
- CSS-native method diagram built from normal layout, borders, text, and existing icon primitives.
- Accessible native button for details.

Do not invent code URLs or publication metadata.

- [ ] **Step 4: Run the research test**

Expected: PASS.

### Task 5: Rebuild experience, skills, education, and contact

**Files:**
- Modify: `src/components/sections/ExperienceSection.tsx`
- Modify: `src/components/sections/ExperienceSection.test.tsx`
- Modify: `src/components/sections/SkillsSection.tsx`
- Create: `src/components/sections/SkillsSection.test.tsx`
- Create: `src/components/sections/EducationSection.tsx`
- Create: `src/components/sections/EducationSection.test.tsx`
- Modify: `src/components/sections/ContactSection.tsx`
- Modify: `src/components/sections/ContactSection.test.tsx`

- [ ] **Step 1: Update failing tests**

Cover:

- Latest-resume employers and quantified highlights.
- Four current skill groups.
- Correct degrees and dates.
- Contact copy targets algorithm and applied AI / ML roles.
- Email, LinkedIn, GitHub, and resume destinations.

- [ ] **Step 2: Run the section tests and confirm failure**

Run:

```bash
npm test -- --run src/components/sections/ExperienceSection.test.tsx src/components/sections/SkillsSection.test.tsx src/components/sections/EducationSection.test.tsx src/components/sections/ContactSection.test.tsx
```

Expected: FAIL against stale content and missing sections.

- [ ] **Step 3: Implement editorial experience rows**

Use company, role, period, and three high-signal quantified bullets. Keep logos optional and preserve text when an image fails.

- [ ] **Step 4: Implement compact skills and education**

Skills use grouped technical indices rather than cards. Education remains visually subordinate to research and experience.

- [ ] **Step 5: Implement the closing contact spread**

Use job-search-specific copy and direct actions. External web links open safely; email remains a normal `mailto:` link.

- [ ] **Step 6: Run the section tests**

Expected: PASS.

---

## Chunk 3: Visual System and Verification

### Task 6: Apply the Editorial Research Dossier visual system

**Files:**
- Modify: `src/index.css`
- Modify: `src/components/sections/PortfolioMainPage.tsx`
- Modify: section files from Chunk 2 as required for class hooks

- [ ] **Step 1: Add visual-system foundations**

Implement:

- Editorial serif and neutral sans fonts.
- Ivory, ink, muted line, and burnt-orange tokens.
- Subtle paper grain using CSS backgrounds.
- Registration marks and fine technical rules.
- Responsive display typography.
- Strong focus-visible treatment.

- [ ] **Step 2: Add restrained motion**

Use hero entrance and section reveal classes only where they improve hierarchy. Respect `prefers-reduced-motion`.

- [ ] **Step 3: Verify responsive CSS manually**

Check:

- No horizontal overflow.
- Header remains operable at mobile widths.
- Hero portrait follows the text on mobile.
- Proof strip becomes two or one columns.
- Research spreads preserve reading order.
- Chinese copy does not collide.

### Task 7: Run full verification

**Files:**
- Modify tests only if verification exposes a real missing requirement

- [ ] **Step 1: Run all tests**

```bash
npm test -- --run
```

Expected: all tests pass.

- [ ] **Step 2: Run the production build**

```bash
npm run build
```

Expected: TypeScript and Vite build succeed.

- [ ] **Step 3: Run desktop browser verification**

At approximately 1440px width, verify:

- Hero hierarchy matches the selected concept.
- First viewport contains role, specialization, portrait, actions, and proof.
- Research and experience content is accurate.
- No console errors.

- [ ] **Step 4: Run mobile browser verification**

At approximately 390px width, verify:

- No clipping or horizontal overflow.
- Navigation, language switch, disclosure buttons, and actions are usable.
- English and Chinese layouts both remain readable.

- [ ] **Step 5: Compare the implementation with the selected visual**

Use a same-viewport side-by-side comparison. Fix visible mismatches in hierarchy, typography, color, spacing, rules, and portrait treatment before completion.
