export type LinkItem = {
  label: string
  href: string
}

export type IntroPageSection = {
  title: string
  lines: string[]
}

export type IntroCoverPage = {
  id: 'cover'
  meta: string
  fromLabel: string
  fromLines: string[]
  toLabel: string
  toLines: string[]
  portfolioLabel: string
  displayName: string
  entryLabel: string
}

export type IntroAboutPage = {
  id: 'about'
  heading: string
  profileName: string
  profileRole: string
  portraitSrc: string
  paragraphs: string[]
}

export type IntroNotePage = {
  id: 'note'
  heading: string
  sections: IntroPageSection[]
}

export type IntroSequencePage = IntroCoverPage | IntroAboutPage | IntroNotePage

export type IntroContent = {
  brandMark: string
  footerWordmark: string
  pages: [IntroCoverPage, IntroAboutPage, IntroNotePage]
}

export type Capability = {
  kicker: string
  title: string
  summary: string
  imageSrc: string
  imageAlt: string
}

export type ExperienceEntry = {
  company: string
  role: string
  location: string
  period: string
  logoSrc?: string
  logoAlt?: string
  highlights: string[]
}

export type EducationEntry = {
  school: string
  degree: string
  period: string
  logoSrc?: string
  logoAlt?: string
}

export type ProofPoint = {
  title: string
  detail: string
}

export type FeaturedWorkEntry = {
  title: string
  tag: string
  summary: string
  href: string
  linkLabel: string
  secondaryHref?: string
  secondaryLabel?: string
  imageSrc?: string
  imageAlt?: string
  logoSrc?: string
  logoAlt?: string
  stack: string[]
}

export type SkillCategory = {
  title: string
  items: string[]
}

export type NoteCard = {
  title: string
  summary: string
  href: string
  ctaLabel: string
}

export type PortfolioData = {
  intro: IntroContent
  profile: {
    name: string
    eyebrow: string
    headline: string
    summary: string
    portraitSrc: string
    aboutPortraitSrc?: string
    introLabel: string
    quote: string
    heroStat: string
    heroStatLabel: string
  }
  primaryLinks: LinkItem[]
  capabilities: Capability[]
  experience: ExperienceEntry[]
  education: EducationEntry[]
  proofPoints: ProofPoint[]
  featuredWork: FeaturedWorkEntry[]
  skills: SkillCategory[]
  notes: NoteCard[]
  tickerItems: string[]
  contact: {
    email: string
    links: LinkItem[]
    resumeHref: string
  }
}

export type Language = 'en' | 'zh'

export type LocalizedNavigation = {
  research: string
  experience: string
  skills: string
  education: string
  contact: string
  resume: string
  openMenu: string
  closeMenu: string
}

export type HeroContent = {
  name: string
  role: string
  specialization: string
  summary: string
  location: string
  availability: string
  portraitSrc: string
  portraitAlt: string
  resumeLabel: string
  contactLabel: string
}

export type ProofMetric = {
  value: string
  label: string
}

export type ResearchLink = {
  label: string
  href: string
}

export type ResearchEntry = {
  id: string
  number: string
  title: string
  subtitle: string
  venue: string
  period: string
  summary: string
  contributions: string[]
  benchmarkValue: string
  benchmarkLabel: string
  detailLabel: string
  collapseLabel: string
  detail: string
  tags: string[]
  imageSrc: string
  imageAlt: string
  links: ResearchLink[]
}

export type EditorialExperienceEntry = {
  company: string
  role: string
  location: string
  period: string
  highlights: string[]
  logoSrc?: string
  logoAlt?: string
}

export type EditorialSkillGroup = {
  title: string
  items: string[]
}

export type EditorialEducationEntry = {
  school: string
  degree: string
  location: string
  period: string
  logoSrc?: string
  logoAlt?: string
}

export type ContactContent = {
  eyebrow: string
  heading: string
  summary: string
  emailLabel: string
  email: string
  linkedInLabel: string
  linkedInHref: string
  gitHubLabel: string
  gitHubHref: string
  resumeLabel: string
  resumeHref: string
  footer: string
}

export type PortfolioContent = {
  navigation: LocalizedNavigation
  hero: HeroContent
  proof: ProofMetric[]
  researchEyebrow: string
  researchHeading: string
  researchIntro: string
  research: ResearchEntry[]
  experienceEyebrow: string
  experienceHeading: string
  experienceIntro: string
  experience: EditorialExperienceEntry[]
  skillsEyebrow: string
  skillsHeading: string
  skillsIntro: string
  skills: EditorialSkillGroup[]
  educationEyebrow: string
  educationHeading: string
  education: EditorialEducationEntry[]
  contact: ContactContent
}
