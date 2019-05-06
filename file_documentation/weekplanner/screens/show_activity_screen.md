# show_activity_screen

## Functionality
The *show_activity_screen* is the screen used to display a chosen activity. From the screen the user have the possibilty to mark an activity as done, or remove the mark from the activity

## Layout
![Screen used to show an activity](../pictures/show_activity_screen.png)


## Buttons
pressing the checkmark ether marks the activity as done or unmarks it. 

## Code
The primary functionaility of the screen is implemented in the functions *buildActivity* and *buildButtonBar*. The *buildActivity* function uses a streambuilder with the *_activityBloc.activityModelStream* to get the tapped activity. The *buildActivity* function also uses a stack to, place a checkmark above the pictogram.

The *buildButtonBar* function also uses a streambuilder with the same stream as *buildActivity*. The reason for this is to be able to check if the loaded adcitivty is already marked as done, or not done. The layout of the button also has to change depending on the situation, either it should be a checkmark as seen in layout or an arrow, indicating a revert. 


