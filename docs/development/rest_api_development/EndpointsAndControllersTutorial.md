# Endpoints and Controllers Tutorial
This tutorial is created to help developers understand and create new controllers and endpoints in the Giraf project.

An endpoint is basically the end of a communication channel.
It is this point the API uses to access resources needed to fulfill a request.
Any time the API wants to access the database, it happens through endpoints.
Each endpoint has its own url that the API uses when it wants a specific action. 

A controller is a collection of endpoints.
Each controller is responsible for a limited area of the server/API and contains the endpoints related to said area.
All communication is done through 'requests' and 'responses'.

## How to Make
A quick example of how to make a controller and an endpoint. 

### Controller
When creating a new controller, you start by creating a new class deriving from the `Controller` class.
The `Controller` class provides usesful responses that are used when sending responses to the API.\
Here is an example of a controller
```C# 
[Authorize]
[Route("v1/[controller]")]
public class TestController : Controller
{
}
```
Before the class declaration are to arguments `[Authorize]` and `[Route]`.
The `[Authorize]` argument dictates who has access to the controller and the endpoints. 
If there is no `[Authorize]`, any one can access the controller and its endpoints, while if there is a `[Authorize]` you have to be logged in to access the controller and the endpoints. 
Additionally you can define what roles the logged in user needs to get access like this `[Authorize(Roles = GirafRole.Guardian)]` or if you want more roles to have access `[Authorize(Roles = GirafRole.SuperUser + "," + GirafRole.Department + "," + GirafRole.Guardian)]`.
Typically, you would only want to use `[Authorize]` for the controller as specifying the role prevents you from specifying that some endpoints can only be used specific roles.

The `[Route("v1/[controller]")]` argument modifies the url for endpoints to include the pre-fix define in the quotationmarks.
The `[controller]` uses the name of the controller excluding `Controller` in this case it would be `v1/Test`.

### Endpoint
Endpoint is a fuinction/method  
What is Http...  
What is authorize/allowAnonimous  
What is ProducesResponseType  
Can make help functions when required  
