import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { ThemeProvider } from './contexts/ThemeContext'
import { FavoritesProvider } from './hooks/useFavorites'
import { Layout } from './components/layout/Layout'
import { HomePage } from './pages/HomePage'
import { MoviesPage } from './pages/MoviesPage'
import { MovieDetailPage } from './pages/MovieDetailPage'
import { ActorsPage } from './pages/ActorsPage'
import { ActorDetailPage } from './pages/ActorDetailPage'
import { DirectorsPage } from './pages/DirectorsPage'
import { DirectorDetailPage } from './pages/DirectorDetailPage'
import { FavoritesPage } from './pages/FavoritesPage'

// Create a client
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 5 * 60 * 1000, // 5 minutes
      retry: 1,
    },
  },
})

function App() {
  return (
    <ThemeProvider>
      <QueryClientProvider client={queryClient}>
        <FavoritesProvider>
          <Router>
            <Layout>
              <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/movies" element={<MoviesPage />} />
                <Route path="/movies/:id" element={<MovieDetailPage />} />
                <Route path="/actors" element={<ActorsPage />} />
                <Route path="/actors/:id" element={<ActorDetailPage />} />
                <Route path="/directors" element={<DirectorsPage />} />
                <Route path="/directors/:id" element={<DirectorDetailPage />} />
                <Route path="/favorites" element={<FavoritesPage />} />
                <Route path="*" element={
                <div className="text-center py-12">
                  <div className="text-gray-400 dark:text-gray-500 text-6xl mb-4">🎬</div>
                  <h3 className="text-lg font-medium text-gray-900 dark:text-gray-100 mb-2">Page not found</h3>
                  <p className="text-gray-600 dark:text-gray-400">The page you're looking for doesn't exist.</p>
                </div>
              } />
            </Routes>
          </Layout>
        </Router>
        </FavoritesProvider>
      </QueryClientProvider>
    </ThemeProvider>
  )
}

export default App
