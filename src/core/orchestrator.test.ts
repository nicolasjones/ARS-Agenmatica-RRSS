import { describe, it, expect } from "vitest";
import { Orchestrator } from "./orchestrator.js";
import type {
  Agent,
  AgentCapability,
  AgentResult,
  AgentTask,
} from "./types.js";

function createMockAgent(role: "content" | "scheduler"): Agent {
  return {
    id: `mock-${role}`,
    name: `Mock${role}Agent`,
    role,
    async execute(task: AgentTask): Promise<AgentResult> {
      return {
        taskId: task.id,
        agentId: `mock-${role}`,
        status: "success",
        data: { echo: task.payload },
        executedAt: new Date(),
        durationMs: 1,
      };
    },
    getCapabilities(): AgentCapability[] {
      return [{ name: "test", description: "Test capability" }];
    },
  };
}

describe("Orchestrator", () => {
  it("registers and lists agents", () => {
    const orchestrator = new Orchestrator();
    const agent = createMockAgent("content");
    orchestrator.registerAgent(agent);

    const agents = orchestrator.listRegisteredAgents();
    expect(agents).toHaveLength(1);
    expect(agents[0]?.role).toBe("content");
  });

  it("dispatches task to correct agent", async () => {
    const orchestrator = new Orchestrator();
    orchestrator.registerAgent(createMockAgent("content"));

    const task: AgentTask = {
      id: "task-1",
      agentRole: "content",
      type: "generate",
      payload: { topic: "test" },
      priority: 1,
      createdAt: new Date(),
    };

    const result = await orchestrator.dispatch(task);
    expect(result.status).toBe("success");
    expect(result.taskId).toBe("task-1");
  });

  it("throws when no agent registered for role", async () => {
    const orchestrator = new Orchestrator();

    const task: AgentTask = {
      id: "task-2",
      agentRole: "analytics",
      type: "report",
      payload: {},
      priority: 1,
      createdAt: new Date(),
    };

    await expect(orchestrator.dispatch(task)).rejects.toThrow(
      "No agent registered for role: analytics"
    );
  });
});
