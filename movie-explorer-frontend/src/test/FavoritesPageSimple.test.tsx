import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import { FavoritesPage } from '../pages/FavoritesPage'

// Mock localStorage
const localStorageMock = {
  getItem: vi.fn(),
  setItem: vi.fn(),
  removeItem: vi.fn(),
}
Object.defineProperty(window, 'localStorage', { value: localStorageMock })

const renderWithRouter = (component: React.ReactElement) => {
  return render(<BrowserRouter>{component}</BrowserRouter>)
}

describe('FavoritesPage', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    localStorageMock.getItem.mockReturnValue(null)
  })

  it('renders empty state correctly', () => {
    renderWithRouter(<FavoritesPage />)
    expect(screen.getByText('No favorites yet')).toBeInTheDocument()
    expect(screen.getByText('Start adding movies to your favorites to see them here.')).toBeInTheDocument()
  })

  it('renders browse movies link in empty state', () => {
    renderWithRouter(<FavoritesPage />)
    const browseLink = screen.getByRole('link', { name: /browse movies/i })
    expect(browseLink).toHaveAttribute('href', '/movies')
  })
})
