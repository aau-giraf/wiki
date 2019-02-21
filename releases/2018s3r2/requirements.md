## PO Requirements for release 2018S3R2 - User settings

Scheduled for releases on Tuesday 8th of May 2018

**Relevant user stories**
[T1236](http://web.giraf.cs.aau.dk/T1236), [T1237](http://web.giraf.cs.aau.dk/T1237), [T1239](http://web.giraf.cs.aau.dk/T1239), [T1240](http://web.giraf.cs.aau.dk/T1240), [T1241](http://web.giraf.cs.aau.dk/T1241), [T1242](http://web.giraf.cs.aau.dk/T1242), [T1243](http://web.giraf.cs.aau.dk/T1243), [T1261](http://web.giraf.cs.aau.dk/T1261)

**Requirements**

The settings menu as shown in the prototype must be implemented and accessible from the weekschedule view when viewing from the guardian perspective.

Furthermore, the ability for citizens to mark activities as completed, and for guardians to mark activities as cancelled, must be included in this release.

![settings](https://github.com/swuf/wiki/blob/master/releases/2018s3r2/settings.png "settings")

Following user stories must be implemented:

* Marking an activity as completed (Task ~~[T1221](http://web.giraf.cs.aau.dk/T1221)~~)
    * Citizens must be able to mark an activity as completed, using a variety of visual options. These include checkmark, making the activity appear grey, removing the activity from the view, and moving them to the right.
    * An activity can be marked as completed by accessing the activity page in citizen mode and pressing a button in this page.
    * **This release must include the option to checkmark an activity.**
* Marking an activity as cancelled (Task ~~[T1221](http://web.giraf.cs.aau.dk/T1221)~~)
    * Guardians must be able to mark an activity as cancelled, using a variety of visual options. These include a red cross, and removing the activity from the view.
    * An activity can be marked as cancelled by accessing the activity page in guardian mode, and pressing a button in this page.
    * **This release must include the option to cross an activity off with a red cross.**

The following functionality must be implemented:
* When exiting a week schedule, a popup window should warn whether or not the guardian would like to save the changes made to the schedule.

The following user settings must be implemented:
* App theme (Valg af tema)
    * Changing the app theme affects the colours of bars and buttons, but not the days or activities.
    * **For this release, four themes must be implemented: red, yellow, green, and the standard blue android.**
    * The implementation should prepare for more themes to be added in the future.

* Week Schedule Colours (Farver på ugeplan)
    * Changing the week schedule theme determines the colours of the day-columns in the weekschedule.
    * The guardian must be able to specify the colour of each day in the schedule.
    * Citizens must as a default use the colour-scheme used by the department.
        * Monday: Green, Tuesday: Purple, Wednesday: Orange, Thursday: Blue, Friday: Yellow, Saturday: Red, Sunday: White.
    * The optimal solution would be to choose from at least 16 predefined colours.
    * **This release must include at least 8 different colours, 7 of them being the colours used in the colour-scheme mentioned above.**
