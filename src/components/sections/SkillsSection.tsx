import type { PortfolioData } from '../../types/portfolio'
import { SectionHeading } from '../ui/SectionHeading'

type SkillsSectionProps = {
  skills: PortfolioData['skills']
}

export function SkillsSection({ skills }: SkillsSectionProps) {
  return (
    <section className="rounded-[32px] bg-[#202020] px-6 py-10 text-white shadow-[0_24px_70px_rgba(15,23,42,0.18)] sm:px-8">
      <div className="flex flex-col gap-8">
        <SectionHeading
          eyebrow="Tech Stack / Skills Matrix"
          title="Tools and systems I use"
          accent="to ship"
          description="Structured for recruiter keyword scans while still reflecting how the stack groups together in real projects."
        />
        <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-4">
          {skills.map((category) => (
            <article key={category.title} className="rounded-[24px] bg-white/8 p-6">
              <h3 className="text-lg font-semibold text-white">{category.title}</h3>
              <ul className="mt-5 space-y-3 text-sm leading-7 text-slate-200">
                {category.items.map((item) => (
                  <li key={item} className="flex items-start gap-3">
                    <span className="mt-2 h-2 w-2 shrink-0 rounded-full bg-[#fd853a]" aria-hidden="true" />
                    <span>{item}</span>
                  </li>
                ))}
              </ul>
            </article>
          ))}
        </div>
      </div>
    </section>
  )
}
