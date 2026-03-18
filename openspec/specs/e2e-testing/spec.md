## ADDED Requirements

### Requirement: Playwright is configured for E2E testing
El proyecto SHALL tener Playwright configurado en un directorio `e2e/` en la raíz, con `playwright.config.ts` apuntando al frontend en `http://localhost:5173` y al backend en `http://localhost:8000`.

#### Scenario: E2E tests are discovered and run
- **WHEN** running `npx playwright test` from the project root
- **THEN** Playwright discovers all `e2e/**/*.spec.ts` files and executes them

#### Scenario: Tests run in Chromium by default
- **WHEN** running `npx playwright test` without `--browser` flag
- **THEN** tests execute in Chromium headless mode

---

### Requirement: E2E tests cover the dashboard health check flow
El sistema SHALL tener un test E2E que valide que el Dashboard muestra el estado correcto del sistema cuando el backend está disponible.

#### Scenario: Dashboard shows backend status as 'ok'
- **WHEN** the user navigates to `/`
- **THEN** the Dashboard page is displayed with system status showing "ok"

---

### Requirement: E2E tests cover content creation flow
El sistema SHALL tener un test E2E que valide el flujo completo de solicitud de generación de contenido desde el frontend hasta la respuesta de la API.

#### Scenario: User submits content generation form
- **WHEN** the user navigates to `/content` and fills the content form with topic and platform
- **THEN** the form is submitted successfully and the response is displayed in the UI

---

### Requirement: Playwright generates HTML test reports
El sistema SHALL configurar Playwright para generar un reporte HTML con resultados de tests, screenshots de fallos, y trazas de ejecución.

#### Scenario: HTML report generated after test run
- **WHEN** `npx playwright test` completes (pass or fail)
- **THEN** an HTML report is generated in `playwright-report/` and can be opened with `npx playwright show-report`

#### Scenario: Screenshots captured on failure
- **WHEN** an E2E test fails
- **THEN** a screenshot of the browser state at failure is saved in `test-results/`

---

### Requirement: E2E tests can run with a mocked backend
El sistema SHALL soportar un modo de E2E donde el frontend usa MSW para mockear las respuestas de la API, permitiendo tests E2E de UI sin backend real.

#### Scenario: Frontend-only E2E test passes without backend
- **WHEN** running Playwright tests con la variable `E2E_MOCK=true`
- **THEN** los tests de UI pasan usando MSW handlers sin necesidad de `uvicorn` corriendo
