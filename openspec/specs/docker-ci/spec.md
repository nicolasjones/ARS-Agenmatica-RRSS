## ADDED Requirements

### Requirement: Backend tests run in container
The CI compose SHALL define a service that runs `pytest` inside a container with all backend dependencies installed.

#### Scenario: Run backend tests
- **WHEN** `docker compose -f docker-compose.yml -f docker-compose.ci.yml run backend-test` is executed
- **THEN** pytest runs all backend tests with coverage
- **THEN** the exit code reflects test results (0 = pass, non-zero = fail)

### Requirement: Frontend tests run in container
The CI compose SHALL define a service that runs `vitest` inside a container with all frontend dependencies installed.

#### Scenario: Run frontend tests
- **WHEN** `docker compose -f docker-compose.yml -f docker-compose.ci.yml run frontend-test` is executed
- **THEN** vitest runs all frontend tests
- **THEN** the exit code reflects test results

### Requirement: E2E tests run with Playwright container
The CI compose SHALL define a service using the official Playwright Docker image to run E2E tests against the frontend dev server.

#### Scenario: Run E2E tests
- **WHEN** `docker compose -f docker-compose.yml -f docker-compose.ci.yml run e2e-test` is executed
- **THEN** the frontend dev server starts as a dependency
- **THEN** Playwright runs all E2E tests in Chromium
- **THEN** the exit code reflects test results

#### Scenario: E2E test artifacts are accessible
- **WHEN** E2E tests complete (pass or fail)
- **THEN** Playwright HTML report and screenshots are available in a mounted volume

### Requirement: Makefile provides unified commands
A `Makefile` in the project root SHALL provide shorthand commands for all Docker operations.

#### Scenario: Dev commands
- **WHEN** the developer runs `make dev`
- **THEN** `docker compose up` starts the dev environment

#### Scenario: Test commands
- **WHEN** the developer runs `make test`
- **THEN** all test suites (backend, frontend, E2E) run in containers sequentially

#### Scenario: Build command
- **WHEN** the developer runs `make build`
- **THEN** production images are built for backend and frontend

#### Scenario: Clean command
- **WHEN** the developer runs `make clean`
- **THEN** all containers, images, and volumes are removed
