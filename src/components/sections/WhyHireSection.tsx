import type { PortfolioData } from '../../types/portfolio'
import { PrimaryButton } from '../ui/PrimaryButton'
import { SectionHeading } from '../ui/SectionHeading'

type WhyHireSectionProps = {
  profile: PortfolioData['profile']
  proofPoints: PortfolioData['proofPoints']
  education: PortfolioData['education']
  resumeHref: string
}

export function WhyHireSection({
  profile,
  proofPoints,
  education,
  resumeHref,
}: WhyHireSectionProps) {
  return (
    <section className="grid gap-8 rounded-[32px] bg-[#eef2f6] px-6 py-8 shadow-[0_24px_70px_rgba(15,23,42,0.08)] lg:grid-cols-[360px_minmax(0,1fr)] lg:px-8">
      <div className="relative mx-auto flex w-full max-w-[320px] items-end justify-center overflow-hidden rounded-[28px] bg-[#fdcf99]">
        <img
          alt="Portrait of Gaoyi Wu in a warm profile card"
          className="h-full w-full object-cover object-top"
          src={profile.portraitSrc}
        />
      </div>
      <div className="flex flex-col gap-6">
        <SectionHeading
          eyebrow="Why Hire Me"
          title="Research depth with"
          accent="delivery focus"
          description="I work comfortably across model development, AI infrastructure, and product-facing implementation, which makes me effective in both applied AI and ML engineering roles."
        />
        <div className="grid gap-4 sm:grid-cols-3">
          {proofPoints.map((point) => (
            <div key={point} className="rounded-[24px] bg-white px-5 py-5 shadow-[0_18px_48px_rgba(15,23,42,0.06)]">
              <p className="text-sm leading-7 text-slate-700">{point}</p>
            </div>
          ))}
        </div>
        <div className="rounded-[28px] bg-white px-6 py-5 shadow-[0_18px_48px_rgba(15,23,42,0.06)]">
          <p className="text-sm font-medium uppercase tracking-[0.18em] text-[#fd853a]">Education</p>
          <div className="mt-4 grid gap-4 sm:grid-cols-2">
            {education.map((entry) => (
              <div key={entry.school} className="space-y-1">
                <h3 className="text-lg font-semibold text-slate-950">{entry.school}</h3>
                <p className="text-sm text-slate-700">{entry.degree}</p>
                <p className="text-sm text-slate-500">{entry.period}</p>
              </div>
            ))}
          </div>
        </div>
        <div>
          <PrimaryButton href={resumeHref}>See Resume</PrimaryButton>
        </div>
      </div>
    </section>
  )
}
