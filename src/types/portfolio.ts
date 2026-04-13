export type LinkItem = {
  label: string
  href: string
}

export type Capability = {
  title: string
  summary: string
}

export type ExperienceEntry = {
  company: string
  role: string
  location: string
  period: string
  highlights: string[]
}

export type EducationEntry = {
  school: string
  degree: string
  period: string
}

export type FeaturedWorkEntry = {
  title: string
  tag: string
  summary: string
  href: string
  secondaryHref?: string
}

export type SkillCategory = {
  title: string
  items: string[]
}

export type PortfolioData = {
  profile: {
    name: string
    eyebrow: string
    headline: string
    summary: string
    portraitSrc: string
  }
  primaryLinks: LinkItem[]
  capabilities: Capability[]
  experience: ExperienceEntry[]
  education: EducationEntry[]
  proofPoints: string[]
  featuredWork: FeaturedWorkEntry[]
  skills: SkillCategory[]
  contact: {
    email: string
    links: LinkItem[]
    resumeHref: string
  }
}
