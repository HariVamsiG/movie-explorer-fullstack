import { vi } from 'vitest'
import type { Movie, Actor, Director, Genre, Review, PaginatedResponse } from '../types'

// Mock data
export const mockMovie: Movie = {
  id: 1,
  title: 'Test Movie',
  release_year: 2023,
  rating: 8.5,
  poster_url: 'https://example.com/poster.jpg',
  backdrop_url: 'https://example.com/backdrop.jpg',
  director_name: 'Test Director',
  genres: ['Action', 'Drama'],
  average_rating: 8.5,
  review_count: 10,
  duration: 120,
  plot: 'Test plot'
}

export const mockActor: Actor = {
  id: 1,
  name: 'Test Actor',
  birth_date: '1990-01-01',
  nationality: 'American',
  biography: 'Test biography',
  image_url: 'https://example.com/actor.jpg',
  movies_count: 5,
  movies: [mockMovie],
  created_at: '2023-01-01T00:00:00Z',
  updated_at: '2023-01-01T00:00:00Z'
}

export const mockDirector: Director = {
  id: 1,
  name: 'Test Director',
  birth_date: '1980-01-01',
  nationality: 'American',
  biography: 'Test biography',
  image_url: 'https://example.com/director.jpg',
  movies_count: 3,
  movies: [mockMovie],
  created_at: '2023-01-01T00:00:00Z',
  updated_at: '2023-01-01T00:00:00Z'
}

export const mockGenre: Genre = {
  id: 1,
  name: 'Action',
  description: 'Action movies',
  movies_count: 100,
  created_at: '2023-01-01T00:00:00Z',
  updated_at: '2023-01-01T00:00:00Z'
}

export const mockReview: Review = {
  id: 1,
  reviewer_name: 'Test Reviewer',
  rating: 9,
  comment: 'Great movie!',
  is_featured: true,
  created_at: '2023-01-01T00:00:00Z',
  updated_at: '2023-01-01T00:00:00Z'
}

export const mockPaginatedMovies: PaginatedResponse<Movie> = {
  count: 1,
  next: null,
  previous: null,
  results: [mockMovie]
}

// Mock hooks
export const mockUseMovies = vi.fn(() => ({
  data: mockPaginatedMovies,
  isLoading: false,
  error: null
}))

export const mockUseMovie = vi.fn(() => ({
  data: mockMovie,
  isLoading: false,
  error: null
}))

export const mockUseActors = vi.fn(() => ({
  data: { results: [mockActor] },
  isLoading: false,
  error: null
}))

export const mockUseDirectors = vi.fn(() => ({
  data: { results: [mockDirector] },
  isLoading: false,
  error: null
}))

export const mockUseGenres = vi.fn(() => ({
  data: { results: [mockGenre] },
  isLoading: false,
  error: null
}))

export const mockUseReviews = vi.fn(() => ({
  data: { results: [mockReview] },
  isLoading: false,
  error: null
}))

export const mockUseTopRatedMovies = vi.fn(() => ({
  data: { results: [mockMovie] },
  isLoading: false,
  error: null
}))

export const mockUseFeaturedReviews = vi.fn(() => ({
  data: { results: [mockReview] },
  isLoading: false,
  error: null
}))

// Mock React Router
export const mockNavigate = vi.fn()
export const mockUseParams = vi.fn(() => ({ id: '1' }))
export const mockUseSearchParams = vi.fn(() => [new URLSearchParams(), vi.fn()])
