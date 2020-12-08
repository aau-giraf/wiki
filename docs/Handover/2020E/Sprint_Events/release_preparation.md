# Release Preparation

If a release is made a Release Preparation event should be held at the end of the sprint, before the release.

## Expected Duration

1 day

## Purpose

To find system breaking bugs and then fixing them before making a release.

## Before Release Preparation

The Process group will set up a release branch for each of the repositories.

## Agenda

The release branches are tested and fixed continuously in all their respective repositories.
All the Development teams will test all the time and when they find a bug, they must create an issue on github. 

### Testing

The whole system should be tested by the development teams,
with the intention of finding bugs or deficiencies in the code base. 

If a bug or a missing functionality is discovered:

- If it is a system breaking bug:
    - Create an issue in the relevant repository, using the _ReleaseFix_ label.
- If it is a bug that does not hinder release, a missing functionality, or badly written code etc.:
    - Create an issue in the relevant repository, using the relevant labels.
    
The GitHub bot posts a notification in the #issues channel on slack whenever a new issue is created.
If the issue is labelled ReleaseFix, the Process group will assign the issue to a Development team.

### Fixing Release Bugs

You get ReleaseFix issues from the Process group. 

Then you must make a new branch named releasefix/#IssueNumber, branched out from the release branch. 

After fixing the issue in said branch, you should make a pull request for it. 
