# Sac Strict A Portfolio Redesign

Date: 2026-06-30
Status: Approved design brief, pending written-spec review
Primary visual and interaction baseline: `Sac-Y/sac-ai.com` commit `86473fc4431a631a0f5fa22bdcd3c333ba9537c1`
Audit baseline: `tmp/audit-sac-reference-2026-06-30/audit-report.md`

## Goal

Rebuild Gaoyi Wu's bilingual job-search portfolio as a source-faithful adaptation
of the six-stage Sac editorial site. Preserve Sac's screen composition, spacing,
type scale, dark transition, navigation behavior, reveal motion, portrait
treatment, terminal animation, and responsive rhythm. Replace Sac's identity and
content with Gaoyi's verified resume, publication, experience, project, and
contact information.

The result must serve recruiters and engineering hiring managers for AI Agent,
AI Algorithm, Applied AI, ML Infrastructure, MLE, Data Science, and SDE roles.

## Source of Truth

Use these sources in priority order:

1. Reference repository and screenshots at commit `86473fc`.
2. The strict-reference audit report and its same-viewport comparisons.
3. Six current resumes in `/Users/wugaoyi/Learning/求职/英文简历(最新)`.
4. Public project repositories, paper pages, and live deployments.
5. Existing portfolio assets that depict Gaoyi or his work.

Do not preserve a current layout merely because it already exists when it
conflicts with the reference composition.

## Information Architecture

The page keeps the reference's six full-screen stages:

1. `Hero`
2. `About`
3. `Writing`
4. `Shoot`
5. `Build`
6. `Contact`

Each desktop stage has a clear visual beginning and ending and targets one
viewport at the reference desktop size of `1672 x 941`. Content may reflow and
grow naturally on smaller screens without horizontal overflow.

The navigation maps the reference labels to recruiter-friendly labels without
changing its geometry:

- ABOUT
- RESEARCH
- EXPERIENCE
- PROJECTS
- CONTACT

The right-side statistic becomes a concise job-search signal rather than a
follower count. The GitHub icon links to Gaoyi's GitHub profile. The active
section indicator, smooth scrolling, and dark-section inversion match the
reference behavior.

## Screen Mapping

### 1. Hero

Match the reference's approximately `38% / 62%` left-right composition.

- Left: oversized `GAOYI WU` wordmark, target-role kicker, two-line positioning
  statement, Resume and Contact actions.
- Right: Gaoyi's transparent portrait at the reference scale and overlap.
- Portrait treatment: canvas-driven orange/black particle aggregation and
  reveal, with a reduced-motion static fallback.
- Preserve the reference paper texture, registration marks, rhythm rail, title
  texture, entry reveal, and CTA geometry.

### 2. About

Keep the reference's two-column blueprint and signal-console structure.

- Left: `About me`, short positioning statement, and a blueprint portrait card
  based on Gaoyi's real portrait.
- Blueprint annotations summarize role focus, location, degree, and technical
  domains.
- Right flow nodes become `RESEARCH / BUILD / SHIP`.
- The signal console becomes a compact recruiter evidence table containing
  publications, deployed systems, current research, and availability.
- Education and skill proof are embedded in the reference table density rather
  than extending the section beyond one desktop viewport.

### 3. Writing -> Research

Recreate the reference Writing screen rather than the current equal-card grid.

- Oversized distressed `Research` heading in the reference position.
- One featured item: iSeal.
- Three archive rows: WebWeaver, federated LLM systems, and LangChain
  multi-agent auditing/evaluation.
- Preserve the reference feature image ratio, metadata row, category status,
  reading-time-like metadata, hover movement, and archive separators.
- All available destinations are real links. iSeal links to its paper and public
  implementation; WebWeaver links to arXiv.
- Images use pre-sized source assets appropriate for their slots. No image is
  stretched or forced through an incompatible `object-fit: cover` crop.

### 4. Shoot -> Experience

Keep the reference's full dark cinematic stage and navigation inversion.

- The stage communicates production experience rather than video content.
- Intellisys Lab is the primary episode; DHL Express is the secondary role.
- Preserve REC/status treatment, frame marks, timeline/player rail, timecode,
  oversized background word, and dark image overlay.
- Use a real Gaoyi/technical source image, treated to fit the target crop.
- Experience outcomes remain concise and metric-led so the screen retains the
  reference density.

### 5. Build -> Projects

Use Approach A: two flagship systems plus three research/agent projects, all
within the reference Build visual system.

The five canonical projects are:

1. Prediction Router MCP
2. XClaw
3. iSeal
4. WebWeaver
5. LangChain Multi-Agent Auditing and Evaluation Framework

Prediction Router MCP is the active terminal project. Its real build/search
language replaces the reference placeholder terminal copy. The remaining four
projects appear in the Git-style queue/archive area.

Every project exposes only verified destinations:

- Prediction Router MCP: GitHub and live deployment.
- XClaw: GitHub and live product site.
- iSeal: GitHub implementation and AAAI/paper destination.
- WebWeaver: arXiv paper.
- LangChain auditing: complete on-page project summary; no fabricated repository
  or deployment link. A resume-evidence link may be used only when labeled
  explicitly.

Preserve the reference terminal typing loop, compile-state labels, progress bar,
measurement marks, queue styling, ruler, and reduced-motion completion state.

### 6. Contact

Restore the one-screen contact composition from the reference.

- Direct job-search statement and availability status.
- Keyword marquee.
- Email, LinkedIn, GitHub, and Resume visible in the first desktop viewport.
- Footer and location/status metadata remain inside the screen boundary.
- All contact controls use semantic anchors and visible keyboard focus.

## Content Model

Keep content separate from presentation and localize all user-facing strings.

Required data groups:

- navigation
- hero
- about evidence
- research feature and archive
- experience episodes
- five canonical projects
- contact and resume links

Project entries support:

- title
- category
- period
- concise outcome
- technologies
- status
- optional GitHub URL
- optional live URL
- optional paper URL
- optional evidence URL

Missing URLs remain absent. Components must not render empty or misleading
buttons.

## Interaction Model

- Intersection-based active navigation.
- Navigation and global decoration invert only while the navigation line
  overlaps the dark Experience stage.
- Smooth in-page navigation with reduced-motion fallback.
- Section reveal animations modeled on the reference timing.
- Hero particle animation pauses or simplifies when off-screen.
- Build terminal begins when visible, pauses when hidden, and loops using the
  reference rhythm.
- Mobile navigation is fully operable by keyboard and closes after selection.
- External links open in a new tab with safe `rel` attributes.

## Image Handling

- Measure every image slot before selecting its asset.
- Use Gaoyi's transparent cutout for Hero.
- Create or derive a real portrait-based blueprint asset for About; do not use a
  placeholder drawing.
- Use the existing iSeal and WebWeaver source graphics for Research.
- Use project screenshots only where the reference composition has an image
  slot.
- Set explicit aspect ratios and intrinsic dimensions to prevent layout shift.
- Choose `contain` for diagrams and `cover` only for photographic slots whose
  source crop has been verified at desktop and mobile breakpoints.

## Accessibility and Failure Handling

- Preserve semantic regions and heading order.
- Ensure every image has meaningful alternate text or is marked decorative.
- Add visible focus treatment matching the visual system.
- Darken small orange and muted text enough to meet WCAG AA without visibly
  changing the palette.
- Respect `prefers-reduced-motion`.
- If canvas, image, or animation initialization fails, content and links remain
  visible and usable.
- If clipboard or storage APIs are unavailable, navigation and contact links
  still work.

## Testing

### Unit and component tests

- all six sections render in reference order
- all five canonical projects render
- verified project destinations have correct URLs
- missing project URLs do not create fake actions
- language switching preserves corresponding content
- mobile menu exposes every navigation target
- reduced-motion fallbacks render completed states
- image components use the intended fit mode and dimensions

### Build verification

- TypeScript build passes
- production Vite build passes
- existing unrelated user changes are preserved

### Browser QA

Use the in-app browser selected by the user.

- Compare source and implementation at `1672 x 941`.
- Capture and compare all six desktop stages.
- Verify `390 x 844` mobile hero, navigation, and every section for overflow.
- Test active navigation, dark inversion, external links, terminal animation,
  and keyboard focus.
- Run at least two visual correction passes against combined source/current
  comparisons.

## Non-Goals

- Do not reproduce Sac's personal identity, claims, social metrics, or written
  content.
- Do not add unrelated routes, dashboards, CMS, analytics, or backend services.
- Do not list every public GitHub repository.
- Do not use generic placeholder imagery or fabricated project links.
- Do not keep the current equal research-card or static skill-card project
  layouts when they conflict with the reference.

## Acceptance Criteria

The redesign is complete when:

1. The six-stage desktop composition is visibly aligned with reference commit
   `86473fc`.
2. The audit's major structural failures are resolved.
3. The five canonical projects are present with accurate, usable destinations.
4. Research and project images display without accidental cropping or
   distortion.
5. Navigation highlighting, dark inversion, portrait treatment, reveal motion,
   terminal typing, progress animation, and reduced-motion fallbacks work.
6. Contact information is visible within the Contact desktop viewport.
7. Tests and production build pass.
8. Desktop and mobile browser QA show no broken layout, overflow, or console
   errors.
