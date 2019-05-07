# weekplan_screen.dart
This file documents the `weekplan_screen.dart` file in the Weekplanner project.

## Functionality
The screen is the one responsible for showing all the days of the week. The `weekplan_screen` displays each day with all its planned activities. The colors of the days are a standard to help autistic children. From the Weekplan screen different functionality can be accessed:

* Adding activities
* Accessing an activity
* Moving activities

The `weekplan_screen` also uses the `giraf_appbar` which also adds some functionality.

## Layout 
The weekplan screen is displayed as seen here:
![Layout of the screen](../pictures/weekPlannerScreen.PNG) 
The activity on Thursday is an activty marked as done, whereas the one on Wednesday is not done yet.

## Buttons
The buttons used in the weekplan screen are the addactivity buttons. One button is placed at the bottom of each day. 


## Code
The `weekplan_screen` is a widget must, therefore, implement the build method, as seen here:

```dart
@override
  Widget build(BuildContext context) {
    return StreamBuilder<WeekplanMode>(
        stream: authBloc.mode,
        builder: (BuildContext context,
            AsyncSnapshot<WeekplanMode> weekModeSnapshot) {
          return Scaffold(
            appBar: GirafAppBar(
                title: 'Ugeplan',
                appBarIcons: (weekModeSnapshot.data == WeekplanMode.guardian)
                    ? <AppBarIcon>[
                        AppBarIcon.changeToCitizen,
                        AppBarIcon.settings,
                        AppBarIcon.logout,
                      ]
                    : <AppBarIcon>[AppBarIcon.changeToGuardian]),
            body: StreamBuilder<UserWeekModel>(
              stream: weekplanBloc.userWeek,
              initialData: null,
              builder: (BuildContext context,
                  AsyncSnapshot<UserWeekModel> snapshot) {
                if (snapshot.hasData) {
                  return _buildWeeks(snapshot.data.week, context);
                } else {
                  return const Center(
                    child: CircularProgressIndicator(),
                  );
                }
              },
            ),
          );
        });
  }
```

The *build* method returns a `StreamBuilder` which uses the `AuthBloc`'s `mode` stream. The `AuthBloc`'s `mode` stream tells whether a guardian or citizen uses the app. The layout of the screen is dependant on this. The `StreamBuilder` inside the `Scaffold` uses the stream of `WeekplanBloc.userWeek`. This stream emits the active `UserWeek`. We call *_buildWeeks* if there is data in the stream, and a `CircularProgressIndicator` is shown otherwise.

The *_buildWeeks* method is one of the multiple help functions used to build the layout. *_buildWeek* creates all the different days of the week. The *_buildWeek* method does so by returning a `Row` for each day.

The *_day* function returns a `Column` with a `ListView` in it. The `ListView` contains all the activities for a day. The *_day* function also calls *_dragTargetPlaceholder()* to display grey placeholders, when an activity is to be moved. The *_day* function also builds the `addActivity` buttons in the bottom of each day.

The *_pictogramIconStack* is used to add the accept icon once an activity is done as seen on Thursday in the layout section.

Two functions allow for the moving of images, *_dragTargetPlaceholder* and *_dragTargetPictogram*

The *_getPictograms* is used to load the image of a specific image id.

The *_translateWeekDay* is used to translate an enum type to a textstring. 

## Structure
The UML diagram shows the structure of *weekplan_screen*.
![The structure of](../pictures/WeekPlanScreen.png)
