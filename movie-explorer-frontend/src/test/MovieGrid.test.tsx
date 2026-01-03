import { describe, it, expect, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import { MovieGrid } from '../components/features/MovieGrid'
import { mockMovie } from './mocks'

const renderWithRouter = (component: React.ReactElement) => {
  return render(<BrowserRouter>{component}</BrowserRouter>)
}

// Mock MovieCard component
vi.mock('../components/features/MovieCard', () => ({
  MovieCard: ({ movie }: { movie: any }) => (
    <div data-testid={`movie-card-${movie.id}`}>
      {movie.title}
    </div>
  )
}))

describe('MovieGrid', () => {
  const movies = [
    mockMovie,
    { ...mockMovie, id: 2, title: 'Movie 2' },
    { ...mockMovie, id: 3, title: 'Movie 3' }
  ]

  it('renders all movies in grid', () => {
    renderWithRouter(<MovieGrid movies={movies} />)
    
    expect(screen.getByTestId('movie-card-1')).toBeInTheDocument()
    expect(screen.getByTestId('movie-card-2')).toBeInTheDocument()
    expect(screen.getByTestId('movie-card-3')).toBeInTheDocument()
  })

  it('applies grid layout classes', () => {
    const { container } = renderWithRouter(<MovieGrid movies={movies} />)
    const grid = container.firstChild as HTMLElement
    
    expect(grid).toHaveClass('grid', 'grid-cols-1', 'sm:grid-cols-2', 'lg:grid-cols-3', 'xl:grid-cols-4')
  })

  it('renders empty grid when no movies', () => {
    const { container } = renderWithRouter(<MovieGrid movies={[]} />)
    
    // Should show the "No movies found" message instead of empty grid
    expect(screen.getByText('No movies found')).toBeInTheDocument()
    expect(screen.getByText('Try adjusting your search criteria or filters.')).toBeInTheDocument()
  })

  it('handles single movie', () => {
    renderWithRouter(<MovieGrid movies={[mockMovie]} />)
    
    expect(screen.getByTestId('movie-card-1')).toBeInTheDocument()
    expect(screen.queryByTestId('movie-card-2')).not.toBeInTheDocument()
  })
})
