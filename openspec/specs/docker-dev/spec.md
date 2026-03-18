## ADDED Requirements

### Requirement: Dev environment starts with a single command
The system SHALL provide a `docker compose` configuration that starts backend, frontend, and PostgreSQL with one command. All services MUST be available and connected after startup.

#### Scenario: Start dev environment
- **WHEN** the developer runs `make dev` (or `docker compose up`)
- **THEN** the backend is accessible at `http://localhost:8000`
- **THEN** the frontend is accessible at `http://localhost:5173`
- **THEN** PostgreSQL is running and accepting connections on port 5432

#### Scenario: First-time setup
- **WHEN** a new developer clones the repo and runs `make dev` for the first time
- **THEN** Docker builds all images automatically
- **THEN** all services start without manual configuration

### Requirement: Hot-reload for backend in dev
The backend container SHALL mount the source code as a volume and use uvicorn `--reload` so that code changes are reflected without rebuilding the container.

#### Scenario: Backend code change
- **WHEN** the developer edits a Python file in `backend/app/`
- **THEN** uvicorn detects the change and restarts automatically
- **THEN** the API reflects the updated code within seconds

### Requirement: Hot-reload for frontend in dev
The frontend container SHALL mount the source code as a volume and use Vite dev server so that code changes trigger HMR without rebuilding.

#### Scenario: Frontend code change
- **WHEN** the developer edits a TSX file in `frontend/src/`
- **THEN** Vite HMR updates the browser automatically
- **THEN** the change is visible without full page reload

### Requirement: PostgreSQL with persistent data
The dev environment SHALL include a PostgreSQL container with a named volume for data persistence across restarts.

#### Scenario: Database survives restart
- **WHEN** the developer runs `docker compose down` and then `docker compose up`
- **THEN** PostgreSQL data from the previous session is preserved

#### Scenario: Clean database reset
- **WHEN** the developer runs `docker compose down -v`
- **THEN** the PostgreSQL volume is removed and the database starts fresh

### Requirement: Backend .dockerignore
The backend SHALL have a `.dockerignore` file excluding `.venv/`, `__pycache__/`, `.pytest_cache/`, `htmlcov/`, and `.ruff_cache/`.

#### Scenario: Build context is minimal
- **WHEN** Docker builds the backend image
- **THEN** the build context excludes virtual environments, caches, and coverage artifacts

### Requirement: Frontend .dockerignore
The frontend SHALL have a `.dockerignore` file excluding `node_modules/`, `dist/`, and `coverage/`.

#### Scenario: Build context is minimal
- **WHEN** Docker builds the frontend image
- **THEN** the build context excludes node_modules and build artifacts
