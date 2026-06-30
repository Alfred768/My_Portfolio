import { render, screen } from '@testing-library/react'
import { portfolioByLanguage } from '../../data/portfolio'
import { SkillsSection } from './SkillsSection'

test('renders the current resume skill index', () => {
  const content = portfolioByLanguage.en

  render(
    <SkillsSection
      eyebrow={content.skillsEyebrow}
      heading={content.skillsHeading}
      intro={content.skillsIntro}
      items={content.skills}
    />,
  )

  expect(screen.getByRole('heading', { name: 'LLM & Generative AI' })).toBeInTheDocument()
  expect(screen.getByRole('heading', { name: 'ML Security Research' })).toBeInTheDocument()
  expect(screen.getByRole('heading', { name: 'Agent Systems' })).toBeInTheDocument()
  expect(screen.getByRole('heading', { name: 'Infrastructure' })).toBeInTheDocument()
  expect(screen.getByText('Hugging Face Transformers')).toBeInTheDocument()
  expect(screen.queryByText('Spring Boot')).not.toBeInTheDocument()
})
