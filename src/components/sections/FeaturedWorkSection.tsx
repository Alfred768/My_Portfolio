import type { PortfolioData } from '../../types/portfolio'
import { SectionHeading } from '../ui/SectionHeading'

type FeaturedWorkSectionProps = {
  items: PortfolioData['featuredWork']
}

const cardAccents = [
  'from-[#f9d4b4] via-[#f7eee4] to-white',
  'from-[#d7e8ff] via-[#eff5ff] to-white',
  'from-[#d9f5e5] via-[#eef9f2] to-white',
  'from-[#fce2ee] via-[#fff3f8] to-white',
]

export function FeaturedWorkSection({ items }: FeaturedWorkSectionProps) {
  return (
    <section id="projects" className="rounded-[32px] bg-white px-6 py-10 shadow-[0_24px_70px_rgba(15,23,42,0.08)] sm:px-8">
      <div className="flex flex-col gap-10">
        <div className="flex flex-col gap-5 md:flex-row md:items-end md:justify-between">
          <SectionHeading
            eyebrow="Featured Work"
            title="Selected projects and"
            accent="ongoing research"
            description="This section keeps the portfolio energy of the Figma gallery while focusing the copy on shipped systems, research outcomes, and engineering credibility."
          />
        </div>
        <div className="grid gap-6 xl:grid-cols-2">
          {items.map((item, index) => (
            <article
              key={item.title}
              className={`overflow-hidden rounded-[28px] bg-gradient-to-br ${cardAccents[index % cardAccents.length]} shadow-[0_18px_48px_rgba(15,23,42,0.08)]`}
            >
              <div className="space-y-6 p-6">
                <div className="flex items-start justify-between gap-4">
                  <span className="rounded-full bg-white/90 px-4 py-2 text-xs font-medium uppercase tracking-[0.18em] text-slate-700">
                    {item.tag}
                  </span>
                  <div className="flex gap-2">
                    <a
                      className="rounded-full bg-slate-950 px-4 py-2 text-sm font-medium text-white"
                      href={item.href}
                      target={item.href.startsWith('http') ? '_blank' : undefined}
                      rel={item.href.startsWith('http') ? 'noreferrer' : undefined}
                    >
                      Open
                    </a>
                    {item.secondaryHref ? (
                      <a
                        className="rounded-full border border-slate-300 bg-white px-4 py-2 text-sm font-medium text-slate-900"
                        href={item.secondaryHref}
                        target="_blank"
                        rel="noreferrer"
                      >
                        Live
                      </a>
                    ) : null}
                  </div>
                </div>
                <div className="rounded-[24px] bg-white/70 p-5 backdrop-blur-sm">
                  <div className="grid gap-4 sm:grid-cols-[1.2fr_0.8fr]">
                    <div className="space-y-3">
                      <h3 className="text-3xl font-semibold tracking-[-0.05em] text-slate-950">
                        {item.title}
                      </h3>
                      <p className="text-sm leading-7 text-slate-700">{item.summary}</p>
                    </div>
                    <div className="grid grid-cols-2 gap-3">
                      <div className="rounded-[18px] bg-white px-4 py-5 shadow-[0_12px_30px_rgba(15,23,42,0.05)]" />
                      <div className="rounded-[18px] bg-white/80 px-4 py-5 shadow-[0_12px_30px_rgba(15,23,42,0.05)]" />
                      <div className="col-span-2 rounded-[18px] bg-slate-950 px-4 py-5 shadow-[0_12px_30px_rgba(15,23,42,0.05)]" />
                    </div>
                  </div>
                </div>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  )
}
