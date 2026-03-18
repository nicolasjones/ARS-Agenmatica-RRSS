# AGENTS.md - Instructions for AI Coding Agents

## Project Context

This is **ARS Agenmatica RRSS**, an AI agent-based social media management system built with TypeScript and Node.js.

## Before Writing Code

1. Read the relevant specs in `openspec/specs/` to understand the current system state
2. Check `openspec/changes/` for any active change proposals
3. Follow the OpenSpec workflow: propose → design → implement → archive

## Code Guidelines

- Use TypeScript strict mode. No `any` types unless absolutely necessary
- All async operations must handle errors explicitly
- Use the project's `AppError` hierarchy for error handling
- Log with Pino logger, never `console.log`
- All platform API calls go through PlatformAdapter interface
- Agent implementations must be stateless between executions
- Use Drizzle ORM for all database operations

## Architecture Rules

- Agents do NOT call platform APIs directly — they use PlatformAdapter
- The Orchestrator is the only entity that creates and assigns tasks to agents
- Inter-agent communication goes through the event/queue system, not direct calls
- All agent decisions must be logged for auditability

## File Naming

- Source files: `kebab-case.ts`
- Test files: `kebab-case.test.ts`
- Types/interfaces: dedicated `types.ts` per module
- Constants: `constants.ts` per module

## Testing Requirements

- Unit tests for all agent logic
- Integration tests for platform adapters (with mocked APIs)
- Test files colocated with source files
