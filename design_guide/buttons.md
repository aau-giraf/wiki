# Buttons
This section describes the design guides for using buttons in Giraf.

## States
A button should have three sates: default, pressed and disabled. 
The background of a default button should have a orange/yellow (See color guide) gradient background with a darker border. 
When a button is pressed the background should become darker alongside a darker border. 
When a button is disabled the background and the border should be identical to the default button however this button should be 65% opaque.

| ![ButtonDefault](./images/ButtonDefault.png) | ![ButtonPressed](./images/ButtonPressed.png "ButtonPressed") | ![ButtonDisabled](./images/ButtonDisabled.png "ButtonDisabled") |
|:--:| :--: | :--: |
| *Default button* | *Pressed button* | *Disabled button* |

## Content
Buttons can either contain text, and icon or both. 
If the action of the button easily can be symbolized with an icon that the users are familiar with, an icon only should be used for the button. 
If an icon is not sufficient for explaining the action, text should be used to describe it instead. 
An icon together with text should be used in cases where the icon helps understand the text.

## Contextual ordering
When a collection of buttons are shown in the same context, the buttons should be ordered by negative and positive actions. Leftmost buttons should cause negative actions and the rightmost should cause positive actions.