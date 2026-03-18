# ARS Agenmatica RRSS - System Overview

## Purpose

ARS Agenmatica RRSS es un sistema agéntico inteligente para la gestión automatizada de redes sociales. Utiliza agentes de IA especializados que trabajan de forma coordinada para analizar, crear, publicar y optimizar contenido en múltiples plataformas sociales.

## Core Concepts

### Agentes
El sistema se basa en una arquitectura multi-agente donde cada agente tiene una responsabilidad específica:

- **ContentAgent**: Genera contenido adaptado a cada plataforma (texto, hashtags, CTAs)
- **SchedulerAgent**: Planifica publicaciones optimizando horarios según audiencia
- **AnalyticsAgent**: Recopila y analiza métricas de rendimiento
- **EngagementAgent**: Monitorea y gestiona interacciones (comentarios, menciones, DMs)
- **StrategyAgent**: Define y ajusta la estrategia de contenido basándose en datos

### Plataformas Soportadas
- Twitter/X
- Instagram
- LinkedIn
- TikTok

### Arquitectura de Alto Nivel

```
┌─────────────────────────────────────────┐
│            Orchestrator                  │
│    (Coordinador de Agentes)             │
├─────────┬──────────┬──────────┬─────────┤
│ Content │Scheduler │Analytics │Engage-  │
│ Agent   │ Agent    │ Agent    │ment     │
│         │          │          │ Agent   │
├─────────┴──────────┴──────────┴─────────┤
│         Platform Adapters               │
│  ┌───────┬──────────┬────────┬────────┐ │
│  │Twitter│Instagram │LinkedIn│ TikTok │ │
│  └───────┴──────────┴────────┴────────┘ │
├─────────────────────────────────────────┤
│         Data Layer                      │
│   (Queue, Storage, Cache, DB)           │
└─────────────────────────────────────────┘
```

## Technical Stack

- **Runtime**: Node.js 20+ con TypeScript
- **AI/LLM**: Anthropic Claude API (principal), OpenAI (secundario)
- **Base de datos**: PostgreSQL con Drizzle ORM
- **Cola de tareas**: BullMQ con Redis
- **API**: Hono (HTTP framework ligero)
- **Testing**: Vitest
- **Observabilidad**: Structured logging con Pino

## Design Principles

1. **Agent-First**: Toda operación es ejecutada por un agente con contexto y objetivo claro
2. **Platform-Agnostic**: Los agentes trabajan con abstracciones; los adapters manejan las APIs específicas
3. **Event-Driven**: Comunicación entre agentes basada en eventos y colas
4. **Observable**: Todo agente registra sus decisiones y acciones para auditoría
5. **Spec-Driven**: Desarrollo guiado por especificaciones OpenSpec
