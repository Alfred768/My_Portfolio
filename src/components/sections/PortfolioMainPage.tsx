import type { Language, PortfolioContent } from '../../types/portfolio'
import { EvidenceStrip } from './EvidenceStrip'
import { EducationSection } from './EducationSection'
import { ExperienceSection } from './ExperienceSection'
import { HeroSection } from './HeroSection'
import { MainHeader } from './MainHeader'
import { ResearchSection } from './ResearchSection'
import { SkillsSection } from './SkillsSection'
import { ContactSection } from './ContactSection'

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
    <div id="portfolio-main" className="portfolio-page">
      <MainHeader
        language={language}
        navigation={content.navigation}
        onLanguageChange={onLanguageChange}
        resumeHref={content.contact.resumeHref}
      />
      <HeroSection hero={content.hero} resumeHref={content.contact.resumeHref} />
      <EvidenceStrip proof={content.proof} />
      <ResearchSection
        eyebrow={content.researchEyebrow}
        heading={content.researchHeading}
        intro={content.researchIntro}
        items={content.research}
      />
      <ExperienceSection
        eyebrow={content.experienceEyebrow}
        heading={content.experienceHeading}
        intro={content.experienceIntro}
        items={content.experience}
      />
      <SkillsSection
        eyebrow={content.skillsEyebrow}
        heading={content.skillsHeading}
        intro={content.skillsIntro}
        items={content.skills}
      />
      <EducationSection
        eyebrow={content.educationEyebrow}
        heading={content.educationHeading}
        items={content.education}
      />
      <ContactSection contact={content.contact} />
    </div>
  )
}
