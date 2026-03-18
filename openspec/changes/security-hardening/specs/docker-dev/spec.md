## MODIFIED Requirements

### Requirement: Dev environment starts with a single command
The system SHALL provide a `docker compose` configuration that starts backend, frontend, and PostgreSQL with one command. Credentials MUST be loaded from a `.env` file, not hardcoded in compose.

#### Scenario: Start dev environment
- **WHEN** the developer has a `.env` file and runs `make dev`
- **THEN** the backend is accessible at `http://localhost:8000`
- **THEN** the frontend is accessible at `http://localhost:5173`
- **THEN** PostgreSQL is running and accepting connections on port 5432

#### Scenario: Missing .env shows clear error
- **WHEN** the developer runs `make dev` without a `.env` file
- **THEN** the application fails with a clear message about missing configuration

## ADDED Requirements

### Requirement: .env excluded from Docker build context
The `.dockerignore` files for both backend and frontend SHALL exclude `.env` and `.env.*` files.

#### Scenario: Build context is clean
- **WHEN** Docker builds the backend or frontend image
- **THEN** `.env` files are not included in the build context
