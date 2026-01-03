import { describe, it, expect, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import { Layout } from '../components/layout/Layout'

// Mock Header component
vi.mock('../components/layout/Header', () => ({
  Header: () => <header>Header Component</header>
}))

const renderWithRouter = (component: React.ReactElement) => {
  return render(<BrowserRouter>{component}</BrowserRouter>)
}

describe('Layout', () => {
  it('renders header component', () => {
    renderWithRouter(
      <Layout>
        <div>Test content</div>
      </Layout>
    )
    
    expect(screen.getByText('Header Component')).toBeInTheDocument()
  })

  it('renders children content', () => {
    renderWithRouter(
      <Layout>
        <div>Test content</div>
      </Layout>
    )
    
    expect(screen.getByText('Test content')).toBeInTheDocument()
  })

  it('applies correct layout structure', () => {
    const { container } = renderWithRouter(
      <Layout>
        <div>Test content</div>
      </Layout>
    )
    
    const layout = container.firstChild as HTMLElement
    expect(layout).toHaveClass('min-h-screen', 'bg-gray-50')
  })

  it('renders main content area', () => {
    renderWithRouter(
      <Layout>
        <div>Test content</div>
      </Layout>
    )
    
    const main = screen.getByRole('main')
    expect(main).toBeInTheDocument()
    expect(main).toHaveClass('flex-1', 'max-w-7xl', 'mx-auto', 'px-4', 'py-8')
  })

  it('handles multiple children', () => {
    renderWithRouter(
      <Layout>
        <div>First child</div>
        <div>Second child</div>
      </Layout>
    )
    
    expect(screen.getByText('First child')).toBeInTheDocument()
    expect(screen.getByText('Second child')).toBeInTheDocument()
  })
})
