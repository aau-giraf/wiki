# Guidelines for error handling in the weekplanner from the wep-api
This section will cover guidelines on how to catch exception in the weekplanner from the web-api and what should happen 
when the exception is caught.

##TL;DR guidelines

* Use OnError function when listening to a stream: ``` Listen().OnError ``` to catch the error.
* Add a case with the requested ErrorCode in the switch statement within getErrorMessage method

## How to use a stream
In order to be able to get values from a stream you need to do something referred to as subscribing or listening.
When you subscribe to a stream you will only get the values that are emitted (put onto the stream)
after the subscription. You subscribe to the stream by calling the listen function and supplying it with a method to 
call back to when there's a new value available, commonly referred to as a callback method, or just a callback.

### Catching an API error from a stream in the weekplanner
The listen call returns a ````StreamSubscription```` with the type of the stream. With a stream subscription
it is possible to use the onError function, which takes and error object and the stack trace as parameters.
An example of onError usage on a listen call from new_citizen_screen.dart on the weekplanner can be seen below.

````

onPressed: () {
   _bloc.createCitizen().listen((GirafUserModel response) {
     if (response != null) {
       Routes.pop<GirafUserModel>(context, response);
       _bloc.resetBloc();
     }
   }).onError((Object error) =>
       _translator.catchApiError(error, context));
}

````

_translator is the referenced ApiErrorTranslater class that holds the catchApiError method.
This class is found in errorcode_translater.dart. Referring to this class is done by instantiating the class:
```` final ApiErrorTranslater _translator = ApiErrorTranslater(); ````
The class ApiErrorTranslater holds two methods: catchApiError and getErrorMessage.

#### Catching API errors method
The catchApiError method builds a pop up GirafNotifyDialog. The string for the error message is received
from the other method getErrorMessage.

```

void catchApiError(Object error, BuildContext context) {
   showDialog<Center>(

   /// exception handler to handle web_api exceptions
   barrierDismissible: false,
   context: context,
   builder: (BuildContext context) {
   return GirafNotifyDialog(
   title: 'Fejl',
   description: getErrorMessage(error),
   key: const Key('ErrorMessageDialog'));
   });
}  

```

#### Creating new error message method
In this method you will need to add a new case for a specific ErrorKey with a return call on an error message string.
````

///Get apropriate error message based on error code
  String getErrorMessage(ApiException error) {
    switch (error.errorKey) {
        case ErrorKey.UserAlreadyExists:
        return 'Brugernavnet eksisterer allerede';
      case ErrorKey.Error:
        // Undefined errors, the message is in english
        // as we cant predict why it was cast
        return 'message: ' +
            error.errorMessage +
            '\nDetails: ' +
            error.errorDetails;
      default:
        return 'Ukendt fejl';
    }
  }

````