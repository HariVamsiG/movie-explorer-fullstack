import { vi } from 'vitest'

export const mockUseMovies = vi.fn()
export const mockUseMovie = vi.fn()
export const mockUseActors = vi.fn()
export const mockUseActor = vi.fn()
export const mockUseDirectors = vi.fn()
export const mockUseDirector = vi.fn()
export const mockUseGenres = vi.fn()
export const mockUseReviews = vi.fn()
export const mockUseTopRatedMovies = vi.fn()
export const mockUseFeaturedReviews = vi.fn()

// Set default return values
mockUseMovies.mockReturnValue({
  data: { results: [], count: 0 },
  isLoading: false,
  error: null
})

mockUseMovie.mockReturnValue({
  data: null,
  isLoading: false,
  error: null
})

mockUseActors.mockReturnValue({
  data: { results: [] },
  isLoading: false,
  error: null
})

mockUseActor.mockReturnValue({
  data: null,
  isLoading: false,
  error: null
})

mockUseDirectors.mockReturnValue({
  data: { results: [] },
  isLoading: false,
  error: null
})

mockUseDirector.mockReturnValue({
  data: null,
  isLoading: false,
  error: null
})

mockUseGenres.mockReturnValue({
  data: { results: [] },
  isLoading: false,
  error: null
})

mockUseReviews.mockReturnValue({
  data: { results: [] },
  isLoading: false,
  error: null
})

mockUseTopRatedMovies.mockReturnValue({
  data: { results: [] },
  isLoading: false,
  error: null
})

mockUseFeaturedReviews.mockReturnValue({
  data: { results: [] },
  isLoading: false,
  error: null
})
