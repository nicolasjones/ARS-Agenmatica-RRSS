## Context

El proyecto tiene un backend FastAPI (Python 3.11+) y un frontend React/Vite que actualmente se ejecutan con venvs y npm manualmente. PostgreSQL es una dependencia futura. La suite de tests incluye pytest (backend), vitest (frontend) y playwright (E2E). No existe containerización.

## Goals / Non-Goals

**Goals:**
- Levantar todo el entorno dev con un solo `docker compose up`
- Builds de producción optimizados (imágenes pequeñas, multi-stage)
- Suite de tests completa ejecutable en contenedores aislados para CI
- Hot-reload funcional en modo dev (tanto backend como frontend)
- PostgreSQL como servicio en compose para preparar migración futura

**Non-Goals:**
- Kubernetes / Helm charts (fuera de alcance por ahora)
- Registry push automatizado (se hará en un cambio de CI/CD futuro)
- SSL/TLS en Nginx (se configurará por entorno en despliegue)
- Docker Swarm o clustering

## Decisions

### 1. Multi-stage Dockerfiles

Cada servicio usa un Dockerfile con stages `dev` y `prod`:
- **dev**: instala todas las dependencias, monta volumes para hot-reload
- **prod**: build optimizado, solo dependencias de producción, imagen mínima

**Backend prod**: `python:3.11-slim` → copiar wheel → uvicorn con workers
**Frontend prod**: build con node → copiar dist a `nginx:alpine`

_Alternativa descartada_: Dockerfiles separados por entorno — duplica mantenimiento.

### 2. Compose profiles en lugar de archivos separados

Usar un solo `docker-compose.yml` con profiles (`dev`, `prod`, `ci`):
- `docker compose --profile dev up` → dev con hot-reload
- `docker compose --profile prod up` → builds optimizados
- `docker compose --profile ci run tests` → tests en contenedores

_Alternativa descartada_: Múltiples archivos compose — más complejo de mantener. Sin embargo, se usa `docker-compose.override.yml` para dev por convención Docker.

**Decisión final**: Un `docker-compose.yml` base + `docker-compose.prod.yml` (override prod) + `docker-compose.ci.yml` (override CI). Es más idiomático Docker Compose.

### 3. Nginx como reverse proxy en prod

En producción, Nginx sirve el frontend estático y hace proxy al backend en `/api`:
- Reduce latencia (frontend estático servido directamente)
- Un solo punto de entrada (puerto 80)
- Health checks en `/api/v1/health`

### 4. Makefile como interfaz unificada

Comandos frecuentes abstraídos en `Makefile`:
- `make dev` → levanta entorno dev
- `make prod` → levanta entorno prod
- `make test` → corre toda la suite en containers
- `make build` → construye imágenes prod

_Alternativa descartada_: Scripts bash — Makefile es estándar, idempotente, y soporta dependencias.

### 5. PostgreSQL en dev aunque aún no se use

Incluir PostgreSQL en compose dev desde ahora para:
- Preparar la migración a SQLAlchemy sin cambios en Docker
- Los servicios ya tendrán `DATABASE_URL` disponible
- Se usa `healthcheck` para esperar a que esté ready

### 6. Playwright en CI con imagen oficial

Usar `mcr.microsoft.com/playwright:v1.52.0-noble` como base para tests E2E:
- Incluye todos los browsers pre-instalados
- Evita el problema de `playwright install` en red

## Risks / Trade-offs

- **[Imágenes grandes en dev]** → Aceptable; solo se usan localmente. Prod usa slim/alpine.
- **[PostgreSQL sin uso actual]** → Overhead mínimo (~50MB RAM). Facilita migración futura.
- **[Playwright imagen pesada (~2GB)]** → Solo se descarga en CI. Se cachea en CI layers.
- **[Hot-reload lento en Docker en macOS]** → Mitigado con `volumes` y `poll` mode en Vite/uvicorn.
- **[Secrets en env vars]** → Para dev es aceptable. Prod debería usar Docker secrets o vault (futuro).
