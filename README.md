# ARS Agenmatica RRSS

Sistema multi-agente inteligente para gestión automatizada de redes sociales para artistas.

## Stack

| Layer | Tech |
|-------|------|
| Backend | FastAPI + Python 3.11 |
| Frontend | React + Tailwind CSS + Vite |
| Agents | CrewAI (orchestrator, replaceable) |
| LLM | Claude API / OpenAI |
| API Docs | OpenAPI/Swagger (auto-generated) |

## Agentes

| Agente | Responsabilidad |
|--------|----------------|
| **ContentCreatorAgent** | Generación de contenido adaptado por plataforma |
| **SchedulerAgent** | Planificación optimizada de publicaciones |
| **AnalyticsAgent** | Análisis de métricas y rendimiento |
| **EngagementAgent** | Gestión de interacciones y menciones |
| **StrategyAgent** | Estrategia de contenido basada en datos |

## Setup

```bash
# Backend
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload    # http://localhost:8000
# API docs: http://localhost:8000/docs

# Frontend
cd frontend
npm install
npm run dev                       # http://localhost:5173
```

## Arquitectura: Business Logic Aislada

La lógica de negocio vive en `backend/app/agents/services/` y es **independiente del orquestador**. CrewAI es el orquestador inicial (en `agents/crews/`), pero puede reemplazarse por LangGraph u otro sin tocar el core del negocio.

## Desarrollo con OpenSpec

```bash
/opsx:propose "descripción del cambio"   # Crear propuesta
/opsx:apply                               # Implementar
/opsx:archive                             # Archivar
```

Specs del sistema en `openspec/specs/`.

## Licencia

MIT
