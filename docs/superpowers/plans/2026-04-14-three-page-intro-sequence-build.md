# Three-Page Intro Sequence Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the current one-card intro with a Figma-faithful three-page horizontal intro sequence that uses the approved source material, fixes the cover underline collision, and keeps the main portfolio hidden until entry.

**Architecture:** Keep the app as a single React experience with the existing `entered` state, but replace the current `IntroPage` implementation with a horizontally scrollable three-card sequence on a dark canvas. Store the three intro pages in structured local data derived from `project_source.md`, render them through one shared page-shell component so the card chrome stays consistent, and map normal wheel/trackpad scrolling to horizontal movement so the intro behaves like the reference screenshot instead of requiring shift-scroll. Leave the main portfolio behind the existing post-entry gate.

**Tech Stack:** React, TypeScript, Tailwind CSS, Vitest, Testing Library, Vite

---

## File Map

- Modify: `src/App.tsx`
  Keep the intro-vs-main branching, but make the intro branch render the full three-page strip.
- Modify: `src/App.test.tsx`
  Replace the single-cover expectation with assertions for the three-page intro sequence.
- Modify: `src/App.template.test.tsx`
  Keep the entry and direct-hash flow tests, but anchor them to the new multi-page intro.
- Modify: `src/types/portfolio.ts`
  Replace the current flat `intro` shape with a structured three-page intro model.
- Modify: `src/data/portfolio.ts`
  Populate page 1, page 2, and page 3 using `project_source.md` and the approved recruiter-facing content direction.
- Modify: `src/data/portfolio.test.ts`
  Assert the presence of the three intro pages and key headings.
- Modify: `src/components/sections/IntroPage.tsx`
  Turn it into the horizontal intro-sequence container rather than a single page.
- Modify: `src/components/sections/IntroPage.test.tsx`
  Assert the three-page strip, not just one cover card.
- Create: `src/components/sections/IntroSequenceCard.tsx`
  Encapsulate the repeated page shell: rounded white card, top-right mark, and bottom cropped wordmark treatment.
- Create: `src/components/sections/IntroSequenceCard.test.tsx`
  Verify the shared card shell renders children and the repeated page chrome.
- Modify: `src/index.css`
  Add narrowly scoped horizontal scroll-snap and scrollbar-hiding rules if Tailwind utilities alone become clumsy.

Do not introduce shadcn as part of this work. The repo does not currently have an active shadcn setup, and the Figma pages are custom enough that generic components would create more drift than value here.

## Chunk 1: Lock The Three-Page Intro Into Tests

### Task 1: Replace The Top-Level Intro Smoke Test

**Files:**
- Modify: `src/App.test.tsx`

- [ ] **Step 1: Replace the current intro smoke test with a three-page expectation**

Update `src/App.test.tsx` to:

```tsx
import { render, screen } from '@testing-library/react'
import App from './App'

test('renders the three-page intro sequence before the main portfolio', () => {
  render(<App />)

  expect(screen.getByText(/^from[.,]?$/i)).toBeInTheDocument()
  expect(screen.getByRole('heading', { name: /about me/i })).toBeInTheDocument()
  expect(screen.getByRole('heading', { name: /recruiter note/i })).toBeInTheDocument()
  expect(screen.queryByText(/my services/i)).not.toBeInTheDocument()
})
```

- [ ] **Step 2: Run the smoke test to verify RED**

Run:

```bash
npm test -- --run src/App.test.tsx
```

Expected: FAIL because the current intro only renders one page and does not yet expose the approved page 2 and page 3 headings.

### Task 2: Update The App Flow Test

**Files:**
- Modify: `src/App.template.test.tsx`

- [ ] **Step 1: Rewrite the app flow test around the three-page intro**

Update `src/App.template.test.tsx` to:

```tsx
import { fireEvent, render, screen } from '@testing-library/react'
import App from './App'

test('switches from the three-page intro sequence to the main portfolio after entry', () => {
  render(<App />)

  expect(screen.getByRole('heading', { name: /about me/i })).toBeInTheDocument()
  expect(screen.getByRole('heading', { name: /recruiter note/i })).toBeInTheDocument()

  fireEvent.click(screen.getByRole('link', { name: /enter portfolio/i }))

  expect(screen.getByText(/my services/i)).toBeInTheDocument()
  expect(screen.queryByRole('heading', { name: /about me/i })).not.toBeInTheDocument()
  expect(screen.queryByRole('heading', { name: /recruiter note/i })).not.toBeInTheDocument()
})

test('opens the main portfolio directly when the hash is present', () => {
  window.location.hash = '#portfolio-main'

  render(<App />)

  expect(screen.getByText(/my services/i)).toBeInTheDocument()
  expect(screen.queryByRole('heading', { name: /about me/i })).not.toBeInTheDocument()
  expect(screen.queryByRole('link', { name: /enter portfolio/i })).not.toBeInTheDocument()

  window.location.hash = ''
})
```

- [ ] **Step 2: Run the app flow test to verify RED**

Run:

```bash
npm test -- --run src/App.template.test.tsx
```

Expected: FAIL because the intro component still exposes only one card.

### Task 3: Lock The Intro Data Shape

**Files:**
- Modify: `src/data/portfolio.test.ts`

- [ ] **Step 1: Replace the flat intro assertions with three-page data expectations**

Update `src/data/portfolio.test.ts` to:

```tsx
import { portfolio } from './portfolio'

test('contains the approved homepage sections and three intro pages', () => {
  expect(portfolio.featuredWork).toHaveLength(4)
  expect(portfolio.experience).toHaveLength(3)
  expect(portfolio.capabilities.map((item) => item.title)).toEqual([
    'Applied AI Products',
    'ML Engineering',
    'AI Security Research',
  ])
  expect(portfolio.intro.pages).toHaveLength(3)
  expect(portfolio.intro.pages.map((page) => page.id)).toEqual(['cover', 'about', 'note'])
  expect(portfolio.intro.pages[1].heading).toBe('About Me')
  expect(portfolio.intro.pages[2].heading).toBe('Recruiter Note')
})
```

- [ ] **Step 2: Run the data test to verify RED**

Run:

```bash
npm test -- --run src/data/portfolio.test.ts
```

Expected: FAIL because the current `intro` object is still a single flat cover-page shape.

### Task 4: Update The Intro Component Test

**Files:**
- Modify: `src/components/sections/IntroPage.test.tsx`

- [ ] **Step 1: Rewrite the intro component test around the three-page strip**

Update `src/components/sections/IntroPage.test.tsx` to:

```tsx
import { render, screen } from '@testing-library/react'
import { portfolio } from '../../data/portfolio'
import { IntroPage } from './IntroPage'

test('renders the three intro cards and the entry CTA', () => {
  render(<IntroPage intro={portfolio.intro} onEnter={() => {}} />)

  expect(screen.getByRole('heading', { name: /about me/i })).toBeInTheDocument()
  expect(screen.getByRole('heading', { name: /recruiter note/i })).toBeInTheDocument()
  expect(screen.getAllByRole('article')).toHaveLength(3)
  expect(screen.getByRole('link', { name: /enter portfolio/i })).toBeInTheDocument()
})
```

- [ ] **Step 2: Run the intro component test to verify RED**

Run:

```bash
npm test -- --run src/components/sections/IntroPage.test.tsx
```

Expected: FAIL because the current `IntroPage` renders only one page and no repeated page-shell structure.

## Chunk 2: Add Structured Three-Page Intro Data

### Task 5: Replace The Flat Intro Type With A Sequence Model

**Files:**
- Modify: `src/types/portfolio.ts`
- Test: `src/data/portfolio.test.ts`

- [ ] **Step 1: Replace `IntroContent` with a structured sequence model**

Update `src/types/portfolio.ts` to add focused types such as:

```ts
export type IntroPageSection = {
  title: string
  lines: string[]
}

export type IntroSequencePage =
  | {
      id: 'cover'
      meta: string
      fromLabel: string
      fromLines: string[]
      toLabel: string
      toLines: string[]
      portfolioLabel: string
      displayName: string
      entryLabel: string
    }
  | {
      id: 'about'
      heading: string
      profileName: string
      profileRole: string
      paragraphs: string[]
    }
  | {
      id: 'note'
      heading: string
      sections: IntroPageSection[]
    }

export type IntroContent = {
  brandMark: string
  footerWordmark: string
  pages: IntroSequencePage[]
}
```

Keep the type narrow and page-specific. Do not keep the old flat intro fields around as compatibility clutter.

- [ ] **Step 2: Run the data test to confirm the type change is still RED until data exists**

Run:

```bash
npm test -- --run src/data/portfolio.test.ts
```

Expected: FAIL because the data module has not been updated to the new sequence shape yet.

### Task 6: Populate Pages 1-3 From The Source Material

**Files:**
- Modify: `src/data/portfolio.ts`
- Test: `src/data/portfolio.test.ts`

- [ ] **Step 1: Replace the existing flat `intro` object with three real pages**

Update `src/data/portfolio.ts` so `portfolio.intro` has:

```ts
intro: {
  brandMark: 'GW',
  footerWordmark: 'GAOYI',
  pages: [
    {
      id: 'cover',
      meta: 'Apr 2026',
      fromLabel: 'From,',
      fromLines: ['Gaoyi Wu', 'Applied AI Engineer', 'ML Engineer'],
      toLabel: 'To,',
      toLines: ['Recruiters, hiring managers,', 'and collaborators'],
      portfolioLabel: 'AI Portfolio',
      displayName: 'GAOYI',
      entryLabel: 'Enter Portfolio',
    },
    {
      id: 'about',
      heading: 'About Me',
      profileName: 'Gaoyi Wu',
      profileRole: 'Applied AI Engineer / ML Engineer',
      paragraphs: [
        'I build practical AI products, machine learning pipelines, and infrastructure that connect research ideas to systems teams can actually ship and maintain.',
        'My work sits between research and delivery: LLM systems, ML infra, AI security, and full-stack product execution.',
        'As a teaching assistant and active lab researcher, I care about clear communication, technical depth, and momentum across both public and ongoing work.',
      ],
    },
    {
      id: 'note',
      heading: 'Recruiter Note',
      sections: [
        {
          title: 'What This Portfolio Shows',
          lines: [
            'This portfolio is built for recruiter review and engineering hiring conversations across Applied AI, ML Engineering, AI Infra, AI Security, and software roles.',
          ],
        },
        {
          title: 'Public Work And Ongoing Work',
          lines: [
            'Some projects link to public artifacts such as XClaw and iSeal.',
            'Current lab work represents active research momentum and may be summarized at a higher level when details are not public.',
          ],
        },
        {
          title: 'How To Read It',
          lines: [
            'Look for evidence of research-to-production thinking, communication strength, and practical system ownership across modeling, infrastructure, and shipped interfaces.',
          ],
        },
      ],
    },
  ],
},
```

Use `project_source.md` as the content source of truth while keeping the copy concise enough for the Figma page layout.

- [ ] **Step 2: Run the data test to verify GREEN**

Run:

```bash
npm test -- --run src/data/portfolio.test.ts
```

Expected: PASS

## Chunk 3: Build The Horizontal Page Strip And Verify

### Task 7: Add A Shared Intro Page Shell

**Files:**
- Create: `src/components/sections/IntroSequenceCard.tsx`
- Create: `src/components/sections/IntroSequenceCard.test.tsx`

- [ ] **Step 1: Write a failing test for the shared page shell**

Create `src/components/sections/IntroSequenceCard.test.tsx`:

```tsx
import { render, screen } from '@testing-library/react'
import { IntroSequenceCard } from './IntroSequenceCard'

test('renders a reusable intro page shell with page chrome', () => {
  render(
    <IntroSequenceCard brandMark="GW" footerWordmark="GAOYI">
      <h2>About Me</h2>
    </IntroSequenceCard>,
  )

  expect(screen.getByText('GW')).toBeInTheDocument()
  expect(screen.getByText('About Me')).toBeInTheDocument()
  expect(screen.getByText('GAOYI')).toBeInTheDocument()
})
```

- [ ] **Step 2: Run the new shell test to verify RED**

Run:

```bash
npm test -- --run src/components/sections/IntroSequenceCard.test.tsx
```

Expected: FAIL because the shared shell component does not exist yet.

- [ ] **Step 3: Implement the shared page shell**

Create `src/components/sections/IntroSequenceCard.tsx` with a shape like:

```tsx
import type { ReactNode } from 'react'

type IntroSequenceCardProps = {
  brandMark: string
  footerWordmark: string
  children: ReactNode
}

export function IntroSequenceCard({
  brandMark,
  footerWordmark,
  children,
}: IntroSequenceCardProps) {
  return (
    <article className="relative h-full min-h-[720px] w-[min(38rem,86vw)] shrink-0 overflow-hidden rounded-[40px] bg-[#fbfaf7] shadow-[0_28px_80px_rgba(0,0,0,0.18)]">
      <div className="absolute right-[6.5%] top-[4.5%] font-display text-[clamp(1.75rem,2.2vw,2.35rem)] font-semibold text-[#1f1f1f]">
        {brandMark}
      </div>
      {children}
      <div className="pointer-events-none absolute bottom-[-2%] left-0 text-[clamp(8rem,15vw,13rem)] font-display font-semibold leading-[0.8] text-[#1f1f1f]">
        {footerWordmark}
      </div>
    </article>
  )
}
```

Keep it focused on the shared page shell only. Do not bake page-specific layouts into this component.

- [ ] **Step 4: Run the shell test to verify GREEN**

Run:

```bash
npm test -- --run src/components/sections/IntroSequenceCard.test.tsx
```

Expected: PASS

### Task 8: Rebuild `IntroPage` As A Horizontal Three-Card Sequence

**Files:**
- Modify: `src/components/sections/IntroPage.tsx`
- Modify: `src/components/sections/IntroPage.test.tsx`
- Modify: `src/index.css`
- Test: `src/App.test.tsx`
- Test: `src/App.template.test.tsx`

- [ ] **Step 1: Replace the one-card layout with a horizontal snap strip**

Rewrite `src/components/sections/IntroPage.tsx` so it:
- accepts the new `intro.pages` sequence shape
- renders a dark full-screen canvas
- renders a horizontally scrollable track with exactly three `IntroSequenceCard` instances
- uses `overflow-x-auto`, `snap-x`, `snap-mandatory`, and per-card `snap-center`
- translates ordinary vertical wheel movement into horizontal scrolling inside the intro viewport so desktop scrolling naturally advances across the pages
- keeps the `Enter Portfolio` action only on the cover page unless the Figma evidence forces a repeat

Page-specific content rules:
- page 1 keeps the cover composition and fixes the underline collision
- page 2 follows the Figma About Me page structure with heading, underline, profile block, and sourced paragraphs
- page 3 follows the Figma note page structure with heading, underline, and stacked sections derived from source material

- [ ] **Step 2: Add only minimal CSS support in `src/index.css`**

If scrollbar removal and scroll behavior are awkward in utilities, add scoped rules such as:

```css
.intro-sequence-scroll {
  scrollbar-width: none;
}

.intro-sequence-scroll::-webkit-scrollbar {
  display: none;
}
```

Do not move generic app styling into these selectors.

- [ ] **Step 3: Run the focused tests to verify GREEN**

Run:

```bash
npm test -- --run src/components/sections/IntroPage.test.tsx src/App.test.tsx src/App.template.test.tsx
```

Expected: PASS

- [ ] **Step 4: Commit the intro-sequence slice**

Run:

```bash
git add src/types/portfolio.ts src/data/portfolio.ts src/data/portfolio.test.ts src/components/sections/IntroSequenceCard.tsx src/components/sections/IntroSequenceCard.test.tsx src/components/sections/IntroPage.tsx src/components/sections/IntroPage.test.tsx src/App.test.tsx src/App.template.test.tsx src/index.css
git commit -m "feat: add three-page intro sequence"
```

### Task 9: Verify The Integrated Experience

**Files:**
- Verify only

- [ ] **Step 1: Run the full test suite**

Run:

```bash
npm test -- --run
```

Expected: PASS

- [ ] **Step 2: Run the production build**

Run:

```bash
npm run build
```

Expected: PASS

- [ ] **Step 3: Start the local dev server**

Run:

```bash
npm run dev -- --host 127.0.0.1 --port 4173
```

Expected: Vite serves locally on an available `127.0.0.1` port

- [ ] **Step 4: Capture browser screenshots for the intro strip**

Use Playwright to capture desktop screenshots and compare them to the approved screenshot:
- confirm the three pages appear side by side
- confirm the page chrome is consistent
- confirm the cover underline no longer collides with the oversized wordmark
- confirm pages 2 and 3 use the sourced content while preserving the Figma structure

- [ ] **Step 5: Commit the verified integration**

Run:

```bash
git add src/App.tsx
git commit -m "feat: integrate intro sequence with portfolio entry"
```
