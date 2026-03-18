## ADDED Requirements

### Requirement: Backend tests are organized by test type
El backend SHALL organizar los tests en subdirectorios `unit/` e `integration/` dentro de `backend/tests/`, con un `conftest.py` raíz para fixtures compartidas.

#### Scenario: Unit tests run without I/O
- **WHEN** running `pytest tests/unit/`
- **THEN** all service tests execute without network calls, database access, or external dependencies

#### Scenario: Integration tests use TestClient
- **WHEN** running `pytest tests/integration/`
- **THEN** all API endpoint tests use FastAPI's TestClient and mock external services with respx or pytest-mock

---

### Requirement: Backend test coverage is measured and reported
El backend SHALL generar un reporte de cobertura HTML y por terminal al correr la suite completa.

#### Scenario: Coverage report generated
- **WHEN** running `pytest --cov=app --cov-report=term-missing --cov-report=html`
- **THEN** a coverage report is generated in `htmlcov/` and printed to terminal with uncovered lines

#### Scenario: Coverage minimum enforced
- **WHEN** coverage for `app/agents/services/` falls below 90%
- **THEN** the pytest run exits with a non-zero code

---

### Requirement: External HTTP calls are mocked in integration tests
El sistema SHALL usar `respx` para interceptar y mockear todas las llamadas HTTP externas (platform APIs, LLM) durante tests de integración.

#### Scenario: Platform API call is mocked
- **WHEN** an integration test triggers a platform API call
- **THEN** `respx` intercepts the call and returns a configured mock response without hitting real APIs

#### Scenario: Unmocked HTTP call raises error
- **WHEN** an HTTP call is made during tests without a corresponding `respx` mock
- **THEN** the test fails with a clear error indicating the unmatched request

---

### Requirement: Test factories provide reusable data fixtures
El sistema SHALL proveer factories usando `factory-boy` para crear instancias de datos de test (ContentBrief, Post, PostMetrics, etc.) sin repetición.

#### Scenario: Factory creates valid ContentBrief
- **WHEN** `ContentBriefFactory()` is called
- **THEN** a valid `ContentBrief` instance is returned with sensible defaults

#### Scenario: Factory allows overrides
- **WHEN** `ContentBriefFactory(platform="tiktok")` is called
- **THEN** the resulting instance has `platform="tiktok"` with all other fields at defaults

---

### Requirement: Async endpoints are tested with async fixtures
El sistema SHALL soportar tests async mediante `pytest-asyncio` con modo `auto` configurado.

#### Scenario: Async test runs without explicit loop management
- **WHEN** a test function is defined with `async def test_*()`
- **THEN** pytest-asyncio runs it automatically without requiring explicit `@pytest.mark.asyncio`
