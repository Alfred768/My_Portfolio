import { portfolio } from './portfolio'

test('contains the approved homepage sections and featured work entries', () => {
  expect(portfolio.featuredWork).toHaveLength(4)
  expect(portfolio.experience).toHaveLength(3)
  expect(portfolio.capabilities.map((item) => item.title)).toEqual([
    'Applied AI Systems',
    'ML Engineering',
    'AI Infrastructure',
  ])
})
