import { useQuery } from '@tanstack/react-query'
import { moviesApi, actorsApi, directorsApi, genresApi, reviewsApi } from '../services/api'
import type { MovieFilters } from '../types'

// Movies queries
export const useMovies = (filters?: MovieFilters & { page?: number; page_size?: number; ordering?: string }) => {
  return useQuery({
    queryKey: ['movies', filters?.page || 1, filters?.page_size || 20, filters?.ordering || '', filters],
    queryFn: () => moviesApi.getMovies(filters),
    select: (data) => data.data,
  })
}

export const useMovie = (id: number) => {
  return useQuery({
    queryKey: ['movie', id],
    queryFn: () => moviesApi.getMovie(id),
    select: (data) => data.data,
    enabled: !!id,
  })
}

export const useTopRatedMovies = () => {
  return useQuery({
    queryKey: ['movies', 'top-rated'],
    queryFn: () => moviesApi.getTopRatedMovies(),
    select: (data) => data.data,
  })
}

// Actors queries
export const useActors = (params?: { page?: number; name?: string; page_size?: number }) => {
  return useQuery({
    queryKey: ['actors', params?.page || 1, params?.page_size || 20, params],
    queryFn: () => actorsApi.getActors(params),
    select: (data) => data.data,
  })
}

export const useActor = (id: number) => {
  return useQuery({
    queryKey: ['actor', id],
    queryFn: () => actorsApi.getActor(id),
    select: (data) => data.data,
    enabled: !!id,
  })
}

// Directors queries
export const useDirectors = (params?: { page?: number; name?: string; page_size?: number }) => {
  return useQuery({
    queryKey: ['directors', params?.page || 1, params?.page_size || 20, params],
    queryFn: () => directorsApi.getDirectors(params),
    select: (data) => data.data,
  })
}

export const useDirector = (id: number) => {
  return useQuery({
    queryKey: ['director', id],
    queryFn: () => directorsApi.getDirector(id),
    select: (data) => data.data,
    enabled: !!id,
  })
}

// Genres queries
export const useGenres = () => {
  return useQuery({
    queryKey: ['genres'],
    queryFn: () => genresApi.getGenres(),
    select: (data) => data.data,
  })
}

// Reviews queries
export const useReviews = (params?: { movie_id?: number; page?: number }) => {
  return useQuery({
    queryKey: ['reviews', params],
    queryFn: () => reviewsApi.getReviews(params),
    select: (data) => data.data,
  })
}

export const useFeaturedReviews = () => {
  return useQuery({
    queryKey: ['reviews', 'featured'],
    queryFn: () => reviewsApi.getFeaturedReviews(),
    select: (data) => data.data,
  })
}
