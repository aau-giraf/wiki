# Branch Strategy

GIRAF uses trunk-based development. Each repo has a single default branch that represents the latest stable code.

## Branch Naming

| Prefix | Use |
|--------|-----|
| `feat/123-description` | New features |
| `fix/123-description` | Bug fixes |
| `docs/description` | Documentation changes |
| `chore/description` | Maintenance, CI, dependencies |

Include the issue number when one exists.

## Default Branches

| Repository | Default Branch |
|------------|----------------|
| giraf-core | `main` |
| weekplanner | `main` |
| visual-tangible-artefacts | `dev-main` |
| foodplanner | `staging` |
| foodplanner-api | `staging` |
| wiki | `master` |
| deploy | `main` |

## Workflow

1. **Fork** the repository
2. **Create a feature branch** from the default branch
3. **Open a PR** against the default branch
4. **Squash merge** after approval

No release branches. No develop/staging intermediate branches for new work.

## Commit Messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat: add citizen validation`
- `fix: handle null pictogram ID`
- `docs: update API examples`
- `chore: bump .NET to 8.0.4`
