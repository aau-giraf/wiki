# 2. DB-First for VTA

**Date:** 2025-01-01

**Status:** accepted

## Context

VTA's database schema predates the current .NET backend. Schema changes are designed in MySQL directly by developers familiar with SQL.

## Decision

Use DB-first with `dotnet ef dbcontext scaffold` instead of code-first migrations. `mysql_schema.sql` is the schema source of truth.

## Consequences

Schema changes are explicit SQL. No migration conflicts. Developers must scaffold after schema changes. Can't use EF migration tooling for rollbacks.
