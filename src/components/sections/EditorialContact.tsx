import {
  ArrowRight,
  ArrowUp,
  EnvelopeSimple,
  GithubLogo,
  LinkedinLogo,
} from '@phosphor-icons/react'
import type { ContactContent, Language } from '../../types/portfolio'
import { Reveal } from '../editorial/Reveal'

type EditorialContactProps = {
  contact: ContactContent
  language: Language
}

export function EditorialContact({ contact, language }: EditorialContactProps) {
  const copy =
    language === 'zh'
      ? {
          kicker: '可接受新的工作机会',
          status: '正在寻找 AI 算法与应用 AI / ML 职位',
          back: '返回顶部',
          location: '美国新泽西州霍博肯',
        }
      : {
          kicker: 'OPEN TO NEW OPPORTUNITIES',
          status: 'Available for AI Algorithm and Applied AI / ML roles',
          back: 'Back to top',
          location: 'Hoboken, New Jersey',
        }
  const marquee = [
    'LLM SECURITY',
    'MULTI-AGENT SYSTEMS',
    'APPLIED ML',
    'FEDERATED LEARNING',
    'AI INFRASTRUCTURE',
  ]

  return (
    <section aria-labelledby="contact-title" className="sac-contact" id="contact">
      <Reveal className="sac-contact__center">
        <p className="sac-contact__kicker">
          <span aria-hidden="true" />
          {copy.kicker}
          <span aria-hidden="true" />
        </p>
        <h2 id="contact-title">{contact.heading}</h2>
        <p>{contact.summary}</p>
        <span className="sac-contact__status">
          <i aria-hidden="true" />
          {copy.status}
        </span>
      </Reveal>

      <div aria-hidden="true" className="sac-marquee">
        <div>
          {[...marquee, ...marquee].map((item, index) => (
            <span key={`${item}-${index}`}>{item} · </span>
          ))}
        </div>
      </div>

      <div className="sac-contact__bar">
        <a aria-label={contact.email} href={`mailto:${contact.email}`}>
          <EnvelopeSimple aria-hidden="true" weight="thin" />
          <span>
            <small>{contact.emailLabel}</small>
            <strong>{contact.email}</strong>
          </span>
          <ArrowRight aria-hidden="true" weight="thin" />
        </a>
        <a href={contact.linkedInHref} rel="noreferrer" target="_blank">
          <LinkedinLogo aria-hidden="true" weight="thin" />
          <span>{contact.linkedInLabel}</span>
          <ArrowRight aria-hidden="true" weight="thin" />
        </a>
        <a href={contact.gitHubHref} rel="noreferrer" target="_blank">
          <GithubLogo aria-hidden="true" weight="thin" />
          <span>{contact.gitHubLabel}</span>
          <ArrowRight aria-hidden="true" weight="thin" />
        </a>
        <a href={contact.resumeHref} rel="noreferrer" target="_blank">
          <span>{contact.resumeLabel}</span>
          <ArrowRight aria-hidden="true" weight="thin" />
        </a>
      </div>

      <footer className="sac-contact__footer">
        <span>{contact.footer}</span>
        <span>{copy.location}</span>
        <a aria-label="Back to top" href="#hero">
          {copy.back}
          <ArrowUp aria-hidden="true" weight="thin" />
        </a>
      </footer>
    </section>
  )
}
