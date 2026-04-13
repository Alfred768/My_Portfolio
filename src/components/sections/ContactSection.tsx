import type { PortfolioData } from '../../types/portfolio'
import { PrimaryButton } from '../ui/PrimaryButton'
import { SectionHeading } from '../ui/SectionHeading'

type ContactSectionProps = {
  contact: PortfolioData['contact']
}

export function ContactSection({ contact }: ContactSectionProps) {
  return (
    <section className="rounded-[32px] bg-[#101010] px-6 py-8 text-white shadow-[0_24px_70px_rgba(15,23,42,0.18)] sm:px-8">
      <div className="flex flex-col gap-8">
        <div className="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">
          <SectionHeading
            eyebrow="Contact"
            title="Let’s connect on"
            accent="the next role"
            description="Public contact stays simple: email, GitHub, LinkedIn, and the current resume."
          />
          <PrimaryButton href={`mailto:${contact.email}`}>Get in Touch</PrimaryButton>
        </div>
        <div className="grid gap-4 md:grid-cols-4">
          {contact.links.map((link) => (
            <a
              key={link.label}
              className="rounded-[24px] border border-white/10 bg-white/6 px-5 py-5 text-sm font-medium text-slate-100 transition hover:-translate-y-1"
              href={link.href}
              target={link.href.startsWith('http') ? '_blank' : undefined}
              rel={link.href.startsWith('http') ? 'noreferrer' : undefined}
            >
              <span className="block text-xs uppercase tracking-[0.18em] text-[#fd853a]">{link.label}</span>
              <span className="mt-3 block break-all text-base">{link.label === 'Email' ? contact.email : link.href.replace(/^mailto:/, '')}</span>
            </a>
          ))}
        </div>
      </div>
    </section>
  )
}
