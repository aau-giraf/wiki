# weekplan_screen.dart
This file documents the weekplan_screen.dart file in the weekplanner project.

## Functionality
The screen is the one responsible for showing all the days of the week. Each day in the weekplan_screen is displayed with all the planned activities for this single day. The colors of the days are a standard to help autistic children. From the Weekplan screen different functionality can be accessed:

* Adding activies
* Accessing an activity
* Move mctivities

The weekplan screen also uses the giraf_appbar which also adds functionality

## Layout 
The weekplan screen is displayed as seen here:
![Layout of screen](../pictures/weekPlannerScreen.PNG)

## Buttons
The buttons used in the weekplan screen are the addactivity buttons. One button is placed at the bottom of each day. 
Tapping an ad activity button open a new screen the pictogram_search_screen in which the user can search for pictogram to add. 


## Code

Each day is a column with a ListView, the ListView is 
scrollable. Thus when enough activities are added to a day. You can scroll (finger upwards) to see
the next activies. The activities are added by pushing the button with a plus button, located at the
bottom of the column. The button for add activity are located inside the day column but outside of the listview and thus they don't follow the scrolling.<br>


## How is the screen built
