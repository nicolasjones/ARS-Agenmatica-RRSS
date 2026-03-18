# API Domain

## Overview

FastAPI backend que expone una API REST documentada con OpenAPI/Swagger. Sirve tanto al frontend React como a integraciones externas.

## Endpoints

### Content (`/api/v1/content`)
- `POST /` — Solicitar generación de contenido al ContentCreatorAgent
- `GET /` — Listar contenido generado (con filtros)
- `GET /{id}` — Detalle de un contenido
- `PUT /{id}` — Editar contenido antes de publicar
- `DELETE /{id}` — Eliminar contenido

### Schedule (`/api/v1/schedule`)
- `POST /` — Programar publicación
- `GET /` — Calendario de publicaciones
- `PUT /{id}` — Reprogramar
- `DELETE /{id}` — Cancelar publicación programada

### Analytics (`/api/v1/analytics`)
- `GET /dashboard` — Métricas generales del dashboard
- `GET /posts/{id}/metrics` — Métricas de un post
- `GET /platforms/{platform}` — Métricas por plataforma
- `POST /report` — Generar report con AnalyticsAgent

### Engagement (`/api/v1/engagement`)
- `GET /mentions` — Menciones recientes
- `GET /comments` — Comentarios pendientes
- `POST /reply` — Responder (con sugerencia del agent)

### Strategy (`/api/v1/strategy`)
- `GET /current` — Estrategia actual
- `POST /generate` — Generar nueva estrategia con StrategyAgent
- `PUT /` — Actualizar estrategia

### Platforms (`/api/v1/platforms`)
- `GET /` — Plataformas conectadas
- `POST /connect` — Conectar nueva plataforma (OAuth)
- `DELETE /{platform}` — Desconectar plataforma

### Health
- `GET /health` — Health check
- `GET /docs` — Swagger UI (auto-generated)
- `GET /redoc` — ReDoc (auto-generated)

## Auth

- JWT tokens para autenticación de usuarios
- API keys para integraciones externas
- OAuth 2.0 para conexión con plataformas sociales

## Response Format

```json
{
  "data": { ... },
  "meta": {
    "page": 1,
    "per_page": 20,
    "total": 100
  }
}
```

Errores:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "...",
    "details": { ... }
  }
}
```
