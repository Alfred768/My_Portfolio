import { fireEvent, render, screen } from '@testing-library/react'
import { portfolioByLanguage } from '../../data/portfolio'
import { MainHeader } from './MainHeader'

test('provides anchored navigation and an accessible language switch', () => {
  const onLanguageChange = vi.fn()

  render(
    <MainHeader
      language="en"
      navigation={portfolioByLanguage.en.navigation}
      onLanguageChange={onLanguageChange}
      resumeHref={portfolioByLanguage.en.contact.resumeHref}
    />,
  )

  expect(screen.getByRole('link', { name: 'Research' })).toHaveAttribute('href', '#research')
  expect(screen.getByRole('link', { name: 'Experience' })).toHaveAttribute('href', '#experience')
  expect(screen.getByRole('link', { name: 'Skills' })).toHaveAttribute('href', '#skills')
  expect(screen.getByRole('link', { name: 'Education' })).toHaveAttribute('href', '#education')
  expect(screen.getByRole('link', { name: 'Contact' })).toHaveAttribute('href', '#contact')
  expect(screen.getByRole('button', { name: 'EN' })).toHaveAttribute('aria-pressed', 'true')

  fireEvent.click(screen.getByRole('button', { name: '中文' }))
  expect(onLanguageChange).toHaveBeenCalledWith('zh')
})
