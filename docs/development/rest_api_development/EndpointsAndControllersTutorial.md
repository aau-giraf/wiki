# Endpoints and Controllers Tutorial
This tutorial is created to help developers understand and create new controllers and endpoints in the Giraf project.

An endpoint is basically the end of a communication channel.
It is this point the API uses to access resources needed to fulfill a request.
Any time the API wants to access the database, it happens through endpoints.
Each endpoint has its own URL that the API uses when it wants a specific action. 

A controller is a collection of endpoints.
Each controller is responsible for a limited area of the server/API and contains the endpoints related to said area.
All communication is done through 'requests' and 'responses'.

## How to Make
A quick example of how to make a controller and an endpoint. 

### Controller
When creating a new controller, you start by creating a new class deriving from the `Controller` class.
The `Controller` class provides useful responses that are used when sending responses to the API.\
Here is an example of a controller
```C# 
[Authorize]
[Route("v1/[controller]")]
public class ExampleController : Controller
{
    ...
}
```
Before the class declaration are two arguments `[Authorize]` and `[Route("v1/[controller]")]`.
The `[Authorize]` argument dictates who has access to the controller and the endpoints. 
If there is no `[Authorize]`, anyone can access the controller and its endpoints, while if there is a `[Authorize]` you have to be logged in to access the controller and the endpoints. 
Additionally you can define what roles the logged in user needs to get access like this `[Authorize(Roles = GirafRole.Guardian)]` or if you want more roles to have access `[Authorize(Roles = GirafRole.SuperUser + "," + GirafRole.Department + "," + GirafRole.Guardian)]`.
Typically, you would only want to use `[Authorize]` for the controller as specifying the role prevents you from specifying that some endpoints can only be used specific roles.

The `[Route("v1/[controller]")]` argument modifies the URL for endpoints to include the pre-fix define in the quotation marks.
The `[controller]` uses the name of the controller excluding `Controller` in this case it would be `v1/Example`.

### Endpoint
Endpoints are essencially methods in a controller. 
Like the controller, an endpoint has some special arguments. 
Here is an example of an endpoint

```C#
[HttpPost("ExampleEndpoint")]
[Authorize]
[ProducesResponseType(StatusCodes.Status200OK)]
public Task<ActionResult> ExampleEndpoint()
{
    ...
}
```

The `[HttpPost("ExampleEndpoint")]` does two thing, it defines the endpoint's URL with `"ExampleEndpoint"` and the endpoint's operation.


Endpoint is a fuinction/method  
What is Http...  
What is authorize/allowAnonymous  
What is ProducesResponseType  
Describe how to document an endpoint
Can make help functions when required  
















