## Context

El proyecto tiene un backend FastAPI en Python 3.11 con 16 tests básicos (pytest) y un frontend React 19 + TypeScript sin ningún test. La pirámide de testing está incompleta: hay unit tests de servicios, tests de API con TestClient, pero no hay mocks para servicios externos (LLM, platform APIs), no hay tests de componentes React, y no hay ninguna prueba E2E que valide el stack completo. La arquitectura del backend (servicios framework-agnostic separados de CrewAI crews) facilita el testing unitario sin dependencias externas.

## Goals / Non-Goals

**Goals:**
- Configurar Vitest + React Testing Library + MSW para el frontend
- Ampliar pytest con pytest-cov, pytest-mock, respx y factories para el backend
- Configurar Playwright E2E para flujos críticos (generar contenido, ver dashboard)
- Establecer convenciones TDD: red → green → refactor con targets de cobertura
- Scripts unificados para correr toda la pirámide de tests

**Non-Goals:**
- Tests de performance o carga
- Tests de accesibilidad automatizados (a11y)
- CI/CD pipeline (es parte de `setup-docker-local`)
- Testing de platform adapters reales (requieren credenciales externas)

## Decisions

### 1. Vitest sobre Jest para el frontend

**Decisión**: Vitest como runner de tests para el frontend.

**Rationale**: El proyecto usa Vite como bundler. Vitest reutiliza la configuración de Vite (plugins, path aliases, transforms) sin configuración adicional. API compatible con Jest, por lo que la curva de aprendizaje es mínima. Velocidad superior a Jest gracias al aprovechamiento del HMR de Vite.

**Alternativa descartada**: Jest requiere configuración extra de Babel/SWC para TypeScript + JSX, y no aprovecha la infraestructura Vite ya existente.

### 2. MSW (Mock Service Worker) para mocks de API en frontend

**Decisión**: MSW para interceptar llamadas a la API en tests de componentes y en desarrollo.

**Rationale**: MSW intercepta a nivel de red (no a nivel de módulo), por lo que los tests prueban el código real de fetching sin modificarlo. Los mismos handlers se pueden reutilizar en desarrollo para trabajar sin backend. Compatible con Vitest, Playwright y el navegador.

**Alternativa descartada**: Mockear `fetch` directamente con `vi.mock` acopla los tests a la implementación del cliente HTTP.

### 3. Playwright sobre Cypress para E2E

**Decisión**: Playwright para pruebas end-to-end.

**Rationale**: Playwright es más rápido (ejecuta en paralelo por defecto), soporta múltiples browsers (Chromium, Firefox, WebKit) con una sola API, y tiene soporte nativo para esperar por estados de red y DOM sin timeouts arbitrarios. La API moderna con `async/await` es más intuitiva.

**Alternativa descartada**: Cypress es más lento, soporta un solo browser por run, y su arquitectura de iframe tiene limitaciones con ciertas operaciones de red.

### 4. Estructura de tests backend: `unit/` + `integration/` en `tests/`

**Decisión**: Reestructurar `backend/tests/` en subdirectorios por tipo.

```
backend/tests/
├── conftest.py          # fixtures globales
├── factories/           # factory-boy factories
│   └── content.py
├── unit/                # tests de servicios puros (sin I/O)
│   ├── test_content_service.py
│   ├── test_schedule_service.py
│   ├── test_analytics_service.py
│   └── test_strategy_service.py
└── integration/         # tests de API con TestClient + mocks
    ├── test_health.py
    └── test_content_api.py
```

**Rationale**: Los tests de servicios son puro Python (sin FastAPI, sin HTTP), y los de integración usan TestClient. Separarlos permite correr cada capa independientemente y facilita el mantenimiento.

### 5. respx para mockear HTTP en backend

**Decisión**: `respx` para interceptar llamadas `httpx` en tests de integración.

**Rationale**: El backend usa `httpx` para llamadas a APIs externas (platform APIs, LLM). `respx` se integra nativamente con `httpx` y permite definir mocks declarativos a nivel de request, sin parchear módulos. Compatible con pytest-asyncio.

### 6. Coverage mínima por capa

| Capa | Target |
|------|--------|
| Backend services (unit) | 90% |
| Backend API (integration) | 80% |
| Frontend utils/hooks | 80% |
| Frontend components | 70% |
| E2E (flujos críticos) | 3 happy paths mínimo |

### 7. Ubicación de tests frontend: colocados junto al código

**Decisión**: `Component.test.tsx` junto a `Component.tsx`, no en directorio separado.

**Rationale**: Facilita encontrar y mantener tests al modificar un componente. Vitest descubre automáticamente `*.test.tsx`. Los archivos E2E van en `e2e/` separado porque prueban flujos cross-cutting.

## Risks / Trade-offs

- **Playwright requiere browsers instalados** → Mitigation: `playwright install` en setup; en Docker se instalan en la imagen
- **MSW en Vitest requiere `jsdom` o `happy-dom`** → Usar `jsdom` como environment (ya disponible en Vitest)
- **Los tests de CrewAI (crews/) no se pueden testear sin LLM** → Los crews no se testean directamente; se testean los servicios que llaman. El wiring CrewAI → Service se testa con mocks del LLM
- **Reestructurar `tests/` puede romper paths en pytest.ini** → Actualizar `testpaths` en pyproject.toml

## Open Questions

- ¿Targets de cobertura mínima para bloquear PR? (sugerencia: 80% backend, 70% frontend)
- ¿Playwright en modo headless siempre, o headed para debug local?
