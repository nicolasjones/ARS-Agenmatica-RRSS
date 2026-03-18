import type {
  AccountMetrics,
  DateRange,
  PlatformCredentials,
  PlatformType,
  Post,
  PostMetrics,
  PublishResult,
} from "../core/types.js";

export interface Comment {
  id: string;
  postId: string;
  authorId: string;
  authorName: string;
  text: string;
  createdAt: Date;
}

export interface Mention {
  id: string;
  authorId: string;
  authorName: string;
  text: string;
  postUrl?: string;
  createdAt: Date;
}

export interface ScheduleResult {
  scheduledId: string;
  scheduledFor: Date;
  platform: PlatformType;
}

export interface AuthToken {
  accessToken: string;
  refreshToken?: string;
  expiresAt: Date;
  platform: PlatformType;
}

export interface PlatformAdapter {
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
