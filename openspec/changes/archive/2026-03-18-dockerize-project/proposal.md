## Why

El proyecto tiene backend (FastAPI) y frontend (React/Vite) que se instalan y ejecutan manualmente. No hay forma estandarizada de levantar el entorno de desarrollo, generar builds de producción optimizados, ni correr la suite de tests completa en un entorno aislado. Dockerizar todo permite onboarding en un solo comando, paridad dev/prod, y CI reproducible.

## What Changes

- Crear `backend/Dockerfile` con multi-stage build (dev + prod)
- Crear `frontend/Dockerfile` con multi-stage build (dev + prod con Nginx)
- Crear `docker-compose.yml` para desarrollo local con hot-reload (backend + frontend + PostgreSQL)
- Crear `docker-compose.prod.yml` con builds optimizados y Nginx reverse proxy
- Crear `docker-compose.ci.yml` para correr pytest, vitest y playwright en contenedores
- Crear `.dockerignore` para backend y frontend
- Agregar scripts en `Makefile` para comandos Docker unificados
- Actualizar `CLAUDE.md` con comandos Docker

## Capabilities

### New Capabilities
- `docker-dev`: Entorno de desarrollo dockerizado con hot-reload, volumes, y PostgreSQL
- `docker-prod`: Build de producción multi-stage con Nginx reverse proxy y health checks
- `docker-ci`: Ejecución de tests en contenedores aislados (pytest, vitest, playwright)

### Modified Capabilities

_Ninguna. Docker es infraestructura nueva que no modifica los requerimientos de las specs existentes._

## Impact

- **Archivos nuevos**: `backend/Dockerfile`, `frontend/Dockerfile`, `docker-compose.yml`, `docker-compose.prod.yml`, `docker-compose.ci.yml`, `backend/.dockerignore`, `frontend/.dockerignore`, `Makefile`
- **Archivos modificados**: `CLAUDE.md` (nuevos comandos Docker)
- **Dependencias nuevas**: Docker Engine ≥24, Docker Compose v2
- **Puertos expuestos**: 8000 (backend), 5173 (frontend dev), 80/443 (Nginx prod)
- **Sistemas afectados**: Desarrollo local, CI/CD pipeline, despliegue
