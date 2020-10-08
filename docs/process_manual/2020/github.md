# Use of GitHub in GIRAF

As explained in [the process manual of 2019](../2019/changing_the_process.md#github), 
they changed from GitLab to GitHub.

This article will explain how GitHub is used in the 2020 GIRAF project.

## Issues

Issues are created by the development teams as well as the PO group.
An issue can be a bug report or a task creation request.

The PO group prioritises, assigns and adds milestones to issues.

The list of issues can be seen at each repository, eg. <https://github.com/aau-giraf/weekplanner/issues>
, or a [complete list](https://github.com/issues?q=is%3Aopen+is%3Aissue+archived%3Afalse+user%3Aaau-giraf)
for the whole organization.

### Getting an Issue to Work on

If you have time to work on a new issue, you can get a new one by following
these steps:

1. Find an issue you want to work on
1. Ask the PO group if you can work on that issue
    - The PO group might say no for various reasons and they have the final say,
      as they have a better overview.
    - There is usually a greater chance of getting a yes if the issue you've
      picked is either _highest_ or _high_ priority.

If you don't have a preferred issue you can ask the PO group to be assigned the
most pressing issue, as they have a good overview of the project and they will
most likely have some issues that they would like you to work with.

### Creating an Issue

If you find a bug, or have a task creation request you can create an issue:

1. Go the the "Issues" tab of the relevant repository (E.g. <https://github.com/aau-giraf/weekplanner/issues>).
1. Press the green "New issue" button.
1. Choose whether to submit a bug report or task creation request, and press
   "Get started".
1. Create a title and description for the issue. Please follow the template, and
   don't delete the headers!
    - The title for the *Task Creation Request* should tell what functionality
      you would like added using the shown form "As a developer I would like the
      docker config file to automatically update so that I don´t have to manually
      update the config file". 
      Instead of the task being for the developer, guardian or user is also
      frequently used.
1. Label the issue with appropriate labels.
1. It can be a good idea to inform the PO group when you are done, so they can
   assign and refine the issue.

## Branches and Pull Requests

We follow the [GitFlow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
as explained in [the process manual of 2019](../2019/process_group_information.md#our-adaptation-of-gitflow).

During the sprints, all development is done in feature branches, branching out
from the `develop` branch.

![GitFlow diagram](./images/gitflow.png "Gitflow diagram")

The **naming convention** for feature branches is `feature/xx` where `xx` is
replaced by the issue number.

When the [Release Preparation](./giraf_events.md#release-preparation) phase
begins, a release branch is created from the `develop` branch.
This branch is now used **instead** of `develop` until the sprint is over.

The **naming convention** for release branches is `release/YYYYsXrZ` where `YYYY`
is replaced by year, `X` with the sprint number and `Z` with the release number.

E.g. `release/2020s1r1` for 2020, sprint 1, release 1.

### Creating a Branch

#### During Sprints

When you start working on an issue, you create a branch from `develop` called
`feature/xx` where `xx` is the issue number.

From the terminal:

```bash
git checkout develop
git checkout -b feature/xx
```

Or from GitHub:

1. Make sure `develop` is selected.

   ![Selecting develop branch](./images/github-branch-develop-selected.png)
   
1. Input the name of the branch (e.g. for feature 400).

   ![Create new branch](./images/github-create-branch.png)

1. Press "Create branch: feature/xx from 'develop'"

#### During Release Preparation

When you start working on a release fix, you create a branch from `release/*`
called `releasefix/xx` where `xx` is the issue number.

```bash
git checkout release/*
git checkout -b releasefix/xx
```

Or from GitHub using the same procedure as above, **but** with the release
branch as base instead, and with the release fix naming convention.

### Creating a Pull Request

When you have finished your issue, it is time to create a pull request.
A pull request is a request to merge your branch into another branch.

Before making the pull request, make sure that the code:

- Only relates to a single issue. (One PR per user story)
- Is fully tested.
- Is reachable when opening the application.

**Fully tested means that if any piece of the functionality is removed, a test
should fail.**

**Creating a pull request on GitHub:**

1. Open the "Pull requests" tab in the repository (e.g. <https://github.com/aau-giraf/weekplanner/pulls>)
1. Press "New pull request"
1. Select the appropriate branch as base.
    - `develop` if during sprint
    - `release/*` if during release preparation
1. Select your branch for as compare
1. Press "Create pull request" 
1. Name the pull request `Feature xx` or `Feature xx: A title describing changes`
1. Write a description
    - If you write `closes #xx` or `fixes #xx`, issue xx will be linked to the PR
      and will close when the PR is merged. ([All keywords](https://help.github.com/en/enterprise/2.16/user/github/managing-your-work-on-github/closing-issues-using-keywords#about-issue-references))

## Code Review

After being assigned a pull request, the group should review the code under the
_Files changed_ tab. Look for code that may be deprecated, unnecessary,
non-optimized or has weird formatting. 

Start at <https://github.com/aau-giraf/>

1. Choose repository eg. weekplanner.
1. Click on the **Pull Request** tab.
1. Choose an open pull request from the list.
1. Click on the **Files Changed Tab**. All the changes can be seen in these files.
    ![Files changed tab!](./images/files-changed.png "The code you should review is here")
    1. Make a comment or suggestion on a single line or multiple lines by pressing
        the blue + icon (move the cursor to a line). 
        The red square marks the selection icon which can be used to suggest code
        that replaces the line(s).
        ![Write suggestions!](./images/write-suggestion.png "Try dragging the blue icon across multiple lines")
        You can view what the author will see by clicking **Preview**.
        ![Preview suggestions!](./images/preview_example.PNG "Comment and suggestion")
1. Having looked over all the files, click **Review changes**.
    1. If you made comments, make sure the author looks them through by choosing
        **Request changes** before clicking **Submit review**. If changes are made,
        you have to re-review the pull request!
        ![Request changes!](./images/request-changes.png "Request changes. The author cannot merge yet!")
    1. If the changes makes sense, click **Approve**.
        ![Approve changes!](./images/approve-changes.png "Approve changes. The author can merge")