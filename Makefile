.PHONY: dev prod build test test-backend test-frontend test-e2e clean logs

# Development
dev:
	docker compose up --build

dev-d:
	docker compose up --build -d

# Production
prod:
	docker compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d

# Build production images
build:
	docker compose -f docker-compose.yml -f docker-compose.prod.yml build

# Tests
test: test-backend test-frontend

test-backend:
	docker compose -f docker-compose.yml -f docker-compose.ci.yml run --rm backend-test

test-frontend:
	docker compose -f docker-compose.yml -f docker-compose.ci.yml run --rm frontend-test

test-e2e:
	docker compose -f docker-compose.yml -f docker-compose.ci.yml run --rm e2e-test

# Utilities
logs:
	docker compose logs -f

clean:
	docker compose -f docker-compose.yml -f docker-compose.prod.yml -f docker-compose.ci.yml down -v --rmi local --remove-orphans
