import { render, screen } from '@testing-library/react'
import { portfolioByLanguage } from '../../data/portfolio'
import { EditorialHero } from './EditorialHero'

test('renders the oversized identity, transparent portrait, and recruiter actions', () => {
  const content = portfolioByLanguage.en

  render(<EditorialHero hero={content.hero} resumeHref={content.contact.resumeHref} />)

  expect(screen.getByRole('heading', { level: 1, name: 'Gaoyi Wu' })).toBeVisible()
  expect(screen.getByAltText('Portrait of Gaoyi Wu')).toHaveAttribute(
    'src',
    '/assets/gaoyi-wu-cutout.png',
  )
  expect(screen.getByRole('link', { name: 'View Resume' })).toHaveAttribute(
    'href',
    '/resume/gaoyi-wu-resume.pdf',
  )
  expect(screen.getByRole('link', { name: 'Contact Me' })).toHaveAttribute(
    'href',
    '#contact',
  )
})
