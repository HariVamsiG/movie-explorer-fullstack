import axios from 'axios'
import type { 
  Movie, 
  MovieDetail, 
  Actor, 
  Director, 
  Genre, 
  Review, 
  PaginatedResponse, 
  MovieFilters 
} from '../types'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Movies API
export const moviesApi = {
  getMovies: (params?: MovieFilters & { page?: number; page_size?: number }) =>
    api.get<PaginatedResponse<Movie>>('/movies/', { params }),
  
  getMovie: (id: number) =>
    api.get<MovieDetail>(`/movies/${id}/`),
  
  getMoviesByGenre: (genreName: string, page?: number, pageSize?: number) =>
    api.get<PaginatedResponse<Movie>>('/movies/by_genre/', { 
      params: { name: genreName, page, page_size: pageSize } 
    }),
  
  getMoviesByDirector: (directorName: string, page?: number, pageSize?: number) =>
    api.get<PaginatedResponse<Movie>>('/movies/by_director/', { 
      params: { name: directorName, page, page_size: pageSize } 
    }),
  
  getTopRatedMovies: () =>
    api.get<Movie[]>('/movies/top_rated/'),
}

// Actors API
export const actorsApi = {
  getActors: (params?: { page?: number; name?: string; page_size?: number }) =>
    api.get<PaginatedResponse<Actor>>('/actors/', { params }),
  
  getActor: (id: number) =>
    api.get<Actor>(`/actors/${id}/`),
}

// Directors API
export const directorsApi = {
  getDirectors: (params?: { page?: number; name?: string; page_size?: number }) =>
    api.get<PaginatedResponse<Director>>('/directors/', { params }),
  
  getDirector: (id: number) =>
    api.get<Director>(`/directors/${id}/`),
}

// Genres API
export const genresApi = {
  getGenres: () =>
    api.get<PaginatedResponse<Genre>>('/genres/'),
  
  getGenre: (id: number) =>
    api.get<Genre>(`/genres/${id}/`),
}

// Reviews API
export const reviewsApi = {
  getReviews: (params?: { movie_id?: number; page?: number }) =>
    api.get<PaginatedResponse<Review>>('/reviews/', { params }),
  
  getFeaturedReviews: () =>
    api.get<PaginatedResponse<Review>>('/reviews/featured/'),
}
