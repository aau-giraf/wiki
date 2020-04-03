# GIRAF Events

This page lists and explains the events was used during GIRAF 2020.
We took inspiration from [Scrum](https://www.scrum.org/resources/scrum-guide), 
but changed some of the events to fit the GIRAF project better.

- [Sprint Planning](#sprint-planning)
- [Cross-group Standups](#cross-group-standups)
- [Sprint Release Preparation](#sprint-release-preparation)
- [Release Party](#release-party)
- [Sprint Review + Retrospective](#sprint-review--retrospective)

## Sprint Planning

The sprint planning happens before the start of every sprint.
Before the sprint planning, the PO group has planned a sprint goal for the sprint.

### Purpose

The purpose of the sprint planning is to plan the next sprint by giving all groups a number of issues to start working on.

### Practice
* All members of the development teams should be present in the same room.
* The meeting follows the structure presented below

#### Presentations

1. The process group presents changes made to the process.
    * The changes are based on the retrospective. 
2. The PO group presents the following:
    1. The project vision.
        * What is the overall goal for the project?
        * Did this change since last meeting? (This will be a recap, if there are no changes)
    2. The sprint vision.
        * What do we want to acomplish with this release?
    3. New and important issues for this sprint.
        * These are typically based on usability tests made with the customer.

#### Time Estimation

1. All development teams are split into crossgroups.
    * The crossgroups are made at random.
2. Each crossgroup are assigned a number of issues to time estimate using **planning poker**.
    * Some crossgroups might only be assigned a single issue, which they then have to split into smaller issues and then time estimate.

##### Planning Poker Rules
* The Fibonacci numbers are used as weights
    * 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 and ∞
* 5 is equal to a single person's workload for a full day
    * A full day's workload is 8 hours
* If no cards are available, the participants think of a number and say them one by one
    * Cards are the most optimal solution
    * If the participants have to say their estimations aloud, it is benneficial to start with a different person each time.
* If the participants are not in agreement, the person with the lowest and highest estimation presents their arguments for their estimation. The "game" is then played again.
    * If there are still disagreements, it can be beneficial to have an open discussion.
* When an estimation has been decided upon, the issue should be assigned as a label to the issue on GitHub.

#### Groups Choose Issues
When all crossgroups are done with their estimation, the development teams should meet again and decide which issues they would like to work with.

1. Each development team creates a prioritized list of issues they would like to work with
    * The list should also include the estimatios found on GitHub


## Cross-group Standups

The cross-group standups are held once or twice a week.
This is the GIRAF counterpart to the Daily Scrum.

### Purpose

The purpose of the cross-group standup meeting is to share knowledge between the groups,
figure out what the other groups are working on, and talk about issues that groups have run into.

### Practice

* One representative from each group.
    * The process group might be two: one as develop team, and one as process group.
* Every group goes through:
    * What have you done since last time?
    * What will you do until next time?
    * Do you have any hindrances that stops you from solving a problem?

## Sprint Release Preparation

The last two work-days before a sprint ends should be spent actively hunting for, and fixing bugs.
We strongly recommend that all groups are present in the same rooms.

### Purpose

The purpose of the release preparation is to find bugs and prepare the applications for release.

### Practice

The release preparation is split into two phases:

* Testing
* Bugfixing

The bugfixing phase might start while the testing phase is still ongoing.

#### Testing Solved Issues

During this phase the applications are tested.
This includes issued that have been solved, but also the **application as a whole**.

Each issue closed in the sprint is handed out to two groups, none of them being the author group.
Each group will then be responsible for testing the **issue** according to the following checklist.

* Note that you should focus on the **issues** and **not** on the pull requests!

A new issue should be created on GitHub if 'no' is the answer to any of the following questions:

- [ ] Can the screen be reached through navigation in the application?
- [ ] Can you perform all the functionality defined in the issue?
- [ ] Can it be used without crashing?
- [ ] Does it run without bugs?
- [ ] Does all of the above still look acceptable if you change to a new device or change orientation?

If a bug is discovered:

* If it is **related** to the release:
    * [Create an issue](./github.md#issues) in the relevant repository, using the ![releaseFix](./images/releasefix-label.png) label.
* If it is **unrelated** to the release, maybe a bug that does not hinder release or some badly written code:
    * [Create an issue](./github.md#issues) in the relavant repository, using the relevant labels.

After an issue has been created, contact the PO group, who will then assign the *releaseFix* issues.

#### Fixing Release Bugs

1. You get a *releaseFix* issues from the PO group.
2. Write a regression test
    * A regression test should fail before solving the issue and pass after

**Remember to help each other out!**

If there is extra time, groups might be asked to write new tests.
These tests will be assigned by the process or the PO group.
This could be along the lines of "test file X according to issues Y."

## Release Party

The release party is mainly a social event. 
The purpose of this meeting is to push the features and fixes onto the master branch. 
Afterwards, people are encouraged to participate in a social event. 
This is of course optional, but we highly encourage people to talk to their fellow students to make new friends or to get an insight of what they are working on.


## Sprint Review

All developers meets and discuss problems they have experienced while fixing their assigned issues. This event should last a maximum of 4 hours.

### Purpose

* To get an understanding of difficulties other developer teams have met, and what their solutions were.
* To get an overview of all the issues fixed in this sprint. 
* To get an overview of the project as a whole, and what condition it is currently in.

### Practice

* All developers meets in a meeting room or on discord.
* The process group notes which developer teams are present, and assigns a person to write a summary.
* A person from each developer team starts off with explaining:
    * Issues: What were they meant to solve, and how did they solve it.
    * Problems: Which problems did they face in solving the issues, and how did they resolve it.
    * Noteworthy changes that needs to be mentioned to all the developers.
* PO presents the status on the product backlog. 

Remember to __ask questions__ to other developers if you are confused or would more information about their solutions!


## Sprint Retrospective

All developers meet and gives feedback to the previous sprint about the process and what can be improved

### Purpose

* To improve the quality of life for the developers by gathering feedback from the developers
* To make sure everyone gets a chance to say what they have on their mind

### Practice
* All developers split into multiple rooms with a member of the process group in each group.
* The process group have prepared the subjects to go through for feedback, which will be gone through sequential. 
* Through each of the subjects can the developers give feedback, positive and negative, to improve the sprints overall. 
* When done, the meeting is over.

Remember not to discuss the feedback brougth up. When the retrospective is over, the proces group will make a questionary to judge what feedback should be looked into. 

### After Review and Retrospective

Make sure that you don't have leftover branches from the sprint.
Look through the branches and delete branches that was created by you and that you don't use or plan to use anymore.