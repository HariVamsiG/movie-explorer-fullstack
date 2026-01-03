import React, { createContext, useContext, useState, useEffect } from 'react'
import type { FavoriteMovie } from '../types'

const FAVORITES_KEY = 'movie-explorer-favorites'

interface FavoritesContextType {
  favorites: FavoriteMovie[]
  addToFavorites: (movie: FavoriteMovie) => void
  removeFromFavorites: (movieId: number) => void
  isFavorite: (movieId: number) => boolean
  toggleFavorite: (movie: FavoriteMovie) => void
}

const FavoritesContext = createContext<FavoritesContextType | undefined>(undefined)

export function FavoritesProvider({ children }: { children: React.ReactNode }) {
  const [favorites, setFavorites] = useState<FavoriteMovie[]>([])

  useEffect(() => {
    const stored = localStorage.getItem(FAVORITES_KEY)
    if (stored) {
      try {
        setFavorites(JSON.parse(stored))
      } catch (error) {
        console.error('Error parsing favorites from localStorage:', error)
      }
    }
  }, [])

  const addToFavorites = (movie: FavoriteMovie) => {
    setFavorites(prev => {
      if (prev.some(fav => fav.id === movie.id)) return prev
      const newFavorites = [...prev, movie]
      localStorage.setItem(FAVORITES_KEY, JSON.stringify(newFavorites))
      return newFavorites
    })
  }

  const removeFromFavorites = (movieId: number) => {
    setFavorites(prev => {
      const newFavorites = prev.filter(movie => movie.id !== movieId)
      localStorage.setItem(FAVORITES_KEY, JSON.stringify(newFavorites))
      return newFavorites
    })
  }

  const isFavorite = (movieId: number) => {
    return favorites.some(movie => movie.id === movieId)
  }

  const toggleFavorite = (movie: FavoriteMovie) => {
    if (isFavorite(movie.id)) {
      removeFromFavorites(movie.id)
    } else {
      addToFavorites(movie)
    }
  }

  return (
    <FavoritesContext.Provider value={{
      favorites,
      addToFavorites,
      removeFromFavorites,
      isFavorite,
      toggleFavorite,
    }}>
      {children}
    </FavoritesContext.Provider>
  )
}

export function useFavorites() {
  const context = useContext(FavoritesContext)
  if (context === undefined) {
    throw new Error('useFavorites must be used within a FavoritesProvider')
  }
  return context
}
