import { useState } from 'react'
import type { Language, LocalizedNavigation } from '../../types/portfolio'

type MainHeaderProps = {
  navigation: LocalizedNavigation
  language: Language
  onLanguageChange: (language: Language) => void
  resumeHref: string
}

export function MainHeader({
  navigation,
  language,
  onLanguageChange,
  resumeHref,
}: MainHeaderProps) {
  const [menuOpen, setMenuOpen] = useState(false)
  const links = [
    { label: navigation.research, href: '#research' },
    { label: navigation.experience, href: '#experience' },
    { label: navigation.skills, href: '#skills' },
    { label: navigation.education, href: '#education' },
    { label: navigation.contact, href: '#contact' },
  ]

  return (
    <header className="editorial-header">
      <a className="editorial-brand" href="#portfolio-main" aria-label="Gaoyi Wu home">
        <span aria-hidden="true">GW</span>
        <strong>GAOYI WU</strong>
      </a>

      <nav aria-label="Primary navigation" className={menuOpen ? 'is-open' : undefined}>
        {links.map((link) => (
          <a key={link.href} href={link.href} onClick={() => setMenuOpen(false)}>
            {link.label}
          </a>
        ))}
      </nav>

      <div className="header-actions">
        <div className="language-switch" aria-label="Language">
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
        <a className="header-resume" href={resumeHref} target="_blank" rel="noreferrer">
          {navigation.resume}
        </a>
        <button
          aria-expanded={menuOpen}
          aria-label={menuOpen ? navigation.closeMenu : navigation.openMenu}
          className="menu-toggle"
          onClick={() => setMenuOpen((open) => !open)}
          type="button"
        >
          {menuOpen
            ? language === 'zh'
              ? '关闭'
              : 'Close'
            : language === 'zh'
              ? '菜单'
              : 'Menu'}
        </button>
      </div>
    </header>
  )
}
