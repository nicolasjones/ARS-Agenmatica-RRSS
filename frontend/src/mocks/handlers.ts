import { http, HttpResponse } from 'msw'

export const handlers = [
  http.get('/api/v1/health', () => {
    return HttpResponse.json({
      status: 'ok',
      version: '0.1.0',
      timestamp: new Date().toISOString(),
    })
  }),

  http.post('/api/v1/content/', async ({ request }) => {
    const body = await request.json() as Record<string, string>
    return HttpResponse.json({
      data: {
        id: 'mock-content-id',
        content: `Generated content about ${body['topic']} for ${body['platform']}`,
        platform: body['platform'],
        hashtags: [],
        media_suggestions: [],
        status: 'draft',
        created_at: new Date().toISOString(),
        updated_at: null,
      },
    })
  }),

  http.get('/api/v1/content/', () => {
    return HttpResponse.json({ data: [] })
  }),
]
