## ADDED Requirements

### Requirement: Secrets use SecretStr and have no defaults
All API keys and credentials in `Settings` SHALL use Pydantic `SecretStr` type and MUST NOT have default values. The application SHALL fail at startup if required secrets are missing.

#### Scenario: Missing API key fails startup
- **WHEN** the application starts without `ANTHROPIC_API_KEY` set
- **THEN** Pydantic validation raises an error before the server starts
- **THEN** the error message indicates which variable is missing

#### Scenario: SecretStr prevents accidental logging
- **WHEN** settings are logged or serialized
- **THEN** SecretStr fields display `**********` instead of the actual value

### Requirement: Database URL has no insecure default
The `database_url` setting SHALL NOT have a default value containing credentials. It MUST be provided via environment variable.

#### Scenario: Missing database URL fails startup
- **WHEN** the application starts without `DATABASE_URL` set
- **THEN** Pydantic validation raises an error
- **THEN** the error message indicates `DATABASE_URL` is required

### Requirement: CORS origins configurable via environment
The `cors_origins` setting SHALL be loaded from the `CORS_ORIGINS` environment variable as a comma-separated string. It MUST NOT default to a wildcard or hardcoded URL.

#### Scenario: CORS origins loaded from env
- **WHEN** `CORS_ORIGINS=http://localhost:5173,http://localhost:3000` is set
- **THEN** the CORS middleware allows requests from both origins

#### Scenario: Empty CORS origins rejects cross-origin
- **WHEN** `CORS_ORIGINS` is empty or not set
- **THEN** no cross-origin requests are allowed

### Requirement: .env.example template exists
A `.env.example` file SHALL exist at the project root with all required environment variables documented with placeholder values.

#### Scenario: Developer copies .env.example
- **WHEN** a developer copies `.env.example` to `.env` and fills in values
- **THEN** the application starts successfully

### Requirement: OpenAPI docs disabled in production
The FastAPI app SHALL set `docs_url`, `redoc_url`, and `openapi_url` to `None` when `debug=False`.

#### Scenario: Docs disabled in production
- **WHEN** the application runs with `DEBUG=false`
- **THEN** `GET /docs` returns 404
- **THEN** `GET /redoc` returns 404
- **THEN** `GET /openapi.json` returns 404

#### Scenario: Docs enabled in development
- **WHEN** the application runs with `DEBUG=true`
- **THEN** `GET /docs` returns Swagger UI
