# Scrum in GIRAF

This page explains how GIRAF implements Scrum, framed through the three pillars of empiricism. For the complete Scrum framework definition, see the official [Scrum Guide](https://scrumguides.org/scrum-guide.html).

## The Three Pillars of Empiricism

Scrum is founded on empiricism—making decisions based on observation and experience rather than upfront planning. Three pillars support this approach. For more details, see [The Three Pillars of Empiricism](https://www.scrum.org/resources/blog/three-pillars-empiricism-scrum) on Scrum.org.

### Transparency

All aspects of work must be visible to those responsible for the outcome.

**How GIRAF implements transparency:**

- GitHub Issues and Projects provide visibility into all work items
- Scrum of Scrums ensures information flows between PO/SM groups and development teams
- Sprint Backlog is shared with all team members before Sprint Planning
- Pull requests and code reviews make code changes visible to the entire team

### Inspection

Scrum artifacts and progress must be frequently inspected to detect problems early.

**How GIRAF implements inspection:**

- Sprint Planning: Teams inspect and estimate issues collaboratively
- Sprint Review: Teams demonstrate completed work and gather feedback
- Pull Request Reviews: Code is inspected before merging
- PO group conducts usability testing to inspect product quality

### Adaptation

When inspection reveals issues, the process or product must be adjusted promptly.

**How GIRAF implements adaptation:**

- Sprint Retrospective: Teams reflect on what went well and what to improve
- Process changes are communicated at the start of each Sprint Planning
- Sprint Backlog can be adjusted based on Planning Poker outcomes
- Teams can request additional issues if capacity allows

## Sprint Events

GIRAF uses a 2-week sprint cycle. The following events occur each sprint:

### Sprint Planning

See the [Process](process.md) page for detailed Sprint Planning procedures including Planning Poker estimation.

### Sprint Review

The Sprint Review occurs at the end of each sprint to inspect the increment and adapt the Product Backlog. See the [Scrum Guide](https://scrumguides.org/scrum-guide.html#sprint-review) for the official definition.

**Expected Duration:** Max 2 hours (adjusted for 2-week sprint).

**Purpose:**

- Development teams demonstrate completed work
- PO group and stakeholders provide feedback
- Product Backlog is updated based on learnings

**Participants:** All GIRAF team members and available stakeholders.

### Sprint Retrospective

The Sprint Retrospective occurs after the Sprint Review to inspect the team's process and create a plan for improvements. See the [Scrum Guide](https://scrumguides.org/scrum-guide.html#sprint-retrospective) for the official definition.

**Expected Duration:** Max 1.5 hours (adjusted for 2-week sprint).

**Purpose:**

- Identify what went well during the sprint
- Identify what could be improved
- Create actionable improvements for the next sprint

**Format:** Each team conducts their own retrospective. The SM group then aggregates insights and communicates process changes at the next Sprint Planning.
