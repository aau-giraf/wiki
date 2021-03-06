# Buttons

This section describes the design guides for using buttons in GIRAF.

## States

A button should have three states: default, pressed and disabled.
The background of a default button should have a yellow/orange (see color guide)
gradient background with a darker border. When a button is pressed, the background
should become darker alongside an even darker border. The background and the border
should be identical to the default button when a button is disabled, however this
button should have an opacity of 40%.

| ![ButtonDefault](images/ButtonDefault.png) | ![ButtonPressed](images/ButtonPressed.png "ButtonPressed") | ![ButtonDisabled](images/ButtonDisabled.png "ButtonDisabled") |
|:--:| :--: | :--: |
| *Default button* | *Pressed button* | *Disabled button* |

A widget called GirafButton has been created in the weekplanner repo which should
be used for buttons in the weekplanner app. If the button is added within the citizen view, no text should be added to buttons.

## Content

Buttons can either contain text, an icon or both.
If the action of the button can be symbolized easily with an icon that the users
are familiar with, only an icon should be used for the button.
Text should be used to describe it instead if an icon is not sufficient for explaining
the action. An icon together with text should be used in cases where the icon helps
to understand the text.

## Contextual ordering

When a collection of buttons are shown in the same context, the buttons should be
ordered by whether or not the button represents an action to confirm a change.
The leftmost buttons should cause the action to not occur, such as cancelling the
deletion, and the rightmost buttons should confirm the action, such as saying yes
to a deletion.

## Multiple state selection buttons

If multiple states need to be represented it should be done by creating a multiple state button. On this button the current state should have a darker gradient than the other states. This should **only** be used when only one of the states can be selected at the time.

![TripleStateButton](images/TrippleStateButton.png)
