import type { EditorialSkillGroup } from '../../types/portfolio'

type SkillsSectionProps = {
  eyebrow: string
  heading: string
  intro: string
  items: EditorialSkillGroup[]
}

export function SkillsSection({ eyebrow, heading, intro, items }: SkillsSectionProps) {
  return (
    <section id="skills" className="editorial-section skills-section" aria-labelledby="skills-heading">
      <header className="section-intro">
        <p className="section-eyebrow">{eyebrow}</p>
        <h2 id="skills-heading">{heading}</h2>
        <p>{intro}</p>
      </header>

      <div className="skills-index">
        {items.map((group, index) => (
          <article key={group.title}>
            <span>{String(index + 1).padStart(2, '0')}</span>
            <h3>{group.title}</h3>
            <ul>
              {group.items.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          </article>
        ))}
      </div>
    </section>
  )
}
