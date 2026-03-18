## 1. Secrets y Configuración

- [ ] 1.1 Crear `.env.example` en la raíz con todas las variables requeridas (DATABASE_URL, ANTHROPIC_API_KEY, OPENAI_API_KEY, CORS_ORIGINS, DEBUG, etc.) con valores placeholder
- [ ] 1.2 Crear `.env` a partir de `.env.example` con valores de desarrollo funcionales (postgres://postgres:postgres@localhost:5432/ars_agenmatica, etc.)
- [ ] 1.3 Refactorizar `backend/app/core/config.py`: eliminar defaults inseguros, usar `SecretStr` para API keys, hacer `database_url` requerido, agregar `cors_origins: str`
- [ ] 1.4 Actualizar `backend/app/main.py`: cargar CORS origins desde `settings.cors_origins`, usar métodos explícitos `["GET", "POST", "PUT", "DELETE"]`, headers explícitos `["Content-Type", "Authorization"]`
- [ ] 1.5 Actualizar `backend/app/main.py`: deshabilitar `docs_url`, `redoc_url`, `openapi_url` cuando `settings.debug is False`
- [ ] 1.6 Verificar que `pytest` pasa con la nueva configuración (tests usan env vars o fixtures)

## 2. Security Headers

- [ ] 2.1 Agregar middleware de security headers en `backend/app/main.py`: `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy: strict-origin-when-cross-origin`, `X-XSS-Protection: 1; mode=block`
- [ ] 2.2 Actualizar `frontend/nginx.conf`: agregar `server_tokens off` y headers de seguridad (`X-Frame-Options: SAMEORIGIN`, `X-Content-Type-Options: nosniff`, `Referrer-Policy`)
- [ ] 2.3 Escribir test de integración que verifique la presencia de security headers en respuestas de la API

## 3. Input Validation y Error Handling

- [ ] 3.1 Actualizar `backend/app/schemas/content.py`: agregar `Field(max_length=1000)` a `topic`, `Field(max_length=200)` a `tone`, `Field(max_length=500)` a `brand_voice`
- [ ] 3.2 Refactorizar error handler en `backend/app/main.py`: en producción retornar solo `code` + mensaje genérico, loggear detalle completo con structlog
- [ ] 3.3 Agregar handler para excepciones no capturadas que retorne 500 genérico y loggee traceback
- [ ] 3.4 Escribir tests unitarios para validación de campos (topic demasiado largo, tone demasiado largo)
- [ ] 3.5 Escribir test de integración para error sanitization (verificar que mensajes internos no se exponen)

## 4. Docker Hardening

- [ ] 4.1 Actualizar `backend/Dockerfile`: agregar `RUN useradd -m -u 1000 appuser` y `USER appuser` en stage `prod`
- [ ] 4.2 Actualizar `frontend/Dockerfile`: usar `USER nginx` en stage `prod`, ajustar permisos de directorios
- [ ] 4.3 Agregar `.env`, `.env.*`, `.git` a `backend/.dockerignore` y `frontend/.dockerignore`
- [ ] 4.4 Actualizar `docker-compose.yml`: reemplazar credenciales hardcodeadas con `${VARIABLES}`, agregar `env_file: .env`
- [ ] 4.5 Actualizar `docker-compose.prod.yml`: agregar `networks` (frontend-net, backend-net), `deploy.resources.limits` para backend y frontend
- [ ] 4.6 Verificar que `docker compose config` resuelve correctamente las variables con `.env`

## 5. Tests y Documentación

- [ ] 5.1 Actualizar tests existentes para funcionar con nueva config (agregar env vars en conftest.py o monkeypatch)
- [ ] 5.2 Ejecutar `pytest` completo y verificar ≥80% coverage
- [ ] 5.3 Ejecutar `npm run test` en frontend y verificar que pasa
- [ ] 5.4 Actualizar `CLAUDE.md` con nota sobre `.env` setup requerido
