import { ArrowUpRight } from '@phosphor-icons/react'
import type { ResearchEntry } from '../../types/portfolio'
import { Reveal } from '../editorial/Reveal'

type EditorialResearchProps = {
  eyebrow: string
  heading: string
  intro: string
  items: ResearchEntry[]
}

export function EditorialResearch({
  eyebrow,
  heading,
  intro,
  items,
}: EditorialResearchProps) {
  return (
    <section aria-labelledby="research-title" className="sac-research" id="research">
      <span className="sac-section-anchor" id="projects" />
      <header className="sac-research__header">
        <Reveal>
          <h2 className="sac-section-title" id="research-title">
            {eyebrow}
          </h2>
        </Reveal>
        <Reveal>
          <p className="sac-research__statement">{heading}</p>
          <p className="sac-research__intro">{intro}</p>
        </Reveal>
      </header>

      <div className="sac-research__grid">
        {items.map((item, index) => (
          <Reveal className={index === 0 ? 'sac-paper sac-paper--featured' : 'sac-paper'} key={item.id}>
            <article>
              <figure className="sac-paper__media">
                <img alt={item.imageAlt} src={item.imageSrc} />
                <span>{item.number}</span>
              </figure>
              <div className="sac-paper__body">
                <p className="sac-paper__meta">
                  <span>{item.venue}</span>
                  <span>{item.period}</span>
                </p>
                <h3>{item.title}</h3>
                <p className="sac-paper__subtitle">{item.subtitle}</p>
                <p className="sac-paper__summary">{item.summary}</p>
                <div className="sac-paper__benchmark">
                  <strong>{item.benchmarkValue}</strong>
                  <span>{item.benchmarkLabel}</span>
                </div>
                <div className="sac-paper__links">
                  {item.links.map((link) => (
                    <a href={link.href} key={link.href} rel="noreferrer" target="_blank">
                      {link.label}
                      <ArrowUpRight aria-hidden="true" weight="thin" />
                    </a>
                  ))}
                </div>
              </div>
            </article>
          </Reveal>
        ))}
      </div>
    </section>
  )
}
