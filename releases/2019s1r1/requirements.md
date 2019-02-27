# PO requirements for release 2019S1R1

Scheduled for release on TBD 2019

### Relevant user stories
[T1005](http://web.giraf.cs.aau.dk/T1005) and [T1242](http://web.giraf.cs.aau.dk/T1242).

## Requirements
This release focuses on one small guardian quality-of-life feature, as well as a setting for the citizens. 

### Mark activities
The guardian must be able to enter a mark state from a button on the master-detail page. The mark state enables the guardian to mark one or multiple activities (much like how it works with email inboxes, where you can mark the emails you wish to interact with.) Then after they've entered this mark state, the button to enter marked mode must be replaced by a return button that leaves mark mode and removes all marks. Also, the ability to delete all marked activities should be implemented.

### Completed marker
The completed marker is the ability to change the way an activity is marked as completed. The following options must be implemented for this release:
- Checkmark: A checkmark is placed on top of the activity. (This is already implemented, but must be an option once more options are added)
- Hide activity: The activity disappears from the citizens perspective but must still be visible to guardians so they can remove the completion marker.
- Move to the right: Move the activity further to the right in the day-column. This should only be available if the citizen also only prefers to have the weekplanner shown in portrait mode, and thus prefers to have a single day shown. 

This must be implemented on the settingspage.
