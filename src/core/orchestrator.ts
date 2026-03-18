import { createChildLogger } from "../shared/logger.js";
import type { Agent, AgentResult, AgentRole, AgentTask } from "./types.js";

export class Orchestrator {
  private agents = new Map<AgentRole, Agent>();
  private readonly log = createChildLogger("Orchestrator");

  registerAgent(agent: Agent): void {
    this.agents.set(agent.role, agent);
    this.log.info(
      { agentName: agent.name, role: agent.role },
      "Agent registered"
    );
  }

  getAgent(role: AgentRole): Agent | undefined {
    return this.agents.get(role);
  }

  async dispatch(task: AgentTask): Promise<AgentResult> {
    const agent = this.agents.get(task.agentRole);
    if (!agent) {
      throw new Error(`No agent registered for role: ${task.agentRole}`);
    }

    this.log.info(
      { taskId: task.id, agentRole: task.agentRole, type: task.type },
      "Dispatching task to agent"
    );

    return agent.execute(task);
  }

  async dispatchAll(tasks: AgentTask[]): Promise<AgentResult[]> {
    this.log.info({ count: tasks.length }, "Dispatching batch of tasks");
    return Promise.all(tasks.map((task) => this.dispatch(task)));
  }

  listRegisteredAgents(): Array<{ name: string; role: AgentRole }> {
    return Array.from(this.agents.values()).map((a) => ({
      name: a.name,
      role: a.role,
    }));
  }
}
