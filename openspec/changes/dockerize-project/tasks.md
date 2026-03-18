## 1. Dockerfiles

- [ ] 1.1 Crear `backend/Dockerfile` con stages `dev` y `prod` (base `python:3.11-slim`, `uv pip install`, uvicorn entrypoint)
- [ ] 1.2 Crear `frontend/Dockerfile` con stages `dev` (Vite dev server) y `prod` (build + `nginx:alpine`)
- [ ] 1.3 Crear `frontend/nginx.conf` con proxy `/api` → backend:8000 y SPA fallback a `index.html`
- [ ] 1.4 Crear `backend/.dockerignore` excluyendo `.venv/`, `__pycache__/`, `.pytest_cache/`, `htmlcov/`, `.ruff_cache/`
- [ ] 1.5 Crear `frontend/.dockerignore` excluyendo `node_modules/`, `dist/`, `coverage/`

## 2. Docker Compose — Dev

- [ ] 2.1 Crear `docker-compose.yml` con servicios `backend`, `frontend`, `postgres` (perfiles dev)
- [ ] 2.2 Configurar backend con volume mount `./backend:/app`, `--reload`, y `DATABASE_URL` apuntando a postgres
- [ ] 2.3 Configurar frontend con volume mount `./frontend:/app` (excluyendo `node_modules`), expuesto en puerto 5173
- [ ] 2.4 Configurar PostgreSQL con named volume `pgdata`, health check `pg_isready`, credenciales en env vars
- [ ] 2.5 Verificar `docker compose up` levanta los 3 servicios y hot-reload funciona

## 3. Docker Compose — Prod

- [ ] 3.1 Crear `docker-compose.prod.yml` override con targets `prod`, restart `unless-stopped`, health checks
- [ ] 3.2 Configurar backend prod con `--workers 4` y health check `GET /api/v1/health`
- [ ] 3.3 Configurar frontend prod usando Nginx con `nginx.conf` montado, expuesto en puerto 80
- [ ] 3.4 Verificar `docker compose -f docker-compose.yml -f docker-compose.prod.yml up` funciona correctamente

## 4. Docker Compose — CI

- [ ] 4.1 Crear `docker-compose.ci.yml` con servicios `backend-test`, `frontend-test`, `e2e-test`
- [ ] 4.2 Configurar `backend-test` para ejecutar `pytest` con coverage, exit code propagado
- [ ] 4.3 Configurar `frontend-test` para ejecutar `vitest run`, exit code propagado
- [ ] 4.4 Configurar `e2e-test` usando `mcr.microsoft.com/playwright` con frontend como dependencia, volumes para reportes
- [ ] 4.5 Verificar que `docker compose -f docker-compose.yml -f docker-compose.ci.yml run backend-test` pasa

## 5. Makefile y Documentación

- [ ] 5.1 Crear `Makefile` con targets: `dev`, `prod`, `build`, `test`, `test-backend`, `test-frontend`, `test-e2e`, `clean`, `logs`
- [ ] 5.2 Actualizar `CLAUDE.md` con sección de comandos Docker y requisitos (Docker Engine ≥24)
- [ ] 5.3 Agregar `docker-compose.override.yml` a `.gitignore` para permitir overrides locales personales
