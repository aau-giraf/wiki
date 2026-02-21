# Architecture Overview

A guide for new students to understand how the GIRAF ecosystem fits together.

## The Big Picture

GIRAF apps share a common platform so they don't each reinvent users, authentication, or pictograms. The architecture has three layers:

```
┌─────────────────────────────────────────────────────────────────┐
│                         Mobile Apps                             │
│   Weekplanner              VTA                Foodplanner       │
│   (Expo/React Native)      (Flutter)          (Flutter)         │
└──────┬──────────────────────┬───────────────────┬──────────────┘
       │                      │                   │
       ▼                      ▼                   ▼
┌──────────────┐   ┌──────────────────┐   ┌──────────────┐
│ Weekplanner  │   │ VTA Backend      │   │ Foodplanner  │
│ Backend      │   │ (.NET + SignalR) │   │ Backend      │
│ (.NET 8)     │   │                  │   │ (.NET)       │
│              │   │                  │   │              │
│ Activities,  │   │ Boards,          │   │ Meals,       │
│ Schedules    │   │ Artefacts        │   │ Food items   │
└──────┬───────┘   └──────┬───────────┘   └──────┬───────┘
       │                  │                      │
       │    users, orgs, citizens, pictograms    │
       ▼                  ▼                      ▼
┌─────────────────────────────────────────────────────────────────┐
│                       Shared Services                           │
│                                                                 │
│  ┌───────────────────────────────────┐  ┌────────────────────┐  │
│  │ GIRAF Core (Django + PostgreSQL)  │  │ GIRAF AI (FastAPI) │  │
│  │                                   │  │                    │  │
│  │ Auth/JWT, Users, Orgs, Citizens,  │  │ Image generation,  │  │
│  │ Grades, Pictograms, Invitations   │  │ Text-to-speech     │  │
│  └───────────────────────────────────┘  └────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Shared Services

### GIRAF Core

The single source of truth for everything shared across apps:

- **Users and authentication** — one account works across all GIRAF apps
- **Organizations** — schools and institutions that group users together
- **Citizens** — the children who use GIRAF
- **Pictograms** — the visual symbols used throughout the platform
- **Invitations** — how new users join an organization

When a user logs in, Core issues a JWT that all app backends trust. Apps never need their own user databases.

**Repository:** [giraf-core](https://github.com/aau-giraf/giraf-core)

### GIRAF AI

A shared microservice for AI capabilities that any app can use:

- **Image generation** — creating pictograms from text descriptions
- **Text-to-speech** — reading pictogram labels aloud

Swapping AI providers happens in one place rather than across every app.

**Repository:** [giraf-ai](https://github.com/aau-giraf/giraf-ai)

---

## App Backends

Each app has its own backend that stores **only its own domain data**. When it needs shared data (like checking whether a citizen exists), it asks Core.

| App | What its backend stores | Repository |
|-----|------------------------|------------|
| **Weekplanner** | Activities and schedules | [weekplanner](https://github.com/aau-giraf/weekplanner) |
| **VTA** | Communication boards and artefact configs | [visual-tangible-artefacts](https://github.com/aau-giraf/visual-tangible-artefacts) |
| **Foodplanner** | Meal plans and food items | [foodplanner](https://github.com/aau-giraf/foodplanner) / [foodplanner-api](https://github.com/aau-giraf/foodplanner-api) |

---

## How Authentication Works

All backends share a `JWT_SECRET` with Core. When a user logs in through Core, the JWT they receive contains an `org_roles` claim that tells backends what role the user has in each organization — no extra API calls needed for authorization.

```
1. User logs in via any app
2. App calls Core → gets JWT with org_roles: {"1": "owner", "5": "member"}
3. App sends JWT to its own backend
4. Backend validates JWT locally using shared secret
5. Backend reads org_roles from the token to authorize the request
```

---

## What This Means for New Teams

1. **You'll work on one app** — each team typically owns one app and its backend
2. **Core is shared infrastructure** — you'll use it, but probably won't change it
3. **Authentication is handled for you** — your backend validates tokens from Core
4. **Pictograms and users already exist** — you query Core for them

For setup instructions and technical details, see the README in each repository at [github.com/aau-giraf](https://github.com/aau-giraf).
