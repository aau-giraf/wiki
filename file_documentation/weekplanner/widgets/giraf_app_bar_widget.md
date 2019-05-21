# Documentation of giraf_app_bar_widget.dart
This files contains the documentaion of the `giraf_app_bar_widget.dart` file from the weekplanner project.

## Functionality
This widget is the appbar at the top of many screens in the weekplanner application. The displayed icons are chosen dynamically and depends on the current screen and user mode. The icons as well as their functionality are provided by `toolbar_bloc.dart`. 

## Layout
The Giraf appbar is displayed as seen here, when located on the weekplan screen (`weekplan_screen.dart`):

![Layout of Giraf app bar](../pictures/GirafAppbar.PNG)

## Buttons
The appbar can contain many different buttons. To name a few: settings, logout, change to guardian, and change to citizen, all the icons can bee seen in `toolbar_bloc.dart`.

## Code
Giraf appbar is a stateless widget, thus it contains the build function which "describes" how the appbar should look:

```dart
 @override
  Widget build(BuildContext context) {
    toolbarBloc.updateIcons(appBarIcons, context);
    return AppBar(
        title: Text(title, overflow: TextOverflow.clip),
        flexibleSpace: const GirafTitleHeader(),
        actions: <Widget>[
          StreamBuilder<List<IconButton>>(
              initialData: const <IconButton>[],
              key: const Key('streambuilderVisibility'),
              stream: toolbarBloc.visibleButtons,
              builder: (BuildContext context, 
                AsyncSnapshot<List<IconButton>> snapshot) {
                return Row(
                  children: snapshot.data
                );
              }),
        ],
        automaticallyImplyLeading: isGuardian,
    );
  }
  ```
The Giraf app bar consists of an app bar with buttons which are emitted from the stream called `toolbarBloc.visibleButtons`. That stream is populated with buttons by the method `toolbarBloc.updateIcons` which is the reason it is called as the first method.
