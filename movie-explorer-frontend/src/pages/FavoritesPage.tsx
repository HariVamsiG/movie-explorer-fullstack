import React from 'react'
import { Link } from 'react-router-dom'
import { Trash2, Calendar } from 'lucide-react'
import { Card, CardContent } from '../components/ui/Card'
import { Button } from '../components/ui/Button'
import { useFavorites } from '../hooks/useFavorites'
import { formatYear } from '../utils'

export function FavoritesPage() {
  const { favorites, removeFromFavorites } = useFavorites()

  if (favorites.length === 0) {
    return (
      <div className="text-center py-12">
        <div className="text-gray-400 dark:text-gray-500 text-6xl mb-4">💝</div>
        <h3 className="text-lg font-medium text-gray-900 dark:text-gray-100 mb-2">No favorites yet</h3>
        <p className="text-gray-600 dark:text-gray-400 mb-6">
          Start adding movies to your favorites to see them here.
        </p>
        <Link to="/movies">
          <Button>Browse Movies</Button>
        </Link>
      </div>
    )
  }

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-2">My Favorites</h1>
        <p className="text-gray-600 dark:text-gray-400">
          You have {favorites.length} favorite movie{favorites.length !== 1 ? 's' : ''}
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        {favorites.map((movie) => (
          <div key={movie.id} className="relative">
            <Link to={`/movies/${movie.id}`}>
              <Card hover className="group overflow-hidden h-[420px] flex flex-col relative">
                <div 
                  className="absolute inset-0 bg-cover bg-center bg-top transition-transform duration-300 group-hover:scale-105"
                  style={{
                    backgroundImage: movie.poster_url 
                      ? `linear-gradient(to bottom, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.9) 100%), url(${movie.poster_url})`
                      : 'linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%)'
                  }}
                />
                <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent" />
                
                {/* Remove Button */}
                <Button
                  variant="ghost"
                  size="sm"
                  className="absolute top-3 right-3 p-2 rounded-full bg-black/30 dark:bg-white/5 text-red-500 dark:text-red-400 hover:text-red-600 dark:hover:text-red-300 backdrop-blur-sm z-50"
                  onClick={(e) => {
                    e.preventDefault()
                    e.stopPropagation()
                    removeFromFavorites(movie.id)
                  }}
                >
                  <Trash2 className="h-4 w-4" />
                </Button>

                {/* Content */}
                <CardContent className="relative h-full p-4 flex flex-col justify-end text-white z-10">
                  <div className="space-y-3">
                    <h3 className="text-lg font-bold leading-tight line-clamp-2">
                      {movie.title}
                    </h3>
                    
                    <div className="space-y-2 text-sm text-gray-200">
                      <div className="flex items-center gap-2">
                        <Calendar className="h-3 w-3" />
                        <span>{formatYear(movie.release_year)}</span>
                      </div>
                      
                      <div className="flex items-center gap-2">
                        <span className="text-xs">Director:</span>
                        <span className="text-xs font-medium line-clamp-1">{movie.director_name}</span>
                      </div>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </Link>
          </div>
        ))}
      </div>
    </div>
  )
}
