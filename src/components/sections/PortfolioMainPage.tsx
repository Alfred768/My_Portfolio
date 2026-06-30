import type { Language, PortfolioContent } from '../../types/portfolio'
import { Crosshair } from '../editorial/Crosshair'
import { EditorialAbout } from './EditorialAbout'
import { EditorialContact } from './EditorialContact'
import { EditorialExperience } from './EditorialExperience'
import { EditorialHeader } from './EditorialHeader'
import { EditorialHero } from './EditorialHero'
import { EditorialResearch } from './EditorialResearch'

type PortfolioMainPageProps = {
  content: PortfolioContent
  language: Language
  onLanguageChange: (language: Language) => void
}

export function PortfolioMainPage({
  content,
  language,
  onLanguageChange,
}: PortfolioMainPageProps) {
  return (
    <div id="portfolio-main" className="sac-page">
      <EditorialHeader
        language={language}
        navigation={content.navigation}
        onLanguageChange={onLanguageChange}
        resumeHref={content.contact.resumeHref}
      />
      <aside aria-hidden="true" className="sac-rail">
        <span />
        <i />
        <i />
        <i />
      </aside>
      <Crosshair className="sac-page__cross sac-page__cross--tr" />
      <Crosshair className="sac-page__cross sac-page__cross--bl" />
      <Crosshair className="sac-page__cross sac-page__cross--br" />

      <EditorialHero hero={content.hero} resumeHref={content.contact.resumeHref} />
      <EditorialAbout
        education={content.education}
        hero={content.hero}
        language={language}
        proof={content.proof}
        skills={content.skills}
      />
      <EditorialResearch
        eyebrow={content.researchEyebrow}
        heading={content.researchHeading}
        intro={content.researchIntro}
        items={content.research}
      />
      <EditorialExperience
        eyebrow={content.experienceEyebrow}
        heading={content.experienceHeading}
        intro={content.experienceIntro}
        items={content.experience}
        skills={content.skills}
      />
      <EditorialContact contact={content.contact} language={language} />
    </div>
  )
}
