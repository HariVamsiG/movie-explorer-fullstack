import React from 'react'

interface SortSelectorProps {
  sortBy: string
  onSortChange: (sort: string) => void
}

const sortOptions = [
  { value: '', label: 'Default' },
  { value: 'title', label: 'Title (A-Z)' },
  { value: '-title', label: 'Title (Z-A)' },
  { value: 'release_year', label: 'Year (Oldest)' },
  { value: '-release_year', label: 'Year (Newest)' },
  { value: 'rating', label: 'Rating (Low-High)' },
  { value: '-rating', label: 'Rating (High-Low)' },
]

export function SortSelector({ sortBy, onSortChange }: SortSelectorProps) {
  return (
    <div className="flex items-center space-x-2">
      <span className="text-sm text-gray-600 dark:text-gray-400">Sort by:</span>
      <select
        value={sortBy}
        onChange={(e) => onSortChange(e.target.value)}
        className="px-3 py-1 text-sm border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500"
      >
        {sortOptions.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
    </div>
  )
}
