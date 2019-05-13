# Test in Flutter

The Process manual states that code should be properly tested before a user story is done. This guide describes how you test in Flutter, and what the test criteria is in both blocs and screens/ widgets. 

## Test location
All tests have to be located in the "test" folder. All Weekplanner files should have a corresponding file in the test folder where all tests related to the file are located. The test files should be in the folder that corresponds to the content of the file. For example, screen testes should be in the screen folder.

## Test basics
A test file always contain a main function. The main function is placed directly into the file, and not in any type of class, and all tests are written in the main function.

### Setup
When several tests are run, they often share the same setup. You can automate the setup by creating a setUp() function in the main function. The setup function is then called every time a new test is run. The main function could look like this:

``` Dart
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

The variables you use in the setUp() function should be declared in the beginning of the main function, right before the setUp() function. 

### Expect
When you run a test you need to compare values to see if the test is successful. In Flutter this is done with an expect function. This is written:
``` Dart
    expect(value, expected_value);
```

There can be several expects inside the same test. Aside from an actual value, you can use a lot of different find predicate. The most commonly used is the following:
``` Dart
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
In the normal test, the test will finish when all the code are executed, while an async test on a standard class will finish when the done() function is called. If you do an async test, you should always remember to call the done() function in standard classes, because else test will continue until timeout and then fail. 

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
        await tester.<Something to wait for>;
    });
```
Inside the testWidget you use a WidgetTester. This is used to interact with widgets in the test environment. When you use the WidgetTester for actions, you should use the await key word before. 

In standard classes you use the done() function when running an async test. This is not done in testWidgets. However, if you use a listener in your expect, you use something called a completer.
``` Dart
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

There are some basic functions we use a lot on the WidgetTester.

The first is pumpWidget. This acts by setting up a screen. You can write it like this:
``` Dart
await tester.pumpWidget(MaterialApp(home:SomeScreen()));
```
This set up the SomeScreen screen.

Another important function is the pump() function. This is used to execute actions, by rendering the screen.

You can also use the tester.enterText widget. This looks like this:
``` Dart
await tester.enterText(find.byType(TextField,query));
```
This also shows the find.byType function, that searches in the widgets in the tester and finds by a certain type, here TextField, a widget with a name matching the query. The query is a string and could for example be 'cat'.

The WidgetTester have many other functions you should explore when needed. The key thing is to understand that a WidgetTester interacts with widgets in the test environment. The environment can be updated with the WidgetTester, and widgets extracted with "find".

The expect is similar to the standard class expect, but in the actual part you can use "find" to choose the widgets you test on.

Examples of TestWidget expects are:

```
    expect(find.byWidgetPredicate((Widget widget) =>widget is WidgetType), <FINDINGS>);
    expect(find.byType(WidgetType),<FINDINGS>);
```

## Mocking
When you write tests, you will often need to mock certain objects. This section describes the different mocking often used in GIRAF testing. 

### Mock screen 
When you test a non screen widget you can use to have a MockScreen as a container. This is written in the test document, outside the main() function and can look like this:
``` Dart
class MockScreen extends StatelessWidget {
    @override 
    Widget build(BuildContext context) {
        return Scaffold()
    }
}
```
You can fill the MockScreen with all the content you find necessary to do the tests.

### Dependency injection 
All dependency injections are automatically set up in the bootStrap.dart file. If you need to change a dependency in for a test, you can do it directly on the dependency injector. This can look like this:
```` Dart
newDependencyBloc = SomeBloc();
di.clearAll();
di.registerDependency<SomeBloc>((_)=> newDependencyBloc);
di.registerDependency<Bloc1>((_)=> StandardBloc1());
di.registerDependency<Bloc2>((_)=> StandardBloc2());
```` 
The newDependencyBloc is the bloc that you want to replace the original dependency with. Before you add a new dependency, you have to clear all dependencies. This means that if you need dependencies that are otherwise there as a standard, you have to add them agin. I dependencies are not relevant, you should not add them. 

### Mock Api
All Weekplanner testing should be independent of the current state of the database. If you need database access for your test, you create a mock Api.
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

