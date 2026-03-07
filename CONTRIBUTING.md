# Contributing to the GIRAF Wiki

For general workflow and guidelines, see the [organization CONTRIBUTING.md](https://github.com/aau-giraf/.github/blob/main/CONTRIBUTING.md).

## Development Setup

### Prerequisites

- Python 3.x
- pip

### Local Development

```bash
pip install mkdocs-material mkdocs-awesome-pages-plugin
mkdocs serve                  # Dev server at localhost:8000
```

### Page Conventions

- Each section has an `index.md` as its landing page
- Use `.pages` files to control navigation order
- Place images in `docs/resources/`

### Creating Pages

1. Add your `.md` file in the appropriate section under `docs/`
2. Update the section's `.pages` file to include it
3. Verify with `mkdocs build` — should produce zero warnings
