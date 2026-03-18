import { render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { describe, expect, it } from 'vitest'
import Sidebar from './Sidebar'

function renderSidebar(initialPath = '/') {
  return render(
    <MemoryRouter initialEntries={[initialPath]}>
      <Sidebar />
    </MemoryRouter>
  )
}

describe('Sidebar', () => {
  it('renders without crashing', () => {
    renderSidebar()
    expect(screen.getByText('ARS Agenmatica')).toBeInTheDocument()
  })

  it('shows app subtitle', () => {
    renderSidebar()
    expect(screen.getByText('RRSS para Artistas')).toBeInTheDocument()
  })

  it('renders all navigation links', () => {
    renderSidebar()
    expect(screen.getByRole('link', { name: /Dashboard/i })).toBeInTheDocument()
    expect(screen.getByRole('link', { name: /Content/i })).toBeInTheDocument()
    expect(screen.getByRole('link', { name: /Calendar/i })).toBeInTheDocument()
    expect(screen.getByRole('link', { name: /Analytics/i })).toBeInTheDocument()
    expect(screen.getByRole('link', { name: /Engagement/i })).toBeInTheDocument()
    expect(screen.getByRole('link', { name: /Settings/i })).toBeInTheDocument()
  })

  it('marks Dashboard link as active on root path', () => {
    renderSidebar('/')
    const dashboardLink = screen.getByRole('link', { name: /Dashboard/i })
    expect(dashboardLink.className).toContain('bg-indigo-600')
  })

  it('marks Content link as active on /content path', () => {
    renderSidebar('/content')
    const contentLink = screen.getByRole('link', { name: /Content/i })
    expect(contentLink.className).toContain('bg-indigo-600')
  })
})
