# Documentation of auth_bloc.dart
This file documents the `auth_bloc.dart` file from the weekplanner project.

## Functionality
`auth_bloc.dart` is responsible for handling the authentication in the system, such as logging in and out - and switching between guardian and citizen mode.

## Code
The function `authenticate` is used to verify if there is a matching account in the database with the given username and password. If that is the case, it sets `_loggedIn` to true and sets the users mode to guardian mode per default.

The function `logout` is used to log out the user, and sets `_loggedIn` back to false.

The function `setMode` is used to switch between guardian and citizen mode in the application.