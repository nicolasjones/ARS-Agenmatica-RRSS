## MODIFIED Requirements

### Requirement: Multi-stage backend Dockerfile
The backend Dockerfile SHALL use multi-stage builds with a `dev` target and a `prod` target. The prod image MUST use `python:3.11-slim`, contain only production dependencies, and run as a non-root user.

#### Scenario: Prod image is minimal
- **WHEN** the prod image is built with `docker build --target prod`
- **THEN** the image size is under 250MB
- **THEN** dev dependencies (pytest, ruff, etc.) are not present

#### Scenario: Dev image has all tools
- **WHEN** the dev image is built with `docker build --target dev`
- **THEN** all dev dependencies are installed (pytest, ruff, etc.)

#### Scenario: Prod container runs as non-root
- **WHEN** the prod container starts
- **THEN** the process runs as `appuser` (UID 1000), not root

### Requirement: Multi-stage frontend Dockerfile
The frontend Dockerfile SHALL use multi-stage builds. The prod target MUST build the Vite app, serve it via `nginx:alpine`, and run as non-root.

#### Scenario: Prod frontend serves static files
- **WHEN** the prod image is built and started
- **THEN** Nginx serves the built frontend assets on port 80
- **THEN** the image size is under 100MB

#### Scenario: Prod container runs as non-root
- **WHEN** the prod frontend container starts
- **THEN** Nginx runs as the `nginx` user, not root

### Requirement: Production compose override
A `docker-compose.prod.yml` SHALL override the base compose to use prod targets, optimized settings, restart policies, network isolation, and resource limits.

#### Scenario: Start production environment
- **WHEN** the operator runs `docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d`
- **THEN** all services start with prod-optimized images
- **THEN** services restart automatically on failure

#### Scenario: Network isolation enforced
- **WHEN** production compose is running
- **THEN** the frontend container cannot reach the postgres container directly

#### Scenario: Resource limits applied
- **WHEN** production compose is running
- **THEN** backend and frontend containers have CPU and memory limits

## ADDED Requirements

### Requirement: .env excluded from Docker build context
Both backend and frontend `.dockerignore` files SHALL exclude `.env` and `.env.*` files to prevent secrets leaking into image layers.

#### Scenario: .env not in image
- **WHEN** the backend image is built with a `.env` file present
- **THEN** the `.env` file is not present in the built image

### Requirement: Compose uses env_file for secrets
Docker compose files SHALL use `env_file` directive to load secrets from `.env` instead of hardcoding credentials.

#### Scenario: Credentials loaded from .env
- **WHEN** `docker compose up` is run with a `.env` file containing `DATABASE_URL`
- **THEN** the backend container receives the `DATABASE_URL` from the `.env` file
- **THEN** no credentials appear in the compose YAML files
