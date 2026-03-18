## ADDED Requirements

### Requirement: FastAPI security headers middleware
The backend SHALL add a middleware that sets security headers on every HTTP response.

#### Scenario: Security headers present on API response
- **WHEN** a client makes any request to the API
- **THEN** the response includes `X-Content-Type-Options: nosniff`
- **THEN** the response includes `X-Frame-Options: DENY`
- **THEN** the response includes `Referrer-Policy: strict-origin-when-cross-origin`
- **THEN** the response includes `X-XSS-Protection: 1; mode=block`

### Requirement: CORS uses explicit methods and headers
The CORS middleware SHALL specify explicit allowed methods and headers instead of wildcards.

#### Scenario: Only specified methods are allowed
- **WHEN** a preflight request asks for `OPTIONS` with method `PATCH`
- **THEN** the CORS response does not include `PATCH` in `Access-Control-Allow-Methods`

#### Scenario: Allowed methods are explicit
- **WHEN** a preflight request asks for `POST`
- **THEN** the CORS response includes `POST` in `Access-Control-Allow-Methods`
- **THEN** `Access-Control-Allow-Methods` contains only `GET, POST, PUT, DELETE`

### Requirement: Nginx security hardening
The Nginx config SHALL include security directives that prevent information leakage and common attacks.

#### Scenario: Server version hidden
- **WHEN** a client makes a request to the frontend
- **THEN** the `Server` header does not include the Nginx version

#### Scenario: Security headers on static files
- **WHEN** a client requests a frontend page
- **THEN** the response includes `X-Frame-Options: SAMEORIGIN`
- **THEN** the response includes `X-Content-Type-Options: nosniff`
- **THEN** the response includes `Referrer-Policy: strict-origin-when-cross-origin`
