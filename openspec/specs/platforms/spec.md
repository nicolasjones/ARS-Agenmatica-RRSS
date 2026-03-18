# Platforms Domain

## Overview

La capa de plataformas proporciona adaptadores uniformes para interactuar con las APIs de cada red social. Cada adaptador implementa una interfaz común que abstrae las diferencias entre plataformas.

## Platform Adapter Interface

```typescript
interface PlatformAdapter {
  platform: PlatformType;

  // Content
  publish(post: Post): Promise<PublishResult>;
  schedule(post: Post, publishAt: Date): Promise<ScheduleResult>;
  delete(postId: string): Promise<void>;

  // Analytics
  getPostMetrics(postId: string): Promise<PostMetrics>;
  getAccountMetrics(period: DateRange): Promise<AccountMetrics>;

  // Engagement
  getComments(postId: string): Promise<Comment[]>;
  replyToComment(commentId: string, text: string): Promise<Comment>;
  getMentions(since: Date): Promise<Mention[]>;

  // Auth
  authenticate(credentials: PlatformCredentials): Promise<AuthToken>;
  refreshToken(token: AuthToken): Promise<AuthToken>;
}
```

## Supported Platforms

### Twitter/X
- API: Twitter API v2
- Auth: OAuth 2.0
- Capabilities: text posts, threads, media, polls, analytics
- Rate limits: variable by endpoint

### Instagram
- API: Meta Graph API
- Auth: OAuth 2.0 (Meta Business Suite)
- Capabilities: posts, stories, reels, carousels, insights
- Rate limits: 200 calls/hour per user

### LinkedIn
- API: LinkedIn Marketing API
- Auth: OAuth 2.0
- Capabilities: posts, articles, company pages, analytics
- Rate limits: varies by endpoint and plan

### TikTok
- API: TikTok for Developers
- Auth: OAuth 2.0
- Capabilities: video posts, analytics, comment management
- Rate limits: varies by endpoint

## Content Normalization

Cada plataforma tiene restricciones diferentes:

| Platform  | Max Text | Media Types       | Hashtags |
|-----------|----------|-------------------|----------|
| Twitter/X | 280 char | img, video, gif   | inline   |
| Instagram | 2200 char| img, video, carousel| max 30  |
| LinkedIn  | 3000 char| img, video, doc   | max 5    |
| TikTok    | 2200 char| video             | inline   |

El `ContentAgent` usa estas restricciones para adaptar el contenido a cada plataforma.
