# Intro-First Portfolio Design Spec

Date: 2026-04-14
Owner: Gaoyi Wu
Status: Approved in chat, awaiting written spec review

## Goal

Rework the portfolio so it opens on a dedicated introduction cover page first, then enters the main portfolio page only after the visitor clicks the entry button.

The introduction cover must follow the provided Figma introduction template closely, using it as the structural source of truth instead of a loose visual reference.

## User-Approved Direction

Approved approach:
- Build a true intro-first experience with two explicit screens inside the same React app
- Keep the transition in place inside the app rather than routing to a separate URL path
- Preserve hash-based direct entry to the main portfolio page as a convenience
- Follow the provided Figma template strictly for the intro page composition

Rejected approaches:
- Reusing the current hero section as both intro and portfolio entry
- Using an overlay or modal over the existing main page
- Treating the Figma intro as inspiration instead of a close template

## Source Of Truth

Primary design source:
- Figma introduction template: `https://www.figma.com/design/8Eg0eht5nwFGortCleaaJ1/Portfolio---Product-Designer-Portfolio-Website--Community-?node-id=1205-2330&m=dev&t=75uDZq0i6CcuFDB9-1`

Supporting local sources:
- [project_source.md](/Users/wugaoyi/Learning/求职/Portfolio/project_source.md)
- [src/App.tsx](/Users/wugaoyi/Learning/求职/Portfolio/src/App.tsx)
- [src/components/sections/HeroSection.tsx](/Users/wugaoyi/Learning/求职/Portfolio/src/components/sections/HeroSection.tsx)
- [src/data/portfolio.ts](/Users/wugaoyi/Learning/求职/Portfolio/src/data/portfolio.ts)

## Information Architecture

The application should behave as a two-screen flow:

1. Introduction cover page
2. Main portfolio page

The introduction cover is not a shortened version of the main page hero. It is its own screen with its own layout, copy blocks, and entry action.

The main portfolio page remains the portfolio experience and contains the existing portfolio sections only after entry.

## Screen Design

### 1. Introduction Cover Page

Purpose:
- Create the first impression before any portfolio content is shown
- Mirror the supplied Figma introduction page structure as closely as possible
- Provide a single clear action to enter the portfolio

Visual rules:
- Treat Figma node `1205:2330` as the source of truth for composition
- Preserve the template's overall balance, spacing rhythm, block placement, and oversized central name treatment
- Keep the clean rounded page frame and minimal surface styling from the template
- Adapt only the text content and portfolio identity details needed for Gaoyi Wu
- Do not remix this screen into the current orange portrait hero layout

Expected content zones:
- Small top metadata area
- Sender or identity block
- Receiver or audience block
- Large central display name or portfolio title treatment
- Entry CTA

### 2. Main Portfolio Page

Purpose:
- Present the actual portfolio content after the introduction step
- Keep the current portfolio sections grouped as the second screen in the experience

Behavioral rules:
- Main-page sections are hidden on the default intro-first load
- After entry, the main page becomes the active screen and starts from its top
- Intro-only content should not remain visible once the main page is active

## Interaction Design

Default behavior:
- App loads on the introduction cover page

Entry behavior:
- Clicking `Enter Portfolio` switches the app from intro mode to main-page mode in place
- The main page should appear at its top, like entering the second page of the Figma flow

Direct-entry behavior:
- If the app loads with `#portfolio-main`, it should skip the intro and open the main portfolio page directly

This preserves the existing direct-entry convenience while making the default user journey intro-first.

## Component Architecture

Recommended component split:
- `App`: owns the entered/not-entered state and direct-entry detection
- `IntroPage`: new component for the introduction cover screen
- `PortfolioMainPage`: wrapper component for the existing portfolio sections

Supporting principle:
- The current `HeroSection` should stop acting as both the intro and the top of the portfolio
- Existing portfolio sections should remain part of the main page only

## Data Model

The intro page should have its own data shape instead of borrowing hero-specific fields.

Recommended addition to the portfolio data:
- `intro` object containing the copy and labels needed only for the cover page, such as:
  - metadata label
  - sender block
  - receiver block
  - display title or name
  - entry button label

Reason:
- The intro screen has a different layout and purpose than the main portfolio hero
- Keeping intro content separate prevents the main-page content model from becoming distorted

## Verification

Behavior tests should cover:
- default render shows the intro page first
- clicking `Enter Portfolio` shows the main portfolio page
- loading with `#portfolio-main` opens the main page directly
- intro-only content is absent after entry

Visual acceptance should check the intro page against the Figma template for:
- overall composition
- spacing rhythm
- oversized wordmark scale and placement
- small text-block placement
- rounded frame and minimal styling

## Constraints

- Follow the Figma introduction template strictly
- Keep the transition inside the same React app
- Avoid inventing new layout flourishes before matching the Figma source
- Adapt content to Gaoyi Wu's profile without changing the core intro composition

## Out Of Scope

- Creating a separate route like `/main`
- Reworking the entire portfolio information architecture
- Replacing the main portfolio with a second unrelated visual language
