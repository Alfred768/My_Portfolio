import { useEffect, useState } from 'react'
import { PortfolioMainPage } from './components/sections/PortfolioMainPage'
import { portfolioByLanguage } from './data/portfolio'
import type { Language } from './types/portfolio'

function App() {
  const [language, setLanguage] = useState<Language>(() => {
    if (typeof window === 'undefined') return 'en'

    try {
      return window.localStorage.getItem('portfolio-language') === 'zh' ? 'zh' : 'en'
    } catch {
      return 'en'
    }
  })

  useEffect(() => {
    document.documentElement.lang = language === 'zh' ? 'zh-CN' : 'en'

    try {
      window.localStorage.setItem('portfolio-language', language)
    } catch {
      // The portfolio remains usable when storage is unavailable.
    }
  }, [language])

  return (
    <main className="min-h-screen text-[#191714]">
      <PortfolioMainPage
        content={portfolioByLanguage[language]}
        language={language}
        onLanguageChange={setLanguage}
      />
    </main>
  )
}

export default App
