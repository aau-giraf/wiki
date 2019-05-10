# Process group information
This section mostly contains information that is relevant for the process group, and as such it is written to the process group.
It might be used for development groups for the sake of documenting the process in the reports.

## General development
This is a short section that outlines how a single sprint went.
If you want more in-depth information, you should check the [Project Meetings section](project_meetings.md).
We started by using the Scrum of Scrums framework, where each group would send a representative to attend one or two standup meetings per week.  
We would also do both poker planning where each group did poker planning until they had filled out their points, and we would be doing review and retrospective.

After talking to Carsten Ruseng, our lecturer in software engineering, as well as realizing how inefficient poker planning is when you start out, we would skip poker planning.
We did this because we experienced that most estimates were off by quite a margin, and this meant that if groups took two high-priority tasks and were delayed on their first, the second would be blocked while other groups worked on different things.

Instead, a sprint went something like this:
At the very first day of the sprint a [sprint intro](project_meetings.md#sprint-intro) is held.
At this event the PO group will present the product vision and the sprint goal for all developers.  
The process group will present any changes that they have come up with during the previous retrospective.  
At the end of the meeting each group will be assigned their first issue to work with.  
This is done by the PO group who have ranked the issues as lowest, low, medium, high, or highest priority.

Then ordinary development ensues.
When a development group feels that they are done with a user story, a PR will be created, and the process group will be responsible for [finding reviewers](#assigning-reviewers).

During the week you should have some [cross-group standups](project_meetings.md#cross-group-standups).
In the beginning when you still follow lectures we recommend a single standup a week.
It's also a good idea to organize the standup between the two days with the most time for your project.  
For an example, if you have no lectures Monday and Tuesday, but full schemes the rest of the week, then place the standup somewhere at the end of Monday or start of Tuesday.

When you no longer have any lectures we found 2 standups to be beneficial.

At the end of the sprint the process group should host a [release preparation](project-meetings.md#release-preparation), where you take everything that was developed during the sprint and test it thoroughly to polish the little details.

The release preparation ends with a [release party](project-meetings.md#release-party) where each group is given the opportunity to showcase the work they did during the sprint.
This aims to help other developers gain an overview of the project, as well as instill a feeling of teamwork.

## Fullstack teams
In the previous years, groups worked with a horizontal slice of the architecture, i.e. some groups only worked on the database, some groups only worked on frontend, etc.  
This meant that features were developed like on an assembly line.
Instead, we were suggested to create fullstack groups, where groups independently implement an issue from server, through backend, to frontend.

We were recommended to drop the horizontal slice approach for several reasons:
1. Groups will only know what the state of the app is for the particular area that they work with. Frontend won't know how the backend works, and the server group will most likely never compile the frontend.
2. Groups will be more isolated and not have as many developers to ask for help.
3. You have been working as a fullstack team in previous years anyway.
4. It is harder to assign reviewers, as there are fewer people who understand the area in which you work.
5. If you choose fullstack teams, all development of a single feature happens in a single group, instead of having to hand over a feature.

## How to handle roles
You will be interacting with most of the other GIRAF students during the semester, and will be interacting with the students as they take on different roles.
This section will try to describe and prepare you for handling the different roles that exist in the project.

### Development groups
The development groups are simply the groups in which you write the report.
Every single group of students are a development group - even the process group, and the PO group.

The process group's role will mostly be to listen to these groups' concerns during the semester.
They usually bring questions about the process, [how to create pull requests](for_development_groups.md#how-to-create-a-pull-request), who to ask for issues and such.
We recommend that for issue related questions you refer to the PO group, and let them handle that, to ensure that they can keep an overview of what is happening in the project.
You should of course help by remembering and recommending good practices, e.g. creating one issue per bug/feature, creating one pull request per issue.

If the questions are related to pull requests, collaboration, testing, or anything else, we recommend that you, if you haven't already, discuss the issue in your group and try to reach the agreement that benefits the project the most.
Remember that even though it is always recommended to follow all best code-practices, this is sometimes impossible as you have a limited amount of time available.
Try to get an overview of the kind of best practices we followed as we recommend that you follow them.  
For anything else, see the developers' time as a scarce resource.
What will the project and next year's students benefit from the most?
Following the practice, or simply developing new features / document the existing ones?

### Skill groups
These groups have a representative from each development group, and have a single responsibility area, i.e. the frontend, backend, or server.  
They will do work that is not directly related to an issue, but is more related to general maintenance and management of the three areas.
We recommend that major changes or decisions related to one of the areas are discussed in these groups, as they will be the most qualified at making these decisions.
The development groups should also be able to consult their representative when they have specific questions to one of the areas.

We did not have a lot to do with these groups, other than setting the time and place for the first meeting, and introducing the idea to them.
From this point they figured out how they could gain an overview of the area, and continue work.
They also organized their own meetings after the first meeting.

### Product owner group
The product owner group, also called the PO group, is the group responsible for the issues in the project.
According to regular Scrum, that we started with an intention to follow, product owner is a bit of a misleading name.
But the responsible that they were assigned by us, was to handle the issues.
When a feature suggestion was provided, the PO group would make it an issue, prioritize it, create and add prototypes to it, and assign it when development groups came and asked for new issues.
They would also prune overlapping issues, and approve the design of all pull requests, to ensure that they are consistent with the prototypes and the design guide.

We were assigned the same room as the PO group in 2019.
This was very beneficial for the cooperation, as we could quickly take a short discussion with them about the different aspects of the project.  
In certain areas your work will be overlapping, and other students coming into your group rooms to discuss something, will not always know which one of you to address.
If you are seated in the same room, you will be able to eavesdrop on the requests to the PO group, and vice versa.

This will both give you an overview of the project, as well as provide the PO group with an overview of the process changes that you discuss.
Embrace their feedback and input, as they will have the overview of the issues in the project - and the progress of these.

You should remind the PO group of the different meetings, and what they should do to prepare.
For the sprint intro, the PO group should bring the product vision and the sprint vision.
For the release preparation, please refer to the [release preparation section](project_meetings.md#release-preparation) as this requires some work from both of you.

# Your role and relevant information for you
This section includes information directly related to your role as the process group.
It is meant as a work of reference that you can consult when in doubt about the different tasks that you should perform during the semester.

## Communication
We created a Slack channel that we used for communication in the project.
All groups had their own channel that could be used for getting a hold of the group.
Each skill group also had their own channel.
Other than that, he had the following channels:
- Announcements - only used for very important information that all should receive.
- General - mostly used for relevant discussions and talks about the project, or for asking everyone for help.
- github_watch - GitHub bot so you can follow all the sweet progress.
- Flutter - general resources and questions about Flutter.
- Random - to keep everything meme-related away from the other channels

We very strongly recommend that you add the setting that [displays people's full name instead of their obscure username](https://get.slack.help/hc/en-us/articles/115004686586-Show-members-full-names-in-your-workspace#show-full-names-1).
Likewise, it is beneficial if people put their group in the *What I do* field, so that it is easy for everyone to identify where the person they're talking to belongs.

We also recommended that you ask people to add their real name to GitHub, so you can search for that when assigning them, instead of having to deal with their GitHub usernames.
They change that by going to <https://github.com/settings/profile> and changing their name to their real name.

## General about meetings
You will be responsible for planning most meetings.
We created a GIRAF Google Calendar that we shared with people, where we asked them to add all meetings all groups are welcome - that included skill group meetings and the general process meetings.
When people add this calendar to theirs, it wasn't necessary for us to promote the meeting on Slack, saving a lot of messages.
If you choose to do the same, remember to add location to the meetings.

We generally planned a retrospective on Monday morning and sprint intro on Tuesday morning, so you have time to review any changes to the process.
This also gives the PO group time to organize their issues, and the development groups a bit of short time to catch up on their reports.

Release preparation would usually be two full days.
If the sprint ends on a Friday, we would hold a release preparation from Thursday morning until Friday at 13 o'clock. From 13 to 14 we would hold the release party.
We had the release party early in the day, so as many as possible would attend it.

## Our adaptation of GitFlow
We used the [GitFlow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) as the branching strategy in the GIRAF project.
We also enforce squash merges from feature branches into the develop branch, so each feature will be in a single commit.

This is our adaptation, but please read the entire section, as there might be better ways to do it.

For the [release preparation](project_meetings.md#release-preparation), the process group creates a release branch, which is merged out from the master branch.
Then commits are chosen from the develop branch by the PO-group.
Only commits that are actually relevant for the upcoming release are added.
This is called cherry picking commits.
In the release preparation, developers will add bug-fixes to the release branch.
When the release preparation ends, the release branch is merged into the master branch, which is then merged into the develop branch.
This ensures that bug-fixes are also added to the develop branch.

One problem with this approach is the manual part with the creation of the feature branch.
If you forget a commit, or miss it, you risk having critical functionality that was never added to the master branch, but will be present on the develop branch.
You will never get a complete and automatic addition of the changes from the develop branch, and as such you cannot guarantee that everything was added to the master branch.

To accommodate this problem, one solution would be to make even stricter rules for the develop branch.
As it is currently, the develop branch allows sub-features to be pushed, which are parts of bigger features.
As such you might have a "login" button, but not the "create user" button.
This renders the login button useless, but it can still be included in the develop branch right now.

An example of how to properly handle this, could be to create a feature branch where all login related functionality could be added.
Different issues could be merged into this feature branch.
When everything login related has been fixed and merged to the feature branch, this feature branch can be merged into the develop branch.

## Assigning reviewers
Assigning reviewers is done in an excel document.

![Google Sheets Review Assignment](https://i.imgur.com/WBkdycF.png)

This sheet will keep track of the number of PRs a group reviewed and the size of these.
We reset it once in a while, when the numbers become too big.

It helps to gain an overview of which group to assign for review.
Every PR needs two groups, who are not the author, as reviewers, as well as an approving review from a PO group member if it contains anything GUI related.
When groups have been chosen, you should assign a representative from the group as a reviewer on the PR.

We provide a checklist to the reviewers, depending on if the PR is made to a [code repository](review_checklist_code.md) or the [wiki repository](review_checklist_wiki.md).
This is provided as a comment on the PR on GitHub.

## Gatekeepers of good code practice
You, the process group, will be mostly responsible for maintaining a good code practice.
Some developers will not be informed about the best practices, others will not care, and others yet again will fail to see the reasons for good code practice.

As such you will be responsible for sustaining a good code practice.
You should actively seek out more information, and ensure that you thoroughly research pros and cons of both existing practices and new practices.

### Definition of done
For an issue, we have defined the following definition of done:

>An issue and its associated tasks are considered done when the feature branch has been successfully merged into the development branch by a single pull request and the feature documentation has been updated in the GIRAF wiki.

This means that all functionality should have been designed and implemented, so you have fully working functionality merged.
Essentially things should be included in the develop branch when you would publish it to the user (after a bug test).

You should check that people practice this mentality.
You will be able to spot this if you keep an eye on the incoming pull requests.
Some groups will add several pieces of functionality in a single PR, and others will add incomplete functionality, stating that "it wasn't specified in the issue that we should do it."

For the second case, tell them that it is a shortcoming of the issue, and when they discovered this they should have taken immediate contact to the PO group and asked for it to be included in the issue.
Functionality isn't worth much, if it isn't finished, and as such shouldn't be included in the develop branch.

### Issue reporting
Once in a while, someone will approach you and tell you about something that the program should have, or something that doesn't work.
You should be responsible for one of the two things:
1. Creating an issue describing it.
2. Making sure the developer creates an issue describing it.

If you don't do it, you probably won't remember it.

### Reviews
It will be so easy to cut corners with this.
A lot of your time will be spent doing reviews, and you will probably be tempted to cut down on the time spent on reviews.
Know for sure that other students will, at least.

We really hope that you encourage people to spend the time on the reviews.
It will save you so much time in the long run, as you will catch a lot of errors and bad practices before they even emerge.

The students will also get a lot of insight into other people's way of writing code, as well as the insight of learning how other parts of the codebase were developed.

The time spent is well invested and will benefit you and the coming years in the long run, as the code will be much more aligned, and developers will increase their knowledge a lot.
