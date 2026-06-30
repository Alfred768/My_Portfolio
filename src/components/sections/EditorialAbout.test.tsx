import { render, screen } from '@testing-library/react'
import { portfolioByLanguage } from '../../data/portfolio'
import { EditorialAbout } from './EditorialAbout'

test('turns the profile into a Sac-style blueprint and evidence signal board', () => {
  const content = portfolioByLanguage.en

  render(
    <EditorialAbout
      education={content.education}
      hero={content.hero}
      language="en"
      proof={content.proof}
      skills={content.skills}
    />,
  )

  expect(screen.getByRole('heading', { level: 2, name: 'About me' })).toBeVisible()
  expect(screen.getByText('AAAI 2026')).toBeVisible()
  expect(screen.getByText('2 Published Papers')).toBeVisible()
  expect(screen.getByText('100+ Edge Devices')).toBeVisible()
  expect(screen.getByText('61% → 94% Accuracy')).toBeVisible()
  expect(screen.getByText('Stevens Institute of Technology')).toBeVisible()
})
