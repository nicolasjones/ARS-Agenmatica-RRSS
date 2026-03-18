# CLAUDE.md - ARS Agenmatica RRSS

## Project Overview

ARS Agenmatica RRSS es un sistema agéntico inteligente para gestión automatizada de redes sociales. Usa agentes de IA especializados (ContentAgent, SchedulerAgent, AnalyticsAgent, EngagementAgent, StrategyAgent) coordinados por un Orchestrator.

## Tech Stack

- **Runtime**: Node.js 20+ / TypeScript (ESM)
- **AI**: Anthropic Claude API (`@anthropic-ai/sdk`)
- **HTTP**: Hono
- **DB**: PostgreSQL + Drizzle ORM
- **Queue**: BullMQ + Redis
- **Logging**: Pino
- **Testing**: Vitest

## Development Methodology

Este proyecto usa **OpenSpec** (Spec-Driven Development). Antes de implementar cualquier feature:
1. Revisar specs existentes en `openspec/specs/`
2. Proponer cambios con `/opsx:propose <name>`
3. Implementar con `/opsx:apply`
4. Archivar con `/opsx:archive`

## Project Structure

```
src/
├── agents/          # Agentes de IA (ContentAgent, SchedulerAgent, etc.)
├── core/            # Orchestrator, tipos base, config
├── platforms/       # Adapters para cada red social
├── data/            # DB schemas, repositories, queue jobs
├── api/             # HTTP routes (Hono)
└── shared/          # Utilidades compartidas, logger, errors
openspec/
├── specs/           # Source of truth - estado actual del sistema
├── changes/         # Propuestas de cambio activas
│   └── archive/     # Cambios completados
```

## Commands

```bash
npm run dev          # Dev server con hot reload
npm run build        # Compilar TypeScript
npm run test         # Tests con Vitest
npm run typecheck    # Verificar tipos sin compilar
npm run lint         # ESLint
```

## Conventions

- Código y comentarios técnicos en inglés
- Documentación y specs pueden ser en español
- Archivos TypeScript con extensión `.ts`
- Imports con path alias `@/` → `src/`
- Nombres de agentes en PascalCase con sufijo `Agent`
- Platform adapters implementan `PlatformAdapter` interface
- Todos los agentes implementan `Agent` interface base
- Errors extendiendo `AppError` base class
- Logging estructurado con Pino (no console.log)

## Testing

- Tests unitarios junto al código: `*.test.ts`
- Tests de integración en `src/__tests__/`
- Mocks de APIs externas siempre
- `npm run test` ejecuta todo con Vitest
