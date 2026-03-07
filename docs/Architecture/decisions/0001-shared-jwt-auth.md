# 1. Shared JWT Auth

**Date:** 2025-01-01

**Status:** accepted

## Context

Multiple app backends need to authorize requests from users who authenticate with Core. Calling Core on every request adds latency and a single point of failure.

## Decision

Core issues JWTs with an `org_roles` claim. All backends validate locally using a shared `JWT_SECRET` (HS256). Role hierarchy: owner > admin > member.

## Consequences

Backends authorize without network calls. Adding a new backend only requires the shared secret. Revoking access requires token expiry (no instant revocation). Secret rotation requires coordinated deployment.
