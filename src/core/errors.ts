export class AppError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly statusCode: number = 500,
    public readonly details?: Record<string, unknown>
  ) {
    super(message);
    this.name = "AppError";
  }
}

export class PlatformError extends AppError {
  constructor(
    message: string,
    public readonly platform: string,
    details?: Record<string, unknown>
  ) {
    super(message, "PLATFORM_ERROR", 502, details);
    this.name = "PlatformError";
  }
}

export class AgentError extends AppError {
  constructor(
    message: string,
    public readonly agentId: string,
    details?: Record<string, unknown>
  ) {
    super(message, "AGENT_ERROR", 500, details);
    this.name = "AgentError";
  }
}

export class ValidationError extends AppError {
  constructor(message: string, details?: Record<string, unknown>) {
    super(message, "VALIDATION_ERROR", 400, details);
    this.name = "ValidationError";
  }
}

export class AuthenticationError extends AppError {
  constructor(
    message: string,
    platform?: string,
    details?: Record<string, unknown>
  ) {
    super(message, "AUTH_ERROR", 401, { platform, ...details });
    this.name = "AuthenticationError";
  }
}

export class RateLimitError extends AppError {
  constructor(
    public readonly platform: string,
    public readonly retryAfter?: number,
    details?: Record<string, unknown>
  ) {
    super(
      `Rate limit exceeded for ${platform}`,
      "RATE_LIMIT_ERROR",
      429,
      details
    );
    this.name = "RateLimitError";
  }
}
