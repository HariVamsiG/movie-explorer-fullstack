import React from 'react'
import { MovieCard } from './MovieCard'
import { LoadingCard } from '../ui/Loading'
import type { Movie } from '../../types'

interface MovieGridProps {
  movies: Movie[]
  loading?: boolean
  className?: string
  showSearchMessage?: boolean
}

export function MovieGrid({ movies, loading = false, className, showSearchMessage = true }: MovieGridProps) {
  if (loading) {
    return (
      <div className={`grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 ${className}`}>
        {Array.from({ length: 8 }).map((_, index) => (
          <LoadingCard key={index} />
        ))}
      </div>
    )
  }

  if (movies.length === 0) {
    return (
      <div className="text-center py-12">
        <div className="text-gray-400 dark:text-gray-500 text-6xl mb-4">🎬</div>
        <h3 className="text-lg font-medium text-gray-900 dark:text-gray-100 mb-2">No movies found</h3>
        {showSearchMessage && (
          <p className="text-gray-600 dark:text-gray-400">Try adjusting your search criteria or filters.</p>
        )}
      </div>
    )
  }

  return (
    <div className={`grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 ${className}`}>
      {movies.map((movie) => (
        <MovieCard key={movie.id} movie={movie} />
      ))}
    </div>
  )
}
