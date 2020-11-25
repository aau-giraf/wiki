# How to's for developers

This file is intended for helping developers understand their role in the
process.

## How to: Get an issue to work on

If you have enough time to work on another issue after finishing your previous
ones you should get another.
Try to aim for no more than two or three issues, as you shouldn't take on
another issue before you can actually work on it.
There's no need for you to be assigned to an issue that you can't work on right
now, as it might block others progress.

When you have decided that you have enough time for a new issue, you should go
and get one.
This process is very simple.
You have two options:

### Option number 1

You go to the issues tab of one of the repositories, e.g. github.com/aau-giraf/weekplanner/issues
and locate an interesting issue.
Then, when you have located the issue, you note the number.
That is denoted by the # and a number.

Remember the number and do a time estimation of the issue.
Thereafter go to the product owner (PO) group, and ask if you can work on this
issue.
The PO group might say no for various reasons.
Just remember: they have the overview of the project and probably have good
reasons for saying as they do.
There is usually a greater chance of getting a yes if the issue you've picked
is either *highest* or *high* priority.

### Option number 2

Go ask the PO group to be assigned the most pressing issue, as they have a good
overview of the project, they will most likely have some issues that they would
love to have you work on.

## How to: Write code

To get started writing code, you should first setup the project.
This is described in the [Setup from scratch tutorial](../../Development/Apps/development_environment_setup.md).

Then, after setting up the code, you should make a branch for the feature you
are going to implement.
Name the branch fixes_ISSUENUMBER, where the ISSUENUMBER is the number of the
issue you are implementing.

Follow the default coding standards that you can find.
For Flutter the linter should catch most things that go out of style.
If in doubt, try to find other places in the code that does similar things to
what you want, and follow that standard.
Remember that all functionality related to an issue should be implemented with
unit tests before an issue is considered done.

In the [How to review section](#how-to-review-a-pull-request) you can read more
about how that will happen.
Make sure that you plan for the pull request to go through as fast as possible.
And if you are in doubt and stuck, just go ask another group for help, as there
are a lot of clever people on the GIRAF project, and they usually love to help.

## How to: Create a pull request

When development of a piece of software is done, and it is deemed that
the code solves the assigned issue, a pull request should be made.

Before making the pull request, make sure that the code:

- Only relates to a single issue (One PR per user story).
- Is fully tested.
- Is reachable when opening the application.

**Fully tested means that if any piece of the functionality is removed, a test
should fail.**

To create the pull request, you should go to the relevant repository, click on
pull requests and click the green "New Pull Request" button. The base branch
should be "develop" and the compare branch should be your feature branch, with
the code that you want to add to the develop branch. Then click the green 
"Create pull request" button.

Name the pull request the same as your branch. To the right there is a tab
called projects. Add the request to the current GIRAF project. For the first
sprint you would add it to the project called "2020 1. sprint", for the second
sprint "2020 2. sprint" and so on.   

Next, include pictures (or a gif/video) of all the screens that you added, in
the text field, so someone from the product owner group can verify that the
screens follow the design manual.

Remember to include the text "fixes \#YourIssueID". This will automatically
close the issue when the pull request is merged.
When the PR is closed, check your issue to make sure that it has been closed
too.

Now all that is left is for you to inform the process group, and ask them to
assign reviewers. They will assign reviewers who will review your pull request.

## How To: Get Code in Review

In order to get code into review, you firstly have to make sure that the tests
you wrote all pass, and that they cover the relevant parts of the written code.
The way you make a pull request (PR) starts by visiting github.com. You navigate
to the repository in which you've done your work. Go to the pull requests tab,
click the "new pull request" button. Then you select the correct base and
compare branch, and then your create a pull request.

Otherwise, if you have recently pushed commits github will actually suggest if
you want to create a pull requests, this eases the process. 

When a pull request have been created, you have to notify the process group,
write them or talk to them. The process group is responsible for delegating the
two reviews which are needed to merge the pull request.
The review will be performed by others than the group who wrote the code, thus
we use external review.
Once the pull request is in the review phase, you should be able to in the
meantime work on other user stories, or simply write about the user story in
your report.
When other groups review you PR, they most likely have some form of feedback,
comments, or some things they do not understand.
Thus it is to prefer if both the reviewers and the ones responsible for the pull
request are quickly to respond to comments on github.
Once the reviewers have approved the pull request is able to merged.

## How To: Review a Pull Request

When reviewing a pull request it is absolutely important that you consider the
goal of the review: Value should be added to the project, and the developers
involved should gain knowledge and improve.
As such, it is important to keep a light and educational tone when involved with
the pull requests.

When reviewing a pull request, you should check for points in the
[Code Review Checklist](../Review_Checklists/2020F/review_checklist_code.md).

In case a point is not fulfilled you should leave a comment that points out the
problem, why it is a problem, and, if possible, how to develop a solution. When
reviewing the code, you can click on the "Files Changed" tab, in which you will
be able to see all changes to the code. If you click on the left side of the
code, right besides the line numbers, there will be a small, blue plus button
available, which will let you leave a comment to this specific line of the code.
If possible, you should always leave a comment on the line of the code that is
problematic.

As a reviewer you should never commit to the branch with the pull request, merge
the pull request, or delete the pull request. Since the first two actions
*might* introduce problems to the codebase, the author of the pull request
should always do these things, as that person will be best suited to handle
potential problems.

If you are reviewing a complex piece of code, or a particularly problematic
piece of code, it is highly advisable that you locate the author of the pull
request, and walk through the code with them, side by side, in order to clarify
any misunderstandings efficiently and effectively.

## How to: Create an issue

While the PO group are the ones responsible for creating user stories, there
might be times where other groups feel the need to create issues on GitHub.
With the Weekplanner repository as the example, people can either create a
*Task Creation Request* or a *Bug Report*. To do this you go to the Weekplanner
repository on GitHub and select the Issues tab. On the right side of the page,
right above the list of issues you should see a green button labeled
*New issue*. Clicking on this button takes you to a page where you can select to
create either a *Bug Report* or a *Task Creation Request*. If you are in doubt
as to which one to choose the the following can be of help:

- If you want to report unexpected behavior in already existing functionality of
  the application, you should choose *Bug Report*.
- If you feel that the application needs functionality that is out of your
  current scope and that you do not feel is being represented in other user
  stories, then you should choose *Task Creation Request*.

Once you choose one of the two options and click the respective button you
should see a page with a form that asks you for a title.
The title for the *Task Creation Request* should tell what functionality you
would like added using the shown form "As a developer I would like the docker
config file to automatically update so that I don´t have to manually update the
config file". 
Instead of the task being for the developer, guardian or user is also frequently
used.
For the bug the title should be the problem at hand, not the solution. ex. "A
error message pops up whenever the app is open".
  
There is a field underneath the title in which you write a description of what
you want to report on.  
Note that the field where you can write a description is already filled out with
a template on how to structure your own description. 
Once you have created a good title and written a description of the issue you
click on the green *Submit new issue* button at the bottom of the form. With
this you have created your issue.

It can be a good idea to inform the PO group, so they can assign and refine the
issue.

You have now created your issue, congratulations!
