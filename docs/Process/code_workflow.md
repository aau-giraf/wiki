# Code Workflow

This page covers the complete workflow from picking up an issue to merging your code.

## Overview

```
Issue → Branch → Code → Pull Request → Review → Merge
```

---

## 1. Working with Issues

### Finding an Issue

Issues are managed in [GitHub Issues](https://github.com/orgs/aau-giraf/repositories) and [GitHub Projects](https://github.com/orgs/aau-giraf/projects/).

During sprints, issues are assigned to teams by the SM group after Sprint Planning. If you need more work:

1. Find an unassigned issue in the Sprint Backlog
2. Ask the SM group for approval
3. Prefer high-priority issues for better approval chances

### Creating an Issue

If you find a bug or have a feature idea:

1. Go to the repository's Issues tab (e.g., [foodplanner issues](https://github.com/aau-giraf/foodplanner/issues))
2. Click "New issue"
3. Choose Bug Report or Task Creation Request
4. Follow the template — don't delete the headers
5. Add appropriate labels
6. Inform the PO group so they can prioritize

---

## 2. Branching

GIRAF follows [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).

### During Sprints

Create feature branches from `develop` (or `staging` for some repos):

```bash
git checkout develop
git checkout -b feature/123
```

**Naming:** `feature/XX` where XX is the issue number.

### During Release Preparation

Create fix branches from the release branch:

```bash
git checkout release/2024s1r1
git checkout -b releasefix/456
```

---

## 3. Pull Requests

When your work is complete, create a pull request.

### Before Creating a PR

Ensure your code:
- Addresses only one issue (one PR per user story)
- Is fully tested (removing any functionality should break a test)
- Is reachable in the application

### Creating the PR

1. Go to the repository's Pull Requests tab
2. Click "New pull request"
3. Select base branch:
   - `develop` or `staging` during sprints
   - `release/*` during release preparation
4. Select your feature branch
5. Title: `Feature 123` or `Feature 123: Short description`
6. Description: Use `closes #123` or `fixes #123` to auto-link and close the issue

---

## 4. Code Review

**Reviewing PRs is the highest priority for developers.**

### As a Reviewer

1. Open the PR and go to "Files changed"
2. Review each file for:
   - Deprecated or unnecessary code
   - Non-optimized implementations
   - Formatting issues
   - Missing tests
3. Add comments or suggestions on specific lines (click the blue + icon)
4. Submit your review:
   - **Request changes** if issues need fixing
   - **Approve** if the code is ready to merge

### As an Author

- Respond to all feedback
- Make requested changes and push updates
- Request re-review after addressing comments

---

## 5. Merging

Once approved:
1. Ensure CI checks pass
2. Merge the PR (squash or regular merge per repo conventions)
3. Delete the feature branch
4. Verify the issue is closed

---

## Quick Reference

| I want to... | Command/Action |
|--------------|----------------|
| Start work on issue #42 | `git checkout -b feature/42` |
| Link PR to issue | Write `closes #42` in PR description |
| Request review | Assign reviewers in PR sidebar |
| See all open PRs | Go to repository → Pull Requests tab |
