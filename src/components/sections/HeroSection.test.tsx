import { render, screen } from '@testing-library/react'
import { portfolioByLanguage } from '../../data/portfolio'
import { EvidenceStrip } from './EvidenceStrip'
import { HeroSection } from './HeroSection'

test('renders the recruiter-first identity and primary actions', () => {
  const content = portfolioByLanguage.en

  render(
    <>
      <HeroSection hero={content.hero} resumeHref={content.contact.resumeHref} />
      <EvidenceStrip proof={content.proof} />
    </>,
  )

  expect(screen.getByText('GAOYI WU')).toBeInTheDocument()
  expect(screen.getByRole('heading', { name: 'AI Algorithm Engineer' })).toBeInTheDocument()
  expect(screen.getByText('LLM Security × Multi-Agent Systems × Applied ML')).toBeInTheDocument()
  expect(screen.getByRole('img', { name: 'Portrait of Gaoyi Wu' })).toHaveAttribute(
    'src',
    '/assets/gaoyi-wu-cutout.png',
  )
  expect(screen.getByRole('link', { name: 'View Resume' })).toHaveAttribute(
    'href',
    '/resume/gaoyi-wu-resume.pdf',
  )
  expect(screen.getByRole('link', { name: 'Contact Me' })).toHaveAttribute('href', '#contact')
  expect(screen.getByText('61% → 94% Accuracy')).toBeInTheDocument()
})
