import React from 'react'
import { Link } from 'react-router-dom'
import { ArrowRight, Star, TrendingUp, Users, Film } from 'lucide-react'
import { Card, CardContent, CardHeader } from '../components/ui/Card'
import { Button } from '../components/ui/Button'
import { MovieGrid } from '../components/features/MovieGrid'
import { LoadingCard } from '../components/ui/Loading'
import { useTopRatedMovies, useGenres, useFeaturedReviews } from '../hooks/useQueries'

export function HomePage() {
  const { data: topMovies, isLoading: moviesLoading } = useTopRatedMovies()
  const { data: genresData, isLoading: genresLoading } = useGenres()
  const { data: featuredReviews, isLoading: reviewsLoading } = useFeaturedReviews()

  return (
    <div className="space-y-12">
      {/* Hero Section */}
      <section className="text-center py-12 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-2xl">
        <div className="max-w-4xl mx-auto px-6">
          <h1 className="text-5xl font-bold mb-6">
            Discover Amazing Movies
          </h1>
          <p className="text-xl mb-8 opacity-90">
            Explore our vast collection of movies, discover new favorites, and dive deep into the world of cinema.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link to="/movies">
              <Button size="lg" className="bg-white text-blue-600 hover:bg-gray-100 dark:bg-gray-100 dark:text-blue-600 dark:hover:bg-gray-200">
                <Film className="h-5 w-5 mr-2" />
                Browse Movies
              </Button>
            </Link>
            <Link to="/favorites">
              <Button size="lg" variant="ghost" className="text-white border border-white hover:bg-white/10">
                View Favorites
                <ArrowRight className="h-5 w-5 ml-2" />
              </Button>
            </Link>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card>
          <CardContent className="p-6 text-center">
            <Film className="h-12 w-12 text-blue-600 dark:text-blue-400 mx-auto mb-4" />
            <h3 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-2">Movies</h3>
            <p className="text-gray-600 dark:text-gray-400">Discover thousands of movies</p>
          </CardContent>
        </Card>
        
        <Card>
          <CardContent className="p-6 text-center">
            <Users className="h-12 w-12 text-green-600 dark:text-green-400 mx-auto mb-4" />
            <h3 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-2">Artists</h3>
            <p className="text-gray-600 dark:text-gray-400">Explore actors and directors</p>
          </CardContent>
        </Card>
        
        <Card>
          <CardContent className="p-6 text-center">
            <Star className="h-12 w-12 text-yellow-500 dark:text-yellow-400 mx-auto mb-4" />
            <h3 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-2">Reviews</h3>
            <p className="text-gray-600 dark:text-gray-400">Read authentic movie reviews</p>
          </CardContent>
        </Card>
      </section>

      {/* Top Rated Movies */}
      <section>
        <div className="flex items-center justify-between mb-6">
          <div>
            <h2 className="text-3xl font-bold text-gray-900 dark:text-gray-100 flex items-center gap-2">
              <TrendingUp className="h-8 w-8 text-blue-600 dark:text-blue-400" />
              Top Rated Movies
            </h2>
            <p className="text-gray-600 dark:text-gray-400 mt-2">The highest rated movies in our collection</p>
          </div>
          <Link to="/movies?sort=rating">
            <Button variant="outline">
              View All
              <ArrowRight className="h-4 w-4 ml-2" />
            </Button>
          </Link>
        </div>

        {moviesLoading ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {Array.from({ length: 4 }).map((_, index) => (
              <LoadingCard key={index} />
            ))}
          </div>
        ) : (
          <MovieGrid movies={topMovies?.slice(0, 4) || []} showSearchMessage={false} />
        )}
      </section>

      {/* Genres */}
      {
        genresData && genresData?.results.length > 0 && <section>
          <div className="mb-6">
            <h2 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-2">Browse by Genre</h2>
            <p className="text-gray-600 dark:text-gray-400">Find movies by your favorite genres</p>
          </div>

          {genresLoading ? (
            <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
              {Array.from({ length: 6 }).map((_, index) => (
                <div key={index} className="animate-pulse">
                  <div className="h-20 bg-gray-200 dark:bg-gray-700 rounded-lg"></div>
                </div>
              ))}
            </div>
          ) : (
            <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
              {genresData?.results.slice(0, 6).map((genre) => (
                <Link
                  key={genre.id}
                  to={`/movies?genre=${encodeURIComponent(genre.name)}`}
                  className="group"
                >
                  <Card hover className="h-20 flex items-center justify-center text-center p-4 transition-colors group-hover:bg-blue-50 dark:group-hover:bg-blue-900/20">
                    <div>
                      <h3 className="font-medium text-gray-900 dark:text-gray-100 group-hover:text-blue-600 dark:group-hover:text-blue-400">
                        {genre.name}
                      </h3>
                      <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
                        {genre.movies_count} movies
                      </p>
                    </div>
                  </Card>
                </Link>
              ))}
            </div>
          )}
        </section>
      }

      {/* Featured Reviews */}
      {featuredReviews && featuredReviews.results.length > 0 && (
        <section>
          <div className="mb-6">
            <h2 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-2">Featured Reviews</h2>
            <p className="text-gray-600 dark:text-gray-400">What our community is saying</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {featuredReviews.results.slice(0, 3).map((review) => (
              <Card key={review.id}>
                <CardHeader>
                  <div className="flex items-center justify-between">
                    <h3 className="font-medium text-gray-900 dark:text-gray-100">{review.reviewer_name}</h3>
                    <div className="flex items-center gap-1">
                      <Star className="h-4 w-4 fill-current text-yellow-400" />
                      <span className="text-sm font-medium text-gray-900 dark:text-gray-100">{review.rating}/10</span>
                    </div>
                  </div>
                </CardHeader>
                <CardContent>
                  <p className="text-gray-700 dark:text-gray-300 line-clamp-3">{review.comment}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </section>
      )}
    </div>
  )
}
