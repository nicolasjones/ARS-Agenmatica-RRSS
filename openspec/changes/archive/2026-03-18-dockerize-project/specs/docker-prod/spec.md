## ADDED Requirements

### Requirement: Multi-stage backend Dockerfile
The backend Dockerfile SHALL use multi-stage builds with a `dev` target and a `prod` target. The prod image MUST use `python:3.11-slim` and contain only production dependencies.

#### Scenario: Prod image is minimal
- **WHEN** the prod image is built with `docker build --target prod`
- **THEN** the image size is under 250MB
- **THEN** dev dependencies (pytest, ruff, etc.) are not present

#### Scenario: Dev image has all tools
- **WHEN** the dev image is built with `docker build --target dev`
- **THEN** all dev dependencies are installed (pytest, ruff, etc.)

### Requirement: Multi-stage frontend Dockerfile
The frontend Dockerfile SHALL use multi-stage builds. The prod target MUST build the Vite app and serve it via `nginx:alpine`.

#### Scenario: Prod frontend serves static files
- **WHEN** the prod image is built and started
- **THEN** Nginx serves the built frontend assets on port 80
- **THEN** the image size is under 100MB

#### Scenario: Dev frontend uses Vite dev server
- **WHEN** the dev image is built with `docker build --target dev`
- **THEN** Vite dev server is available for development with HMR

### Requirement: Nginx reverse proxy in production
The production compose SHALL configure Nginx to serve frontend static files and proxy `/api` requests to the backend.

#### Scenario: API requests are proxied
- **WHEN** a request is made to `http://host/api/v1/health`
- **THEN** Nginx forwards it to the backend container on port 8000
- **THEN** the response is returned to the client

#### Scenario: Frontend routes use fallback
- **WHEN** a request is made to a frontend route like `/content`
- **THEN** Nginx serves `index.html` (SPA fallback)

### Requirement: Health checks in production
All production services SHALL define Docker health checks.

#### Scenario: Backend health check
- **WHEN** the backend container is running
- **THEN** Docker health check calls `GET /api/v1/health` and expects status 200

#### Scenario: PostgreSQL health check
- **WHEN** PostgreSQL is running
- **THEN** Docker health check runs `pg_isready` and reports healthy

### Requirement: Production compose override
A `docker-compose.prod.yml` SHALL override the base compose to use prod targets, optimized settings, and restart policies.

#### Scenario: Start production environment
- **WHEN** the operator runs `docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d`
- **THEN** all services start with prod-optimized images
- **THEN** services restart automatically on failure
