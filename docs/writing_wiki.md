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

The wiki can be run locally by doing the following in a terminal:

1. Install Python 3.
2. Check that pip is using python3 with ``pip -V``.
    * if not, check ``pip3 -V``
3. Set up a virtual environment (steps assume that your current dir is project root) 
      1. Install virtualenv with ``pip install virtualenv``
            - else ``pip3 install virtualenv``
      2. run ``python -m venv venv``
            - else ``python3 -m venv venv``
      3. source the virtual environment
            - Linux:    ``source venv/bin/activate`` 
            - Windows:  ``.\venv\Scripts\activate.bat``
4. Install plugins with ``pip install -r requirements.txt`` (if pip is using python3)
    * else ``pip3 install -r requirements.txt``
5. Start local server with ``mkdocs serve``

You should now be able to access the wiki at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
Step 1 to 3 only has to be done the first time, unless new plugins have been added (if so do steop 3 again).



## Important files and directories

```
.
├── .github
│   └── workflows
│       └── page-build.yml      # GH Actions configuration
├── docs                        # Contains all wiki files
│   └── extra                   # Contains extra css as well as the logo. NO Markdown files here!
├── mkdocs.yml                  # MkDocs configuration file
└── requirements.txt            # Contains python dependencies
```

## Writing pages

Pages are written in Markdown. 
A guide for writing Markdown can be seen [here](https://www.markdownguide.org/basic-syntax/).

All Markdown files have to be in the `docs` folder. 
Every folder in the `docs` folder creates a new section.
If a folder contains a file named index.md, that file will be the main page of the section.

Since changes to the wiki are tracked by GitHub, using one line per sentence, will make it easier to keep track of.
This means that every time you finish a sentence with a dot, you should change line.
This cannot be seen in the render.

### Common mistakes

MkDocs can be a bit more strict in regards to its Markdown syntax, compared to GitHub.
This means that some mistakes happens often, since they work in some Markdown renders but not in MkDocs.
Here are some examples:

### Only one level one header

MkDocs only supports one level one header (`# header`) per page.
If another level one header is present, the rest of the page won't be shown in the overview.

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
