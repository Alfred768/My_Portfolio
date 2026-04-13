import type { PortfolioData } from '../../types/portfolio'
import { SectionHeading } from '../ui/SectionHeading'

type ExperienceSectionProps = {
  experience: PortfolioData['experience']
}

export function ExperienceSection({ experience }: ExperienceSectionProps) {
  return (
    <section className="rounded-[32px] bg-white px-6 py-10 shadow-[0_24px_70px_rgba(15,23,42,0.08)] sm:px-8">
      <div className="flex flex-col gap-10">
        <SectionHeading
          align="center"
          eyebrow="My Work Experience"
          title="Previous roles that shaped"
          accent="how I build"
          description="A recruiter-readable view of the environments, systems, and responsibilities I have worked through in recent years."
        />
        <div className="grid gap-8 lg:grid-cols-[1fr_64px_1fr]">
          <div className="space-y-10">
            {experience.map((entry) => (
              <article key={entry.company} className="space-y-2">
                <h3 className="text-2xl font-semibold tracking-[-0.04em] text-slate-950">
                  {entry.company}
                </h3>
                <p className="text-sm font-medium uppercase tracking-[0.18em] text-slate-500">
                  {entry.period}
                </p>
                <p className="text-base leading-7 text-slate-600">{entry.location}</p>
              </article>
            ))}
          </div>
          <div className="hidden lg:flex lg:justify-center">
            <div className="relative flex w-12 flex-col items-center py-2">
              <div className="absolute bottom-6 top-6 w-px bg-slate-300" aria-hidden="true" />
              {experience.map((entry) => (
                <span
                  key={entry.company}
                  className="relative my-[3.85rem] h-5 w-5 rounded-full border-4 border-white bg-[#fd853a] shadow-[0_0_0_6px_rgba(253,133,58,0.12)]"
                />
              ))}
            </div>
          </div>
          <div className="space-y-10">
            {experience.map((entry) => (
              <article key={`${entry.company}-${entry.role}`} className="space-y-3">
                <div>
                  <h3 className="text-2xl font-semibold tracking-[-0.04em] text-slate-950">
                    {entry.role}
                  </h3>
                  <p className="text-base text-slate-600">{entry.company}</p>
                </div>
                <ul className="space-y-3 text-sm leading-7 text-slate-600">
                  {entry.highlights.map((highlight) => (
                    <li key={highlight} className="flex gap-3">
                      <span className="mt-2 h-2 w-2 shrink-0 rounded-full bg-[#fd853a]" aria-hidden="true" />
                      <span>{highlight}</span>
                    </li>
                  ))}
                </ul>
              </article>
            ))}
          </div>
        </div>
      </div>
    </section>
  )
}
