import type { AppConfig } from "./types.js";

function requireEnv(key: string): string {
  const value = process.env[key];
  if (!value) {
    throw new Error(`Missing required environment variable: ${key}`);
  }
  return value;
}

function optionalEnv(key: string): string | undefined {
  return process.env[key];
}

export function loadConfig(): AppConfig {
  return {
    port: parseInt(process.env["PORT"] ?? "3000", 10),
    nodeEnv: (process.env["NODE_ENV"] as AppConfig["nodeEnv"]) ?? "development",
    database: {
      url: requireEnv("DATABASE_URL"),
    },
    redis: {
      url: process.env["REDIS_URL"] ?? "redis://localhost:6379",
    },
    platforms: {
      twitter: optionalEnv("TWITTER_API_KEY")
        ? {
            clientId: requireEnv("TWITTER_API_KEY"),
            clientSecret: requireEnv("TWITTER_API_SECRET"),
            accessToken: optionalEnv("TWITTER_ACCESS_TOKEN"),
          }
        : undefined,
      instagram: optionalEnv("META_APP_ID")
        ? {
            clientId: requireEnv("META_APP_ID"),
            clientSecret: requireEnv("META_APP_SECRET"),
            accessToken: optionalEnv("INSTAGRAM_ACCESS_TOKEN"),
          }
        : undefined,
      linkedin: optionalEnv("LINKEDIN_CLIENT_ID")
        ? {
            clientId: requireEnv("LINKEDIN_CLIENT_ID"),
            clientSecret: requireEnv("LINKEDIN_CLIENT_SECRET"),
            accessToken: optionalEnv("LINKEDIN_ACCESS_TOKEN"),
          }
        : undefined,
      tiktok: optionalEnv("TIKTOK_CLIENT_KEY")
        ? {
            clientId: requireEnv("TIKTOK_CLIENT_KEY"),
            clientSecret: requireEnv("TIKTOK_CLIENT_SECRET"),
          }
        : undefined,
    },
    ai: {
      anthropicApiKey: optionalEnv("ANTHROPIC_API_KEY"),
      openaiApiKey: optionalEnv("OPENAI_API_KEY"),
    },
    logLevel: process.env["LOG_LEVEL"] ?? "info",
  };
}
