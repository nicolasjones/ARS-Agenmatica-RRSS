## Why

Una auditoría de seguridad reveló 3 vulnerabilidades CRITICAL, 7 HIGH y 8 MEDIUM en el proyecto. Los problemas principales son: credenciales hardcodeadas en código y compose files, endpoints sin autenticación ni validación de input, ausencia de security headers, CORS permisivo, y containers corriendo como root. Estos deben resolverse antes de cualquier despliegue.

## What Changes

- **BREAKING** Mover credenciales de BD y API keys a `.env` files, eliminar defaults inseguros de `config.py`
- Agregar security headers middleware en FastAPI (X-Frame-Options, HSTS, CSP)
- Deshabilitar `/docs` y `/redoc` cuando `debug=False`
- Restringir CORS: métodos y headers explícitos, origins desde env var
- Agregar validación de longitud en schemas Pydantic (`max_length` en campos string)
- Sanitizar respuestas de error en producción (no exponer mensajes internos)
- Agregar `USER` no-root en Dockerfiles (backend y frontend)
- Agregar security headers en Nginx (`server_tokens off`, `X-Frame-Options`, etc.)
- Agregar `.env` a `.dockerignore` de ambos servicios
- Agregar network isolation en Docker Compose (separar frontend de postgres)
- Agregar resource limits en `docker-compose.prod.yml`
- Crear `.env.example` como template documentado

## Capabilities

### New Capabilities
- `security-config`: Gestión segura de secrets y configuración (env vars, .env files, SecretStr, validación al startup)
- `security-headers`: Security headers HTTP en backend (middleware FastAPI) y frontend (Nginx hardening)
- `input-validation`: Validación y sanitización de inputs en schemas y respuestas de error

### Modified Capabilities
- `docker-prod`: Agregar USER no-root, network isolation, resource limits, `.env` excluido de build context
- `docker-dev`: Agregar `.env` file support, excluir `.env` de .dockerignore

## Impact

- **Backend**: `app/core/config.py`, `app/main.py`, `app/schemas/content.py`, `app/core/errors.py`
- **Frontend/Nginx**: `frontend/nginx.conf`
- **Docker**: `backend/Dockerfile`, `frontend/Dockerfile`, `docker-compose.yml`, `docker-compose.prod.yml`, `backend/.dockerignore`, `frontend/.dockerignore`
- **Root**: `.env.example`, `.gitignore`
- **Dependencias**: Ninguna nueva
- **Breaking**: Apps que dependan de defaults vacíos en config fallarán al startup hasta configurar env vars
