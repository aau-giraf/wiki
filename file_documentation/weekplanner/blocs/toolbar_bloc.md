# Documentation of toolbar_bloc.dart
This file documents the `toolbar_bloc.dart` file from the weekplanner project.

## Functionality
`toolbar_bloc.dart` is responsible for emitting icons through the stream `visibleButtons` which is used by the Giraf appbar to determine which icons it should display.

## Code
The function `updateIcons` is used by the Giraf appbar to indicate which icons should be shown.

The function `_addIconButton` links an AppBarIcon-enum to the correct function that creates an `IconButton` with the icon and functionality specified by the input parameters. The "_createX-methods" return an `IconButton` with the icon and functionality of X, i.e. `_createIconChangeToCitizen` returns an `IconButton` with the ChangeToCitizen icon that also has the desired functionality.