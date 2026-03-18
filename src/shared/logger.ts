import { pino } from "pino";

export const logger = pino({
  level: process.env["LOG_LEVEL"] ?? "info",
  transport:
    process.env["NODE_ENV"] !== "production"
      ? { target: "pino-pretty", options: { colorize: true } }
      : undefined,
});

export type Logger = typeof logger;

export function createChildLogger(
  name: string,
  bindings?: Record<string, unknown>
) {
  return logger.child({ module: name, ...bindings });
}
