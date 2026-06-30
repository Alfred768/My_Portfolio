import type { HeroContent } from '../../types/portfolio'

type HeroSectionProps = {
  hero: HeroContent
  resumeHref: string
}

export function HeroSection({ hero, resumeHref }: HeroSectionProps) {
  return (
    <section className="hero-section" aria-labelledby="hero-role">
      <div className="hero-copy motion-rise">
        <p className="hero-wordmark">GAOYI WU</p>
        <h1 id="hero-role">{hero.role}</h1>
        <p className="hero-specialization">{hero.specialization}</p>
        <p className="hero-summary">{hero.summary}</p>

        <div className="hero-actions">
          <a className="editorial-button editorial-button--filled" href={resumeHref} target="_blank" rel="noreferrer">
            {hero.resumeLabel}
          </a>
          <a className="editorial-button" href="#contact">
            {hero.contactLabel}
          </a>
        </div>

        <dl className="hero-meta">
          <div>
            <dt>LOC.</dt>
            <dd>{hero.location}</dd>
          </div>
          <div>
            <dt>STATUS.</dt>
            <dd>{hero.availability}</dd>
          </div>
        </dl>
      </div>

      <figure className="hero-portrait motion-rise">
        <img alt={hero.portraitAlt} src={hero.portraitSrc} />
        <figcaption>
          <span>PROFILE / 2026</span>
          <span>AI · SECURITY · SYSTEMS</span>
        </figcaption>
      </figure>
    </section>
  )
}
