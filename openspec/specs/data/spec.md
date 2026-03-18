# Data Domain

## Overview

La capa de datos gestiona toda la persistencia, caché y colas del sistema.

## Database (PostgreSQL)

### Core Entities

- **Post**: Contenido creado para publicación
- **Publication**: Instancia de un post publicado en una plataforma específica
- **Account**: Cuenta de red social conectada
- **Campaign**: Agrupación de posts con un objetivo común
- **Metric**: Datos de rendimiento de publicaciones
- **AgentLog**: Registro de ejecuciones de agentes

### Key Relations

```
Account 1──N Publication
Post 1──N Publication
Campaign 1──N Post
Publication 1──N Metric
AgentLog N──1 AgentTask
```

## Queue System (BullMQ + Redis)

### Queues

- `publish`: Posts programados para publicación
- `analytics`: Tareas de recolección de métricas
- `engagement`: Notificaciones y respuestas pendientes
- `agent-tasks`: Tareas genéricas para agentes

### Job Processing

- Jobs son idempotentes
- Retry con backoff exponencial (3 intentos)
- Dead letter queue para jobs fallidos
- Prioridad configurable por tipo de tarea

## Cache (Redis)

- Token de autenticación de plataformas
- Rate limit counters por plataforma
- Métricas frecuentes (TTL: 5 min)
- Resultados de análisis recientes (TTL: 1 hora)

## File Storage

- Media files (imágenes, videos) para publicaciones
- Reportes generados en PDF/CSV
- Configuración por local filesystem o S3-compatible
