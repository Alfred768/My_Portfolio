import type { EditorialExperienceEntry } from '../../types/portfolio'

type ExperienceSectionProps = {
  eyebrow: string
  heading: string
  intro: string
  items: EditorialExperienceEntry[]
}

export function ExperienceSection({ eyebrow, heading, intro, items }: ExperienceSectionProps) {
  return (
    <section id="experience" className="editorial-section experience-section" aria-labelledby="experience-heading">
      <header className="section-intro">
        <p className="section-eyebrow">{eyebrow}</p>
        <h2 id="experience-heading">{heading}</h2>
        <p>{intro}</p>
      </header>

      <div className="experience-list">
        {items.map((item, index) => (
          <article key={item.company} className="experience-row">
            <div className="experience-index">{String(index + 1).padStart(2, '0')}</div>
            <div className="experience-company">
              {item.logoSrc ? (
                <img
                  alt={item.logoAlt ?? ''}
                  onError={(event) => {
                    event.currentTarget.hidden = true
                  }}
                  src={item.logoSrc}
                />
              ) : null}
              <div>
                <h3>{item.company}</h3>
                <p>{item.role}</p>
              </div>
            </div>
            <div className="experience-period">
              <span>{item.period}</span>
              <span>{item.location}</span>
            </div>
            <ul>
              {item.highlights.map((highlight) => (
                <li key={highlight}>{highlight}</li>
              ))}
            </ul>
          </article>
        ))}
      </div>
    </section>
  )
}
