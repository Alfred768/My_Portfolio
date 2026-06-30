import { render, screen } from '@testing-library/react'
import { portfolioByLanguage } from '../../data/portfolio'
import { ContactSection } from './ContactSection'

test('offers direct job-search contact actions with verified destinations', () => {
  render(<ContactSection contact={portfolioByLanguage.en.contact} />)

  expect(
    screen.getByRole('heading', { name: /building secure ai that works beyond the benchmark/i }),
  ).toBeInTheDocument()
  expect(screen.getByText(/AI Algorithm Engineer and Applied AI \/ ML Engineer roles/i)).toBeInTheDocument()
  expect(screen.getByRole('link', { name: 'Email' })).toHaveAttribute(
    'href',
    'mailto:criswu20010728@gmail.com',
  )
  expect(screen.getByRole('link', { name: 'LinkedIn' })).toHaveAttribute(
    'href',
    'https://www.linkedin.com/in/gaoyiwu/',
  )
  expect(screen.getByRole('link', { name: 'GitHub' })).toHaveAttribute(
    'href',
    'https://github.com/Alfred768',
  )
  expect(screen.getByRole('link', { name: 'Resume' })).toHaveAttribute(
    'href',
    '/resume/gaoyi-wu-resume.pdf',
  )
})
