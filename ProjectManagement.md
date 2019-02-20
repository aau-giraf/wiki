### Purpose
The purpose of the Giraf Configuration Management plan is to establish the rules and guidelines for managing versions of the different components and managing the versions of different components in a complete system release.
Configuration management is important in order to keep track of what versions of which code-files exist where and how they relate to a component. As well as keeping track of baselines, their component versions, changelogs and requirements to future baselines.

Version Control
----
The giraf project consists of different components e.g. the different Android apps, the java libraries, the backend API etc. Each component is managed through the decentralised version control system: Git. The components source code is hosted on [http://git.giraf.cs.aau.dk](http://git.giraf.cs.aau.dk) through the //Gogs - Go Git Service// hosting platform.
It is highly recommended that each repository contains a README.MD file with the following contents:
- Description of the component
- Dependencies and installation guide
- Execution guide
- Unit test guide
- Contributors
- License
- Component specific sections like API reference for the API component

### Git Workflow
Every component should follow the GitFlow Workflow described at [https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) and at [https://datasift.github.io/gitflow/IntroducingGitFlow.html](https://datasift.github.io/gitflow/IntroducingGitFlow.html). All project members should have read either of the two documents.
The short summary is that we work on a set of branches (see table A.1), each with a different responsibility i.e. master should only contain working releases, develop should be used for working, but incomplete versions of the systems as well as a base for any further development etc.

| **Branch** | **Description** | **Created from ..** | **Merged into ..** |
|:--:|:--:|:--:|:--:|
| master | Stable versions suitable for use by the end user |||
| develop | Contains latest working versions and is the base of further development | master ||
| feature-* | Any features under development | develop | develop |
| hotfix-* | Quick fixes to fatal bugs on master that need to be fixed quickly | master | develop and master |
| release-* | Configuration items for each release | develop | develop and master |
(//Table A.1: The different types of branches in the gitflow workflow. At the end of a branch’s lifecycle, it is merged into the mainline branches described in this table//)

The **master** branch contains the newest stable version suitable for users of the Giraf applications. Before code is merged into the master-branch it must be ensured that the code can build and that it is tested. Code from the master branch is merged from a release branch.

The **develop** branch contains the newest functionality for the current sprint. Before configuration items are merged into the develop branch it must have been thoroughly tested and reviewed by members of your own group or members of a fellow Giraf group. Phabricator can be used to facilitate code reviews.

A **feature** branch should be created for each new functionality that is added to a component. Ideally a feature branch should reflect a user-story on the Phabricator task board and should be named feature-task where //task// should be replaced by the task number of the user story or an expressive name for the functionality that is added. Once a feature is implemented and tested, it is merged into the development branch and the corresponding feature branch should be deleted.

A **hotfix** branch must be created from the master, develop, or release branch when a bug should be fixed in order to prevent new bugs to be introduced into these branches. Once the bugs are fixed the branch is merged and deleted.

The **release** branches contain the code for the release of the different versions of the component. These branches should be follow the following format: " `Giraf-<ComponentName>-V<major>.<minor>.<patch>` ". The version naming scheme is described in the upcoming chapter.

Version Management
---
Each software component should have their own baseline, and changes to the individual components should be controlled using Git as described previously. Each component should be uniquely identified as follows: `Giraf-<ComponentName>-V<major>.<minor>.<patch>`
e.g. `Giraf-RestAPI-V2.008.01}, \texttt{Giraf-WeekPlannerApp-V2.022.02`.

**ComponentName:**
**major** The major version starts at 1 and is incremented whenever backwards compatibility is thrown out the window. Every major version should have a requirement specification document on the Phabricator wiki.

**minor** The minor release number starts at 001 whenever the major number is incremented and is itself incremented whenever a new feature which is not simply an internal implementation detail is added.

**patch** The Patch number starts at 01 and is incremented whenever a hotfix is applied to the master branch. it is used simply to differentiate the version before a fix is applied from the version after.

### Managing Component Releases
To keep track of releases we use the Phabricator wiki at [http://web.giraf.cs.aau.dk/w/](http://web.giraf.cs.aau.dk/w/). On the wiki a separate article will be created for each complete system release.

A system release consists of a release schedule, a list of requirements that defines the development task for the release and links to source code for each component related to the release

An example for a release schedule is seen in the table below where each schedule consists of a number of deadlines that has to be met. First deadline for each release is a set of requirements that should be defined for the release and this document should contain enough information about each feature in the release such that it can be developed throughout the stack. An example of the requirement document that we, together with the PO group, created for Release2018S3 can be found by navigating to [http://web.giraf.cs.aau.dk/w/releases/2018s3r2/requirements/](http://web.giraf.cs.aau.dk/w/releases/2018s3r2/requirements/).

**Release2018S3**

| **Deadline** | **Date** | **Document** | **Notes** |
|:--:|:--:|:--:|:--:|
| Release requirements released | Mon 2018-04-16 | | |
| API development finished | Mon 2018-04-30 | | |
| App/Frontend development finished | Thu 2018-05-03 | | |
| PO approves that requirements are met | Mon 2018-05-07 | | |
| Release | Tue 2018-05-08 | | | |




Example of Giraf release

| **Giraf Releases 18S1**                          |
|:--:|:--:|:--|
| **Component** | **Version** | **Link** |
| Backend API      | V2.11.3       |  [Example](http://git.giraf.cs.aau.dk/Giraf-Rest/web-api/commit/d8f7c16a99152f427a1a3c213919b5bfb87d7434)
| Frontend API     | V2.03.7       |  [Example](http://example.com)
| Launcher            | V2.53.1       |  [Example](http://example.com)
| Week Planer      | V2.04.2       | [Example](http://example.com)
| ...                         | V...               |  [Example](http://example.com)
