import { describe, it, expect } from 'vitest'
import { cn, formatYear, formatDuration, formatRating, truncateText, formatDate } from '../utils/index'

describe('Utility Functions', () => {
  describe('cn', () => {
    it('merges class names correctly', () => {
      expect(cn('class1', 'class2')).toBe('class1 class2')
    })

    it('handles conditional classes', () => {
      expect(cn('base', true && 'conditional', false && 'hidden')).toBe('base conditional')
    })

    it('handles tailwind merge conflicts', () => {
      expect(cn('px-2', 'px-4')).toBe('px-4')
    })
  })

  describe('formatYear', () => {
    it('formats year correctly', () => {
      expect(formatYear(2023)).toBe('2023')
    })

    it('handles edge cases', () => {
      expect(formatYear(0)).toBe('0')
      expect(formatYear(9999)).toBe('9999')
    })
  })

  describe('formatDuration', () => {
    it('formats minutes only', () => {
      expect(formatDuration(45)).toBe('45m')
    })

    it('formats hours and minutes', () => {
      expect(formatDuration(125)).toBe('2h 5m')
    })

    it('formats exact hours', () => {
      expect(formatDuration(120)).toBe('2h 0m')
    })

    it('handles zero duration', () => {
      expect(formatDuration(0)).toBe('0m')
    })
  })

  describe('formatRating', () => {
    it('formats rating to one decimal place', () => {
      expect(formatRating(8.5)).toBe('8.5')
    })

    it('rounds to one decimal place', () => {
      expect(formatRating(8.567)).toBe('8.6')
    })

    it('handles whole numbers', () => {
      expect(formatRating(8)).toBe('8.0')
    })
  })

  describe('truncateText', () => {
    it('returns original text if shorter than max length', () => {
      expect(truncateText('short', 10)).toBe('short')
    })

    it('truncates text if longer than max length', () => {
      expect(truncateText('this is a long text', 10)).toBe('this is a ...')
    })

    it('handles exact length', () => {
      expect(truncateText('exact', 5)).toBe('exact')
    })

    it('handles empty string', () => {
      expect(truncateText('', 10)).toBe('')
    })
  })

  describe('formatDate', () => {
    it('formats date string correctly', () => {
      const result = formatDate('2023-01-15')
      expect(result).toBe('January 15, 2023')
    })

    it('handles ISO date string', () => {
      const result = formatDate('2023-01-15T10:30:00Z')
      expect(result).toBe('January 15, 2023')
    })

    it('handles different date formats', () => {
      const result = formatDate('01/15/2023')
      expect(result).toBe('January 15, 2023')
    })
  })
})
