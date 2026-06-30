import { fireEvent, render, screen } from '@testing-library/react'
import { portfolioByLanguage } from '../../data/portfolio'
import { EditorialHeader } from './EditorialHeader'

test('provides the Sac-style navigation, language switch, and mobile menu', () => {
  const onLanguageChange = vi.fn()

  render(
    <EditorialHeader
      language="en"
      navigation={portfolioByLanguage.en.navigation}
      onLanguageChange={onLanguageChange}
      resumeHref={portfolioByLanguage.en.contact.resumeHref}
    />,
  )

  expect(screen.getByRole('link', { name: 'Gaoyi Wu' })).toHaveAttribute(
    'href',
    '#portfolio-main',
  )
  expect(screen.getByRole('link', { name: 'About' })).toHaveAttribute('href', '#about')
  expect(screen.getByRole('link', { name: 'Research' })).toHaveAttribute('href', '#research')
  expect(screen.getByRole('link', { name: 'Experience' })).toHaveAttribute(
    'href',
    '#experience',
  )
  expect(screen.getByRole('link', { name: 'Projects' })).toHaveAttribute('href', '#projects')
  expect(screen.getByRole('link', { name: 'Resume' })).toHaveAttribute(
    'href',
    '/resume/gaoyi-wu-resume.pdf',
  )

  const menuButton = screen.getByRole('button', { name: 'Open navigation' })
  expect(menuButton).toHaveAttribute('aria-expanded', 'false')
  fireEvent.click(menuButton)
  expect(screen.getByRole('button', { name: 'Close navigation' })).toHaveAttribute(
    'aria-expanded',
    'true',
  )

  fireEvent.click(screen.getByRole('button', { name: '中文' }))
  expect(onLanguageChange).toHaveBeenCalledWith('zh')
})
