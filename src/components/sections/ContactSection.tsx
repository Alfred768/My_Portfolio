import type { ContactContent } from '../../types/portfolio'

type ContactSectionProps = {
  contact: ContactContent
}

export function ContactSection({ contact }: ContactSectionProps) {
  const links = [
    {
      label: contact.emailLabel,
      value: contact.email,
      href: `mailto:${contact.email}`,
      external: false,
    },
    {
      label: contact.linkedInLabel,
      value: 'linkedin.com/in/gaoyiwu',
      href: contact.linkedInHref,
      external: true,
    },
    {
      label: contact.gitHubLabel,
      value: 'github.com/Alfred768',
      href: contact.gitHubHref,
      external: true,
    },
    {
      label: contact.resumeLabel,
      value: 'PDF',
      href: contact.resumeHref,
      external: true,
    },
  ]

  return (
    <section id="contact" className="contact-section" aria-labelledby="contact-heading">
      <div>
        <p className="section-eyebrow">{contact.eyebrow}</p>
        <h2 id="contact-heading">{contact.heading}</h2>
        <p>{contact.summary}</p>
      </div>

      <div className="contact-links">
        {links.map((link) => (
          <a
            key={link.label}
            aria-label={link.label}
            href={link.href}
            target={link.external ? '_blank' : undefined}
            rel={link.external ? 'noreferrer' : undefined}
          >
            <span>{link.label}</span>
            <strong>{link.value}</strong>
          </a>
        ))}
      </div>

      <footer>{contact.footer}</footer>
    </section>
  )
}
