# Test in Flutter

The Process manual states that code should be properly tested before a user story
is done. This guide describes how you test in Flutter, and what the test criteria
is in both blocs and screens/widgets.

## Test location

All tests have to be located in the "test" folder. All Weekplanner files should
have a corresponding file in the test folder where all tests related to the file
are located. The test files should be in the folder that corresponds to the content
of the file. For example, screen testes should be in the screen folder.

## Test basics

A test file always contain a main function. The main function is placed directly
into the file, and not in any type of class, and all tests are written in the main
function.

### Setup

When several tests are run, they often share the same setup. You can automate the
setup by creating a `setUp()` function in the main function. The setup function
is then called every time a new test is run. The main function could look like this:

```dart
void main() {
    SomeClass a;
    SomeOtherClass b;
    BlocType bloc;

    setUp((){
        a = <Some value>;
        b = <Some other value>;
        bloc = bloc(some API);
    });

    //The tests go here
}
```

The variables you use in the `setUp()` function should be declared in the beginning
of the main function, right before the `setUp()` function.

### Expect

When you run a test you need to compare values to see if the test is successful.
In Flutter this is done with an expect function. This is written:

```dart
    expect(value, expected_value);
```

There can be several expects inside the same test. Aside from an actual value, you
can use a lot of different find predicate. The most commonly used is the following:

```dart
expect(<variable>, isTrue);
expect(<variable>, isFalse);
expect(<variable>, equals(<value>));
expect(<variable>, findsNothing);
expect(<variable>, findsNWidgets(<number>));
expect(<variable>, findsWidgets);
expect(<variable>, findsOneWidget);
expect(<variable>, find);
expect(<variable>, false);
expect(<variable>, true);
```

## Writing tests

There are a significant difference between a widget/screen test and a bloc test.
The tests for these two are explained separately.

### Blocs
A test for a bloc looks like this:

```dart
 test('Test description',(){

 });
```

If the code does not run in sequence you should use an async test, that looks this
 way:
 
```dart
 test('Test description', async((DoneFn done){
     done();
 }));
```

A standard bloc test will finish when all the code are executed while an async bloc
test will finish when the done() function is called. If you make an async test,
you should always remember to call the done() function in bloc, otherwise the test
will continue until it times out, and then fail. The done() function is placed inside
the async function.

```dart
import 'package:<All the different imports>';

void main() {
    SomeClass a;
    SomeOtherClass b;
    BlocType bloc;

    setUp((){
        a = <Some value>;
        b = <Some other value>;
        bloc = bloc(some API);
    });

    test('This is a standard test',(){
        a.someMethod(b);
        expect(b.someFunction, 2);
        expect(a.someFunction, 3);
    });

    test('This is an async test',async((DoneFn done){
        bloc.steamA.skip(1).listen((SomeModel model){
            expect(model.content, value);
            expect(model.otherContent, otherValue);
            done();
        });
        bloc.setA(value);
    });
}
```

In the async test, the listen function is defined first. In the async test a listen
and listen function is set up on a steam in the bloc. When a set function on the
behaviour subject of the stream is called, the listen function is called, and in
here the expect() and done() functions.

## Widgets and screens
The widget and screen tests separate from the class tests. All tests are still in
the main() function and you can still use a setup function, but instead of the norma
tests you use test widgets.

```dart
    testWidgets('Name',(WidgetTester tester) async {
        await tester.<Something to wait for>;
    });
```

Inside the `testWidget()` you use a `WidgetTester` object. This is used to interact
with widgets in the test environment. When you use the `WidgetTester` object for
actions, you should use the await keyword before.

In blocs you use the done() function when running an async test. This is not done
in `testWidgets()`. However, if you use a listener in your expect, you use something
called a completer.

```dart
    testWidgets('Name',(WidgetTester tester) async {
        final Completer<datatypeA> done = Completer<datatypeA>();

        bloc.someBloc.listen((datatypeA) async{
            await tester.pump();
            expect(success, true);
            done.complete();
        });
        await done.future;
    });
```

There are some basic functions we use a lot on the `WidgetTester` object.

The first is `pumpWidget()`. This acts by setting up a screen in your test environment.
This makes it possible to test on the screen, for example if the right elements
are present. You can write it like this:

```dart
await tester.pumpWidget(MaterialApp(home:SomeScreen()));
```

This set up the `SomeScreen()` screen.

Another important function is the `pump()` function. This is used to execute actions,
by rendering the screen. If you want to wait for a duration of time, you can note
this as an attribute.

If you want to test more actions in sequence, you should use `pumpAndSettle()`.
This is for example if you want to push a button that makes something else happen,
and test if that happens.

You can also use the `tester.enterText()` widget. This looks like this:

```dart
await tester.enterText(find.byType(TextField,query));
```

This also shows the `find.byType()` function, that searches in the widgets in the
tester and finds by a certain type, here `TextField`, a widget with a name matching
the query. The query is a string and could for example be 'cat'.

The `WidgetTester` has many other functions you should explore when needed. The
key thing is to understand that a `WidgetTester` interacts with widgets in the test
environment. The environment can be updated with the `WidgetTester`, and widgets
extracted with "find".

The expect is similar to the bloc expect, but in the actual part you can use "find"
to choose the widgets you test on.

Examples of `TestWidget` expects are:

```
    expect(find.byWidgetPredicate((Widget widget) =>widget is WidgetType), <FINDINGS>);
    expect(find.byType(WidgetType),<FINDINGS>);
```

## Mocking

When you write tests, you will often need to mock certain objects. This section
describes the different mocking often used in GIRAF testing.

### Mock screen
When you test a non screen widget you can use to have a `MockScreen` as a container.
This is written in the test document, outside the `main()` function and can look
like this:

```dart
class MockScreen extends StatelessWidget {
    @override
    Widget build(BuildContext context) {
        return Scaffold()
    }
}
```

You can fill the `MockScreen` with all the content you find necessary to do the
tests.

### Dependency injection

All dependency injections are automatically set up in the `bootStrap.dart` file.
If you need to change a dependency in for a test, you can do it directly on the
dependency injector. This can look like this:

```dart
newDependencyBloc = SomeBloc();
di.clearAll();
di.registerDependency<SomeBloc>((_)=> newDependencyBloc);
di.registerDependency<Bloc1>((_)=> StandardBloc1());
di.registerDependency<Bloc2>((_)=> StandardBloc2());
```

The `newDependencyBloc` is the bloc that you want to replace the original dependency
with. Before you add a new dependency, you have to clear all dependencies. This
means that if you need dependencies that are otherwise there as a standard, you
have to add them again. I dependencies are not relevant, you should not add them.

### Mock API

All Weekplanner testing should be independent of the current state of the database.
If you need database access for your test, you create a mock API. If we for example
wanted to use an API class called `SomeAPI`, we would write it like:

```dart
class MockSomeAPI extends Mock implements SomeAPI {}
```

This is done outside the `main()` function in the test file.

If you need to use the mock API in a bloc you can do it like the following:

```dart
import 'package:<needed packages>';

class MockSomeAPI extends Mock implements SomeAPI {}

void main() {
    BlocClass bloc;
    API api;
    MockSomeAPI someAPI;

    setUp((){
        api = API('Write anything');
        someAPI = MockSomeAPI();
        api.some = someAPI();
        bloc = BlocClass(API);
    });
}
```

Here, the `api.some` field in the API corresponds to the API of the `someAPI` type
in the class. Now you can use your bloc like normal, you just have to add the needed
information to the `someAPI`.

If you need the API to do something when it is updated, you can write a `setupAPICalls()`
function before the `setUp()` function. This function should be called inside the
`setUp()` function, so it is called every time the API is updated inside the tests.
The function could look like the following:

```dart
void setupAPICalls() {
    when(someAPI.update())
}
setUp((){
    setUpAPICalls
})
```

### Override

In mock classes you can override elements to change functionality when needed.

An example of this is in a mock API, where you can override a function that should
give you some specific data from the database.

```dart
class MockSomeAPI extends Mock implements SomeAPI
    @override
    Observable<ARelevantModel> SomeAPIMethod() {
        return Observable<AReleventModel>.just(ARelevantModel(
            id: '1',
            info1: 'Cat'
            info2: 3
        ));
}
```

This is a good way to mock information in the database that you need to test.

When you mock a bloc, you can also do it the same way. The difference is that you
override Observable objects instead of API calls. An example of this is:

```dart
@override
Observable<bool> get someStream =>
    observable<bool>.just(input);
```
