import { describe, it, expect } from 'vitest'
import { render, screen, fireEvent } from '@testing-library/react'
import { Input } from '../components/ui/Input'

describe('Input', () => {
  it('renders with placeholder', () => {
    render(<Input placeholder="Enter text" />)
    expect(screen.getByPlaceholderText('Enter text')).toBeInTheDocument()
  })

  it('handles value changes', () => {
    render(<Input value="test" onChange={() => {}} />)
    const input = screen.getByRole('textbox')
    expect(input).toHaveValue('test')
  })

  it('applies default classes', () => {
    render(<Input />)
    const input = screen.getByRole('textbox')
    expect(input).toHaveClass('w-full', 'px-3', 'py-2', 'border')
  })

  it('applies custom className', () => {
    render(<Input className="custom-class" />)
    const input = screen.getByRole('textbox')
    expect(input).toHaveClass('custom-class')
  })

  it('handles disabled state', () => {
    render(<Input disabled />)
    const input = screen.getByRole('textbox')
    expect(input).toBeDisabled()
  })

  it('forwards ref correctly', () => {
    let inputRef: HTMLInputElement | null = null
    render(<Input ref={(ref) => { inputRef = ref }} />)
    expect(inputRef).toBeInstanceOf(HTMLInputElement)
  })

  it('handles focus and blur events', () => {
    render(<Input />)
    const input = screen.getByRole('textbox')
    
    input.focus()
    expect(input).toHaveFocus()
    
    input.blur()
    expect(input).not.toHaveFocus()
  })
})
