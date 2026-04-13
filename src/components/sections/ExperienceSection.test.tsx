import { render, screen } from '@testing-library/react'
import { ExperienceSection } from './ExperienceSection'
import { portfolio } from '../../data/portfolio'

test('renders the approved experience entries', () => {
  render(<ExperienceSection experience={portfolio.experience} />)

  expect(screen.getAllByText(/intellisys lab/i)[0]).toBeInTheDocument()
  expect(screen.getAllByText(/dhl express/i)[0]).toBeInTheDocument()
  expect(screen.getByText(/graduate teaching assistant/i)).toBeInTheDocument()
})
