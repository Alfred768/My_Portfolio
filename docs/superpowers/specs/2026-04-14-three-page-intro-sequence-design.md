# Three-Page Intro Sequence Design Spec

Date: 2026-04-14
Owner: Gaoyi Wu
Status: Approved in chat, awaiting written spec review

## Goal

Replace the current single intro cover with a three-page introduction sequence that follows the supplied Figma pages more literally.

The three intro pages should appear side by side on a dark canvas like the reference screenshot, then hand off to the main portfolio only after the visitor chooses to enter.

## Source Of Truth

Primary design sources:
- Figma introduction pages: `1205:2330`
- Figma design components: `69:2029`
- User-provided screenshot of the three intro pages

Primary content source:
- [project_source.md](/Users/wugaoyi/Learning/求职/Portfolio/project_source.md)

Supporting content sources:
- `GAOYI WU_AI_AI Algorithm Engineer.pdf`
- `GAOYI WU_AI_ML Infra:MLOps.pdf`
- LinkedIn: `https://www.linkedin.com/in/gaoyiwu/`
- GitHub: `https://github.com/Alfred768`

## User-Approved Direction

Approved direction:
- Build a horizontal three-page intro sequence
- Make it visually track the screenshot closely
- Keep the intro pages as separate white rounded cards on a dark background
- Use real source content from `project_source.md` and the existing resume material
- Keep the main portfolio hidden until the user enters from the intro sequence

Rejected direction:
- A vertical intro stack
- A single intro page
- A loose visual adaptation that does not preserve the Figma page sequence

## Information Architecture

The app should open with a horizontal intro strip composed of:

1. Cover page
2. About Me page
3. Disclaimer or recruiter-note page

After the intro sequence, the user can enter the main portfolio page.

The intro sequence and the main portfolio are different phases of the experience. The main portfolio should not be visible under or mixed into the intro strip before entry.

## Layout And Visual Rules

The intro sequence should preserve these Figma traits:
- dark outer canvas
- three separate white rounded pages
- tall portrait-like page proportions
- small top-right page mark
- bottom cropped oversized branding treatment
- editorial spacing rather than website-section spacing

The intro should feel like three portfolio sheets arranged horizontally, not a marketing carousel or dashboard.

## Interaction Design

The intro should behave as a horizontal scroll sequence:
- the user lands on the intro strip first
- the intro pages are browsed side by side
- scrolling should move across the pages horizontally
- the pages should snap cleanly into place so they read as discrete sheets

Entry behavior:
- the main portfolio remains hidden until the user clicks the entry action
- the entry action can live on page 1 and may be repeated on page 3 if it helps completion of the sequence
- the transition into the main portfolio stays inside the same React app

## Page Content Mapping

### Page 1: Cover

Purpose:
- establish the first impression
- preserve the exact compositional feel of the Figma cover page

Content mapping:
- sender block adapted to Gaoyi Wu
- receiver block aimed at recruiters, hiring managers, and collaborators
- portfolio title adapted from the template
- oversized bottom branding adapted to Gaoyi Wu

Implementation constraint:
- fix the underline collision bug by following the real Figma geometry more closely

### Page 2: About Me

Purpose:
- introduce Gaoyi Wu using recruiter-relevant story and positioning

Content should draw from:
- role targets listed in `project_source.md`
- research-to-production framing
- teaching assistant and communication signal
- active lab work and ongoing momentum

Visual structure should stay close to the Figma page:
- large title with underline
- compact profile block
- paragraph content
- oversized cropped branding at the bottom edge

### Page 3: Disclaimer Or Recruiter Note

Purpose:
- keep the Figma page structure while replacing template filler with useful portfolio context

Content should be adapted into a practical note page, such as:
- attribution and project-ownership note
- context around public and ongoing work
- recruiter-facing note on portfolio intent and materials

Visual structure should remain close to the Figma page:
- large heading
- underline
- stacked editorial text blocks
- oversized cropped branding at the bottom edge

## Technical Design

Recommended architecture:
- `App` owns the entered/not-entered state
- intro sequence is a dedicated component, separate from the main portfolio page
- intro data is stored separately from hero or section data
- main portfolio content stays behind a dedicated post-entry wrapper

Recommended behavior model:
- horizontal scroll container with scroll snapping
- one data object per intro page or one structured intro-sequence object with page sections
- no route change required

## Constraints

- Follow the three-page Figma introduction structure closely
- Use `project_source.md` as the content source of truth for adapting the copy
- Do not let the oversized bottom branding collide with the title underline or reading copy
- Keep the main portfolio hidden before entry
- Preserve the dark-canvas plus white-page composition

## Out Of Scope

- Turning the intro into a landing page
- Replacing the intro with generic modern UI patterns
- Rebuilding the rest of the main portfolio in this spec
