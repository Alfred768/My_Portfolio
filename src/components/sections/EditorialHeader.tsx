import { List, X } from '@phosphor-icons/react'
import { useState } from 'react'
import type { Language, LocalizedNavigation } from '../../types/portfolio'

type EditorialHeaderProps = {
  navigation: LocalizedNavigation
  language: Language
  onLanguageChange: (language: Language) => void
  resumeHref: string
}

export function EditorialHeader({
  navigation,
  language,
  onLanguageChange,
  resumeHref,
}: EditorialHeaderProps) {
  const [menuOpen, setMenuOpen] = useState(false)
  const links = [
    { label: navigation.about, href: '#about' },
    { label: navigation.research, href: '#research' },
    { label: navigation.experience, href: '#experience' },
    { label: navigation.projects, href: '#projects' },
    { label: navigation.contact, href: '#contact' },
  ]

  return (
    <header className="sac-header">
      <a className="sac-header__brand" href="#portfolio-main">
        Gaoyi Wu
      </a>

      <nav
        aria-label="Primary navigation"
        className={`sac-header__nav ${menuOpen ? 'is-open' : ''}`}
        id="primary-navigation"
      >
        {links.map((link, index) => (
          <span className="sac-header__nav-item" key={link.href}>
            <a href={link.href} onClick={() => setMenuOpen(false)}>
              {link.label}
            </a>
            {index < links.length - 1 ? <i aria-hidden="true">·</i> : null}
          </span>
        ))}
      </nav>

      <div className="sac-header__actions">
        <div aria-label="Language" className="sac-language">
          <button
            aria-pressed={language === 'en'}
            onClick={() => onLanguageChange('en')}
            type="button"
          >
            EN
          </button>
          <span aria-hidden="true">/</span>
          <button
            aria-pressed={language === 'zh'}
            onClick={() => onLanguageChange('zh')}
            type="button"
          >
            中文
          </button>
        </div>
        <a className="sac-header__resume" href={resumeHref} rel="noreferrer" target="_blank">
          {navigation.resume}
        </a>
        <button
          aria-controls="primary-navigation"
          aria-expanded={menuOpen}
          aria-label={menuOpen ? navigation.closeMenu : navigation.openMenu}
          className="sac-header__menu"
          onClick={() => setMenuOpen((open) => !open)}
          type="button"
        >
          {menuOpen ? <X aria-hidden="true" /> : <List aria-hidden="true" />}
        </button>
      </div>
    </header>
  )
}
