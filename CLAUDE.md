# CLAUDE.md - ARS Agenmatica RRSS

## Project Overview

ARS Agenmatica RRSS es un sistema multi-agente inteligente para gestión automatizada de redes sociales **orientado a artistas**. Usa CrewAI como orquestador con lógica de negocio aislada (framework-agnostic) para facilitar migración futura.

## Tech Stack

- **Backend**: Python 3.11+ / FastAPI / Pydantic / OpenAPI/Swagger
- **Frontend**: React 19 / TypeScript / Tailwind CSS 4 / Vite
- **Agents**: CrewAI (orquestador reemplazable)
- **AI/LLM**: Anthropic Claude API, OpenAI
- **DB**: PostgreSQL + SQLAlchemy (futuro)
- **Logging**: structlog
- **Testing**: pytest (backend), Vitest (frontend)

## Development Methodology

Este proyecto usa **OpenSpec** (Spec-Driven Development). Antes de implementar cualquier feature:
1. Revisar specs existentes en `openspec/specs/`
2. Proponer cambios con `/opsx:propose <name>`
3. Implementar con `/opsx:apply`
4. Archivar con `/opsx:archive`

## Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── api/v1/              # API routes (health, content, etc.)
│   ├── core/                # Config, logging, errors
│   ├── agents/
│   │   ├── crews/           # CrewAI orchestration (REPLACEABLE)
│   │   ├── services/        # Business logic (FRAMEWORK-AGNOSTIC)
│   │   └── tools/           # Agent tools
│   ├── platforms/           # Social media adapters
│   ├── models/              # DB models
│   └── schemas/             # Pydantic schemas
├── tests/                   # pytest tests
└── pyproject.toml

frontend/
├── src/
│   ├── components/          # Reusable UI components
│   ├── pages/               # Route pages
│   ├── api/                 # API client
│   └── types/               # TypeScript types
├── package.json
└── vite.config.ts

openspec/
├── specs/                   # Source of truth
└── changes/                 # Active change proposals
```

## Commands

```bash
# Backend
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload          # Dev server (port 8000)
pytest                                  # Run tests
ruff check app/                        # Lint

# Frontend
cd frontend
npm run dev                            # Dev server (port 5173)
npm run build                          # Build
npx tsc --noEmit                       # Type check
```

## Conventions

- Código y comentarios técnicos en inglés
- Documentación y specs pueden ser en español
- Backend: Python (PEP 8, ruff), snake_case
- Frontend: TypeScript, PascalCase componentes, camelCase funciones
- Agentes CrewAI son wrappers delgados sobre servicios de negocio
- Servicios de negocio NO importan CrewAI (framework-agnostic)
- Logging con structlog (backend), nunca print()
- Errores extienden AppError

## Architecture Rule: Isolated Business Logic

```
agents/crews/       ← CrewAI-specific (REPLACEABLE)
agents/services/    ← Framework-agnostic (CORE - never import crewai here)
```

Si se migra a LangGraph u otro orquestador, solo se reescribe `crews/`.
