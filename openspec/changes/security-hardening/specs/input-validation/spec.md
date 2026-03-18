## ADDED Requirements

### Requirement: String fields have max_length constraints
All user-facing string fields in Pydantic schemas SHALL define `max_length` to prevent oversized payloads.

#### Scenario: Topic within limit accepted
- **WHEN** a POST to `/api/v1/content/` includes `topic` with 500 characters
- **THEN** the request is accepted

#### Scenario: Topic exceeding limit rejected
- **WHEN** a POST to `/api/v1/content/` includes `topic` with 1001 characters
- **THEN** the response is 422 with validation error

#### Scenario: Tone exceeding limit rejected
- **WHEN** a POST to `/api/v1/content/` includes `tone` with 201 characters
- **THEN** the response is 422 with validation error

### Requirement: Error responses sanitized in production
Error responses SHALL NOT expose internal implementation details when `debug=False`. Only error code and a generic message SHALL be returned.

#### Scenario: Production error response is generic
- **WHEN** an `AppError` is raised with `debug=False`
- **THEN** the JSON response contains `error.code`
- **THEN** the JSON response contains a generic `error.message` (not the internal exception message)

#### Scenario: Development error response includes details
- **WHEN** an `AppError` is raised with `debug=True`
- **THEN** the JSON response contains the full `error.code` and `error.message`

### Requirement: Unhandled exceptions return 500 without stack traces
Unhandled exceptions SHALL return a 500 response with a generic message. Stack traces MUST only be logged server-side.

#### Scenario: Unhandled exception in production
- **WHEN** an unexpected exception occurs with `debug=False`
- **THEN** the response is `{"error": {"code": "INTERNAL_ERROR", "message": "An unexpected error occurred"}}`
- **THEN** the full traceback is logged via structlog
