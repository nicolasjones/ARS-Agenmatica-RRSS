## Context

Auditoría de seguridad identificó vulnerabilidades en 3 capas: backend (config, API, error handling), frontend/Nginx (headers), y Docker (root user, network, secrets). El proyecto está en fase pre-producción — es el momento ideal para hardening antes de exponer a usuarios.

Archivos clave afectados:
- `backend/app/core/config.py` — settings con defaults inseguros
- `backend/app/main.py` — CORS, docs, error handler, middleware
- `backend/app/schemas/content.py` — sin validación de longitud
- `frontend/nginx.conf` — sin security headers
- `backend/Dockerfile`, `frontend/Dockerfile` — corren como root
- `docker-compose.yml`, `docker-compose.prod.yml` — credenciales hardcodeadas

## Goals / Non-Goals

**Goals:**
- Eliminar todas las vulnerabilidades CRITICAL y HIGH de la auditoría
- Establecer patrones de seguridad reutilizables para features futuros
- Mantener la experiencia de desarrollo simple (`.env.example` + `cp .env.example .env`)

**Non-Goals:**
- Implementar autenticación/autorización completa (JWT, API keys) — es un change separado
- Rate limiting — requiere Redis, será otro change
- SSL/TLS en Nginx — se configura por entorno de despliegue
- Auditoría de dependencias / supply chain — herramienta separada

## Decisions

### 1. Secrets management via `.env` + Pydantic validation

Approach: Pydantic `BaseSettings` ya lee env vars. Cambiar defaults inseguros a campos requeridos. Crear `.env.example` como documentación.

- `database_url`: sin default → falla al startup si no se configura
- API keys: usar `SecretStr` de Pydantic → nunca se loggean accidentalmente
- Compose files: referenciar `${VAR}` con `.env` file via `env_file` directive

_Alternativa descartada_: Docker secrets — overkill para stage actual, añade complejidad.

### 2. Security headers como middleware FastAPI + Nginx

Backend: middleware HTTP que agrega headers en cada response. Esto cubre tanto API directa como a través de Nginx.

Nginx: `server_tokens off` + headers de seguridad estáticos. Cubre el frontend estático.

No se usa un proxy/WAF externo — añade complejidad innecesaria para stage actual.

### 3. Error sanitization por environment

- `debug=True`: error responses incluyen `code` + `message` (desarrollo)
- `debug=False`: error responses solo incluyen `code` + mensaje genérico (producción)
- Siempre loggear detalle completo server-side via structlog

### 4. Non-root containers con user `appuser`

Crear usuario `appuser` (UID 1000) en ambos Dockerfiles. Usar `USER appuser` antes del `CMD`.

Para Nginx: usar `nginx` user existente en alpine, ajustar permisos de dirs.

### 5. Network isolation con Docker networks

Crear dos redes: `frontend-net` y `backend-net`.
- `postgres` → solo `backend-net`
- `backend` → ambas redes
- `frontend` → solo `frontend-net`

Esto evita que frontend acceda directamente a postgres.

### 6. CORS configurable por environment

`CORS_ORIGINS` como env var (comma-separated). Default a string vacío en prod (falla si no se configura). En `.env.example`: `CORS_ORIGINS=http://localhost:5173`.

Métodos y headers explícitos (no wildcards).

## Risks / Trade-offs

- **[Breaking change en config]** → Developers existentes necesitan crear `.env` file. Mitigado con `.env.example` + mensaje de error claro al startup.
- **[CSP puede romper funcionalidad]** → Usar CSP permisivo inicialmente (`default-src 'self'; style-src 'self' 'unsafe-inline'`), iterar después.
- **[Non-root puede romper permisos]** → Testeado con volumes y permisos de archivos. Dev stage mantiene root para flexibilidad.
