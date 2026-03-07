# Weekplanner

Schedule management monorepo — .NET 8 backend + Expo/React Native frontend.

## Prerequisites

- Docker
- .NET 8 SDK
- Node.js 18+
- A running [giraf-core](https://github.com/aau-giraf/giraf-core) instance

## Backend

```bash
docker compose up             # API on :5171 + PostgreSQL 15
dotnet test backend/          # Run tests
```

The backend stores only `Activity` entities. It validates that citizens, grades, and pictograms exist in Core via `GirafCoreClient` before creating activities.

## Frontend

```bash
cd frontend
npm install
npx expo start                # Dev server
npm run test                  # Jest (watch mode)
npm run test-ci               # Jest (CI + coverage)
npm run lint                  # ESLint
```

The frontend calls both the Weekplanner API (for activities) and the Core API (for users, citizens, pictograms) directly.

## Architecture

- **Activity-only backend** — all shared entities managed by Core
- **JWT auth** — validates Core-issued JWTs via shared `JWT_SECRET`
- **Claim-based authorization** — reads `org_roles` from JWT, zero DB queries for auth
- **Core validation** — `GirafCoreClient` checks citizens/grades/pictograms exist before mutations

## Tech Stack

| Component | Stack |
|-----------|-------|
| Backend | .NET 8, PostgreSQL 15 |
| Frontend | Expo, React Native, TypeScript |
| State | TanStack Query |
| Routing | Expo Router (file-based) |
| Forms | React Hook Form + Zod |

See the [Architecture overview](../Architecture/index.md) for how Weekplanner fits into the GIRAF ecosystem.
