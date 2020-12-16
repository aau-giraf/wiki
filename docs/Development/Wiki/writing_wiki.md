# Writing Pages for the Wiki

This page gives guidelines for how to write pages for the wiki.

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

Additionally, lines should be kept limited to 120 characters each. 
If a sentence exceeds this limit a linebreak should be added, so the sentence occupies two lines instead of one.

### Common Mistakes

MkDocs can be a bit more strict in regard to its Markdown syntax, compared to
GitHub.
This means that some mistakes happens often, since they work in some Markdown
renders but not in MkDocs.
*ALL* of these mistakes should be caught by the markdown linter described [here](running_wiki.md#markdownlint), unless
any rules have been manually exempt.

Here are some examples of common mistakes:

#### Only One Top Level Header

MkDocs supports only one top level header (`# header`) per page.
If another level one header is present, the rest of the page won't be shown in
the overview.

#### Missing Blank Lines

MkDocs requires elements to be preceded by blank lines.
This also means that headers should be proceded by blank lines before content.

<p style="color: darkred; font-weight: bold;">Wrong:</p>

```markdown
Some text
- List item
...
```

<p style="color: green; font-weight: bold;">Correct:</p>

```markdown
Some text

- List item
...
```

#### List Indentation

MkDocs requires lists to use 4 spaces for indentation.

<p style="color: darkred; font-weight: bold;">Wrong:</p>

```markdown
- List item
  - List subitem
...
```

<p style="color: green; font-weight: bold;">Correct:</p>

```markdown
- List item
    - List subitem
```

### Custom Title

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

### Arranging Pages

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

## Building the Pages

Everytime something is pushed to the ``master`` branch of the wiki, the GitHub
Actions workflow is run.
The workflow deploys the built pages to the ``gh-pages`` branch, which is set
to be the source of the GitHub Pages.
This is configured in the repository settings of the wiki repository.
