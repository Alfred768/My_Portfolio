import { CapabilitiesSection } from './components/sections/CapabilitiesSection'
import { HeroSection } from './components/sections/HeroSection'
import { portfolio } from './data/portfolio'

function App() {
  return (
    <main className="min-h-screen bg-[#f7f4ee] px-4 py-6 text-slate-900 sm:px-6 sm:py-8">
      <div className="mx-auto flex max-w-7xl flex-col gap-6">
        <HeroSection profile={portfolio.profile} links={portfolio.primaryLinks} />
        <CapabilitiesSection capabilities={portfolio.capabilities} />
      </div>
    </main>
  )
}

export default App
