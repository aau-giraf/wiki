# Documentation of giraf_app_bar_widget.dart
This files contains the documentaion of the giraf_app_bar_widget.dart file from the weekplanner project.

## Functionality
This widget is representing the appbar at the top of many screens. The displayed icons are chosen dynamically and depends on the current screen and usermode. The icons as well as their functionality are provided by toolbar_bloc.dart. 

## Layout
The Giraf appbar is displayed as seen here:

![Layout of Giraf app bar](../pictures/GirafAppbar.PNG)

## Buttons
The appbar can contain a vast majority of buttons. To name a few: settings, logout, change to guardian, and change to citizen, all the icons can bee seen in toolbar_bloc.dart.

## Code
Giraf appbar is a stateless widget, thus it contains the build function which "describes" how the appbar should look:

```dart
 @override
  Widget build(BuildContext context) {
    toolbarBloc.updateIcons(appBarIcons, context);
    return AppBar(
        title: Text(title),
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
        ]);
  }
  ```
The Giraf appbar consists of an appbar which actions (i.e. buttons/icons) are the buttons emitted from the stream called toolbarBloc.visibleButtons. That stream is populated with buttons by the method toolbarBloc.updateIcons which is the reason it is called as the first thing.


