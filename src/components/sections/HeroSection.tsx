import type { PortfolioData } from '../../types/portfolio'
import { PrimaryButton } from '../ui/PrimaryButton'

type HeroSectionProps = {
  profile: PortfolioData['profile']
  links: PortfolioData['primaryLinks']
}

export function HeroSection({ profile, links }: HeroSectionProps) {
  return (
    <section className="relative overflow-hidden rounded-[36px] bg-white px-6 py-8 shadow-[0_28px_90px_rgba(15,23,42,0.10)] sm:px-10 sm:py-10 lg:px-12">
      <div className="absolute inset-x-10 bottom-0 h-52 rounded-t-full bg-[#f8b26a] blur-3xl" aria-hidden="true" />
      <div className="relative grid items-center gap-10 lg:grid-cols-[minmax(0,1.15fr)_minmax(280px,440px)]">
        <div className="flex flex-col gap-5">
          <p className="text-sm font-medium uppercase tracking-[0.22em] text-[#fd853a]">
            {profile.eyebrow}
          </p>
          <h1 className="max-w-3xl text-4xl font-semibold leading-none tracking-[-0.05em] text-slate-950 sm:text-6xl">
            {profile.name}
          </h1>
          <p className="max-w-2xl text-xl font-medium leading-8 text-slate-900 sm:text-2xl">
            {profile.headline}
          </p>
          <p className="max-w-2xl text-base leading-7 text-slate-600">{profile.summary}</p>
          <div className="flex flex-wrap gap-3 pt-2">
            {links.map((link, index) => (
              <PrimaryButton
                key={link.label}
                href={link.href}
                target={link.href.startsWith('http') ? '_blank' : undefined}
                rel={link.href.startsWith('http') ? 'noreferrer' : undefined}
                variant={index === 0 ? 'solid' : 'ghost'}
              >
                {link.label}
              </PrimaryButton>
            ))}
          </div>
        </div>
        <div className="relative mx-auto w-full max-w-[420px]">
          <div className="absolute inset-x-8 bottom-4 top-16 rounded-t-full bg-[#fd853a]" aria-hidden="true" />
          <div className="relative overflow-hidden rounded-[32px]">
            <img
              alt="Portrait of Gaoyi Wu"
              className="aspect-[4/5] w-full object-cover object-top"
              src={profile.portraitSrc}
            />
          </div>
        </div>
      </div>
    </section>
  )
}
