import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import { Search, User } from 'lucide-react'
import { Card, CardContent } from '../components/ui/Card'
import { Input } from '../components/ui/Input'
import { LoadingCard } from '../components/ui/Loading'
import { Pagination } from '../components/ui/Pagination'
import { PageSizeSelector } from '../components/ui/PageSizeSelector'
import { useDirectors } from '../hooks/useQueries'
import { useDebounce } from '../hooks/useDebounce'

export function DirectorsPage() {
  const [searchTerm, setSearchTerm] = useState('')
  const [currentPage, setCurrentPage] = useState(1)
  const [pageSize, setPageSize] = useState(20)
  
  const debouncedSearch = useDebounce(searchTerm, 700)

  const { data, isLoading, error } = useDirectors({ 
    page: currentPage, 
    name: debouncedSearch || undefined,
    page_size: pageSize
  })

  const handlePageChange = (page: number) => {
    setCurrentPage(page)
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }

  const handleSearch = (value: string) => {
    setSearchTerm(value)
    setCurrentPage(1)
  }

  const handlePageSizeChange = (size: number) => {
    setPageSize(size)
    setCurrentPage(1)
    // Force query refetch
    setSearchTerm(prev => prev)
  }

  if (error) {
    return (
      <div className="text-center py-12">
        <div className="text-red-500 dark:text-red-400 text-6xl mb-4">⚠️</div>
        <h3 className="text-lg font-medium text-gray-900 dark:text-gray-100 mb-2">Error loading directors</h3>
        <p className="text-gray-600 dark:text-gray-400">Please try again later.</p>
      </div>
    )
  }

  const totalPages = data ? Math.ceil(data.count / pageSize) : 0

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-2">Directors</h1>
        <p className="text-gray-600 dark:text-gray-400">
          Explore the visionary directors behind great movies
        </p>
      </div>

      {/* Search and Page Size */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 mb-6">
        <div className="relative max-w-2xl flex-1">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 dark:text-gray-500 h-4 w-4" />
          <Input
            placeholder="Search directors..."
            value={searchTerm}
            onChange={(e) => handleSearch(e.target.value)}
            className="pl-10"
          />
        </div>
        <PageSizeSelector 
          pageSize={pageSize}
          onPageSizeChange={handlePageSizeChange}
        />
      </div>

      {/* Directors Grid */}
      {isLoading ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {Array.from({ length: 8 }).map((_, index) => (
            <LoadingCard key={index} />
          ))}
        </div>
      ) : data?.results.length === 0 ? (
        // Only show "no results" message if search is applied
        
          <div className="text-center py-12">
            <User className="h-16 w-16 text-gray-400 dark:text-gray-500 mx-auto mb-4" />
            <h3 className="text-lg font-medium text-gray-900 dark:text-gray-100 mb-2">No directors found</h3>
            { debouncedSearch && ( <p className="text-gray-600 dark:text-gray-400">Try adjusting your search criteria.</p> )}
          </div>
      ) : (
        <>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {data?.results.map((director) => (
              <Link key={director.id} to={`/directors/${director.id}`}>
                <Card hover className="h-80 overflow-hidden group relative">
                  <div 
                    className="absolute inset-0 bg-cover bg-center transition-transform duration-300 group-hover:scale-105"
                    style={{
                      backgroundImage: director.image_url 
                        ? `linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.8) 100%), url(${director.image_url})`
                        : 'linear-gradient(135deg, #a855f7 0%, #ec4899 100%)'
                    }}
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent" />
                  
                  <CardContent className="relative h-full p-6 flex flex-col justify-end text-white">
                    <div className="space-y-2">
                      <h3 className="text-xl font-bold leading-tight">{director.name}</h3>
                      
                      {director.nationality && (
                        <p className="text-sm text-gray-200 flex items-center gap-1">
                          <span className="w-1 h-1 bg-purple-400 rounded-full"></span>
                          {director.nationality}
                        </p>
                      )}
                      
                      <div className="flex items-center justify-between pt-2">
                        <span className="text-xs text-gray-300 bg-black/30 px-2 py-1 rounded-full backdrop-blur-sm">
                          {director.movies_count} movie{director.movies_count !== 1 ? 's' : ''}
                        </span>
                        <div className="w-8 h-8 bg-white/20 rounded-full flex items-center justify-center backdrop-blur-sm">
                          <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                            <path fillRule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clipRule="evenodd" />
                          </svg>
                        </div>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </Link>
            ))}
          </div>

          {data && (
            <Pagination
              currentPage={currentPage}
              totalPages={totalPages}
              totalCount={data.count}
              pageSize={pageSize}
              onPageChange={handlePageChange}
              hasNext={!!data.next}
              hasPrevious={!!data.previous}
            />
          )}
        </>
      )}
    </div>
  )
}
