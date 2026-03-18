# Frontend Domain

## Overview

Dashboard React + Tailwind para gestionar el sistema de agentes de redes sociales. Consume la API FastAPI.

## Pages

### Dashboard (`/`)
- Vista general: métricas clave, publicaciones recientes, agenda del día
- Cards con KPIs por plataforma
- Timeline de actividad de agentes

### Content (`/content`)
- Solicitar generación de contenido
- Lista de contenido generado (filtrable por plataforma, estado)
- Editor para revisar/modificar antes de publicar
- Preview por plataforma

### Calendar (`/calendar`)
- Vista calendario (mes/semana/día)
- Drag & drop para reprogramar
- Indicadores de horarios óptimos

### Analytics (`/analytics`)
- Gráficos de rendimiento (engagement, reach, followers)
- Comparativas entre plataformas
- Top/worst performing posts
- Reports generados por AnalyticsAgent

### Engagement (`/engagement`)
- Feed de menciones y comentarios
- Respuestas sugeridas por EngagementAgent
- Sentiment overview

### Settings (`/settings`)
- Conexión de plataformas (OAuth flow)
- Configuración de agentes
- Brand voice / estilo del artista
- Preferencias de publicación

## Tech Details

- React 19 + TypeScript
- Tailwind CSS 4
- Vite como bundler
- React Router para navegación
- Fetch/axios para API calls
- Recharts o similar para gráficos
