# Using the Wiki

## MkDocs

The wiki is built with [MkDocs](https://www.mkdocs.org/), using the
[Material theme](https://squidfunk.github.io/mkdocs-material/).

MkDocs is configured in the
[mkdocs.yml](https://github.com/aau-giraf/wiki/blob/master/mkdocs.yml) file.

The following plugins are used:

- [search](https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-search/)
- [awesome-pages](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin)
- [git-revision-date-localized](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin)

If more plugins are downloaded with pip, remember to add them to the `requirements.txt` file.
If any plugins need to be updated, change the version number for the plugin in the `requirements.txt` file.

### Running the wiki with MkDocs

First, install the newest version of [Python](https://www.python.org/downloads/).

Then, follow these steps (these steps are only necessary when running MkDocs **for the first time**):

1. Open a terminal in the root of the wiki project, or navigate to the root in the
   terminal.
1. Set up a virtual environment
    1. Install virtual environment with ``pip install virtualenv``.
    1. Run ``python -m venv venv``.
    1. Source the virtual environment.
        1. Linux:    ``source venv/bin/activate``
        1. Windows:  ``.\venv\Scripts\activate.bat``
1. Install MkDocs plugins by running ``pip install -r requirements.txt``.

Finally, the wiki can be hosted locally by running `mkdocs serve`.
The local server can then be accessed at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

After following these steps, the wiki can always be hosted by running `mkdocs serve` in the root of the project.
However, if any changes have been made to the `requirements.txt` file (added or updated plugins) step 3 must be done
again.

## markdownlint

During the semester of 2020E, a GitHub Action workflow using
[markdownlint](https://github.com/markdownlint/markdownlint) was set up for the wiki repository. 
This workflow serves as continuous integration for the repository, and is set up in the
[`ci.yml`](https://github.com/aau-giraf/wiki/blob/master/.github/workflows/ci.yml) file.

The rules used by the linter can be found 
[here](https://github.com/markdownlint/markdownlint/blob/master/docs/RULES.md).
Any exceptions to these rules are found or set up in the
[`.mdl_style.rb`](https://github.com/aau-giraf/wiki/blob/master/.mdl_style.rb) file. 

### Running markdownlint locally

First, install the newest version of [Ruby](https://www.ruby-lang.org/en/downloads/).

Second, install markdownlint by opening a terminal and running `gem install mdl`.

**IF**, `gem install mdl` will not work, clone the
[markdownlint repository](https://github.com/markdownlint/markdownlint) and then follow these steps:

1. Open a terminal in the root of the cloned markdownlint repository, or navigate to the root in the terminal, and run
   the following:
    1. `gem install rake`
    1. `gem install bundler`
    1. `rake install`
    
If either `gem` or `mdl` are not recognized, make sure that the `.\bin` of either is in the `PATH` environment variable. 

Finally, markdownlint can be run locally by following these steps:

1. Open a terminal in the root of the wiki project, or navigate to the root in the terminal.
1. Depending on OS, run either:
    - Windows: `run_mdl.bat`
    - Mac/Linux: `mdl docs/`

After running it, markdownlint will report any Markdown issues, or it will report nothing indicating that all of the 
`.md` files follow the rules.

## Important Files and Directories

```bash
.
├── .github
│   └── workflows
│       └── page-build.yml      # GH Actions configuration
├── docs                        # Contains all wiki files
│   └── extra                   # Contains extra css as well as the logo. NO Markdown files here!
├── mkdocs.yml                  # MkDocs configuration file
└── requirements.txt            # Contains python dependencies
```

## Writing Pages

Pages are written in Markdown.
A guide for writing Markdown can be seen [here](https://www.markdownguide.org/basic-syntax/).

All Markdown files have to be in the `docs` folder.
Every folder in the `docs` folder creates a new section.
If a folder contains a file named index.md, that file will be the main page of
the section.

Since changes to the wiki are tracked by GitHub, using one line per sentence,
will make it easier to keep track of.
This means that every time you finish a sentence with a dot, you should change
line.
This cannot be seen in the render.

### Common mistakes

MkDocs can be a bit more strict in regards to its Markdown syntax, compared to
GitHub.
This means that some mistakes happens often, since they work in some Markdown
renders but not in MkDocs.
Here are some examples:

### Only one level one header

MkDocs only supports one level one header (`# header`) per page.
If another level one header is present, the rest of the page won't be shown in
the overview.

#### Missing blank lines

MkDocs requires elements to be preceded by blank lines.
This also means that headers should be proceded by blank lines before content.

<p style="color: darkred; font-weight: bold;">Wrong:</p>

```markdown
Some text
* List item
...
```

<p style="color: green; font-weight: bold;">Correct:</p>

```markdown
Some text

* List item
...
```

#### List indentation

MkDocs requires lists to use 4 spaces for indentation.

<p style="color: darkred; font-weight: bold;">Wrong:</p>

```markdown
* List item
  * List subitem
...
```

<p style="color: green; font-weight: bold;">Correct:</p>

```markdown
* List item
    * List subitem
```

### Custom title

File metadata is written using yaml-frontmatter.
As an example, a page's title can be specified.

```markdown
---
title: "Custom Title"
---

# Hello World
```

If `title` is not specified, the page is given the header's content.
In the above example that would be `Hello World` if the title was not specified
in the metadata.

### Arranging pages

Using *awesome-pages*, a `.pages` file can be created in every folder.
This can be used to arrange pages manually. As an example, the tabs are arranged
with the `.pages` file in the `docs` folder:

```yaml
arrange:
    - index.md
    - getting_started
    - ...               # puts all pages/sections not specified here
    - releases
```

## Building the pages

Everytime something is pushed to the ``master`` branch of the wiki, the GitHub
Actions workflow is run.
The workflow deploys the built pages to the ``gh-pages`` branch, which is set
to be the source of the GitHub Pages.
This is configured in the repository settings of the wiki repository.
