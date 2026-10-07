# ADR-001: Transition to SSR and Containers

- **Status:** Accepted
- **Date:** 2026-10-07

## Context

The blog was previously built as static HTML. The DevOps lab requires a
long-running application server that can expose operational health probes and
structured request logs for a container orchestrator.

## Decision

- Use Astro's `server` output mode with the official `@astrojs/node` adapter in
  standalone mode. The production build is served by
  `node ./dist/server/entry.mjs`.
- Expose `GET /api/health` with the application status, process uptime, and an
  ISO-8601 timestamp.
- Expose `GET /api/health/live` as a liveness probe and
  `GET /api/health/ready` as a readiness probe. A successful response indicates
  the server can handle requests; there are no external dependencies to probe.
- Log each handled request as a JSON object with timestamp, severity, route,
  method, response status, and latency.

## Consequences

- Pages are rendered on demand by the Node.js server rather than emitted as
  standalone HTML files.
- The application must be deployed as a running Node.js process and its
  container must expose the configured port.
- Orchestrators can independently check liveness and readiness, and log
  aggregation tools can filter request events by their JSON fields.

## Local verification

```sh
npm run build
```

In PowerShell, start the standalone server with:

```powershell
$env:HOST = '0.0.0.0'
$env:PORT = '4321'
node .\dist\server\entry.mjs
```

In a second terminal, verify the health endpoints:

```powershell
curl.exe -i http://localhost:4321/api/health
curl.exe -i http://localhost:4321/api/health/live
curl.exe -i http://localhost:4321/api/health/ready
```
