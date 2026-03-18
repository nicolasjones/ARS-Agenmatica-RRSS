## 1. Backend — Dependencias y Configuración

- [ ] 1.1 Agregar `pytest-cov`, `pytest-mock`, `respx`, `factory-boy` a `[project.optional-dependencies].dev` en `backend/pyproject.toml`
- [ ] 1.2 Actualizar `[tool.pytest.ini_options]` en `pyproject.toml`: añadir `--cov=app`, `--cov-fail-under=80`, y actualizar `testpaths` para incluir `tests/unit` y `tests/integration`
- [ ] 1.3 Instalar las nuevas dependencias en el venv: `uv pip install -e ".[dev]"`

## 2. Backend — Reestructuración de Tests

- [ ] 2.1 Crear directorios `backend/tests/unit/`, `backend/tests/integration/`, `backend/tests/factories/`
- [ ] 2.2 Crear `backend/tests/conftest.py` con fixtures globales: `test_client` (FastAPI TestClient), `mock_content_service`, `mock_analytics_service`
- [ ] 2.3 Mover tests de servicios existentes a `tests/unit/` (test_services.py → unit/test_content_service.py, unit/test_schedule_service.py, etc.)
- [ ] 2.4 Mover tests de API existentes a `tests/integration/` (test_health.py, test_content_api.py)
- [ ] 2.5 Crear `backend/tests/factories/content.py` con `ContentBriefFactory` y `PostMetricsSummaryFactory` usando `factory-boy`

## 3. Backend — Tests Nuevos con Mocks

- [ ] 3.1 Crear `tests/unit/test_analytics_service.py` completando cobertura de `AnalyticsService.generate_insight()` con edge cases
- [ ] 3.2 Crear `tests/unit/test_strategy_service.py` con tests de `create_default_strategy()` y `validate_pillar_weights()`
- [ ] 3.3 Crear `tests/integration/test_content_api.py` con `respx` mockeando llamadas HTTP en el endpoint `POST /api/v1/content/`
- [ ] 3.4 Verificar que `pytest --cov=app --cov-report=term-missing` pasa con ≥80% coverage

## 4. Frontend — Vitest + React Testing Library

- [ ] 4.1 Instalar dependencias: `vitest`, `@vitest/coverage-v8`, `jsdom`, `@testing-library/react`, `@testing-library/user-event`, `@testing-library/jest-dom`
- [ ] 4.2 Crear `frontend/vitest.config.ts` con: environment `jsdom`, path aliases `@/→src/`, setup file `src/test/setup.ts`, coverage provider `v8`
- [ ] 4.3 Agregar scripts a `frontend/package.json`: `"test": "vitest run"`, `"test:watch": "vitest"`, `"test:coverage": "vitest run --coverage"`
- [ ] 4.4 Crear `frontend/src/test/setup.ts` con imports de `@testing-library/jest-dom` para los custom matchers

## 5. Frontend — MSW Setup

- [ ] 5.1 Instalar `msw` como dependencia de dev: `npm install --save-dev msw`
- [ ] 5.2 Crear `frontend/src/mocks/handlers.ts` con handlers MSW para: `GET /api/v1/health`, `POST /api/v1/content/`, `GET /api/v1/content/`
- [ ] 5.3 Crear `frontend/src/mocks/server.ts` para Node/Vitest (usando `setupServer` de `msw/node`)
- [ ] 5.4 Agregar al `setup.ts`: `beforeAll(() => server.listen())`, `afterEach(() => server.resetHandlers())`, `afterAll(() => server.close())`

## 6. Frontend — Tests de Componentes

- [ ] 6.1 Crear `frontend/src/components/Sidebar.test.tsx`: renderiza sin crash, links de navegación presentes por role, link activo tiene clase correcta
- [ ] 6.2 Crear `frontend/src/pages/Dashboard.test.tsx`: muestra status "ok" cuando el health endpoint responde correctamente (MSW mock), muestra fallback cuando el backend falla
- [ ] 6.3 Crear `frontend/src/api/client.test.ts`: tests unitarios de `apiFetch` — respuesta exitosa, error HTTP, error de red
- [ ] 6.4 Ejecutar `npm run test:coverage` y verificar cobertura ≥70% en componentes

## 7. E2E — Playwright Setup

- [ ] 7.1 Instalar Playwright: `npm init playwright@latest` en el directorio raíz del proyecto (fuera de `frontend/` y `backend/`)
- [ ] 7.2 Configurar `playwright.config.ts` en la raíz: baseURL `http://localhost:5173`, reportes HTML, screenshots en fallo, timeout de 30s
- [ ] 7.3 Configurar `webServer` en `playwright.config.ts` para levantar `npm run dev` en `frontend/` automáticamente antes de los tests
- [ ] 7.4 Agregar `.gitignore` entries para `playwright-report/`, `test-results/`

## 8. E2E — Tests Playwright

- [ ] 8.1 Crear `e2e/dashboard.spec.ts`: navegar a `/`, verificar que la página carga con título "Dashboard", verificar sección de system status
- [ ] 8.2 Crear `e2e/navigation.spec.ts`: verificar que todos los links del Sidebar navegan a la ruta correcta sin errores 404
- [ ] 8.3 Crear `e2e/content.spec.ts`: navegar a `/content`, verificar que la página renderiza correctamente (smoke test)
- [ ] 8.4 Ejecutar `npx playwright test` y verificar que los 3 spec files pasan en Chromium

## 9. Scripts Unificados y Documentación

- [ ] 9.1 Agregar script `test:all` en `frontend/package.json` que corra `vitest run` + type check
- [ ] 9.2 Actualizar `CLAUDE.md` con los nuevos comandos: `pytest --cov`, `npm run test`, `npm run test:coverage`, `npx playwright test`
- [ ] 9.3 Crear `backend/tests/README.md` documentando la estructura de tests y convenciones TDD del proyecto
