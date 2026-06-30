import type {
  EditorialExperienceEntry,
  EditorialSkillGroup,
} from '../../types/portfolio'
import { Reveal } from '../editorial/Reveal'

type EditorialExperienceProps = {
  eyebrow: string
  heading: string
  intro: string
  items: EditorialExperienceEntry[]
  skills: EditorialSkillGroup[]
}

export function EditorialExperience({
  eyebrow,
  heading,
  intro,
  items,
  skills,
}: EditorialExperienceProps) {
  return (
    <section aria-labelledby="experience-title" className="sac-experience" id="experience">
      <header className="sac-experience__header">
        <Reveal>
          <h2 className="sac-section-title" id="experience-title">
            {eyebrow}
          </h2>
          <p>{heading}</p>
        </Reveal>
        <Reveal>
          <p className="sac-experience__intro">{intro}</p>
        </Reveal>
      </header>

      <div className="sac-experience__archive">
        {items.map((item, index) => (
          <Reveal className="sac-job" key={`${item.company}-${item.role}`}>
            <article>
              <span className="sac-job__index">{String(index + 1).padStart(2, '0')}</span>
              <div className="sac-job__identity">
                {item.logoSrc ? <img alt={item.logoAlt ?? ''} src={item.logoSrc} /> : null}
                <div>
                  <h3>{item.company}</h3>
                  <p>{item.role}</p>
                </div>
              </div>
              <div className="sac-job__details">
                <p className="sac-job__meta">
                  <span>{item.location}</span>
                  <span>{item.period}</span>
                </p>
                <ul>
                  {item.highlights.map((highlight) => (
                    <li key={highlight}>{highlight}</li>
                  ))}
                </ul>
              </div>
            </article>
          </Reveal>
        ))}
      </div>

      <Reveal>
        <section aria-labelledby="systems-title" className="sac-systems">
          <header>
            <p>TECHNICAL ARCHIVE</p>
            <h3 id="systems-title">Projects &amp; systems</h3>
          </header>
          <div>
            {skills.map((group, index) => (
              <article key={group.title}>
                <span>{String(index + 1).padStart(2, '0')}</span>
                <h4>{group.title}</h4>
                <p>{group.items.join(' · ')}</p>
              </article>
            ))}
          </div>
        </section>
      </Reveal>
    </section>
  )
}
