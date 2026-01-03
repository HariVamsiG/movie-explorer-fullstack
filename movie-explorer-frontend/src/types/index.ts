export interface Movie {
  id: number
  title: string
  release_year: number
  rating: number | null
  poster_url: string | null
  backdrop_url: string | null
  director_name: string
  genres: string[]
  average_rating: number | null
  review_count: number
  duration?: number
  plot?: string
}

export interface MovieDetail extends Movie {
  director: Director
  actors: Actor[]
  reviews: Review[]
}

export interface Actor {
  id: number
  name: string
  birth_date: string | null
  nationality: string
  biography: string
  image_url: string | null
  movies_count: number
  movies: Movie[]
  created_at: string
  updated_at: string
}

export interface Director {
  id: number
  name: string
  birth_date: string | null
  nationality: string
  biography: string
  image_url: string | null
  movies_count: number
  movies: Movie[]
  created_at: string
  updated_at: string
}

export interface Genre {
  id: number
  name: string
  description: string | null
  movies_count: number
  created_at: string
  updated_at: string
}

export interface Review {
  id: number
  reviewer_name: string
  rating: number
  comment: string
  is_featured: boolean
  created_at: string
  updated_at: string
}

export interface PaginatedResponse<T> {
  count: number
  next: string | null
  previous: string | null
  results: T[]
}

export interface MovieFilters {
  title?: string
  release_year?: number
  release_year_gte?: number
  release_year_lte?: number
  director?: string
  actor?: string
  genre?: string
  rating_gte?: number
  rating_lte?: number
  page_size?: number
  ordering?: string
}

export interface FavoriteMovie {
  id: number
  title: string
  poster_url: string | null
  release_year: number
  director_name: string
}
