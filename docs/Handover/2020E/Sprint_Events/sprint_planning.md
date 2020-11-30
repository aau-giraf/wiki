# Sprint Planning

Everyone on the GIRAF Scrum team (PO, Process and Development teams) attend this
event that marks the start of a sprint.

## Expected Duration

**Max** 4 hours (Adjusted for 2 week sprint).

## Result 

A prioritized list of issues for each Development team to work on during the sprint.

## Before the Sprint Planning

Prior to Sprint Planning the Process group and the PO group have decided which
issues to include in the Sprint Backlog. Only those issues will be time estimated and
prioritized during Sprint Planning. Minor adjustments may be made afterwards
based on the outcome of the Sprint Planning.

Next, everyone is divided into Sprint Planning Cross-groups. 

- Each Sprint Planning Cross-group has at least one Process group member and one
  PO group member. This means that the number of Sprint Planning Cross-groups
  cannot exceed the number of members in the Process or PO group.
- The Sprint Planning Cross-groups are created randomly for each sprint.
- The Sprint Planning Cross-groups are send out to the whole GIRAF team prior to
  the Sprint Planning.

After the Sprint Planning Cross-groups are made, the issues in the Sprint Backlog
should be divided evenly between the groups.

This process has been automated through the [Sprint Planning Tool](../Tools/Process_Group/sprint_planning_tool.md).

## Agenda

1. Process group member presents the following:
    - Changes made to the process, since the previous sprint, based on the information
      from Sprint Retrospective. 
1. PO group member presents the following:
    - Semester goal
        - The overall goal of the project e.g. has the goal changed since last
          Sprint Planning.
    - Sprint goal
        - The goal of this sprint.
    - New and/or important issues in the sprint
1. Time estimation begins.                             

### Time Estimation

Time estimation is done through **Planning Poker**.

**Remember to include testing, review, documentation and usability test design
in your estimations.**

Everyone has ten cards with these numbers:
 
- 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 (the fibonacci numbers).

5 is equal to an 8-hour work day. The purpose of this is to **not** think of the
numbers as hours but as **relative** to one day's workload.

The Process group member has a list of issues the group should time estimate.
Each issue is only estimated by one group. For every issue follow these steps:

1. Make sure everyone understands a given issue
    - Everyone reads the issue
    - Discuss the issue
    - If anyone is in doubt about the nature of an issue ask the PO member.
1. Guess the time required to complete an issue.
    1. Everyone picks a card and holds the value secret.
    1. Everyone shows their cards simultaneously.
    1. If the cards are more than two steps apart, then the ones with highest and
       lowest numbers present their point of view.
        - By more than two steps means that e.g 3 and 8 are two steps apart. 3
          and 5 are **not**.
    1. Repeat steps 2.a-2.c up to **3 times** or until an agreement is reached.
        - These scenarios are seen as agreements:
            - If everyone has estimated the issue to the same number. This number
              is noted.
            - If there is one between the highest and lowest estimate. The highest
              number is noted.
        - The following is done, if there is no agreement after **3 times**:
            - The median or the number closest to the median is noted e.g. with
              the numbers 3, 3, 5, 8 the median is 4 but 5 is noted since that
              is the closest fibonacci number.   

## After Sprint Planning

When all Sprint Planning Cross-groups have finished time estimation each Development
team gets back together to prioritize the issues. 

- The prioritization are made according to what the Development team would like
  to work with.
- All issues in the sprint should prioritized as either:
    - High (Want the most)
    - Medium
    - Low (Want the least)
- This list should be sent to the Process group by the end of Sprint Planning.

The Process group will then assign the Development teams to certain issues. The
assignment will use the following constraints:

- As many high priority issues as possible.
- As few low priority issues as possible.
- Equal workload between Development Teams.

The issue assignments will be sent out at most 24 hours later along with
a list of which types of issues to solve first e.g. bug fixes before features.
 
                               




