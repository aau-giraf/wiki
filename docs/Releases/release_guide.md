# Release Guide

This guide gives an overview of what to do in the Wiki when making a new release
description for GIRAF. 
It is the PO group's responsibility to make this addition to the Wiki. 

## Placement in Wiki

Below is an illustration of where to place a new release description.

```
Releases
├── Release Guide
├── Semester name       # New section
│   ├── Release 2       #
│   ├── Release 1       #    
│   └── ...             #
├── ...
├── 2020E
│   └── 2020Es3r1
├── 2020F
├── 2019
└── 2018       
```

**Semester name** is the year a semester is held e.g. 2020.
 
2020 is followed by E or F because GIRAF team was worked on in both the Spring (F)
and Autumn (E) semester.

The name of a release should be in the following format:

```
<Semester name>s<Sprint no.>r<Release no.>
```

This means that the first release in Sprint 3 in the 2020E semester is called
**2020Es3r1**.

The newest release should always be the top most in the table of contents
e.g. **Release 2** is above **Release 1** as seen in the illustration.

## Release Description

A release description consists of these two things:

- A brief summary of the things that has changed in the new release
- A complete list of closed issues that is a part of the new release 

## Release Overview

When a release description is done a link and date has to be added to the
[Release Overview](./index.md). The newest release should be placed as the top
most in the table.