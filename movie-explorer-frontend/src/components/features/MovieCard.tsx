import React from 'react'
import { Link } from 'react-router-dom'
import { Heart, Star, Calendar, Clock } from 'lucide-react'
import { Card, CardContent } from '../ui/Card'
import { Button } from '../ui/Button'
import { useFavorites } from '../../hooks/useFavorites'
import { formatYear, formatDuration, formatRating, truncateText, cn } from '../../utils'
import type { Movie } from '../../types'

interface MovieCardProps {
  movie: Movie
  className?: string
}

export function MovieCard({ movie, className }: MovieCardProps) {
  const { isFavorite, toggleFavorite } = useFavorites()
  const favorite = isFavorite(movie.id)

  const handleToggleFavorite = (e: React.MouseEvent) => {
    e.preventDefault()
    e.stopPropagation()
    toggleFavorite({
      id: movie.id,
      title: movie.title,
      poster_url: movie.poster_url,
      release_year: movie.release_year,
      director_name: movie.director_name,
    })
  }

  return (
    <Card hover className={cn('group overflow-hidden h-[420px] flex flex-col relative', className)}>
      <Link to={`/movies/${movie.id}`} className="absolute inset-0 z-0">
        <div 
          className="absolute inset-0 bg-cover bg-center bg-top transition-transform duration-300 group-hover:scale-105"
          style={{
            backgroundImage: movie.poster_url 
              ? `linear-gradient(to bottom, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.9) 100%), url(${movie.poster_url})`
              : 'linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%)'
          }}
        />
        <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent" />
      </Link>
      
      {/* Rating Badge */}
      {movie.average_rating && (
        <div className="absolute top-3 left-3 bg-black/70 text-white px-2 py-1 rounded-full text-xs flex items-center gap-1 backdrop-blur-sm z-10">
          <Star className="h-3 w-3 fill-current text-yellow-400" />
          {formatRating(movie.average_rating)}
        </div>
      )}

      {/* Favorite Button */}
      <Button
        variant="ghost"
        size="sm"
        className={cn(
          'absolute top-3 right-3 p-2 rounded-full bg-black/30 dark:bg-white/5 backdrop-blur-sm z-20',
          favorite 
            ? 'text-red-500 dark:text-red-400' 
            : 'text-white dark:text-gray-200 hover:text-red-500 dark:hover:text-red-400'
        )}
        onClick={handleToggleFavorite}
      >
        <Heart className={cn('h-4 w-4', favorite && 'fill-current')} />
      </Button>

      {/* Content */}
      <CardContent className="relative h-full p-4 flex flex-col justify-end text-white z-10 pointer-events-none">
        <div className="space-y-3">
          <h3 className="text-lg font-bold leading-tight line-clamp-2">
            {movie.title}
          </h3>
          
          <div className="space-y-2 text-sm text-gray-200">
            <div className="flex items-center gap-2">
              <Calendar className="h-3 w-3" />
              <span>{formatYear(movie.release_year)}</span>
              {movie.duration && (
                <>
                  <span>•</span>
                  <Clock className="h-3 w-3" />
                  <span>{formatDuration(movie.duration)}</span>
                </>
              )}
            </div>
            
            <div className="flex items-center gap-2">
              <span className="text-xs">Director:</span>
              <span className="text-xs font-medium line-clamp-1">{movie.director_name}</span>
            </div>
          </div>

          {/* Genres */}
          {movie.genres.length > 0 && (
            <div className="flex flex-wrap gap-1">
              {movie.genres.slice(0, 2).map((genre) => (
                <span
                  key={genre}
                  className="px-2 py-1 bg-white/20 text-white text-xs rounded-full backdrop-blur-sm"
                >
                  {genre}
                </span>
              ))}
              {movie.genres.length > 2 && (
                <span className="px-2 py-1 bg-white/20 text-white text-xs rounded-full backdrop-blur-sm">
                  +{movie.genres.length - 2}
                </span>
              )}
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  )
}
