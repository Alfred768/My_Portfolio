import { fireEvent, render, screen } from '@testing-library/react'
import App from './App'

const storage = new Map<string, string>()

beforeEach(() => {
  storage.clear()
  Object.defineProperty(window, 'localStorage', {
    configurable: true,
    value: {
      getItem: (key: string) => storage.get(key) ?? null,
      setItem: (key: string, value: string) => storage.set(key, value),
      removeItem: (key: string) => storage.delete(key),
      clear: () => storage.clear(),
    },
  })
  window.localStorage.clear()
  window.location.hash = ''
})

test('opens directly on the English job-search homepage', () => {
  render(<App />)

  expect(screen.getByRole('heading', { name: /ai algorithm engineer/i })).toBeInTheDocument()
  expect(screen.getByText(/llm security × multi-agent systems × applied ml/i)).toBeInTheDocument()
  expect(screen.queryByText(/^from[.,]?$/i)).not.toBeInTheDocument()
  expect(document.documentElement.lang).toBe('en')
})

test('switches the complete portfolio to Chinese and remembers the choice', () => {
  render(<App />)

  fireEvent.click(screen.getByRole('button', { name: '中文' }))

  expect(screen.getByRole('heading', { name: /ai 算法工程师/i })).toBeInTheDocument()
  expect(screen.getByText(/大模型安全 × 多智能体系统 × 应用机器学习/i)).toBeInTheDocument()
  expect(window.localStorage.getItem('portfolio-language')).toBe('zh')
  expect(document.documentElement.lang).toBe('zh-CN')
})
