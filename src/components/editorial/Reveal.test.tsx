import { render, screen } from '@testing-library/react'
import { Reveal } from './Reveal'

test('keeps content visible when intersection observation is unavailable', () => {
  render(
    <Reveal>
      <span>Visible research</span>
    </Reveal>,
  )

  expect(screen.getByText('Visible research').parentElement).toHaveClass('is-visible')
})
