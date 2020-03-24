---
title: "Editing the Wiki"
---

# Editing the wiki

## MkDocs

The wiki is built with [MkDocs](https://www.mkdocs.org/), using the [Material theme](https://squidfunk.github.io/mkdocs-material/).

MkDocs is configured in the [mkdocs.yml](https://github.com/aau-giraf/wiki/blob/master/mkdocs.yml) 

The following plugins are used:

* search
* [awesome-pages](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin)
* [git-revision-date-localized](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin)

If more plugins are downloaded with pip, remember to add them to ``requirements.txt``

### Running locally

The wiki can be run locally by doing the following:

* Install python 3
    * check that pip is using python3 with ``pip -V``
    * if not, check ``pip3 -V``
* ``pip install -r requirements.txt`` (if pip is using python3)
    * else ``pip3 install -r requirements.txt``
* ``mkdocs serve``



## Important files and directories

```
.
├── .github
│   └── workflows
│       └── page-build.yml      # GH Actions configuration
├── docs                        # Contains all wiki files
│   └── extra                   # Contains extra css as well as the logo
├── mkdocs.yml                  # MkDocs configuration file
└── requirements.txt            # Contains python dependencies
```

## Writing pages

Pages are written in Markdown. 
A guide for writing Markdown can be seen [here](https://www.markdownguide.org/basic-syntax/).

All Markdown files have to be in the `docs` folder. 
Every folder in the `docs` folder creates a new section.
If a folder contains a file named index.md, that file will be the main page of the section.

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
In the above example that would be `Hello World` if the title was not specified in the metadata

### Arranging pages

Using *awesome-pages*, a `.pages` file can be created in every folder. 
This can be used to arrange pages manually. As an example, the tabs are arranged with the `.pages` file in the `docs` folder:

```yaml
arrange:
    - index.md
    - getting_started
    - ...               # puts all pages/sections not specified here
    - releases
```


## Building the pages

Everytime something is pushed to the ``master`` branch of the wiki, the GitHub Actions workflow is run.
The workflow deploys the built pages to the ``gh-pages`` branch, which is set to be the source of the GitHub Pages.
This is configured in the repository settings of the wiki repository.