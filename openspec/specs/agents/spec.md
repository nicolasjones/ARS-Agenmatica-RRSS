# Agents Domain

## Overview

Los agentes son la unidad fundamental de trabajo en ARS Agenmatica. Cada agente es una entidad autónoma con un objetivo, herramientas y contexto definidos.

## Agent Interface

Todos los agentes implementan la interfaz base `Agent`:

```typescript
interface Agent {
  id: string;
  name: string;
  role: AgentRole;
  execute(task: AgentTask): Promise<AgentResult>;
  getCapabilities(): AgentCapability[];
}
```

## Agent Types

### ContentAgent
- **Rol**: Generación de contenido para redes sociales
- **Input**: Tema, plataforma objetivo, tono, restricciones
- **Output**: Contenido formateado para la plataforma (texto, hashtags, media suggestions)
- **Tools**: LLM (Claude API), image generation API, template engine

### SchedulerAgent
- **Rol**: Planificación temporal de publicaciones
- **Input**: Contenido listo, plataforma, datos de audiencia
- **Output**: Calendario de publicación optimizado
- **Tools**: Analytics data, timezone management, queue system

### AnalyticsAgent
- **Rol**: Recopilación y análisis de métricas
- **Input**: Período de tiempo, plataformas, métricas objetivo
- **Output**: Reports con insights y recomendaciones
- **Tools**: Platform APIs (read), data aggregation, trend analysis

### EngagementAgent
- **Rol**: Gestión de interacciones en redes sociales
- **Input**: Notificaciones, menciones, comentarios
- **Output**: Respuestas sugeridas, alertas de crisis, sentiment analysis
- **Tools**: Platform APIs, sentiment analyzer, notification system

### StrategyAgent
- **Rol**: Definición y ajuste de estrategia de contenido
- **Input**: Analytics reports, objectives, brand guidelines
- **Output**: Content plan, posting strategy, A/B test proposals
- **Tools**: AnalyticsAgent data, market trends, competitor analysis

## Orchestrator

El Orchestrator coordina la ejecución de agentes:

1. Recibe tareas de alto nivel (ej: "crear campaña para lanzamiento de producto")
2. Descompone en sub-tareas asignadas a agentes específicos
3. Gestiona dependencias entre agentes
4. Consolida resultados y reporta estado

## Agent Lifecycle

```
IDLE → ASSIGNED → EXECUTING → COMPLETED/FAILED → IDLE
```

- Los agentes son stateless entre ejecuciones
- El contexto se pasa explícitamente en cada tarea
- Los resultados se persisten en la capa de datos
