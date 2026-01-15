# Issue 418

This issue has a [branch](https://github.com/aau-giraf/weekplanner/tree/feature/418) in the weekplanner repository. 

## What currently exists

At the time of writing (December 2020) the functionality requested in [#418](https://github.com/aau-giraf/weekplanner/issues/418)
has been implemented.
However, the design of the implementation is not made in accordance to the prototype given in the issue. The design is
oriented more towards the Material Design principles, as this is better for interaction on smartphones compared to the
design presented in the prototypes. In the case you want the solution to be more oriented towards the Material Design
principles, it is possible to move the search bar up into the app bar.

## Implementing prototypes

If you want to implement the prototypes given on the issue page, you will need to implement a complete refactor of the
weekplan view. Furthermore, in this case you cannot use the solution on the branch, except for the search method.
This refactor will have to implement a state to contain the weekplans which the user should be viewing. Then have the
weekplan screen reactively alter the view to reflect the weekplans contained in the state.
