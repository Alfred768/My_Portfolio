# Intro-First Portfolio Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a dedicated Figma-faithful introduction cover screen that appears first, then switches into the existing portfolio page only after the visitor clicks the entry button.

**Architecture:** Keep the app as a single React experience with local entry state seeded from `window.location.hash`. Add a new intro-specific data object and a dedicated `IntroPage` component that mirrors Figma node `1205:2330`, then move the existing post-entry sections behind a `PortfolioMainPage` wrapper so the main portfolio is fully hidden until entry. Preserve direct `#portfolio-main` access for deep links without turning this into a separate route.

**Tech Stack:** React, TypeScript, Tailwind CSS, Vitest, Testing Library, Vite

---

## File Map

- Modify: `src/App.tsx`
  Own the intro-vs-main state, seed it from the hash, and switch between the two screens.
- Modify: `src/App.test.tsx`
  Update the top-level smoke test so it asserts intro-first behavior instead of the old hero-first flow.
- Modify: `src/App.template.test.tsx`
  Lock in the click-through and direct-hash entry behavior.
- Modify: `src/types/portfolio.ts`
  Add a dedicated intro content type rather than reusing hero-only fields.
- Modify: `src/data/portfolio.ts`
  Add the intro-page copy and labels that drive the Figma cover screen.
- Modify: `src/data/portfolio.test.ts`
  Assert the new intro data contract alongside the existing content checks.
- Create: `src/components/sections/IntroPage.tsx`
  Render the standalone cover page that closely follows the supplied Figma intro template.
- Create: `src/components/sections/IntroPage.test.tsx`
  Verify the intro page renders the required content zones and entry CTA.
- Create: `src/components/sections/PortfolioMainPage.tsx`
  Wrap the existing post-entry sections so `App` can switch to a single main-page component.
- Modify: `src/index.css`
  Add only the minimal global styling support needed for the intro cover if Tailwind utility classes alone become unwieldy.

Keep `src/components/sections/HeroSection.tsx` untouched unless the integration work proves it is still coupled to the entry flow. Do not refactor unrelated sections during this change.

## Chunk 1: Lock The Intro-First Behavior Into Tests

### Task 1: Replace The Old App Smoke Test

**Files:**
- Modify: `src/App.test.tsx`

- [ ] **Step 1: Replace the smoke test with an intro-first default test**

Update `src/App.test.tsx` to:

```tsx
import { render, screen } from '@testing-library/react'
import App from './App'

test('renders the intro cover before the main portfolio', () => {
  render(<App />)

  expect(screen.getByText(/from\./i)).toBeInTheDocument()
  expect(screen.getByRole('link', { name: /enter portfolio/i })).toBeInTheDocument()
  expect(screen.queryByText(/my services/i)).not.toBeInTheDocument()
})
```

- [ ] **Step 2: Run the smoke test to verify RED**

Run:

```bash
npm test -- --run src/App.test.tsx
```

Expected: FAIL because the current intro screen still doubles as the old hero flow and the main-page visibility expectations have not been enforced yet.

### Task 2: Lock The Entry Transition And Hash Shortcut

**Files:**
- Modify: `src/App.template.test.tsx`

- [ ] **Step 1: Replace the current template test with click-through and hash-entry coverage**

Update `src/App.template.test.tsx` to:

```tsx
import { fireEvent, render, screen } from '@testing-library/react'
import App from './App'

test('switches from the intro cover to the main portfolio after entry', () => {
  render(<App />)

  expect(screen.getByText(/from\./i)).toBeInTheDocument()

  fireEvent.click(screen.getByRole('link', { name: /enter portfolio/i }))

  expect(screen.getByText(/my services/i)).toBeInTheDocument()
  expect(screen.queryByText(/from\./i)).not.toBeInTheDocument()
  expect(screen.queryByRole('link', { name: /enter portfolio/i })).not.toBeInTheDocument()
})

test('opens the main portfolio directly when the hash is present', () => {
  window.location.hash = '#portfolio-main'

  render(<App />)

  expect(screen.getByText(/my services/i)).toBeInTheDocument()
  expect(screen.queryByText(/from\./i)).not.toBeInTheDocument()
  expect(screen.queryByRole('link', { name: /enter portfolio/i })).not.toBeInTheDocument()

  window.location.hash = ''
})
```

- [ ] **Step 2: Run the app flow test to verify RED**

Run:

```bash
npm test -- --run src/App.template.test.tsx
```

Expected: FAIL because the current screen split and click-through behavior do not yet match the approved intro-first design.

### Task 3: Lock The Intro Data Contract

**Files:**
- Modify: `src/data/portfolio.test.ts`

- [ ] **Step 1: Extend the data test with intro-specific expectations**

Update `src/data/portfolio.test.ts` to:

```tsx
import { portfolio } from './portfolio'

test('contains the approved homepage sections, featured work entries, and intro cover data', () => {
  expect(portfolio.featuredWork).toHaveLength(4)
  expect(portfolio.experience).toHaveLength(3)
  expect(portfolio.capabilities.map((item) => item.title)).toEqual([
    'Applied AI Products',
    'ML Engineering',
    'AI Security Research',
  ])
  expect(portfolio.intro.entryLabel).toBe('Enter Portfolio')
  expect(portfolio.intro.displayName).toMatch(/gaoyi/i)
})
```

- [ ] **Step 2: Run the data test to verify RED**

Run:

```bash
npm test -- --run src/data/portfolio.test.ts
```

Expected: FAIL because the `intro` object does not exist yet.

## Chunk 2: Build The Standalone Intro Cover

### Task 4: Add Intro Types And Content

**Files:**
- Modify: `src/types/portfolio.ts`
- Modify: `src/data/portfolio.ts`
- Test: `src/data/portfolio.test.ts`

- [ ] **Step 1: Add a dedicated intro type to `src/types/portfolio.ts`**

Extend the portfolio types with a separate intro shape:

```ts
export type IntroContent = {
  meta: string
  fromLabel: string
  fromLines: string[]
  toLabel: string
  toLines: string[]
  portfolioLabel: string
  displayName: string
  entryLabel: string
}
```

Then add `intro: IntroContent` to `PortfolioData`.

- [ ] **Step 2: Populate the intro content in `src/data/portfolio.ts`**

Add an `intro` object with cover-specific copy, for example:

```ts
intro: {
  meta: 'Apr 2026',
  fromLabel: 'From.',
  fromLines: ['Gaoyi Wu', 'Applied AI Engineer', 'ML Engineer'],
  toLabel: 'To.',
  toLines: ['Recruiters, hiring managers, and collaborators'],
  portfolioLabel: 'Portfolio',
  displayName: 'GAOYI WU',
  entryLabel: 'Enter Portfolio',
},
```

Keep these values cover-specific; do not repurpose `profile.introLabel` or other hero-only fields.

- [ ] **Step 3: Run the data test to verify GREEN**

Run:

```bash
npm test -- --run src/data/portfolio.test.ts
```

Expected: PASS

### Task 5: Write The IntroPage Test First

**Files:**
- Create: `src/components/sections/IntroPage.test.tsx`

- [ ] **Step 1: Create a failing component test for the intro cover**

Create `src/components/sections/IntroPage.test.tsx`:

```tsx
import { render, screen } from '@testing-library/react'
import { IntroPage } from './IntroPage'
import { portfolio } from '../../data/portfolio'

test('renders the intro cover content and entry CTA', () => {
  render(<IntroPage intro={portfolio.intro} onEnter={() => {}} />)

  expect(screen.getByText(portfolio.intro.meta)).toBeInTheDocument()
  expect(screen.getByText(portfolio.intro.displayName)).toBeInTheDocument()
  expect(screen.getByRole('link', { name: /enter portfolio/i })).toBeInTheDocument()
})
```

- [ ] **Step 2: Run the new component test to verify RED**

Run:

```bash
npm test -- --run src/components/sections/IntroPage.test.tsx
```

Expected: FAIL because `IntroPage` does not exist yet.

### Task 6: Implement The Figma-Faithful Intro Cover

**Files:**
- Create: `src/components/sections/IntroPage.tsx`
- Modify: `src/index.css`
- Test: `src/components/sections/IntroPage.test.tsx`

- [ ] **Step 1: Create `src/components/sections/IntroPage.tsx`**

Implement the component with this shape:

```tsx
import type { IntroContent } from '../../types/portfolio'

type IntroPageProps = {
  intro: IntroContent
  onEnter: () => void
}

export function IntroPage({ intro, onEnter }: IntroPageProps) {
  return (
    <section className="...">
      <p>{intro.meta}</p>
      <div>
        <p>{intro.fromLabel}</p>
        {intro.fromLines.map((line) => (
          <p key={line}>{line}</p>
        ))}
      </div>
      <div>
        <span>{intro.portfolioLabel}</span>
        <h1>{intro.displayName}</h1>
      </div>
      <div>
        <p>{intro.toLabel}</p>
        {intro.toLines.map((line) => (
          <p key={line}>{line}</p>
        ))}
      </div>
      <a
        href="#portfolio-main"
        onClick={(event) => {
          event.preventDefault()
          onEnter()
        }}
      >
        {intro.entryLabel}
      </a>
    </section>
  )
}
```

Layout requirements:
- follow Figma node `1205:2330` as the compositional source of truth
- preserve the clean rounded frame, minimal palette, and oversized central wordmark treatment
- keep the cover visually separate from the orange portrait-led hero language used elsewhere
- adapt content only where needed for Gaoyi Wu's identity

- [ ] **Step 2: Add only the minimal global styling support in `src/index.css`**

If the oversized wordmark or frame styling becomes too awkward in utility classes, add narrowly scoped selectors such as:

```css
.intro-cover-wordmark {
  line-height: 0.82;
}

.intro-cover-frame {
  min-height: calc(100vh - 2rem);
}
```

Do not move generic section styling into this file.

- [ ] **Step 3: Run the intro component test to verify GREEN**

Run:

```bash
npm test -- --run src/components/sections/IntroPage.test.tsx
```

Expected: PASS

- [ ] **Step 4: Commit the intro cover slice**

Run:

```bash
git add src/types/portfolio.ts src/data/portfolio.ts src/data/portfolio.test.ts src/components/sections/IntroPage.tsx src/components/sections/IntroPage.test.tsx src/index.css
git commit -m "feat: add figma intro cover"
```

## Chunk 3: Wire The Main Portfolio Behind Entry And Verify

### Task 7: Wrap The Existing Main Portfolio Screen

**Files:**
- Create: `src/components/sections/PortfolioMainPage.tsx`

- [ ] **Step 1: Create a wrapper for the post-entry content**

Create `src/components/sections/PortfolioMainPage.tsx`:

```tsx
import type { PortfolioData } from '../../types/portfolio'
import { CapabilitiesSection } from './CapabilitiesSection'
import { ContactSection } from './ContactSection'
import { ExperienceSection } from './ExperienceSection'
import { FeaturedWorkSection } from './FeaturedWorkSection'
import { MainHeader } from './MainHeader'
import { SkillsSection } from './SkillsSection'
import { WhyHireSection } from './WhyHireSection'

type PortfolioMainPageProps = {
  portfolio: PortfolioData
}

export function PortfolioMainPage({ portfolio }: PortfolioMainPageProps) {
  return (
    <div id="portfolio-main" className="flex flex-col gap-7">
      <MainHeader />
      <CapabilitiesSection capabilities={portfolio.capabilities} />
      <ExperienceSection experience={portfolio.experience} />
      <WhyHireSection
        profile={portfolio.profile}
        proofPoints={portfolio.proofPoints}
        education={portfolio.education}
        resumeHref={portfolio.contact.resumeHref}
      />
      <FeaturedWorkSection items={portfolio.featuredWork} />
      <SkillsSection skills={portfolio.skills} tickerItems={portfolio.tickerItems} />
      <ContactSection contact={portfolio.contact} notes={portfolio.notes} />
    </div>
  )
}
```

- [ ] **Step 2: Leave unrelated sections alone**

Do not refactor the inner section components in this task. The goal is only to group the current main page behind one entry boundary.

### Task 8: Wire The App Screen Switch

**Files:**
- Modify: `src/App.tsx`
- Test: `src/App.test.tsx`
- Test: `src/App.template.test.tsx`

- [ ] **Step 1: Replace the current `HeroSection` entry flow in `src/App.tsx`**

Update `src/App.tsx` to:

```tsx
import { useState } from 'react'
import { IntroPage } from './components/sections/IntroPage'
import { PortfolioMainPage } from './components/sections/PortfolioMainPage'
import { portfolio } from './data/portfolio'

function App() {
  const [entered, setEntered] = useState(() => {
    if (typeof window === 'undefined') return false
    return window.location.hash === '#portfolio-main'
  })

  const handleEnter = () => {
    setEntered(true)

    if (typeof window !== 'undefined') {
      window.location.hash = 'portfolio-main'
      window.requestAnimationFrame(() => {
        document.getElementById('portfolio-main')?.scrollIntoView({ behavior: 'auto' })
      })
    }
  }

  return (
    <main className="min-h-screen bg-[#f5efe7] px-3 py-4 text-[#171717] sm:px-5 sm:py-6">
      <div className="mx-auto flex max-w-[1320px] flex-col gap-7">
        {entered ? (
          <PortfolioMainPage portfolio={portfolio} />
        ) : (
          <IntroPage intro={portfolio.intro} onEnter={handleEnter} />
        )}
      </div>
    </main>
  )
}

export default App
```

Important details:
- default load shows only `IntroPage`
- click-through shows only `PortfolioMainPage`
- direct `#portfolio-main` still bypasses the intro

- [ ] **Step 2: Run the focused app tests to verify GREEN**

Run:

```bash
npm test -- --run src/App.test.tsx src/App.template.test.tsx
```

Expected: PASS

### Task 9: Run Full Verification And Manual Figma Check

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

- [ ] **Step 3: Run the local dev server for a visual check**

Run:

```bash
npm run dev -- --host 127.0.0.1 --port 4173
```

Expected: Vite serves the portfolio locally on `http://127.0.0.1:4173`

- [ ] **Step 4: Compare the intro cover against the Figma source**

Check these items in the browser against Figma node `1205:2330`:
- overall cover-page composition
- spacing rhythm between the metadata, side text blocks, and wordmark
- oversized name scale and placement
- clean rounded frame and minimal styling
- separation between intro cover and main portfolio page

- [ ] **Step 5: Commit the integrated intro-first flow**

Run:

```bash
git add src/App.tsx src/App.test.tsx src/App.template.test.tsx src/components/sections/PortfolioMainPage.tsx
git commit -m "feat: add intro-first portfolio flow"
```
