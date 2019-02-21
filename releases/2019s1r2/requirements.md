# PO requirements for release 2019S1R2

Scheduled for release on TBD 2018

### Relevant user stories
[T913](http://web.giraf.cs.aau.dk/T913) and [T922](http://web.giraf.cs.aau.dk/T922).

## Requirements
The release focuses on a timer for the activitypage, which is the page you get when tapping an activity. This timer is used by the citizens to keep track of time for those activities that need it, and thus the guardians must be able to place a timer on the activity page, which the citizens can then access.

### The timer
The guardian must be able to add a timer to an activity. The purpose of the timer is to time the activities that need to be timed, to remove the necessity of the guardians using a physical timer. If the guardian chooses to time an activity, the timer must be placed on the activitypage of the given activity. The guardian must also be able to set the specific length of the timer, with the visualization of a timer adapting to the length. Furthermore, the guardian must be able to add timers to future activities, to prevent them having to constantly enter the application to add a timer to an activity.

A citizen must be able to start the timer by entering the activity page for an activity marked as active and pressing a “Start” button. If the activity is not marked as active, the timer cannot be started.

### Setting for visualization of timer
Citizens visualize time in different ways. It is, therefore, necessary for the guardians to be able to choose the specific timer that a citizen wants to use. The citizens must, therefore, have a setting that specifies the visualization of the timer. As a start, the visualization setting must include the following different timers.
- Digital clock
- Egg-clock 
- Hourglass

The chosen visualization must then be used as the timer in the activity.
