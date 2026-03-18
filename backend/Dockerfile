# ---- Base ----
FROM python:3.11-slim AS base

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml .

# ---- Dev ----
FROM base AS dev

RUN uv pip install --system -e ".[dev]"

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# ---- Prod ----
FROM base AS prod

RUN uv pip install --system .

COPY . .

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/api/v1/health')" || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
