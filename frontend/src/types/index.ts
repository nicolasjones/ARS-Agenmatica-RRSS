export type PlatformType = 'twitter' | 'instagram' | 'linkedin' | 'tiktok'

export type PostStatus = 'draft' | 'scheduled' | 'published' | 'failed'

export interface ContentItem {
  id: string
  content: string
  platform: PlatformType
  hashtags: string[]
  media_suggestions: string[]
  status: PostStatus
  created_at: string
  updated_at: string | null
}

export interface ApiResponse<T> {
  data: T
  meta?: {
    page: number
    per_page: number
    total: number
  }
}

export interface HealthStatus {
  status: string
  version: string
  timestamp: string
}
