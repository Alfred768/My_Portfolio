import { render, screen } from '@testing-library/react'
import { portfolioByLanguage } from '../../data/portfolio'
import { EducationSection } from './EducationSection'

test('renders current education and dates', () => {
  const content = portfolioByLanguage.en

  render(
    <EducationSection
      eyebrow={content.educationEyebrow}
      heading={content.educationHeading}
      items={content.education}
    />,
  )

  expect(screen.getByText('M.S. Computer Science')).toBeInTheDocument()
  expect(screen.getByText('Expected May 2026')).toBeInTheDocument()
  expect(screen.getByText('B.Mgmt. Logistics')).toBeInTheDocument()
  expect(screen.getByText('July 2024')).toBeInTheDocument()
})
