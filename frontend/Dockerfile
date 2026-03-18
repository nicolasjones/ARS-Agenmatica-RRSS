# ---- Base ----
FROM node:22-slim AS base

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm ci

COPY . .

# ---- Dev ----
FROM base AS dev

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

# ---- Build ----
FROM base AS build

RUN npm run build

# ---- Prod ----
FROM nginx:alpine AS prod

COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD wget -qO- http://localhost/ || exit 1
