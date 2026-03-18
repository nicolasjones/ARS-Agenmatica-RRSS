import { createChildLogger } from "../shared/logger.js";
import { AgentError } from "../core/errors.js";
import type {
  Agent,
  AgentCapability,
  AgentResult,
  AgentRole,
  AgentTask,
} from "../core/types.js";

export abstract class BaseAgent implements Agent {
  public readonly id: string;
  protected readonly log;

  constructor(
    public readonly name: string,
    public readonly role: AgentRole
  ) {
    this.id = `${role}-${Date.now()}`;
    this.log = createChildLogger(name, { agentId: this.id, role });
  }

  async execute(task: AgentTask): Promise<AgentResult> {
    const startTime = Date.now();
    this.log.info({ taskId: task.id, type: task.type }, "Agent executing task");

    try {
      const data = await this.run(task);
      const durationMs = Date.now() - startTime;

      this.log.info(
        { taskId: task.id, durationMs },
        "Agent completed task successfully"
      );

      return {
        taskId: task.id,
        agentId: this.id,
        status: "success",
        data,
        executedAt: new Date(),
        durationMs,
      };
    } catch (error) {
      const durationMs = Date.now() - startTime;
      const message =
        error instanceof Error ? error.message : "Unknown error";

      this.log.error(
        { taskId: task.id, error: message, durationMs },
        "Agent task failed"
      );

      throw new AgentError(
        `Agent ${this.name} failed: ${message}`,
        this.id,
        { taskId: task.id, originalError: message }
      );
    }
  }

  abstract getCapabilities(): AgentCapability[];

  protected abstract run(
    task: AgentTask
  ): Promise<Record<string, unknown> | undefined>;
}
