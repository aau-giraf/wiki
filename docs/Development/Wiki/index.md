# Overview

This section gives an overview of the Wiki repository. 
The wiki is written in [Markdown](https://daringfireball.net/projects/markdown/), and rendered using
[MkDocs](https://www.mkdocs.org/).

- [Running the Wiki locally](running_wiki.md)
- [Writing Pages for the Wiki](writing_wiki.md)

## Important Files and Directories

```bash
.
├── .github
│   └── workflows
│       ├── ci.yml              # GH Actions configuration for Continuous Integration
│       └── page-build.yml      # GH Actions configuration for building
├── docs                        # Contains all wiki files
│   └── extra                   # Contains extra css as well as the logo. NO Markdown files here!
├── mkdocs.yml                  # MkDocs configuration file
├── requirements.txt            # Contains python dependencies
└── run_mdl.bat                 # Batch file for running the Markdown linter locally (Windows only)
```