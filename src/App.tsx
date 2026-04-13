import { CapabilitiesSection } from './components/sections/CapabilitiesSection'
import { ContactSection } from './components/sections/ContactSection'
import { ExperienceSection } from './components/sections/ExperienceSection'
import { FeaturedWorkSection } from './components/sections/FeaturedWorkSection'
import { HeroSection } from './components/sections/HeroSection'
import { SkillsSection } from './components/sections/SkillsSection'
import { WhyHireSection } from './components/sections/WhyHireSection'
import { portfolio } from './data/portfolio'

function App() {
  return (
    <main className="min-h-screen bg-[#f7f4ee] px-4 py-6 text-slate-900 sm:px-6 sm:py-8">
      <div className="mx-auto flex max-w-7xl flex-col gap-6">
        <HeroSection profile={portfolio.profile} links={portfolio.primaryLinks} />
        <CapabilitiesSection capabilities={portfolio.capabilities} />
        <ExperienceSection experience={portfolio.experience} />
        <WhyHireSection
          profile={portfolio.profile}
          proofPoints={portfolio.proofPoints}
          education={portfolio.education}
          resumeHref={portfolio.contact.resumeHref}
        />
        <FeaturedWorkSection items={portfolio.featuredWork} />
        <SkillsSection skills={portfolio.skills} />
        <ContactSection contact={portfolio.contact} />
      </div>
    </main>
  )
}

export default App
