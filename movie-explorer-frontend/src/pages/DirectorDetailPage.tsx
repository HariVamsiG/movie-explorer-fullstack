import React from 'react'
import { useParams, Link } from 'react-router-dom'
import { ArrowLeft, Film } from 'lucide-react'
import { Button } from '../components/ui/Button'
import { LoadingPage } from '../components/ui/Loading'
import { MovieGrid } from '../components/features/MovieGrid'
import { useDirector } from '../hooks/useQueries'
import { formatDate } from '../utils'

export function DirectorDetailPage() {
  const { id } = useParams<{ id: string }>()
  const directorId = parseInt(id || '0')
  const { data: director, isLoading, error } = useDirector(directorId)

  if (isLoading) return <LoadingPage />

  if (error || !director) {
    return (
      <div className="text-center py-12">
        <div className="text-red-500 dark:text-red-400 text-6xl mb-4">⚠️</div>
        <h3 className="text-lg font-medium text-gray-900 dark:text-gray-100 mb-2">Director not found</h3>
        <Link to="/directors">
          <Button>Back to Directors</Button>
        </Link>
      </div>
    )
  }

  return (
    <div>
      {/* Back Button */}
      <Link to="/directors" className="inline-flex items-center text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 mb-6">
        <ArrowLeft className="h-4 w-4 mr-2" />
        Back to Directors
      </Link>

      <div className="mb-8">
        <div className="flex flex-col md:flex-row bg-white dark:bg-gray-900 rounded-lg overflow-hidden shadow-sm">
          {/* Director Image */}
          <div className="md:w-56 h-56 md:h-64 relative flex-shrink-0">
            <div 
              className="absolute inset-0 bg-cover bg-center"
              style={{
                backgroundImage: director.image_url 
                  ? `url(${director.image_url})`
                  : 'linear-gradient(135deg, #a855f7 0%, #ec4899 100%)'
              }}
            />
          </div>

          {/* Director Details */}
          <div className="flex-1 p-6 space-y-4">
            <div>
              <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100">
                {director.name}
              </h1>
              <p className="text-purple-600 dark:text-purple-400 text-sm font-medium">
                Director
              </p>
            </div>

            <div className="space-y-3">
              <div>
                <p className="text-xs text-gray-500 dark:text-gray-400 uppercase tracking-wide">Films</p>
                <p className="text-lg font-bold text-gray-900 dark:text-gray-100">{director.movies.length}</p>
              </div>
              
              {director.birth_date && (
                <div>
                  <p className="text-xs text-gray-500 dark:text-gray-400 uppercase tracking-wide">Age</p>
                  <p className="text-lg font-bold text-gray-900 dark:text-gray-100">
                    {new Date().getFullYear() - new Date(director.birth_date).getFullYear()}
                  </p>
                </div>
              )}
              
              {director.nationality && (
                <div>
                  <p className="text-xs text-gray-500 dark:text-gray-400 uppercase tracking-wide">Nationality</p>
                  <p className="text-sm font-semibold text-gray-900 dark:text-gray-100">{director.nationality}</p>
                </div>
              )}
              
              {director.birth_date && (
                <div>
                  <p className="text-xs text-gray-500 dark:text-gray-400 uppercase tracking-wide">Born</p>
                  <p className="text-sm font-semibold text-gray-900 dark:text-gray-100">
                    {formatDate(director.birth_date)}
                  </p>
                </div>
              )}
            </div>

            {director.biography && (
              <div>
                <p className="text-xs text-gray-500 dark:text-gray-400 uppercase tracking-wide mb-2">Biography</p>
                <p className="text-gray-700 dark:text-gray-300 text-sm leading-relaxed">
                  {director.biography}
                </p>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Movies Section - Full Width */}
      <div className="mt-12">
        <div className="flex items-center justify-between mb-8">
          <div>
            <h2 className="text-3xl font-bold text-gray-900 dark:text-gray-100">Movies Directed</h2>
            <p className="text-gray-600 dark:text-gray-400 mt-1">
              {director.movies.length} {director.movies.length === 1 ? 'movie' : 'movies'} directed by {director.name}
            </p>
          </div>
        </div>
        {director.movies.length > 0 ? (
          <MovieGrid movies={director.movies} />
        ) : (
          <div className="text-center py-16 bg-gray-50 dark:bg-gray-800/50 rounded-xl">
            <Film className="h-20 w-20 text-gray-400 dark:text-gray-500 mx-auto mb-6" />
            <h3 className="text-lg font-medium text-gray-900 dark:text-gray-100 mb-2">No movies found</h3>
            <p className="text-gray-600 dark:text-gray-400">This director hasn't directed any movies yet.</p>
          </div>
        )}
      </div>
    </div>
  )
}
