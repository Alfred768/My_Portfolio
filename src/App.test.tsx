import { render, screen } from '@testing-library/react'
import App from './App'

test('renders a hero heading for Gaoyi Wu', () => {
  render(<App />)

  expect(screen.getByRole('heading', { name: /gaoyi wu/i })).toBeInTheDocument()
})
