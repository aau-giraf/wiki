# Handover Guide

This guide explains which sections that should be added or updated in the Wiki
whenever a GIRAF team is finished with a semester.

## New Sections

Here is a description of the new sections that has to be added to the Wiki.

### Main Handover

The placement of the main handover from a GIRAF team is illustrated below. The
five main things to include are:

- Description of role structure
- Description of sprint events
- Description of the tools that has been used (Scripts, Google Sheets etc.)
- Description of the overarching features that have yet to be implemented and list the issues related to these
- Description of incomplete issues that should continue being worked on

```
Handover
├── Handover Guide
├── Semester name                 # New section
│   ├── Role Structure            #    
│   ├── Sprint Events             #
│   ├── Tools                     #      
│   │   ├── Process Group         #  
│   │   └── Other Tools           #
|   ├── Feature Overview 
│   └── Issues
├── ...
├── 2020E
├── 2020F
├── 2019
└── 2018       
```

**Semester name** is the year a semester is held e.g. 2020.
 
2020 is followed by E or F because GIRAF was worked on in both the Spring (F)
and Autumn (E) semester.

### Feature Overview

This document should describe overarching features that have multiple related issues.
The purpose of this document is to make it easy for the next GIRAF teams to get 
an overview of these larger features without having to go through all issues in 
all the repositories.  

For each feature there should be a headline in the feature_overview.md file. 
Under this headline there should be a description of the feature, as well as 
a table containing all the issues related to the feature.   
The table should have a column containing links to the issues, and a column 
containing their descriptions. This description can simply be the title 
of the issue.

### Issues Handover

Any fundamental issues that have had work done on them can also be handed over to
the next GIRAF team.
These issues can or cannot have an active pull request.
In order to make it possible for future GIRAF teams to work on such issues, an
adequate amount of documentation should be written about the issues in the `Issues`
folder in the main handover.

For these kinds of issues there are two recommendations:

- If an issue warrants continued work by a future GIRAF team, then the issue
  should have handover documentation on the wiki. If there is handover material
  for the issue, then its branch should **NOT** be deleted. If the issue has a pull request, the pull request **SHOULD**
  be rejected.
- If the work done on an issue is not worthy for handover, then its branch should be deleted.
  Then, the assignee should document what they tried to do to solve the issue as
  a comment to the issue itself on GitHub.

## Updated Sections

Here is a description of the sections that needs to be updated.

### Prototypes

The PO group should add links for the new prototype files.

```bash
UI_Design
└── Prototypes
    └── Overview    # File to update       
```

The newest entry should be the top most in the table shown in the overview. 
