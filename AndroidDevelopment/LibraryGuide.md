# Library Guide

Rest Api Client Library is an implementation of the REST architecture style for the Giraf project. The User Guide is a quick explanation on how to use the Client Library, where the Development Guide is a more in depth guide on how we developed the library and problems that occurred during the project

## Contents

1. User Guide
    - Setup
    - Library
2. Development Guide
    - Integrating volley
        - Request queue
        - Request
        - Cache
    - Testing


## User Guide

A simple guide explaining the REST library

### Setup

You will have to include some libraries, because of the library not being transitive

In the gradle.build file of the application

```
dependencies {
compile group: 'dk.aau.cs.giraf', name: 'rest-models', version: '1.0-SNAPSHOT', changing: true
compile group: 'dk.aau.cs.giraf', name: 'rest-api-client-lib', version: '1.0-SNAPSHOT', changing: true
compile 'com.google.code.gson:gson:2.8.0'
compile 'com.android.volley:volley:1.0.0'
...
}
```

In your java code:

```
import dk.aau.cs.giraf.librest.requests.*;
import dk.aau.cs.giraf.librest.serialization.*;
import dk.aau.cs.giraf.models.core.*;
import dk.aau.cs.giraf.models.core.weekschedule.*;
import com.android.volley.*;
import com.android.volley.toolbox.*;
```

### Library

The client library implements the google volley framework. That means that the client library uses request when trying to access resources. The request is based on REST architecture, GET, PUT, POST, DELETE and we have two special request to handle login and array.

How Request general work:

```
Request<object> VolleyRequest = new Request<>(
	New Response.Listener(){
		@Override
		Public void OnResponse(Request response){
		     /** Handle object in here */
		}
	},
	New Response.ErrorListener(){
		@Override
		Public void OnErrorResponse(Request response){
		     /** Handle Error in here */
		}	
	}
); 

/** To process the request it has to be added to a Request queue*/

requestQueue.add(VolleyRequest);
```

The ```requestQueue``` is where the request is queue for execution, and the queue handles when the request is executed.
In the client library we have a singleton requestqueue to have only one queue per application.

Starting the ```requestQueue```

```
requestQueue = RequestQueueHandler.getInstance(this.getApplicationContext()).getRequestQueue();
```

We have implemented our own request based on the REST architecture.

The login request, makes the request to login. If it succeeds it will grant access to the user's data.

```
LoginRequest loginRequest = new LoginRequest(user,
	new Response.Listener<Integer>() {
	@Override
	public void onResponse(Integer statusCode) {
		// statusCode is the http status code
                // add request here to get the users info
		}
	},
	new Response.ErrorListener(){
	@Override
	public void onErrorResponse(VolleyError error) {
		/** Handel error here */
		}
	}
);
```
Get request gets the object on the server, to get user specific data you will have to use this inside a login request, otherwise you can only get public objects. It is the same story with the other request

```
GetRequest<Pictogram> getRequest = new GetRequest<Pictogram>(id, Pictogram.class,
	new Response.Listener<Pictogram>() {
		@Override
		public void onResponse(Pictogram response) {
			/**Handle pictogram here */
		}
	},
	new Response.ErrorListener() {
		@Override
		public void onErrorResponse(VolleyError error) {
			/** Handel error here */
		}
	}

);
```
```
PutRequest<Pictogram> genPutRequest = new PutRequest<>(pictogram2, 1,
        new Response.Listener<Integer>() {
            @Override
            public void onResponse(Integer statusCode) {
		// statusCode is the http status code
                 
            }
        },
        new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                 /** Handel error here */
            }
        }
);
```
```
PostRequest<Pictogram> genPostRequest = new PostRequest<>(pictogram,
        new Response.Listener<Integer>() {
            @Override
            public void onResponse(Integer statusCode) {
		// statusCode is the http status code
            }
        },
        new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                /** Handel error here */
            }
        }
);
```
```
DeleteRequest genDeleteRequest = new DeleteRequest("pictogram", 20,
        new Response.Listener<Integer>() {
            @Override
            public void onResponse(Integer statusCode) {
		// statusCode is the http status code
            }
        },
        new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                /** Handel error here */
            }
        }
);
```

## Development Guide

A more in-depth guide to the REST library

### Integrating volley

Google volley do not have the best documentation. Most of the time we looked at the source code rather then the documentation on [Android development site](https://developer.android.com/index.html).

#### Request queue

Volley makes use of a request queue to process requests. This queue needs to have a cache and a network provided in order to function. The request queue that has been set up in the project, as an singleton, and will check weather a cache is present on the device. When it is instantiated the request queue will use the cache and if there is no cache, a new one is created. To instantiate the request queue a context is provided. This context is the application context.
The request queue also manages the cookie that is provided whenever a user logs in to the application.

#### Request

A number of requests has been implemented. These requests are based on the HTTP requests Put, Post, Get and Delete. furthermore a loginrequest and a getarray request has been implemented. These requests are generics except loginrequest and delete because that way they can be used on all the types of objects in the model layer without having to implement a request for each type. The loginrequest is not a generic because it allways operates on the user type and the deleterequest only needs to know the endpoint and the id of the object. The getarray request is almost the same as the get request the difference being that getarray return an array instaed of a single object. Each method has a number of contructors specific to the Giraf project that sets default parameters, they also have a constructor that takes all the paramters and is used to reach other servers than the Giraf server. All the methods also takes a response listener and an error listener as arguments in their constructor. These are abstract methods and are used as callback for the request.

See [Google volley](https://github.com/google/volley) for the base Request class.

#### Cache

A problem from last semester was that when an application was started it downloaded the entire database, which lead to performance issues. To solve this, A diskbased cache was developed. This cache is an [LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies) cache which means that Least Recently Used objects is at the top of the cache. This cache is a modified version of the diskbased cache that Volley provides. The reason for this is that the cache in Volley loads everything into memory when it is instantiated instead of loading it when requested.

### Testing

During the development of the project a test project called "test-app-client-lib" was used to manually test the "rest-api-client-lib". This is a simple app that displays the results of the requests that that has been processed by the request queue.

We also tried to implement automated tests using a test framework for android called "Robolectric", which is a framework used to make unit tests and mock data. This is implemented in the test application