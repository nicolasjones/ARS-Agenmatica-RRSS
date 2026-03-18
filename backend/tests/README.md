# Backend Tests

## Structure

```
tests/
├── conftest.py          # Global fixtures (test_client, etc.)
├── factories/           # factory-boy data factories
│   └── content.py       # ContentBriefFactory, PostMetricsSummaryFactory
├── unit/                # Pure service tests (no I/O, no HTTP)
│   ├── test_content_service.py
│   ├── test_schedule_service.py
│   ├── test_analytics_service.py
│   └── test_strategy_service.py
└── integration/         # API tests with TestClient + mocks
    ├── test_health.py
    └── test_content_api.py
```

## Running Tests

```bash
# All tests + coverage (80% minimum enforced)
pytest

# Specific layer
pytest tests/unit/
pytest tests/integration/

# With HTML coverage report
pytest --cov-report=html
open htmlcov/index.html
```

## TDD Conventions

1. **Red** — Write a failing test first
2. **Green** — Write the minimum code to pass
3. **Refactor** — Clean up, keeping tests green

### Unit tests (`tests/unit/`)
- Test service classes in isolation
- No network calls, no database, no FastAPI
- Use `factory-boy` factories for test data
- Target: ≥90% coverage on `app/agents/services/`

### Integration tests (`tests/integration/`)
- Test API endpoints via FastAPI `TestClient`
- Mock external HTTP with `respx`
- Mock Python dependencies with `pytest-mock`
- Target: ≥80% coverage overall

## Factories

Use factories instead of hardcoded dicts:

```python
from tests.factories.content import ContentBriefFactory, PostMetricsSummaryFactory

# Default instance
brief = ContentBriefFactory()

# With overrides
brief = ContentBriefFactory(platform="tiktok", tone="fun")

# Multiple
metrics = PostMetricsSummaryFactory.create_batch(5, platform="instagram")
```

## Coverage

Coverage is enforced at `--cov-fail-under=80`. The `app/agents/crews/` directory
is excluded (CrewAI wrappers depend on external LLM — tested via service mocks).
