import { render, screen } from '@testing-library/react'
import { HeroSection } from './HeroSection'
import { portfolio } from '../../data/portfolio'

test('renders the hero headline and core CTA links', () => {
  render(<HeroSection profile={portfolio.profile} links={portfolio.primaryLinks} />)

  expect(screen.getByRole('heading', { name: /gaoyi wu/i })).toBeInTheDocument()
  expect(screen.getByRole('link', { name: /view projects/i })).toBeInTheDocument()
  expect(screen.getByRole('link', { name: /resume/i })).toBeInTheDocument()
})
