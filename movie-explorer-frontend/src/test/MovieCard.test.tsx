import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import { MovieCard } from '../components/features/MovieCard'
import { mockMovie } from './mocks'

// Mock hooks
vi.mock('../hooks/useFavorites', () => ({
  useFavorites: () => ({
    favorites: [],
    addFavorite: vi.fn(),
    removeFavorite: vi.fn(),
    isFavorite: vi.fn(() => false)
  })
}))

const renderWithRouter = (component: React.ReactElement) => {
  return render(<BrowserRouter>{component}</BrowserRouter>)
}

describe('MovieCard', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('renders movie information correctly', () => {
    renderWithRouter(<MovieCard movie={mockMovie} />)
    
    expect(screen.getByText('Test Movie')).toBeInTheDocument()
    expect(screen.getByText('2023')).toBeInTheDocument()
    expect(screen.getByText('Test Director')).toBeInTheDocument()
    expect(screen.getByText('8.5')).toBeInTheDocument()
  })

  it('renders genres when available', () => {
    renderWithRouter(<MovieCard movie={mockMovie} />)
    
    expect(screen.getByText('Action')).toBeInTheDocument()
    expect(screen.getByText('Drama')).toBeInTheDocument()
  })

  it('handles movie without genres', () => {
    const movieWithoutGenres = { ...mockMovie, genres: [] }
    renderWithRouter(<MovieCard movie={movieWithoutGenres} />)
    
    expect(screen.getByText('Test Movie')).toBeInTheDocument()
  })

  it('handles movie with null poster', () => {
    const movieWithoutPoster = { ...mockMovie, poster_url: null }
    renderWithRouter(<MovieCard movie={movieWithoutPoster} />)
    
    expect(screen.getByText('Test Movie')).toBeInTheDocument()
  })

  it('renders favorite button', () => {
    renderWithRouter(<MovieCard movie={mockMovie} />)
    
    const favoriteButton = screen.getByRole('button')
    expect(favoriteButton).toBeInTheDocument()
  })

  it('links to movie detail page', () => {
    renderWithRouter(<MovieCard movie={mockMovie} />)
    
    const link = screen.getByRole('link')
    expect(link).toHaveAttribute('href', '/movies/1')
  })

  it('displays rating with correct format', () => {
    const movieWithRating = { ...mockMovie, average_rating: 7.8 }
    renderWithRouter(<MovieCard movie={movieWithRating} />)
    
    expect(screen.getByText('7.8')).toBeInTheDocument()
  })

  it('handles movie without rating', () => {
    const movieWithoutRating = { ...mockMovie, rating: null }
    renderWithRouter(<MovieCard movie={movieWithoutRating} />)
    
    expect(screen.getByText('Test Movie')).toBeInTheDocument()
  })
})
