## Why

El proyecto no tiene infraestructura de testing completa: el frontend carece de cualquier test, el backend tiene cobertura básica sin mocks ni coverage report, y no existe ninguna prueba E2E que valide el stack completo. Esto bloquea el desarrollo ágil con TDD y hace imposible detectar regresiones entre el frontend React y la API FastAPI.

## What Changes

- **Backend**: Agregar pytest-cov (coverage), pytest-mock y respx (mocking HTTP), fixtures de fábrica reutilizables, y aumentar cobertura de servicios y endpoints
- **Frontend**: Configurar Vitest + React Testing Library para unit y component tests; añadir MSW (Mock Service Worker) para mockear la API en tests
- **E2E**: Configurar Playwright para pruebas end-to-end sobre el stack real (frontend → FastAPI → servicios)
- **TDD baseline**: Establecer convenciones de TDD, estructura de test, y scripts de CI para todos los niveles de la pirámide

## Capabilities

### New Capabilities

- `backend-testing`: Configuración completa de pytest con coverage, mocks HTTP, factories y convenciones TDD para el backend Python
- `frontend-testing`: Configuración de Vitest + React Testing Library + MSW para tests unitarios y de componentes en el frontend React
- `e2e-testing`: Suite Playwright para pruebas end-to-end que validan flujos completos entre frontend y backend

### Modified Capabilities

- `api`: Se añaden tests de integración más profundos con mocks de servicios externos (platform APIs, LLM)

## Impact

- `backend/pyproject.toml`: nuevas dependencias de dev (pytest-cov, pytest-mock, respx, factory-boy)
- `backend/tests/`: reestructuración en `unit/`, `integration/`, con conftest.py y factories
- `frontend/package.json`: nuevas dependencias (vitest, @testing-library/react, @testing-library/user-event, msw)
- `frontend/vitest.config.ts`: nueva config de vitest
- `frontend/src/**/*.test.tsx`: nuevos archivos de test colocados junto al código
- `e2e/`: nuevo directorio raíz con Playwright, `playwright.config.ts` y tests de flujos principales
- `frontend/src/mocks/`: handlers MSW para mock de API en tests y desarrollo
