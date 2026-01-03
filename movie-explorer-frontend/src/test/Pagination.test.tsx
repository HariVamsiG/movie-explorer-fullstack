import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent } from '@testing-library/react'
import { Pagination } from '../components/ui/Pagination'

describe('Pagination', () => {
  const defaultProps = {
    currentPage: 1,
    totalPages: 5,
    onPageChange: vi.fn(),
    hasNext: true,
    hasPrevious: false
  }

  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('renders pagination buttons', () => {
    render(<Pagination {...defaultProps} />)
    expect(screen.getByText('Previous')).toBeInTheDocument()
    expect(screen.getByText('Next')).toBeInTheDocument()
  })

  it('disables previous button when hasPrevious is false', () => {
    render(<Pagination {...defaultProps} hasPrevious={false} />)
    const prevButton = screen.getByText('Previous')
    expect(prevButton).toBeDisabled()
  })

  it('disables next button when hasNext is false', () => {
    render(<Pagination {...defaultProps} currentPage={5} hasNext={false} />)
    const nextButton = screen.getByText('Next')
    expect(nextButton).toBeDisabled()
  })

  it('calls onPageChange when previous button is clicked', () => {
    const onPageChange = vi.fn()
    render(<Pagination {...defaultProps} currentPage={2} hasPrevious={true} onPageChange={onPageChange} />)
    
    fireEvent.click(screen.getByText('Previous'))
    expect(onPageChange).toHaveBeenCalledWith(1)
  })

  it('calls onPageChange when next button is clicked', () => {
    const onPageChange = vi.fn()
    render(<Pagination {...defaultProps} currentPage={2} onPageChange={onPageChange} />)
    
    fireEvent.click(screen.getByText('Next'))
    expect(onPageChange).toHaveBeenCalledWith(3)
  })

  it('renders page numbers correctly', () => {
    render(<Pagination {...defaultProps} currentPage={3} totalPages={5} />)
    
    expect(screen.getByText('1')).toBeInTheDocument()
    expect(screen.getByText('2')).toBeInTheDocument()
    expect(screen.getByText('3')).toBeInTheDocument()
    expect(screen.getByText('4')).toBeInTheDocument()
    expect(screen.getByText('5')).toBeInTheDocument()
  })

  it('highlights current page', () => {
    render(<Pagination {...defaultProps} currentPage={3} />)
    const currentPageButton = screen.getByText('3')
    expect(currentPageButton).toHaveClass('bg-blue-600')
  })

  it('calls onPageChange when page number is clicked', () => {
    const onPageChange = vi.fn()
    render(<Pagination {...defaultProps} onPageChange={onPageChange} />)
    
    fireEvent.click(screen.getByText('3'))
    expect(onPageChange).toHaveBeenCalledWith(3)
  })

  it('does not render when totalPages is 1 or less', () => {
    const { container } = render(<Pagination {...defaultProps} totalPages={1} />)
    expect(container.firstChild).toBeNull()
  })
})
