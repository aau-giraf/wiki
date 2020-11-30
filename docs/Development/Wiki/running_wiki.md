# Running the Wiki locally

This page describes how to run the wiki in order to properly edit it.
It also decribes how to use the markdown linter locally, in order to catch any potential issues before the GitHub
Actions does.

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

### Running the Wiki with MkDocs

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

After following these steps, the wiki can always be hosted by sourcing `venv` again and then running `mkdocs serve` in
the root of the project.
However, if any changes have been made to the `requirements.txt` file (added or updated plugins) step 3 must be done
again after sourcing `venv`.

## Markdownlint

During the semester of 2020E, a GitHub Action workflow using
[Markdownlint](https://github.com/markdownlint/markdownlint) was set up for the wiki repository. 
This workflow serves as continuous integration for the repository, and is set up in the
[`ci.yml`](https://github.com/aau-giraf/wiki/blob/master/.github/workflows/ci.yml) file.

The rules used by the linter can be found 
[here](https://github.com/markdownlint/markdownlint/blob/master/docs/RULES.md).
Any exceptions to these rules are found or set up in the
[`.mdl_style.rb`](https://github.com/aau-giraf/wiki/blob/master/.mdl_style.rb) file. 

### Running Markdownlint locally

First, install the newest version of [Ruby](https://www.ruby-lang.org/en/downloads/).

Second, install Markdownlint by opening a terminal and running `gem install mdl`.

**IF**, `gem install mdl` will not work, clone the
[Markdownlint repository](https://github.com/markdownlint/markdownlint) and then follow these steps:

1. Open a terminal in the root of the cloned Markdownlint repository, or navigate to the root in the terminal, and run
   the following:
    1. `gem install rake`
    1. `gem install bundler`
    1. `rake install`
    
If either `gem` or `mdl` are not recognized, make sure that the `.\bin` of either is in the `PATH` environment variable. 

Finally, Markdownlint can be run locally by following these steps:

1. Open a terminal in the root of the wiki project, or navigate to the root in the terminal.
1. Depending on OS, run either:
    - Windows: `run_mdl.bat`
    - Mac/Linux: `mdl docs/`

After running it, Markdownlint will report any Markdown issues, or it will report nothing indicating that all of the 
`.md` files follow the rules.