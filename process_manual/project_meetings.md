# Project meetings
This section will go through all the different meetings, and describe the agenda and purpose of each meeting.
Generally you should try to waste as little time as possible with the meetings.
Having everyone attend all meetings is a bad strategy, so only invite the necessary students.

## Sprint planning
This meeting is used to introduce and mark the beginning of the sprint.
All developer groups should have a representative present in the same room, and the process group will start by presenting changes to the process, based on the [sprint retrospective](#sprint-retrospective).
Thereafter the PO group will present the following things:
1. The project vision
   - What do we want to accomplish in the entire project?
   - Did this change since last meeting? (if not, just give a recap, so people remember)
2. The sprint vision
   - What do we want to accomplish until the next release?
3. New and important issues in this sprint
   - Typically based on usability tests with the customer.

Thereafter the representative will do the following:
1. Get into teams of 3-4
2. Get some issues from the PO group
3. Refine the issues into smaller sub-issues so the task gets manageable for one or more developer groups to work with
4. The teams gather and quickly runs through the issues and sub-issues
	- If two issues have the same sub-issue it will be discussed which issue should handle that sub-issue  
	
The meeting is then over and the representative meets with his group and does the following:
1. Go through the issues for the sprint
2. Make a list with at least 10 issues in a prioritized order after what issues the group wants to work with
3 Do a time estimate of the issues(Planning poker could be a way of doing it)
4. Give the list with issues and time estimation to the PO-group who officialy assigns issues to the groups
	-It's better to have few issues than to many for a sprint, since 
	 it's always possible to get new issues by contacting the PO group

The first sprint planning will probably be the longest, as the process group should present the major parts of the process.

All following sprint plannigs will probably be shorter meetings, lasting no more than a hour.


## Cross-group standups
This meeting should be held once or twice a week.
When you still have lectures, once a week should be sufficient, and when you don't twice a week will be better.

The purpose of the cross-group standups is to coordinate the events of the project, and to minimize the amount of merge conflicts caused by having multiple groups work in the same files.

The agenda for a cross-group standup is as follows:
You book a room with the secretaries, and announce the meeting in the calendar and on Slack.
At the meeting, which should only take a maximum of 15 minutes, everyone should be standing around a table.
Make sure that you have found the issues for each group. You can typically search for assignees and simply use the representatives username from each group.

They should answer the following questions:

- For each user story
   - What issue number is it?
   - What is it about?
   - How do they solve it?
   - When do they create a PR for it?

Then you should remind everyone that:

- They should contact the author of a PR when they have reviewed it
- They should contact the reviewers when the author responded to all comments
- They should ask the PO group if they have any questions about issues

## Release preparation
The last two work-days before a sprint ends should be spent actively hunting for, and fixing bugs.
We strongly recommend that all groups are present in the same rooms.

We recommend that each issue is handed out to two groups, none of them being the author group.
Each group will then be responsible for testing the issue according to the following checklist:

A new issue should be created on GitHub if 'no' is the answer to any of the following questions:
- Can the screen be reached through navigation in the application?
- Can you perform all the functionality defined in the issue?
- Can it be used without crashing?
- Does it run without bugs?
- Does all of the above still look acceptable if you change to a new device or change orientation?

If a bug is discovered, an issue should be created in the relevant repository, describing the bug.
The label called ReleaseFix should be added to the issue.

The PO group will assign the bug-fixing issues.
When groups solve an issue, they should write a test to verify that that the bug was solved, i.e. the test should fail before solving the bug, and pass after.

Most of the time, there will only be a few bugs left, and most developers will have some extra time with nothing to do.
A way to keep them engaged could be to organize writing tests.
Just asking people to "test the code" will yield approximately 0 new tests.
As such, it is necessary to ask people to write specific tests.
This should be defined by the process group, and could be along the lines of: "test file X according to issues Y."

Also encourage people to help each other out, as someone will be more experienced with testing than others.
That's why you should be in the same room, so helping each other is easier.

We suggest that some hours before the release party, beer is brought in from F-klubben, with someone organizing the purchase of all beers that have been taken.
Ask your local F-klub representative if it is okay.
It should be, and it helps the morale.

## Release party
At the very end of the release preparation you should host a release party.
The party should be planned to start at 1 or 2 o'clock, so people actually want to participate.
This release party will start by merging everything in the release branch into the master branch.
This should be followed by ecstatic cheering and clapping, because you are awesome.

Then, while enjoying a sip of your beer, every group should, in turns, come to the front and present the work that have been done in the sprint.
Encourage people to show what they have done.
Do this by connecting a tablet to the projector.

This will give an overview of the state of the product, and will help people's feeling of involvement in the project.

After this, we had no more activities planned.
We encouraged people to stay and drink a beer, but most would go home - possibly from a lack of things to do.
It could be a good idea to encourage people to play CurveFever Pro, Scribble, or anything like it.

## Sprint Retrospective
The sprint retrospective is the process group's opportunity to hear what problems exist with the process.
This meeting should be held the next workday after the release party.

Initially we used Dotstorming to find issues and suggestions, and then vote on them.
But the problem was that Dotstorming only allows for users to have 3 votes, so if there were 5 ideas that everyone agreed 100% on, it would only show on 3 of the ideas, while 2 of them wouldn't get any votes.

Equally, Dotstorming does not allow for negative votes.
So, controversial topics will only have the positive votes shown.

Instead we came up with the following solution:
First, we split into groups.
The number of groups was determined by the number of members from the process group that were present.

Each group would have their own tab in an Excel sheet. ([See example](https://docs.google.com/spreadsheets/d/1CI3sIuzlVDRX4EsG0C6N0jH4d9QvLtC8BiAPsyhp1gE/edit?usp=sharing))
Members of the process group would be responsible for reporting the issues that developers report.
It does not matter if you write down problems or solutions.
Having a solution is nice, but bringing up a problem is just fine as well.
Remember that the issues isn't an expression of the process group member's feelings or opinions about feedback, so try to report the feedback as accurate as possible.

Oftentimes the discussions in the groups will also be hard to get going.
The process group member should ask about the different parts of the sprint, like "what did you think about the sprint intro?" and "what about the release preparation?"
Also feel free to, as a process group member, bring something up that you felt didn't work out.
The rest might not have experienced it as a problem, they might have a solution, and if not, it might help as an icebreaker for the conversation.

When everyone have had 15-20 minutes in the groups to discuss different problems and/or solutions, the process group members should get together.
Here, they should remove duplicates.
In the example sheet everything have been copied into the "samlet" tab.
Here we marked the duplicate entries that we choose to remove with yellow marking.

Then we created a Google Forms where every suggestion or idea were directly pasted in.
The following, generic, options were given:
- "It's a good idea / I agree"
- "I don't care"
- "It's not a good idea / I disagree"

This meant that every developer had to give their opinion on every problem or solution, and it revealed some controversial topics.

We, the process group, spent the rest of the day discussing changes to the process, and presented it the next day to the sprint intro.
