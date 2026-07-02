import { portfolioByLanguage } from './portfolio'

test('provides complete English and Chinese portfolio content', () => {
  expect(Object.keys(portfolioByLanguage)).toEqual(['en', 'zh'])
  expect(portfolioByLanguage.en.hero.role).toBe('AI Algorithm Engineer')
  expect(portfolioByLanguage.zh.hero.role).toBe('AI 算法工程师')
  expect(portfolioByLanguage.en.navigation.research).toBe('Research')
  expect(portfolioByLanguage.zh.navigation.research).toBe('研究')
})

test('leads with the strongest resume-backed proof', () => {
  expect(portfolioByLanguage.en.proof.map((item) => item.value)).toEqual([
    'AAAI 2026',
    '2 Published Papers',
    '100+ Edge Devices',
    '61% → 94% Accuracy',
  ])
})

test('prioritizes research and experience for algorithm-engineering roles', () => {
  expect(portfolioByLanguage.en.research.map((item) => item.title)).toEqual([
    'iSeal',
    'WebWeaver',
  ])
  expect(portfolioByLanguage.en.experience.map((item) => item.company)).toEqual([
    'Intellisys Lab',
    'DHL Express',
  ])
})

test('uses the latest resume skill groups and project assets', () => {
  expect(portfolioByLanguage.en.skills.map((group) => group.title)).toEqual([
    'LLM & Generative AI',
    'ML Security Research',
    'Agent Systems',
    'Infrastructure',
  ])
  expect(portfolioByLanguage.en.research.map((item) => item.imageSrc)).toEqual([
    '/assets/iseal-editorial-diagram.webp',
    '/assets/webweaver-editorial-diagram.webp',
  ])
})
