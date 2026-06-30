import { render, screen } from '@testing-library/react'
import { portfolioByLanguage } from '../../data/portfolio'
import { EditorialExperience } from './EditorialExperience'

test('renders applied ML experience as recruiter-scannable archive rows', () => {
  const content = portfolioByLanguage.en

  render(
    <EditorialExperience
      eyebrow={content.experienceEyebrow}
      heading={content.experienceHeading}
      intro={content.experienceIntro}
      items={content.experience}
      skills={content.skills}
    />,
  )

  expect(screen.getByRole('heading', { level: 2, name: 'Applied ML Experience' })).toBeVisible()
  expect(screen.getByText('Intellisys Lab')).toBeVisible()
  expect(screen.getByText('DHL Express')).toBeVisible()
  expect(screen.getByRole('heading', { name: 'Projects & systems' })).toBeVisible()
})
