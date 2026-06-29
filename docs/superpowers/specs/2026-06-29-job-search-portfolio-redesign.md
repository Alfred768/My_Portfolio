# Job-Search Portfolio Redesign

## Goal

Redesign Gaoyi Wu's portfolio to improve conversion with US recruiters and hiring managers.

The site should position Gaoyi primarily as an **AI Algorithm Engineer**, supported by concrete Applied AI and ML engineering evidence. A reviewer should understand the role fit, strongest research credentials, and production experience within 15 seconds.

## Audience

- Recruiters screening AI Algorithm Engineer and Applied AI / ML Engineer candidates.
- Hiring managers evaluating LLM security, multi-agent systems, model evaluation, federated learning, and production ML experience.
- Technical reviewers who may continue into publications, GitHub repositories, and detailed project evidence.

## Source of Truth

- Resume: `GAOYI_WU_AI_Algorithm_Engineer.pdf`.
- Current portfolio code and assets.
- Existing public paper, project, LinkedIn, GitHub, and resume links.
- Sac's portfolio is a visual-language reference only. Its content, identity, and exact layouts must not be copied.

## Positioning

### Primary

**AI Algorithm Engineer**

### Supporting

**LLM Security × Multi-Agent Systems × Applied ML**

Applied AI and ML engineering work should prove that the research can become measurable, maintainable systems. It should not compete with the primary algorithm-engineering message.

## Selected Visual Direction

**Editorial Research Dossier**

The selected direction combines:

- Warm ivory paper surfaces.
- Near-black ink.
- A restrained burnt-orange accent.
- Large editorial serif display typography.
- Neutral sans-serif body typography.
- Fine rules, registration marks, scientific annotations, light halftone, and subtle paper grain.
- Generous whitespace and continuous editorial spreads instead of a grid of generic cards.

The visual system should feel personal, rigorous, and memorable. Decorative details must never reduce legibility or recruiter scan speed.

## Information Architecture

The current three-page intro sequence will be removed. The site opens directly on the portfolio homepage.

Page order:

1. Header and hero.
2. Evidence strip.
3. Selected research.
4. Applied ML experience.
5. Technical skills.
6. Education.
7. Contact and footer.

The desktop header will provide anchored navigation to Research, Experience, Skills, Education, and Contact. Resume and language switching remain immediately accessible.

## Hero

The hero must establish identity and role fit above the fold.

Required content:

- `GAOYI WU`
- `AI Algorithm Engineer`
- `LLM Security × Multi-Agent Systems × Applied ML`
- A concise one- or two-sentence value proposition.
- Resume and Contact actions.
- Gaoyi's real portrait.
- English / Chinese language switch.

The hero will use an asymmetrical editorial composition. Large typography carries the identity while the portrait and technical annotations provide balance. The portrait treatment may use halftone, subtle duotone, or paper blending, but must preserve Gaoyi's recognizable appearance.

## Evidence Strip

The evidence strip sits at the bottom of the hero or immediately below it.

Required signals:

- `AAAI 2026`
- `2 Published Papers`
- `100+ Edge Devices`
- `61% → 94% Accuracy`

Each metric receives a short qualifier so it is not misleading when viewed without context. The strip must stay visible and readable at common desktop and mobile sizes.

## Selected Research

### iSeal

Present iSeal as the lead research case study.

Content priorities:

- Encrypted LLM fingerprinting.
- AAAI 2026 and first-author status.
- Cryptographic key-bound encoder using HMAC-SHA256.
- Five-minute LoRA training on an A100.
- 100% FSR across 12 LLMs.
- Robustness against 10+ attacks.
- Paper link and any verified code or project link.

### WebWeaver

Present WebWeaver as the second research case study.

Content priorities:

- LLM multi-agent topology inference attack.
- arXiv 2026.
- Complete communication-graph inference from one arbitrary compromised agent.
- Covert jailbreak-based and jailbreak-free diffusion paths.
- Approximately 60% improvement in inference accuracy over the stated baselines under active anti-jailbreak defenses.
- Paper link and any verified code or project link.

### Research Interaction

Each case study has:

- A concise recruiter-facing summary.
- A contribution list.
- A benchmark result.
- A visual method or system diagram.
- A details control for secondary material.
- Direct publication and code actions when verified links are available.

The default view remains concise. Expanded content must preserve the reading position and be keyboard accessible.

## Applied ML Experience

### Intellisys Lab

Show the strongest measurable work:

- Federated fine-tuning over 100+ edge devices.
- AG News accuracy improvement from 61% to 94%.
- Activation-based backdoor detection reducing attack success from above 90% to below 30%.
- Privacy-aware RAG evaluation with a 15% answer-quality improvement.

### DHL Express

Show the strongest measurable work:

- XGBoost churn prediction over approximately 12K customer records.
- Retention precision improvement from 0.61 to 0.79.
- BERT sentiment model reaching 0.92 F1.
- PSI-triggered retraining and MLflow auditability.
- Reporting latency reduction of 30%.

Experience entries should read as editorial rows or spreads, not stacked generic cards.

## Technical Skills

Skills remain compact and recruiter-friendly.

Groups:

- LLM and Generative AI.
- ML Security Research.
- Agent Systems.
- Infrastructure.

The list must follow the latest resume. Unsupported or stale skills from the current site should be removed.

## Education

Include:

- Stevens Institute of Technology — M.S. Computer Science, expected May 2026.
- Shenzhen University — B.Mgmt. Logistics, July 2024.

Education should remain concise and visually subordinate to research and experience.

## Contact

The closing section should make the next action obvious.

Required actions:

- Email.
- LinkedIn.
- GitHub.
- Resume.

The message should invite conversations about AI Algorithm Engineer and Applied AI / ML Engineer roles without generic project-designer language.

## Language Behavior

- English is the default.
- A visible `EN / 中文` control switches all user-facing portfolio content.
- Navigation labels, summaries, case-study details, actions, metadata, and contact copy all switch together.
- The selected language persists locally for later visits.
- External publication titles and company names may remain in their official language.
- Missing translations must fall back to English without breaking the page.

## Motion and Interaction

- Smooth anchored navigation.
- Restrained hero entrance and scroll-reveal motion.
- Accessible research-case expansion and collapse.
- Clear hover and focus states.
- No decorative cursor replacement.
- No scroll hijacking.
- Respect `prefers-reduced-motion`.

Animations should clarify hierarchy and state. They must not delay access to content.

## Responsive Behavior

### Desktop

- Asymmetrical hero.
- Horizontal navigation.
- Full evidence strip.
- Research spreads may use two columns.

### Tablet

- Reduced display-type scale.
- Flexible two-column hero.
- Evidence strip may wrap into two rows.
- Research diagrams remain beside or below their summaries based on available width.

### Mobile

- Single-column reading order.
- Compact header with accessible navigation.
- Portrait placed after role and primary actions.
- Evidence metrics use a two-column or single-column grid.
- Research summaries precede diagrams and expanded details.
- Minimum comfortable touch targets and no horizontal page overflow.

## Technical Architecture

Retain the existing React, TypeScript, and Vite application.

Recommended boundaries:

- `PortfolioPage`: owns language state and page composition.
- `PortfolioHeader`: navigation, resume action, and language control.
- `HeroSection`: identity, positioning, portrait, and primary actions.
- `EvidenceStrip`: top proof metrics.
- `ResearchSection`: case-study composition and expansion state.
- `ExperienceSection`: measurable work history.
- `SkillsSection`: current resume-aligned skill groups.
- `EducationSection`: concise education entries.
- `ContactSection`: final actions and footer.
- UI primitives for section labels, actions, metric treatments, and accessible disclosure controls.

Portfolio content remains data-driven and type-safe. English and Chinese strings should use matching content keys so incomplete translations are discoverable during development.

## Data Flow

1. The page initializes the selected language from local storage, falling back to English.
2. `PortfolioPage` selects the matching localized data.
3. Section components receive only the data they render.
4. Research sections own or receive controlled expansion state.
5. External actions use verified URLs from portfolio data.
6. Changing language updates the page immediately and persists the choice.

No backend is required.

## Failure Handling

- Missing Chinese copy falls back to English.
- Missing or failed images preserve the surrounding textual content and layout.
- Unavailable optional code links are omitted instead of replaced with generic destinations.
- External links open safely and do not block use of the page.
- The downloadable resume remains accessible even if decorative assets fail.

## Accessibility

- Semantic heading order.
- Keyboard-operable navigation, language switch, and disclosures.
- Visible focus styles.
- Descriptive image alternative text.
- Sufficient color contrast on paper, ink, and orange treatments.
- Reduced-motion support.
- Controls must have clear accessible names in both languages.

## Testing and Verification

Automated coverage:

- English is the default when no preference exists.
- Language switching updates representative content and persists the preference.
- Navigation targets exist.
- Research cases expand and collapse with accessible state.
- Resume, publication, GitHub, LinkedIn, and email links use expected destinations.
- Core resume facts and metrics render correctly.
- Missing optional links are not rendered.

Visual verification:

- Desktop and mobile hero hierarchy.
- No clipping in display typography.
- No horizontal overflow.
- Evidence strip remains legible.
- Research diagrams and details maintain correct reading order.
- Chinese strings do not collide with rules, labels, or controls.
- Reduced-motion behavior.

Final verification must include a production build, full automated test run, console-error check, and browser review at desktop and mobile widths.

## Out of Scope

- A CMS or backend.
- Blog publishing.
- Visitor analytics dashboards.
- Contact forms that send data.
- New research claims or unverified links.
- Copying Sac's assets, illustrations, or page composition.
- A complete rebrand unrelated to job-search conversion.

## Acceptance Criteria

- The site opens directly on the homepage.
- The first viewport communicates Gaoyi's primary role and strongest proof.
- English and Chinese content are fully switchable.
- iSeal and WebWeaver are the lead projects.
- Latest-resume metrics and skills replace stale portfolio claims.
- Resume, paper, GitHub, LinkedIn, and email actions work.
- The visual result clearly follows the selected Editorial Research Dossier direction.
- Desktop and mobile layouts are polished, readable, and accessible.
