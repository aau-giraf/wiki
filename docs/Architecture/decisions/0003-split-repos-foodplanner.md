# 3. Split Repos for Foodplanner

**Date:** 2025-01-01

**Status:** accepted

## Context

Foodplanner frontend (Flutter) and backend (.NET) have different CI pipelines, dependencies, and deployment targets.

## Decision

Separate repos (`foodplanner` for frontend, `foodplanner-api` for backend). VTA keeps its monorepo since frontend and backend are tightly coupled (SignalR real-time sync).

## Consequences

Independent CI/CD per component. Separate versioning. API contract changes require coordinated PRs across repos.
