import { render, screen } from '@testing-library/react'
import { portfolioByLanguage } from '../../data/portfolio'
import { ExperienceSection } from './ExperienceSection'

test('renders the latest measurable ML experience in priority order', () => {
  const content = portfolioByLanguage.en

  render(
    <ExperienceSection
      eyebrow={content.experienceEyebrow}
      heading={content.experienceHeading}
      intro={content.experienceIntro}
      items={content.experience}
    />,
  )

  const companies = screen.getAllByRole('heading', { level: 3 }).map((heading) => heading.textContent)
  expect(companies).toEqual(['Intellisys Lab', 'DHL Express'])
  expect(screen.getByText(/100\+ edge devices/i)).toBeInTheDocument()
  expect(screen.getByText(/0.61 to 0.79/i)).toBeInTheDocument()
  expect(screen.getByText(/0.92 F1/i)).toBeInTheDocument()
})
