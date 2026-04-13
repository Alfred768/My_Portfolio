# AI Portfolio Design Spec

Date: 2026-04-13
Owner: Gaoyi Wu
Status: Approved in chat, awaiting final user review of this written spec

## Goal

Build a new single-page React + Tailwind portfolio in this folder using the provided Figma portfolio template as the visual foundation, while adapting the content and section behavior for AI/ML job search outcomes.

The site should present Gaoyi Wu as a hybrid AI engineer with strong fit for Applied AI Engineer and ML Engineer roles, while still supporting adjacent positions such as AI Infra, AI Security, Data Scientist, Software Engineer, and Full Stack Developer.

## Audience

Primary audience:
- Recruiters doing a fast first-pass screen
- Engineering hiring managers evaluating practical fit

Reading behavior assumption:
- They will scan quickly
- They need a strong first impression
- They should understand role fit, background, and projects without reading dense resume-style text

## Source Of Truth

Primary content and design sources:
- Figma portfolio template file: `8Eg0eht5nwFGortCleaaJ1`
- Main page frame: `Desktop - 1` (`6:11031`)
- Introduction reference in `project_source.md`: node `1205:2330`
- Local source file: [project_source.md](/Users/wugaoyi/Learning/求职/Portfolio/project_source.md)
- Resume source: `GAOYI WU_AI_AI Algorithm Engineer.pdf`
- Resume source: `GAOYI WU_AI_ML Infra:MLOps.pdf`
- Portrait image: [2.jpg](/Users/wugaoyi/Learning/求职/Portfolio/2.jpg)
- LinkedIn: `https://www.linkedin.com/in/gaoyiwu/`
- GitHub: `https://github.com/Alfred768`
- XClaw repo: `https://github.com/Alfred768/xclaw`
- XClaw site: `https://www.x-claw.shop/`
- Published paper: `https://arxiv.org/pdf/2511.08905`

## Chosen Direction

Approved direction: Figma-inspired adaptation.

This means:
- Keep the single-scroll layout and the overall warm visual rhythm of the chosen Figma template
- Keep the portrait-led first impression
- Keep the section-to-section storytelling feel of the template
- Repurpose content blocks so they are useful for AI/ML recruiting rather than product-design self-promotion

Explicitly rejected:
- A dense resume-like engineering page
- A dark dashboard aesthetic
- A strict one-to-one port of generic designer-template copy and section meaning

## Information Architecture

The portfolio will remain a single scrolling page with this section order:

1. Hero
2. Capability Pillars
3. Work Experience
4. Why Hire Me
5. Featured Work
6. Tech Stack / Skills Matrix
7. Contact

This preserves the original Figma page rhythm while replacing designer-specific meaning with AI/ML job-market positioning.

## Section Design

### 1. Hero

Purpose:
- Catch attention quickly
- Introduce Gaoyi Wu as a credible hybrid AI engineer
- Establish immediate visual identity

Content:
- Real portrait from `2.jpg`
- Name: `Gaoyi Wu`
- Headline centered on hybrid AI engineering, optimized for Applied AI Engineer and ML Engineer roles
- Short supporting description focused on building applied AI and production ML systems
- CTA row linking to:
  - `View Projects`
  - `Resume`
  - `LinkedIn`
  - `GitHub`

Constraints:
- Do not show proof-metric chips in the hero
- Keep the hero visually close to the Figma template
- Tone should be direct and technical, not influencer-style

### 2. Capability Pillars

Purpose:
- Replace generic designer-service cards with fast recruiter-readable capability categories

Approved pillars:
- `Applied AI Systems`
- `ML Engineering`
- `AI Infrastructure`

Each pillar should:
- Explain the type of work performed
- Use concise, plain language
- Avoid turning into a raw keyword list

### 3. Work Experience

Purpose:
- Show professional progression clearly
- Provide recruiter-readable proof of applied work

Approved entries:
- `Intellisys Lab | Research Assistant`
- `DHL Express | AI/ML Engineer Intern`
- `Graduate Teaching Assistant | Stevens`

Content strategy:
- Rewrite resume bullets into shorter, outcome-focused portfolio summaries
- Keep the section visually similar to the Figma timeline structure
- Prioritize role clarity, impact, and technical scope

### 4. Why Hire Me

Purpose:
- Translate technical history into a clear hiring case
- Provide a recruiter-facing summary without sounding generic

This section should emphasize:
- Ability to bridge research and production
- Applied AI and ML systems judgment
- Practical engineering range across modeling, infrastructure, and usable software

This section also contains compact education proof:
- `M.S. Computer Science, Stevens Institute of Technology`
- `B.A. Logistics Management, Shenzhen University`

Metrics and stronger proof signals can appear here instead of in the hero.

### 5. Featured Work

Purpose:
- Surface the strongest work in a visually engaging way
- Show both product-building and research/infra depth

Approved featured items:
- `XClaw`
- `iSeal`
- `LangChain Multi-Agent Auditing & Evaluation Framework`
- `Ongoing Lab Work`

Expected emphasis:
- `XClaw` as a product and engineering proof point
- `iSeal` as paper/research/security credibility
- `LangChain` as applied multi-agent system work
- `Ongoing Lab Work` as active momentum in federated LLM / ML infrastructure

Project cards should remain visually prominent, but the copy should be tighter and more engineering-focused than the original template.

### 6. Tech Stack / Skills Matrix

Purpose:
- Support recruiter keyword scanning
- Organize the stack by role relevance rather than by raw tool dump

Approved categories:
- `AI / ML`
- `Infra / MLOps`
- `Backend / Systems`
- `Frontend / Product`

Content should be derived from the resumes and `project_source.md`, with wording tuned for hiring readability.

### 7. Contact

Purpose:
- Provide clear, low-friction next steps

Approved public contact items:
- Email
- LinkedIn
- GitHub
- Resume

Explicitly excluded:
- Public phone number

CTA should appear:
- In the hero
- In the footer/contact section

## Visual Direction

The visual design should stay close to the approved Figma template:
- Warm and polished
- Portrait-led
- Large headings
- Generous spacing
- Strong section transitions
- Visual-first portfolio area

Approved adaptation rules:
- Preserve the overall feel of the Figma template
- Replace designer-specific content and labels with AI/ML hiring-oriented equivalents
- Keep the portfolio page feeling like a portfolio, not a dashboard or resume dump
- Make buttons and labels practical and direct

## Technical Design

Implementation target:
- React
- Tailwind CSS
- Single-page application

Recommended stack for the initial build:
- Vite + React + TypeScript
- Tailwind CSS
- Static content sourced from local modules/files in the app

Content model:
- No CMS
- No external database
- No blog engine
- Portfolio data should live locally in structured objects/modules for easy editing

Suggested internal content groupings:
- Personal profile data
- Experience entries
- Featured project entries
- Skills categories
- External links

## Assets And External Links

Local assets:
- Portrait image from `2.jpg`

External links that should be wired where appropriate:
- LinkedIn
- GitHub
- XClaw repository
- XClaw site
- Published paper

Project visuals may be sourced from:
- The Figma template structure
- Screenshots captured from provided project links if needed for stronger cards

## Responsive Behavior

The site must work on:
- Desktop
- Tablet
- Mobile

Responsive expectations:
- Hero remains visually strong on mobile
- Text should never overflow its container
- Project cards and timeline must remain readable when stacked
- CTA buttons should stay obvious without overwhelming smaller screens

## Accessibility And UX

The site should include:
- Meaningful headings and section structure
- Alt text for portrait and project visuals
- High enough contrast for readability
- Keyboard-accessible links and buttons
- Clear external link behavior

## Non-Goals For The First Build

The first implementation should not include:
- CMS integration
- Separate project detail pages
- Full blog functionality
- Complex animation systems
- Contact forms with backend handling
- Scheduling/calendar integration

## Verification Expectations

Before implementation is called complete, verify:
- App boots locally
- Production build succeeds
- Layout works on desktop and mobile widths
- All primary links resolve correctly
- Key sections match the approved design intent

## Open Implementation Notes

- `project_source.md` must be treated as an input source during implementation, not ignored after planning
- Resume bullets should be adapted for web readability instead of copied verbatim
- The Figma introduction and component references can be used to guide detailed spacing, cards, and section styling during implementation
- The hero should use the real portrait image, not a placeholder

## Approval Summary

Approved by the user during brainstorming:
- Single-page scrolling portfolio
- Recruiter-first but still credible for hiring managers
- Primary role emphasis on Applied AI Engineer and ML Engineer
- Figma-inspired adaptation rather than strict template copy
- Real portrait in the hero
- Experience section including Intellisys Lab, DHL, and Graduate Teaching Assistant
- Education included as compact proof
- Dedicated tech stack / skills section
- Public CTA limited to email, LinkedIn, GitHub, and resume
