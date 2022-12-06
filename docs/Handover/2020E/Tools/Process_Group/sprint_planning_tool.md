# Sprint Planning Tool

This tool consists of a [Google Sheets file](https://docs.google.com/spreadsheets/d/1HfL2-R5popW-aW9GkHG4HtbAxiU_wpno_mMRBVL5FQs/edit?usp=sharing),
and accompanying Google Scripts. The sheets involved are:

- _Sprint planning_
- _Issue overview_
- _Group tags_
- _Time estimations_
- _Milestones_

## Purpose

This tool is meant to assist the Process group during the Sprint Planning event.
The tool generates Sprint planning cross groups, and assigns them the issues labeled 
with the current Sprint milestone and _time estimation needed_.
In the _Issue overview_ sheet, time estimations of an issue can be set and which group is assigned
each issue can be set.

## Setup

The tool needs to be setup with data about the current GIRAF team in order to function.

The _Sprint planning_ sheet must contain the number of groups that should be made for the event, and which milestone
is used for the current sprint.

The _Group tags_ sheet must be updated with the current GIRAF teams group tags.

The _Milestones_ sheet must be updated with the current set of milestones used in GitHub.

The _Google Script_ can be found at `Tools>Script Editor` in the menus bar.
In the `API.gs` file found with the script editor, the `ACCESS_TOKEN` needs to be updated with a GitHub 
access token from one of the team members.
An access token can be generated [here](https://github.com/settings/tokens).

## Usage

As preparation to the Sprint Planning event the _Generate_ button under the _Sprint planning_ sheet should be pressed
in order to generate Sprint planning cross groups.

After an issue has been time estimated its time estimation can be set in the _Issues overview_.
When all issues have been time estimated the _Set time estimations_ button should be pressed, in order to set the
corresponding time estimation tags on GitHub.

The _Issues overview_ sheet can also be used in order to assign the different issues to the Development teams on GitHub
by pressing the _Set group tags_.
