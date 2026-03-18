import { logger } from "./shared/logger.js";
import { Orchestrator } from "./core/orchestrator.js";

const orchestrator = new Orchestrator();

logger.info(
  {
    agents: orchestrator.listRegisteredAgents(),
  },
  "ARS Agenmatica RRSS initialized"
);

export { orchestrator };
