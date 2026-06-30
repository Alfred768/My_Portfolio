import { fireEvent, render, screen } from '@testing-library/react'
import { portfolioByLanguage } from '../../data/portfolio'
import { ResearchSection } from './ResearchSection'

test('presents research in priority order with verified publication links', () => {
  const content = portfolioByLanguage.en

  render(
    <ResearchSection
      eyebrow={content.researchEyebrow}
      heading={content.researchHeading}
      intro={content.researchIntro}
      items={content.research}
    />,
  )

  const headings = screen.getAllByRole('heading', { level: 3 }).map((heading) => heading.textContent)
  expect(headings).toEqual(['iSeal', 'WebWeaver'])
  expect(screen.getByText('100% FSR')).toBeInTheDocument()
  expect(screen.getByText('~60%')).toBeInTheDocument()

  const paperLinks = screen.getAllByRole('link', { name: 'Read Paper' })
  expect(paperLinks[0]).toHaveAttribute('href', 'https://arxiv.org/abs/2511.08905')
  expect(paperLinks[1]).toHaveAttribute('href', 'https://arxiv.org/abs/2603.11132')
  expect(screen.queryByRole('link', { name: /code/i })).not.toBeInTheDocument()
})

test('reveals and hides secondary methodology accessibly', () => {
  const content = portfolioByLanguage.en

  render(
    <ResearchSection
      eyebrow={content.researchEyebrow}
      heading={content.researchHeading}
      intro={content.researchIntro}
      items={content.research}
    />,
  )

  const firstToggle = screen.getAllByRole('button', { name: 'Read methodology' })[0]
  expect(firstToggle).toHaveAttribute('aria-expanded', 'false')
  expect(screen.queryByText(/binds an HMAC-SHA256 key/i)).not.toBeInTheDocument()

  fireEvent.click(firstToggle)
  expect(firstToggle).toHaveAttribute('aria-expanded', 'true')
  expect(screen.getByText(/binds an HMAC-SHA256 key/i)).toBeInTheDocument()

  fireEvent.click(screen.getAllByRole('button', { name: 'Hide methodology' })[0])
  expect(screen.queryByText(/binds an HMAC-SHA256 key/i)).not.toBeInTheDocument()
})
