# ARS Agenmatica RRSS

Sistema agéntico inteligente para gestión automatizada de redes sociales.

## Descripción

ARS Agenmatica RRSS utiliza agentes de IA especializados que trabajan de forma coordinada para analizar, crear, publicar y optimizar contenido en múltiples plataformas sociales (Twitter/X, Instagram, LinkedIn, TikTok).

## Agentes

| Agente | Responsabilidad |
|--------|----------------|
| **ContentAgent** | Generación de contenido adaptado por plataforma |
| **SchedulerAgent** | Planificación optimizada de publicaciones |
| **AnalyticsAgent** | Análisis de métricas y rendimiento |
| **EngagementAgent** | Gestión de interacciones y menciones |
| **StrategyAgent** | Estrategia de contenido basada en datos |

## Setup

```bash
# Requisitos: Node.js 20+
npm install
cp .env.example .env  # Configurar variables de entorno
npm run dev
```

## Desarrollo

Este proyecto usa [OpenSpec](https://github.com/Fission-AI/OpenSpec) para desarrollo guiado por especificaciones:

```bash
# Proponer un cambio
/opsx:propose "descripción del cambio"

# Implementar
/opsx:apply

# Archivar cambio completado
/opsx:archive
```

Las specs del sistema están en `openspec/specs/`.

## Scripts

```bash
npm run dev        # Servidor de desarrollo
npm run build      # Compilar TypeScript
npm run test       # Ejecutar tests
npm run typecheck  # Verificar tipos
npm run lint       # Linter
```

## Licencia

MIT
