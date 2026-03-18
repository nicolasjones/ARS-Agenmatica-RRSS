// === Core Types for ARS Agenmatica RRSS ===

export type AgentRole =
  | "content"
  | "scheduler"
  | "analytics"
  | "engagement"
  | "strategy";

export type PlatformType = "twitter" | "instagram" | "linkedin" | "tiktok";

export type AgentStatus =
  | "idle"
  | "assigned"
  | "executing"
  | "completed"
  | "failed";

export interface AgentTask {
  id: string;
  agentRole: AgentRole;
  type: string;
  payload: Record<string, unknown>;
  priority: number;
  createdAt: Date;
  metadata?: Record<string, unknown>;
}

export interface AgentResult {
  taskId: string;
  agentId: string;
  status: "success" | "error";
  data?: Record<string, unknown>;
  error?: string;
  executedAt: Date;
  durationMs: number;
}

export interface AgentCapability {
  name: string;
  description: string;
  inputSchema?: Record<string, unknown>;
}

export interface Agent {
  id: string;
  name: string;
  role: AgentRole;
  execute(task: AgentTask): Promise<AgentResult>;
  getCapabilities(): AgentCapability[];
}

export interface DateRange {
  from: Date;
  to: Date;
}

export interface Post {
  id: string;
  content: string;
  mediaUrls?: string[];
  hashtags?: string[];
  platform: PlatformType;
  campaignId?: string;
  createdAt: Date;
}

export interface PublishResult {
  postId: string;
  platformPostId: string;
  platform: PlatformType;
  publishedAt: Date;
  url: string;
}

export interface PostMetrics {
  postId: string;
  platform: PlatformType;
  impressions: number;
  reach: number;
  likes: number;
  comments: number;
  shares: number;
  clicks: number;
  engagementRate: number;
  collectedAt: Date;
}

export interface AccountMetrics {
  platform: PlatformType;
  followers: number;
  following: number;
  totalPosts: number;
  engagementRate: number;
  period: DateRange;
}

export interface AppConfig {
  port: number;
  nodeEnv: "development" | "production" | "test";
  database: {
    url: string;
  };
  redis: {
    url: string;
  };
  platforms: {
    twitter?: PlatformCredentials;
    instagram?: PlatformCredentials;
    linkedin?: PlatformCredentials;
    tiktok?: PlatformCredentials;
  };
  ai: {
    anthropicApiKey?: string;
    openaiApiKey?: string;
  };
  logLevel: string;
}

export interface PlatformCredentials {
  clientId: string;
  clientSecret: string;
  accessToken?: string;
  refreshToken?: string;
}
