# How to's for developers
This file is mostly intended for helping developers understand their role in the process.

## How to: Get an issue to work on
If you have enough time to work on another issue you should do so.
Try to aim for no more than two to three issues, as you shouldn't take an issue before you can actually work on it.
There's no need for you to be assigned to an issue that you can't work on right now, as it might block others progress.

When you have decided that you have enough time for a new issue, you should go and get one.
This process is very simple.
You have two options:

**Option number 1**  
You go to the issues tab of one of the repositories, e.g. github.com/aau-giraf/weekplanner/issues and locate an interesting issue.
Then, when you have located the issue, you note the number.
That is denoted by the # and a number.

Remember the number and go to the product owner (PO) group.
Beg and plead that you are assigned the issue that you want.
The PO-group might say no for various mystique reasons.
Just remember: they have the overview of the project and probably have good reasons for saying as they do.

**Option number 2**  
Go ask the PO-group to be assigned the most pressing issue.
They will like you.

## How to: Write code
To get started writing code, you should first setup the project.
This is described in the [Setup from scratch tutorial](./tutorials/setup_tutorial/setup_from_scratch.md).

Then, after setting up the code, you should be ready to go.
Remember that all functionality related to an issue should be implemented before an issue is considered done.

In the [How to review section]()

## How to: Create a pull request

## How to: Get code in review

## How To: Review a Pull Request
When reviewing a pull request it is absolutely important that you consider the goal of the review: Value should be added to the project, and the developers involved should gain knowledge and improve.
As such, it is important to keep a light and educational tone when involved with the pull requests.

When reviewing a pull request you should check for the following points:

In case a point is not fulfilled you should leave a comment that points out the problem, why it is a problem, and, if possible, how to develop a solution. When reviewing the code, you can click on the "Files Changed" tab, in which you will be able to see all changes to the code. If you click on the left side of the code, right besides the line numbers, there will be a small, blue plus button available, which will let you leave a comment to this specific line of the code. If possible, you should always leave a comment on the line of the code that is problematic.

As a reviewer you should never commit to the branch with the pull request, merge the pull request, or delete the pull request. Since the first two actions *might* introduce problems to the codebase, the author of the pull request should always do these things, as that person will be best suited to handle potential problems.

Are you reviewing a complex piece of code, or a particularly problematic piece of code, it is highly advisable that you locate the author of the pull request, and walk through the code with them, side by side, in order to clarify any misunderstandings efficiently and effectively.

## How to: Create an issue