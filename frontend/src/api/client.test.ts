import { http, HttpResponse } from 'msw'
import { describe, expect, it } from 'vitest'
import { apiFetch } from './client'
import { server } from '../mocks/server'

describe('apiFetch', () => {
  it('returns parsed JSON on success', async () => {
    const result = await apiFetch<{ status: string }>('/health')
    expect(result).toHaveProperty('status', 'ok')
  })

  it('throws on HTTP error response', async () => {
    server.use(
      http.get('/api/v1/test-error', () =>
        HttpResponse.json({ error: { message: 'Not found' } }, { status: 404 })
      )
    )
    await expect(apiFetch('/test-error')).rejects.toThrow('Not found')
  })

  it('throws on network error', async () => {
    server.use(
      http.get('/api/v1/test-network', () => HttpResponse.error())
    )
    await expect(apiFetch('/test-network')).rejects.toThrow()
  })
})
