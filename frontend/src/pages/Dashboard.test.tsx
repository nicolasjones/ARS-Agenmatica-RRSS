import { render, screen, waitFor } from '@testing-library/react'
import { http, HttpResponse } from 'msw'
import { MemoryRouter } from 'react-router-dom'
import { describe, expect, it } from 'vitest'
import { server } from '../mocks/server'
import Dashboard from './Dashboard'

function renderDashboard() {
  return render(
    <MemoryRouter>
      <Dashboard />
    </MemoryRouter>
  )
}

describe('Dashboard', () => {
  it('renders the heading', () => {
    renderDashboard()
    expect(screen.getByRole('heading', { name: /Dashboard/i })).toBeInTheDocument()
  })

  it('shows KPI cards', () => {
    renderDashboard()
    expect(screen.getByText('Posts This Week')).toBeInTheDocument()
    expect(screen.getByText('Engagement Rate')).toBeInTheDocument()
    expect(screen.getByText('Scheduled')).toBeInTheDocument()
    expect(screen.getByText('Platforms')).toBeInTheDocument()
  })

  it('shows backend status as ok when health endpoint succeeds', async () => {
    renderDashboard()
    await waitFor(() => {
      expect(screen.getByText('ok')).toBeInTheDocument()
    })
  })

  it('shows fallback when backend is unreachable', async () => {
    server.use(
      http.get('/api/v1/health', () => HttpResponse.error())
    )
    renderDashboard()
    await waitFor(() => {
      expect(screen.getByText('Backend not connected')).toBeInTheDocument()
    })
  })
})
