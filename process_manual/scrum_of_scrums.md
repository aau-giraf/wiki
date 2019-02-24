# Scrum of Scrums

Scrum of Scrums (SOS) is a technique used to scale up scrum to bigger
teams. This chapter details our specific tailoring of a SOS process.
Many of the same activities and principles of are used in this specific
SOS process. In short, the structure of a sprint is:

1.  Sprint Planning

2.  SOS Stand Ups

3.  Skill Group Meetings

4.  Release Preparation

5.  Sprint Review

6.  Sprint Retrospective

7.  Release Party

> Note: SOS stand ups and skill group meetings occur several times
during a sprint.

It is up to the specific development group, whether or not they use
scrum internally.

# Sprint Planning

On the first day of a sprint, all members of the GIRAF multi-project
will meet. The duration of the sprint will be announced beforehand.  
**Agenda**

1.  The PO-group presents the user stories, the vision for the product,
    and the sprint goal.

2.  The development groups choose a user story.

3.  They then refine the user story into smaller tasks, estimates them,
    and gets it accepted by the PO-group.

4.  If the group estimates it can implement more user stories, go to
    step 2.

5.  Otherwise the group can leave the meeting.

Before the meeting, all development groups have an idea of how many
story point they want to take in the upcoming sprint, and the
PO-group must have a prioritized product backlog. 

> Each group can have their own method for estimating user stories into story points, and a single story point can have many definitions.

The user stories in the product backlog will be available to the development groups some
time before via GitHub. The development groups will bring a prioritized
list of the three tasks that they are most interested in working on.  
Each group will choose a user story, which they will refine into tasks.
They will then estimate the workload of these tasks. During this
process, a representative from the PO-group will be present in each of
the groups to answer questions and to get an overview of the tasks
created. If a group deems that it has enough available points for
another user story, they should take another user story from the product
backlog.  
Apart from the very first selection of a user story, all user stories
must be chosen from the highest available category of priority.  
When a development group is done picking user stories and has refined
them into tasks in the sprint backlog the final step is to have it
approved by the PO-representative.

# Sprint backlog changes

It is possible that members of a development group feel that they need
to change the sprint backlog during the sprint. Examples of why this
could happen is that the development group discovers that one of their
user stories contains more tasks than estimated or that changes have to
be made to the tasks. If the changes are large or serious enough then
the PO-group has to approve the changed or new tasks.  
There is no need to talk to the PO-group if the changes are only minor
and do not affect larger parts of the given user story.  
E.g. discovering that a button has to be moved to a totally different
place on the screen would be an example of a change the PO group would
have to approve. Discovering that a new class is needed to implement a
task that the development group thought did not need such a class is a
minor change that would not need to be approved.  
If there are any doubts as to whether the change to the sprint backlog
requires the approval of the PO-group then getting approval from the
PO-group is the correct course of action.

# SOS Stand Up

During a regular week there will be 1-3 SOS Stand Up meetings. These
will be announced through Slack and the GIRAF Google Calendar. Each
development group should send all relevant people (people needed for
answering the particular meeting’s questions) but should focus on
sending as few people as possible (preferably one). Before the meeting,
it is expected that each group has discussed the following points:

  - What has the group completed since the last meeting?

  - What will the group complete until the next meeting?

  - What challenges or difficulties do we face, which could possibly
    slow down or prevent the completion of a task?

  - Are we about to introduce something of relevance to other groups?

  - Have we discovered new dependencies to other user stories?

> Note: The meeting should be as short as possible, so consider if
what you plan to say is relevant information for the other people
attending the meeting.

At the meeting, each representative will answer these questions so that
everyone can get an idea of what is going on internally in every
development group. Then possible problems will be resolved in the
discussion afterwards. The meeting should not take more than 15 minutes,
but the representatives can talk afterwards if they are working on
something similar, and want to share ideas.

# Skill Group Meetings

We advise that skill groups meet at least once per week to keep each
other up to date on what they are working on and the relevant
conventions that need to be enforced. However this is not mandatory and
is up to the individual skill groups. The meetings should be used for
unifying the coding standards in the area that the skill group
represent.  
To see the definition of skill groups, please read section
[Skill Groups](#https://github.com/aau-giraf/wiki/process_manual/scrum_of_scrums.md) in organization overview.

# Release Preparation

Four days before the sprint ends, a release branch will be created by
the PO-group. The branch is created by cherry picking functionality from
the development branch, which will be features that the PO-group deem
ready for inclusion in the release. On the release branch, each
development group will be responsible for preparing the functionality
they have added, and make sure the functionality works in collaboration
with the rest of the features chosen for release. When a development
group is done preparing their stories for release, they should continue
development on other user stories.

# Sprint Review

The sprint review is a meeting held at the end of each sprint. Unlike
the sprint retrospective (see section
[Sprint Retrospective](#sprint-retrospective)), the focus of
the sprint review is on the product and more specifically the user
stories. The reason for the sprint review is to discover needed
functionality.  
**Agenda**

1.  Groups present current state of work.

2.  Open discussion.

3.  End of discussion.

Each development group sends one (and only one) representative to take
part in the meeting.

> As a side note, the PO-group is not limited to only sending one
    representative and should send as many as they deem necessary


During the meeting the representatives take
turns telling what user stories the group implemented and deliver
feedback on the product along with issues that might be important to
include in a future sprint. The PO-group decides whether the user
stories have been implemented in a satisfying manner and can choose to
use the additional feedback for the next sprint. Although it should not
be necessary, the sprint review should not take more than an hour.  

# Sprint Retrospective

All development groups should participate in the sprint retrospective.
The focus of the sprint retrospective is to find issues and/or ideas for
improvement of the process detailed in this manual. Ideas for
improvement can be anything related to the meetings, sections in this
manual, or something else related to the process. The Scrum group will
then incorporate these issues and ideas in the future sprint and write
an updated GIRAF process manual. The sprint retrospective is limited to
one hour.

### Agenda

1.  Introduction.

2.  Mixing of groups across development groups.

3.  Brainstorming of issues/ideas internally in mixed groups using
    [DotStorming](https://dotstorming.com/main).

4.  Break - Scrum Masters sort for duplicates.

5.  Each person votes for an idea/issue.

6.  Feedback on retrospective.

It is expected that before the sprint retrospective each group has
discussed positive and especially negative aspects of the process that
has affected them during the sprint. At the meeting, the groups are
mixed up so that each group member can share their interpretation of
their groups’ ideas. The groups are mixed, so all ideas are shared
across all groups.

# Release Party

The release party is an informal optional gathering. Representatives
from each group can showcase the functionality of the user stories that
they have implemented. Ideas on improvements are also welcome during the
showcase. The release party will most likely be scheduled to take place
on a Friday (Beers and other beverages are encouraged). The goal of
release parties is to enhance the sense of ownership and make
communication easier between development groups.