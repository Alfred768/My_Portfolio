import type { EditorialEducationEntry } from '../../types/portfolio'

type EducationSectionProps = {
  eyebrow: string
  heading: string
  items: EditorialEducationEntry[]
}

export function EducationSection({ eyebrow, heading, items }: EducationSectionProps) {
  return (
    <section id="education" className="editorial-section education-section" aria-labelledby="education-heading">
      <header className="section-intro section-intro--compact">
        <p className="section-eyebrow">{eyebrow}</p>
        <h2 id="education-heading">{heading}</h2>
      </header>

      <div className="education-list">
        {items.map((item) => (
          <article key={item.school}>
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
              <h3>{item.school}</h3>
              <p>{item.degree}</p>
              <span>{item.location}</span>
            </div>
            <strong>{item.period}</strong>
          </article>
        ))}
      </div>
    </section>
  )
}
