## ADDED Requirements

### Requirement: Frontend has Vitest configured as test runner
El frontend SHALL tener Vitest configurado con soporte para TypeScript, JSX, y el mismo sistema de path aliases que Vite (`@/`).

#### Scenario: Tests run via npm script
- **WHEN** running `npm run test` in the `frontend/` directory
- **THEN** Vitest discovers and runs all `*.test.tsx` and `*.test.ts` files

#### Scenario: Path aliases work in tests
- **WHEN** a test file imports using `@/components/Sidebar`
- **THEN** Vitest resolves the alias to `src/components/Sidebar` correctly

---

### Requirement: React components are tested with React Testing Library
El frontend SHALL usar React Testing Library (RTL) para tests de componentes, priorizando queries accesibles (by role, by label, by text) sobre queries de implementación.

#### Scenario: Component renders without crash
- **WHEN** a component test renders `<Sidebar />` with RTL's `render()`
- **THEN** no errors are thrown and the component is in the DOM

#### Scenario: Navigation link is queryable by accessible role
- **WHEN** querying the Sidebar component
- **THEN** navigation links are findable via `screen.getByRole('link', { name: /Dashboard/i })`

---

### Requirement: API calls are intercepted by MSW in component tests
El frontend SHALL usar Mock Service Worker (MSW) para interceptar llamadas `fetch` a la API FastAPI durante tests de componentes, sin modificar el código fuente del cliente API.

#### Scenario: Dashboard health call is mocked
- **WHEN** the Dashboard component mounts in a test with MSW configured
- **THEN** the `/api/v1/health` call is intercepted by MSW and returns mock data without hitting the real backend

#### Scenario: Unhandled API request warns in tests
- **WHEN** a component makes a fetch call without a matching MSW handler
- **THEN** MSW logs a warning to the console (not a test failure, but visible)

---

### Requirement: Frontend test coverage is collected via v8 provider
El frontend SHALL configurar Vitest para colectar coverage con el proveedor `v8`, generando reportes en `lcov` y por terminal.

#### Scenario: Coverage collected on test run
- **WHEN** running `npm run test:coverage`
- **THEN** a coverage summary is printed to terminal and a `coverage/` directory is created

#### Scenario: Uncovered lines are visible
- **WHEN** coverage report is generated
- **THEN** files with less than 70% coverage are highlighted in the terminal output

---

### Requirement: Test utilities and setup are centralized
El frontend SHALL tener un archivo `src/test/setup.ts` que configure el entorno global de tests (MSW server start/stop, matchers de RTL, etc.) y sea referenciado en `vitest.config.ts`.

#### Scenario: MSW server starts before all tests
- **WHEN** the Vitest test suite initializes
- **THEN** the MSW server is started via `beforeAll(() => server.listen())`

#### Scenario: MSW server resets between tests
- **WHEN** each test completes
- **THEN** MSW handlers are reset to defaults via `afterEach(() => server.resetHandlers())`
