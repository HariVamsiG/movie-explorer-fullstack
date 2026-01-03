import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import { LoadingSpinner, LoadingCard, LoadingPage } from '../components/ui/Loading'

describe('LoadingSpinner', () => {
  it('renders with default size', () => {
    const { container } = render(<LoadingSpinner />)
    const spinner = container.firstChild as HTMLElement
    expect(spinner).toHaveClass('animate-spin', 'h-8', 'w-8')
  })

  it('renders with small size', () => {
    const { container } = render(<LoadingSpinner size="sm" />)
    const spinner = container.firstChild as HTMLElement
    expect(spinner).toHaveClass('h-4', 'w-4')
  })

  it('renders with large size', () => {
    const { container } = render(<LoadingSpinner size="lg" />)
    const spinner = container.firstChild as HTMLElement
    expect(spinner).toHaveClass('h-12', 'w-12')
  })

  it('applies custom className', () => {
    const { container } = render(<LoadingSpinner className="custom-class" />)
    const spinner = container.firstChild as HTMLElement
    expect(spinner).toHaveClass('custom-class')
  })
})

describe('LoadingPage', () => {
  it('renders loading message', () => {
    render(<LoadingPage />)
    expect(screen.getByText('Loading...')).toBeInTheDocument()
  })

  it('renders spinner', () => {
    const { container } = render(<LoadingPage />)
    const spinner = container.querySelector('.animate-spin')
    expect(spinner).toBeInTheDocument()
  })
})

describe('LoadingCard', () => {
  it('renders skeleton card', () => {
    const { container } = render(<LoadingCard />)
    const card = container.firstChild as HTMLElement
    expect(card).toHaveClass('rounded-lg', 'border', 'bg-white')
  })

  it('has pulse animation', () => {
    const { container } = render(<LoadingCard />)
    const pulseElement = container.querySelector('.animate-pulse')
    expect(pulseElement).toBeInTheDocument()
  })
})
