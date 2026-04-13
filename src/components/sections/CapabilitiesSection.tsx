import type { PortfolioData } from '../../types/portfolio'
import { SectionHeading } from '../ui/SectionHeading'

type CapabilitiesSectionProps = {
  capabilities: PortfolioData['capabilities']
}

export function CapabilitiesSection({ capabilities }: CapabilitiesSectionProps) {
  return (
    <section className="space-y-8 rounded-[32px] bg-[#1f1f1f] px-6 py-8 text-white shadow-[0_24px_70px_rgba(15,23,42,0.18)] sm:px-8 sm:py-10">
      <div className="flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
        <SectionHeading
          eyebrow="Capability Pillars"
          title="Building applied AI with"
          accent="engineering discipline"
          description="The original Figma service cards become a recruiter-friendly view of the systems work, ML implementation, and infrastructure work I actually do."
        />
      </div>
      <div className="grid gap-5 md:grid-cols-3">
        {capabilities.map((capability) => (
          <article
            key={capability.title}
            className="flex min-h-56 flex-col justify-between rounded-[24px] bg-white/8 p-6 backdrop-blur-sm transition hover:-translate-y-1 hover:bg-white/12"
          >
            <div className="space-y-4">
              <div className="h-12 w-12 rounded-2xl bg-[#fd853a]" aria-hidden="true" />
              <h3 className="text-xl font-semibold text-white">{capability.title}</h3>
              <p className="text-sm leading-7 text-slate-200">{capability.summary}</p>
            </div>
          </article>
        ))}
      </div>
    </section>
  )
}
