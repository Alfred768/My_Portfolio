import { render, screen } from '@testing-library/react'
import { portfolioByLanguage } from '../../data/portfolio'
import { EditorialContact } from './EditorialContact'

test('keeps every recruiter contact action functional', () => {
  const contact = portfolioByLanguage.en.contact

  render(<EditorialContact contact={contact} language="en" />)

  expect(screen.getByRole('link', { name: contact.email })).toHaveAttribute(
    'href',
    `mailto:${contact.email}`,
  )
  expect(screen.getByRole('link', { name: contact.linkedInLabel })).toHaveAttribute(
    'href',
    contact.linkedInHref,
  )
  expect(screen.getByRole('link', { name: contact.gitHubLabel })).toHaveAttribute(
    'href',
    contact.gitHubHref,
  )
  expect(screen.getByRole('link', { name: contact.resumeLabel })).toHaveAttribute(
    'href',
    contact.resumeHref,
  )
  expect(screen.getByRole('link', { name: 'Back to top' })).toHaveAttribute('href', '#hero')
})
