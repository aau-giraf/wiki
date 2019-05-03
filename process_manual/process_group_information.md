# Process group information
This section mostly contains information that is relevant for the process group.
It might be used for development groups for the sake of documenting the process in your reports.

## General development
This is a short section that outlines how a single sprint went.
If you want more in-depth information, you should check the [Project Meetings section](project_meetings.md).
We started by using the Scrum of Scrums framework, where each group would send at representative to attend one or two standup meetings per week.
We would also do both poker planning where each group did poker planning until they had filled out their points, and we would be doing review and retrospective.

After talking to Carsten Ruseng, as well as realizing how inefficient poker planning is when you start out, we would skip poker planning.
We did this because we experienced that most estimates were off by quite a margin, and this meant that if groups took two high-priority tasks and were delayed on their first, the second would be blocked while other groups worked on different things.

Instead a sprint went something like this:
At the very first day of the sprint a [sprint intro](project_meetings.md#sprint-intro) is held.
At this event the PO group will present the product vision and the sprint goal for all developers.
The process group will present any changes that they have come up with during the retrospective.
At the end of the meeting each group will be assigned their first issue to work with.
This is done by the PO group who have ranked the issues as lowest, low, medium, high, or highest priority.

Then ordinary development ensues.
At some point of time a PR will be created, and you will be responsible for [finding reviewers](#assigning-reviewers).

During the week you should have some [cross-group standups](project_meetings.md#cross-group-standups).
In the beginning when you still follow lectures we recommend a single standup a week.
It's also a good idea to place the standup between the two days with the most time for your project.
For an example, if you have no lectures monday and tuesday, but full schemes the rest of the week, then place the standup somewhere at the end of monday or start of tuesday.

When you no longer have any lectures we found 2 standups to be beneficial.

At the end of the sprint you should host a [release preparation](project-meetings.md#release-preparation) where you take everything that was developed during the sprint and test it thorougly to polish the small details.

The release preparation ends with a [release party](project-meetings.md#release-party) where each group is given the opportunity to showcase the work they did during the sprint.
This aims to help other developers gain an overview of the project, as well as instill a feeling of teamwork.

## Fullstack teams
In the previous years, groups worked with a horizontal slice of the arcitechture, i.e. some groups only worked on the database, some groups only worked on frontend, etc.
This meant that features were developed like on an assembly line.
Instead, we were suggested to create fullstack groups, where you implement an issue from server, through backend, to frontend.

We were recommended to drop this practice for several reasons:
1. Groups will only know what the state of the app is for the particular area that they work with. Frontend won't know if the backend is good, and the server group will most likely never compile the frontend.
2. Groups will be more isolated and not have as many developers to ask for help.
3. You have been working as a fullstack team in previous years anyway.
4. It is harder to assign reviewers, as there are fewer people who understand the area in which you work.
5. If you choose fullstack teams, all development of a single feature happens in a single group, instead of having to hand over a feature.

## How to handle roles
You will be interacting with most of the other students during the semester, and you will be interacting with the students as they take on different roles.
This section will try to describe and prepare you for handling the different roles that exist in the project.

### Development groups
The development groups are simply the groups that you write the report in.
Every single group of students are a development group - even you, and the PO group.

Your role will mostly be to listen to these groups concerns during the semester.
They usually bring questions about the process, how to create pull requests, who to ask for issues and such.
We recommend that for most issue-related questions you simply refer to the PO group, and let them handle that.
You should of course help by recommending good practices, i.e. creating one issue per bug/feature, creating one pull request per issue.

If the questions are related to pull requests, standup, testing, or anything else, we recommend that, if you haven't already, discuss the issue in your grup and try to reach the agreement that benefits the project the most.
Remember that even though it is always recommended to follow all best code-practices, this is sometimes impossible as you have a limited amount of time available.
Try to get an overview of the kind of best practices we followed.
We recommend that you follow these.
For anything else, see the developers time as a scarce ressource.
What will the project, and next year's students, benefit the most from?
Following the practice, or simply developing new features / document the existing ones?

### Skill groups
These groups have a representative from each development group, and have a single responsibility area, i.e. the frontend, backend, or server.
They will do work that is not directly related to an issue, but is more related to general maintenance and management of the three areas.
We recommend that major changes or decisions related to one of the areas are discussed in these groups.
The development groups should also be able to consult their representative when they have specific questions to one of the areas.

We did not have a lot to do with these groups, other than setting the time and place for the first meeting, and introducing the idea to them.
From this point they figured out how they could gain an overview of the area, and continue work.
They also organized their own meetings from here on.

### PO group

