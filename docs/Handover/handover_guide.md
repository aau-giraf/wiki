# Handover Guide

This guide explains which sections that should be added or updated in the Wiki
whenever a GIRAF team is finished with a semester.

## New Sections

Here is a description of the new sections that has to be added to the Wiki.

### Main Handover

The placement of the main handover from a GIRAF team is illustrated below. The
four main things to include are:

- Description of role structure
- Description of sprint events
- Description of the tools that has been used (Scripts, Google Sheets etc.)
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

