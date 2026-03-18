# ARS Agenmatica RRSS — System Overview

## Purpose

Sistema multi-agente inteligente para gestión automatizada de redes sociales **orientado a artistas**. Combina agentes de IA especializados para crear, planificar, publicar y analizar contenido en múltiples plataformas sociales.

## Architecture Principles

1. **Framework-Agnostic Business Logic**: La lógica de negocio (estrategia, calendario, reglas, métricas) vive en servicios independientes del orquestador. CrewAI es el orquestador inicial, pero se puede reemplazar sin tocar el core.

2. **Separation of Concerns**:
   - `backend/` — FastAPI + CrewAI agents + business services
   - `frontend/` — React + Tailwind (dashboard de gestión)

3. **API-First**: FastAPI genera OpenAPI/Swagger automáticamente. El frontend consume la API REST.

4. **Observable**: Logging estructurado, trazabilidad de decisiones de agentes.

## High-Level Architecture

```
┌──────────────────────────────────────────────────┐
│                  Frontend (React + Tailwind)       │
│        Dashboard · Calendar · Analytics · Feed     │
└────────────────────────┬─────────────────────────┘
                         │ REST API (OpenAPI)
┌────────────────────────┴─────────────────────────┐
│              FastAPI Backend                       │
├────────────────────────────────────────────────────┤
│  API Layer          │  Agent Layer (CrewAI)        │
│  ┌───────────────┐  │  ┌────────────────────────┐ │
│  │ /content      │  │  │ ContentCreatorAgent    │ │
│  │ /schedule     │  │  │ SchedulerAgent         │ │
│  │ /analytics    │  │  │ AnalyticsAgent         │ │
│  │ /engagement   │  │  │ EngagementAgent        │ │
│  │ /strategy     │  │  │ StrategyAgent          │ │
│  └───────────────┘  │  └──────────┬─────────────┘ │
│                     │             │                │
│  ┌──────────────────┴─────────────┴──────────────┐│
│  │         Business Services (Core)              ││
│  │  ContentService · ScheduleService             ││
│  │  AnalyticsService · PlatformService           ││
│  │  StrategyService · PublishingRules            ││
│  └───────────────────────────────────────────────┘│
│  ┌───────────────────────────────────────────────┐│
│  │         Platform Adapters                     ││
│  │  Twitter/X · Instagram · TikTok · LinkedIn    ││
│  └───────────────────────────────────────────────┘│
│  ┌───────────────────────────────────────────────┐│
│  │         Data Layer (SQLAlchemy / PostgreSQL)   ││
│  └───────────────────────────────────────────────┘│
└──────────────────────────────────────────────────┘
```

## Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Frontend   | React 19, Tailwind CSS 4, Vite    |
| API        | FastAPI, Pydantic, OpenAPI/Swagger|
| Agents     | CrewAI (replaceable orchestrator) |
| LLM        | Anthropic Claude API, OpenAI      |
| Database   | PostgreSQL + SQLAlchemy           |
| Queue      | Celery + Redis (async tasks)      |
| Logging    | structlog                         |
| Testing    | pytest (backend), Vitest (frontend)|

## Design: Isolated Business Logic

```
agents/crews/       ← CrewAI-specific (REPLACEABLE)
  └── social_crew.py

agents/services/    ← Framework-agnostic (CORE)
  ├── content_service.py
  ├── schedule_service.py
  ├── analytics_service.py
  └── strategy_service.py
```

Los **agents** en CrewAI son wrappers delgados que llaman a los **services**. Si se migra a LangGraph, solo se reescriben los wrappers.
