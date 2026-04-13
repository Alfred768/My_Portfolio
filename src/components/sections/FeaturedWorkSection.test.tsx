import { render, screen } from '@testing-library/react'
import { FeaturedWorkSection } from './FeaturedWorkSection'
import { portfolio } from '../../data/portfolio'

test('renders the approved featured work items', () => {
  render(<FeaturedWorkSection items={portfolio.featuredWork} />)

  expect(screen.getByText(/xclaw/i)).toBeInTheDocument()
  expect(screen.getByText(/iseal/i)).toBeInTheDocument()
  expect(screen.getByText(/langchain multi-agent auditing/i)).toBeInTheDocument()
  expect(screen.getByText(/ongoing lab work/i)).toBeInTheDocument()
})
