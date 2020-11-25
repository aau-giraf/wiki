# Issues Overview

This tool consists of a [Google Sheets file](https://docs.google.com/spreadsheets/d/1-sXJVpQ2t_tSH6aG8B6KGxP1lkA2jufn4xXiq2vq_og/edit?usp=sharing), and accompanying Google Scripts. The sheets involved are:

- _Issues overview_
- _Milestones_

## Purpose

This tool is meant to give an overview of all issues in the current sprint.
It finds the issues by looking for a specific milestone, and it includes both open and closed issues.

## Setup

The tool needs to be setup with data about the current GIRAF team in order to function.
The data is entered into some of the sheets, and the Google Scripts found at `Tools>Script Editor` in the menus bar.

The _Milestones_ sheet must contain any milestones used for issues by the GIRAF team on GitHub.

In the `API.gs` file found with the script editor, the `SEMESTER_START_DATE` needs to be updated to the start date of the current GIRAF teams semester.
In the same file, the `ACCESS_TOKEN` needs to be updated with a GitHub access token from one of the team members.
An access token can be generated [here](https://github.com/settings/tokens).

## Usage

The tool is used with the _Issues overview_ sheet. 
First, the milestone must be set to to any from the dropdown.
Then the sheet is updated with information about the isuses by pressing the _Update_ button. 
This button has the `getIssuesOverview` script assigned, which can be found in the `IssuesOverview.gs` file.