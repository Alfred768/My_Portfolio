import { useState } from 'react'
import type { ResearchEntry } from '../../types/portfolio'

type ResearchSectionProps = {
  eyebrow: string
  heading: string
  intro: string
  items: ResearchEntry[]
}

export function ResearchSection({ eyebrow, heading, intro, items }: ResearchSectionProps) {
  const [expanded, setExpanded] = useState<Record<string, boolean>>({})

  return (
    <section id="research" className="editorial-section research-section" aria-labelledby="research-heading">
      <header className="section-intro">
        <p className="section-eyebrow">{eyebrow}</p>
        <h2 id="research-heading">{heading}</h2>
        <p>{intro}</p>
      </header>

      <div className="research-list">
        {items.map((item) => {
          const isExpanded = expanded[item.id] ?? false
          const detailId = `${item.id}-methodology`

          return (
            <article key={item.id} className="research-spread">
              <div className="research-copy">
                <div className="research-meta">
                  <span>{item.number} / PUBLICATION</span>
                  <span>{item.venue}</span>
                  <span>{item.period}</span>
                </div>
                <h3>{item.title}</h3>
                <p className="research-subtitle">{item.subtitle}</p>
                <p className="research-summary">{item.summary}</p>

                <div className="research-contributions">
                  <span>CONTRIBUTION</span>
                  <ul>
                    {item.contributions.map((contribution) => (
                      <li key={contribution}>{contribution}</li>
                    ))}
                  </ul>
                </div>

                <div className="research-benchmark">
                  <strong>{item.benchmarkValue}</strong>
                  <span>{item.benchmarkLabel}</span>
                </div>

                {isExpanded ? (
                  <p className="research-detail" id={detailId}>
                    {item.detail}
                  </p>
                ) : null}

                <div className="research-actions">
                  <button
                    aria-controls={detailId}
                    aria-expanded={isExpanded}
                    onClick={() =>
                      setExpanded((current) => ({ ...current, [item.id]: !isExpanded }))
                    }
                    type="button"
                  >
                    {isExpanded ? item.collapseLabel : item.detailLabel}
                  </button>
                  {item.links.map((link) => (
                    <a key={link.href} href={link.href} target="_blank" rel="noreferrer">
                      {link.label}
                    </a>
                  ))}
                </div>
              </div>

              <div className="research-visual">
                <img alt={item.imageAlt} src={item.imageSrc} />
                <div className="research-tags" aria-label={`${item.title} topics`}>
                  {item.tags.map((tag) => (
                    <span key={tag}>{tag}</span>
                  ))}
                </div>
              </div>
            </article>
          )
        })}
      </div>
    </section>
  )
}
