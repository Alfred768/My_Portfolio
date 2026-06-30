import { render, screen } from '@testing-library/react'
import { portfolioByLanguage } from '../../data/portfolio'
import { EditorialResearch } from './EditorialResearch'

test('presents iSeal and WebWeaver as editorial research features', () => {
  const content = portfolioByLanguage.en

  render(
    <EditorialResearch
      eyebrow={content.researchEyebrow}
      heading={content.researchHeading}
      intro={content.researchIntro}
      items={content.research}
    />,
  )

  expect(screen.getByRole('heading', { level: 2, name: 'Selected Research' })).toBeVisible()
  expect(screen.getByRole('heading', { name: 'iSeal' })).toBeVisible()
  expect(screen.getByRole('heading', { name: 'WebWeaver' })).toBeVisible()
  expect(screen.getAllByRole('link', { name: 'Read Paper' })).toHaveLength(2)
})
