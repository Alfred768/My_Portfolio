import { ArrowRight } from '@phosphor-icons/react'
import { Crosshair } from '../editorial/Crosshair'
import { Reveal } from '../editorial/Reveal'
import type { HeroContent } from '../../types/portfolio'

type EditorialHeroProps = {
  hero: HeroContent
  resumeHref: string
}

export function EditorialHero({ hero, resumeHref }: EditorialHeroProps) {
  return (
    <section aria-labelledby="hero-title" className="sac-hero" id="hero">
      <div className="sac-hero__left">
        <Reveal>
          <h1 className="sac-hero__wordmark" id="hero-title">
            {hero.name}
          </h1>
        </Reveal>

        <div className="sac-hero__lower">
          <Reveal>
            <p className="sac-kicker">
              <span aria-hidden="true" />
              {hero.role}
            </p>
            <p className="sac-hero__specialization">{hero.specialization}</p>
            <p className="sac-hero__summary">{hero.summary}</p>
          </Reveal>

          <Reveal className="sac-hero__actions">
            <a className="sac-button sac-button--accent" href={resumeHref} rel="noreferrer" target="_blank">
              {hero.resumeLabel}
              <ArrowRight aria-hidden="true" weight="thin" />
            </a>
            <a className="sac-button sac-button--ghost" href="#contact">
              {hero.contactLabel}
              <ArrowRight aria-hidden="true" weight="thin" />
            </a>
          </Reveal>
        </div>
      </div>

      <div className="sac-hero__right">
        <figure className="sac-portrait">
          <span className="sac-portrait__field" aria-hidden="true" />
          <img alt={hero.portraitAlt} className="sac-portrait__image" src={hero.portraitSrc} />
          <Crosshair className="sac-portrait__cross sac-portrait__cross--tl" />
          <Crosshair className="sac-portrait__cross sac-portrait__cross--br" />
          <figcaption className="sac-portrait__caption">
            <span>AI / SECURITY / SYSTEMS</span>
            <span>{hero.location}</span>
          </figcaption>
        </figure>
      </div>
    </section>
  )
}
