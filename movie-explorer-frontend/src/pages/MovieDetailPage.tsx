import React from 'react'
import { useParams, Link } from 'react-router-dom'
import { ArrowLeft, Calendar, Clock, Star, Heart, Users, User } from 'lucide-react'
import { Card, CardContent, CardHeader } from '../components/ui/Card'
import { Button } from '../components/ui/Button'
import { LoadingPage } from '../components/ui/Loading'
import { useFavorites } from '../hooks/useFavorites'
import { useMovie } from '../hooks/useQueries'
import { formatYear, formatDuration, formatRating, cn } from '../utils'

export function MovieDetailPage() {
  const { id } = useParams<{ id: string }>()
  const movieId = parseInt(id || '0')
  const { data: movie, isLoading, error } = useMovie(movieId)
  const { isFavorite, toggleFavorite } = useFavorites()

  if (isLoading) return <LoadingPage />

  if (error || !movie) {
    return (
      <div className="text-center py-12">
        <div className="text-red-500 dark:text-red-400 text-6xl mb-4">⚠️</div>
        <h3 className="text-lg font-medium text-gray-900 dark:text-gray-100 mb-2">Movie not found</h3>
        <Link to="/movies">
          <Button>Back to Movies</Button>
        </Link>
      </div>
    )
  }

  const favorite = isFavorite(movie.id)

  const handleToggleFavorite = () => {
    toggleFavorite({
      id: movie.id,
      title: movie.title,
      poster_url: movie.poster_url,
      release_year: movie.release_year,
      director_name: movie.director.name,
    })
  }

  return (
    <div>
      {/* Back Button */}
      <Link to="/movies" className="inline-flex items-center text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 mb-6">
        <ArrowLeft className="h-4 w-4 mr-2" />
        Back to Movies
      </Link>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Movie Poster */}
        <div className="lg:col-span-1">
          <Card>
            <CardContent className="p-0">
              {movie.poster_url ? (
                <img
                  src={movie.poster_url}
                  alt={movie.title}
                  className="w-full h-auto rounded-lg"
                />
              ) : (
                <div className="aspect-[2/3] bg-gray-200 dark:bg-gray-700 rounded-lg flex items-center justify-center">
                  <span className="text-gray-400 dark:text-gray-500">No Image Available</span>
                </div>
              )}
            </CardContent>
          </Card>
        </div>

        {/* Movie Details */}
        <div className="lg:col-span-2 space-y-6">
          {/* Title and Actions */}
          <div>
            <div className="flex items-start justify-between mb-4">
              <h1 className="text-4xl font-bold text-gray-900 dark:text-gray-100">{movie.title}</h1>
              <Button
                variant={favorite ? 'primary' : 'outline'}
                onClick={handleToggleFavorite}
                className="ml-4"
              >
                <Heart className={cn('h-4 w-4 mr-2', favorite && 'fill-current')} />
                {favorite ? 'Remove from Favorites' : 'Add to Favorites'}
              </Button>
            </div>

            {/* Basic Info */}
            <div className="flex flex-wrap items-center gap-4 text-gray-600 dark:text-gray-400 mb-6">
              <div className="flex items-center gap-2">
                <Calendar className="h-4 w-4" />
                <span>{formatYear(movie.release_year)}</span>
              </div>
              
              {movie.duration && (
                <div className="flex items-center gap-2">
                  <Clock className="h-4 w-4" />
                  <span>{formatDuration(movie.duration)}</span>
                </div>
              )}

              {movie.average_rating && (
                <div className="flex items-center gap-2">
                  <Star className="h-4 w-4 fill-current text-yellow-400" />
                  <span>{formatRating(movie.average_rating)} ({movie.review_count} reviews)</span>
                </div>
              )}
            </div>

            {/* Genres */}
            <div className="flex flex-wrap gap-2 mb-6">
              {movie.genres.map((genre) => (
                <span
                  key={genre.id}
                  className="px-3 py-1 bg-blue-100 dark:bg-blue-900/30 text-blue-800 dark:text-blue-300 text-sm rounded-full"
                >
                  {genre.name}
                </span>
              ))}
            </div>
          </div>

          {/* Plot */}
          {movie.plot && (
            <Card>
              <CardHeader>
                <h2 className="text-xl font-semibold text-gray-900 dark:text-gray-100">Plot</h2>
              </CardHeader>
              <CardContent>
                <p className="text-gray-700 dark:text-gray-300 leading-relaxed">{movie.plot}</p>
              </CardContent>
            </Card>
          )}

          {/* Director */}
          <Card>
            <CardHeader>
              <h2 className="text-xl font-semibold text-gray-900 dark:text-gray-100 flex items-center gap-2">
                <User className="h-5 w-5" />
                Director
              </h2>
            </CardHeader>
            <CardContent>
              <Link 
                to={`/directors/${movie.director.id}`}
                className="block hover:bg-gray-50 dark:hover:bg-gray-700 p-4 rounded-lg transition-colors"
              >
                <h3 className="font-medium text-lg text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300">
                  {movie.director.name}
                </h3>
                {movie.director.nationality && (
                  <p className="text-gray-600 dark:text-gray-400">{movie.director.nationality}</p>
                )}
                {movie.director.biography && (
                  <p className="text-gray-700 dark:text-gray-300 mt-2 line-clamp-3">{movie.director.biography}</p>
                )}
              </Link>
            </CardContent>
          </Card>

          {/* Cast */}
          {movie.actors.length > 0 && (
            <Card>
              <CardHeader>
                <h2 className="text-xl font-semibold text-gray-900 dark:text-gray-100 flex items-center gap-2">
                  <Users className="h-5 w-5" />
                  Cast
                </h2>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  {movie.actors.map((actor) => (
                    <Link
                      key={actor.id}
                      to={`/actors/${actor.id}`}
                      className="block hover:bg-gray-50 dark:hover:bg-gray-700 p-4 rounded-lg transition-colors"
                    >
                      <h3 className="font-medium text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300">
                        {actor.name}
                      </h3>
                      {actor.nationality && (
                        <p className="text-gray-600 dark:text-gray-400 text-sm">{actor.nationality}</p>
                      )}
                    </Link>
                  ))}
                </div>
              </CardContent>
            </Card>
          )}

          {/* Reviews */}
          {movie.reviews.length > 0 && (
            <Card>
              <CardHeader>
                <h2 className="text-xl font-semibold text-gray-900 dark:text-gray-100">Reviews</h2>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  {movie.reviews.slice(0, 3).map((review) => (
                    <div key={review.id} className="border-b border-gray-200 dark:border-gray-700 pb-4 last:border-b-0">
                      <div className="flex items-center justify-between mb-2">
                        <h4 className="font-medium text-gray-900 dark:text-gray-100">{review.reviewer_name}</h4>
                        <div className="flex items-center gap-1">
                          <Star className="h-4 w-4 fill-current text-yellow-400" />
                          <span className="text-sm font-medium text-gray-900 dark:text-gray-100">{review.rating}/10</span>
                        </div>
                      </div>
                      <p className="text-gray-700 dark:text-gray-300">{review.comment}</p>
                    </div>
                  ))}
                  {movie.reviews.length > 3 && (
                    <p className="text-sm text-gray-500 dark:text-gray-400 text-center">
                      And {movie.reviews.length - 3} more reviews...
                    </p>
                  )}
                </div>
              </CardContent>
            </Card>
          )}
        </div>
      </div>
    </div>
  )
}
