# Agents Domain

## Overview

El sistema usa 5 agentes especializados orquestados por CrewAI. Cada agente es un wrapper delgado sobre un servicio de negocio framework-agnostic.

## Agent Definitions

### ContentCreatorAgent
- **Goal**: Generar contenido creativo adaptado a cada plataforma y al estilo del artista
- **Service**: `ContentService`
- **Inputs**: Tema, plataforma, tono, brand voice del artista, restricciones
- **Outputs**: Texto, hashtags, sugerencias de media, CTAs
- **Tools**: LLM (Claude/OpenAI), template engine

### SchedulerAgent
- **Goal**: Planificar publicaciones en horarios óptimos
- **Service**: `ScheduleService`
- **Inputs**: Contenido aprobado, datos de audiencia, timezone del artista
- **Outputs**: Calendario de publicación optimizado
- **Tools**: Analytics data, timezone management

### AnalyticsAgent
- **Goal**: Recopilar métricas y generar insights accionables
- **Service**: `AnalyticsService`
- **Inputs**: Período, plataformas, KPIs objetivo
- **Outputs**: Reports con trends, mejores/peores posts, recomendaciones
- **Tools**: Platform APIs, data aggregation

### EngagementAgent
- **Goal**: Gestionar interacciones con la audiencia del artista
- **Service**: `EngagementService`
- **Inputs**: Comentarios, menciones, DMs
- **Outputs**: Respuestas sugeridas, alertas, sentiment analysis
- **Tools**: Sentiment analyzer, notification system

### StrategyAgent
- **Goal**: Definir y ajustar la estrategia de contenido
- **Service**: `StrategyService`
- **Inputs**: Analytics reports, objetivos del artista, tendencias del mercado
- **Outputs**: Content plan, posting strategy, A/B test proposals
- **Tools**: AnalyticsService data, trend analysis

## CrewAI Orchestration

```python
# Crew definition (replaceable layer)
social_media_crew = Crew(
    agents=[content_agent, scheduler_agent, analytics_agent, ...],
    tasks=[...],
    process=Process.sequential  # or hierarchical
)
```

## Isolation Pattern

```
CrewAI Agent (thin wrapper)
    │
    ├── Uses: CrewAI @agent decorator, tools
    ├── Calls: BusinessService methods
    └── Returns: CrewAI-compatible output

BusinessService (framework-agnostic)
    │
    ├── Pure Python classes
    ├── No CrewAI imports
    ├── Testable independently
    └── Reusable with any orchestrator
```
