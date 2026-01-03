import { describe, it, expect, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import { Header } from '../components/layout/Header'

// Mock ThemeToggle component
vi.mock('../components/ui/ThemeToggle', () => ({
  ThemeToggle: () => <button>Theme Toggle</button>
}))

const renderWithRouter = (component: React.ReactElement) => {
  return render(<BrowserRouter>{component}</BrowserRouter>)
}

describe('Header', () => {
  it('renders logo/brand name', () => {
    renderWithRouter(<Header />)
    expect(screen.getByText('Movie Explorer')).toBeInTheDocument()
  })

  it('renders navigation links', () => {
    renderWithRouter(<Header />)
    
    expect(screen.getByText('Home')).toBeInTheDocument()
    expect(screen.getByText('Movies')).toBeInTheDocument()
    expect(screen.getByText('Actors')).toBeInTheDocument()
    expect(screen.getByText('Directors')).toBeInTheDocument()
    expect(screen.getByText('Favorites')).toBeInTheDocument()
  })

  it('renders theme toggle', () => {
    renderWithRouter(<Header />)
    expect(screen.getByText('Theme Toggle')).toBeInTheDocument()
  })

  it('has correct navigation links', () => {
    renderWithRouter(<Header />)
    
    expect(screen.getByRole('link', { name: 'Home' })).toHaveAttribute('href', '/')
    expect(screen.getByRole('link', { name: 'Movies' })).toHaveAttribute('href', '/movies')
    expect(screen.getByRole('link', { name: 'Actors' })).toHaveAttribute('href', '/actors')
    expect(screen.getByRole('link', { name: 'Directors' })).toHaveAttribute('href', '/directors')
    expect(screen.getByRole('link', { name: 'Favorites' })).toHaveAttribute('href', '/favorites')
  })

  it('applies correct styling classes', () => {
    const { container } = renderWithRouter(<Header />)
    const header = container.querySelector('header')
    
    expect(header).toHaveClass('bg-white', 'shadow-sm', 'border-b')
  })

  it('renders mobile menu button', () => {
    renderWithRouter(<Header />)
    // Find the button that's not the theme toggle (which has text "Theme Toggle")
    const buttons = screen.getAllByRole('button')
    const menuButton = buttons.find(button => button.textContent !== 'Theme Toggle')
    expect(menuButton).toBeInTheDocument()
  })
})
