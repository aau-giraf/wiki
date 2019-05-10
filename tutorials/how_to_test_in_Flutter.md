# Test in Flutter

The Process manual states that code should be proporly tested before a user story is done. This guide describes how you test in Flutter, and what the test criteria is in both blocs and screens/ widgets. 

## Test location
All tests have to be located in the "test" project. All Weekplanner files should have a corresponding file in the test folder where all tests related to the file are located. 

## What should be tested
Within a bloc or...

## Test basics
The main body of the test file is written:

``` Dart
void main() {
    
}
```
The main function is placed directly into the file, and not in any type of class, and all tests are written in the main function. 

There are a significant difference between a widget/screen test and a standard class like a bloc. The tests for these two are explained separately. 

### Standard classes
A test for a standard class looks like this:
``` Dart
 test('Test desctription',(){

 });
```
If the code does not run in sequence you should use a async test, that looks this way:
``` Dart
 test('Test description', async((DoneFn done){
     done();
 }));
```
In the normal test, the test will finish when all the code are executed, while a async test will finish when the done() function is called. If you do an async test, you should always remember to call the done() function. 

We use an expect function to test values. There can be several of these in one test. This is written:
``` Dart
    expect(value, expected_value);
```

When several tests are run they often share setup. You can automate the setup by creating a setUp() function in the main function. The setup function is then called every time a new test is run. The variables you use in the setUp() function should be declared in the beginning of the main function, right before the setUp() function. A test file could look like this:
``` Dart
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
        expect(b.something, 2);
        expect(a.something, 3);
    });

    test('This is an async test',async((DoneFn done){
        bloc.something.skip(1).listen((SomeModel model){
            expect(model.content, value);
            expect(model.otherContent, otherValue);
            done();
        });
        bloc.setSomething(value);
    });
}
```
In the async test, the listen function is defined first. When the set function on Something is called, the listen function is notified and all the expect functions are called. 

## Widgets and screens
The widget and screen tests separate from the class tests. All tests are still in the main() function and you can still use a setup function, but instead of the normal tests you use test widgets. 
``` Dart
    testWidgets('Name',(WidgetTester tester) async {
        await <Something to wait for>;
    });
```
This is the basics of a testWidget. The await is used primarily before the testWidget, and the testWidget interacts with widgets and the test environment. This can be used to set up the tests. 
There are some basic functions we use a lot on the WidgetTester.

The first is pumpWidget. This acts by setting up a screen. You can write it like this:
``` Dart
await tester.pumpWidget(MaterialApp(home:SomeScreen()));
```
This set up the SomeScreen screen.

Another important function is the pump() function. This can be used to trigger the frame after some duration of time. 

You can also use the tester.enterText widget. This looks like this:
``` Dart
await tester.enterText(find.byType(TextField,query));
```
This also shows the find.byType function, that searches in the widgets the tester contains and finds, by a certain type, here TextField, a widget with a name matching the query. The query is a string and could for example be 'cat'.

The WidgetTester have many other functions you should explore when needed. The key thing is to understand that a WidgetTester "contains" a screen with widgets and blocs of a certain state. This environment can be changes and widgets extracted as needed. 

The expect in the testWidget can look like this:
```
    expect(find.byWidgetPredicate((Widget widget) =>widget is WidgetType), <FINDINGS>);
    expect(find.byType(WidgetType),<FINDINGS>);
```
The FINDINGS can be things like "findsOneWidget", "findsNothing" or "findsNWidgets(someInteger)". 

## Mock screen 
When you test a non screen widget you can use to have a MockScreen to contain it. This is written in the test document, outside the main() function and can look like this:
``` Dart
class MockScreen extends StatelessWidget {
    @override 
    Widget build(BuildContext context) {
        return Scaffold()
    }
}
```
You can fill the MockScreen with all the content you find necessary to do the tests.
## Mock Api
All Weekplanner testing should be independent of the current state of the database. When a database is needed for a test, we create a mock database.

If we for example wanted to use an Api class called "SomeApi", we would write it like:
``` Dart
class MockSomeApi extends Mock implements SomeApi {}
```
This is done outside the main() function in the test file.

If you need to use the mock api in a bloc you can do it like the following:
```` Dart
import 'package:<needed packages>';

class MockSomeApi extends Mock implements SomeApi {}

void main() {
    BlocClass bloc;
    Api api; 
    MockSomeApi someApi;

    setUp((){
        api = Api('Write anything');
        someApi = MockSomeApi();
        api.some = someApi();
        bloc = BlocClass(api);
    });
}
````
Here, the "some" field in the api corresponds to the api of the SomeApi type in the class. Now you can use your bloc like normal, you just have to add the needed information to the someApi.

If you need the Api to do something when it is updated, you can write a setupApiCalls() function before the setUp() function. This function should be called inside the setUp function, so it is called every time the api is updated inside the tests. The function could look like the following:
``` Dart
void setupApiCalls() {
    when(someApi.update())
}
setUp((){
    setUpApiCalls
})
```

