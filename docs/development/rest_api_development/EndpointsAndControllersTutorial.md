# Endpoints and Controllers Tutorial
This tutorial is created to help developers understand and create new controllers and endpoints in the Giraf project.

An endpoint is basically the end of a communication channel.
It is this point the API uses to access resources needed to fulfill a request.
Any time the API wants to access the database, it happens through endpoints.
Each endpoint has its own URL that the API uses when it wants a specific action.

A controller is a collection of endpoints.
Each controller is responsible for a limited area of the server/API and contains the endpoints related to said area.
All communication is done through 'requests' and 'responses'.

## Controller
When creating a new controller, you start by creating a new class deriving from the `Controller` class.
The `Controller` class provides useful responses that are used when sending responses to the API.<br/>
Here is an example of a controller:
```C#
[Authorize]
[Route("v1/[controller]")]
public class ExampleController : Controller
{
    //Endpoints goes here
}
```
Before the class declaration are two [attributes](https://www.tutorialspoint.com/csharp/csharp_attributes.htm) `[Authorize]` and `[Route("v1/[controller]")]`.
The `[Authorize]` attribute dictates who has access to the controller and the endpoints.
If there is no `[Authorize]`, anyone can access the controller and its endpoints, while if there is a `[Authorize]` you have to be logged in to access the controller and the endpoints.
Additionally you can define what roles the logged in user needs to get access like this `[Authorize(Roles = GirafRole.Guardian)]` or if you want more roles to have access `[Authorize(Roles = GirafRole.SuperUser + "," + GirafRole.Department + "," + GirafRole.Guardian)]`.
Typically, you would only use `[Authorize]` for controllers as specifying what roles have access to the controller, like with `[Authorize(Roles = GirafRole.SuperUser)]`, locks all endpoints to the same access level, meaning you can't make some endpoints accessible only to a guardian while another is accessible only to a superuser.

The `[Route("v1/[controller]")]` attribute modifies the URL for endpoints to include the pre-fix define in the quotation marks.
The `[controller]` uses the name of the controller excluding `Controller` in this case it would be `/v1/Example`.

## Endpoint
Endpoints are essencially methods in a controller.
Like the controller, an endpoint has some special attributes. 
Here is an example of an endpoint

```C#
[HttpPost("ExampleEndpoint")]
[Authorize]
[ProducesResponseType(StatusCodes.Status200OK)]
public Task<ActionResult> ExampleEndpoint()
{
    //Does stuff
}
```

The `[HttpPost("ExampleEndpoint")]` does two thing, it defines the endpoint's URL with `"/ExampleEndpoint"` and describes what type of operation this endpoint executes.
In this case, if the endpoint was a part of `ExampleController` from before, the full URL would be `/v1/Example/ExampleEndpoint`.
If you have an endpoint where you do not want to use the URL defined by the controller, you can start with a `/` to ignore the URL defined in `[Route]`, using `[HttpPost("/NoRoute/ExampleEndpoint")]` would give the URL `/NoRoute/ExampleEndpoint`. 
`[HttpPost]` describes what type of operation the endpoint does. 
There are 4 types of operation, `[HttpPost]`, `[HttpGet]`, `[HttpPut]`, `[HttpDelete]`.
These operations follows [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete).
For more information on how the `api_client` and the `web-api` communicates see [Backend Architecture](https://github.com/aau-giraf/wiki/blob/feature_188/docs/development/rest_api_development/BackendArchitecture.md#making-a-request).

The `[Authorize]` option works in the same way as the `[Authorize]` in controllers.
The main difference is that this only affects this single endpoint.
So if the controller is set to `[Authorize]`, but an endpoint needs access from non-authorized users, this option is given the value `[AllowAnonymous]` as seen in the example below.
This overwrites the `[Authorize]` option provided by the controller.
If the opposite is the case, and the endpoint needs restricted authorization, the option can be set to `[Authorize]` or something more specific like `[Authorize(Roles = GirafRole.SuperUser + "," + GirafRole.Department + "," + GirafRole.Guardian)]`.

```C#
[HttpPost("ExampleEndpoint")]
[AllowAnonymous]
[ProducesResponseType(StatusCodes.Status200OK)]
public Task<ActionResult> ExampleEndpoint()
{
    //Does stuff
}
```

The `[ProducesResponseType(StatusCodes.Status200OK)]` is a response the endpoint can give.
This particular respons is for success.
Typically you would like more than this to accommodate multiple outcomes.
For instance when a user is not found like in the example below.
For a more detailed list of responses please see [this link](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).
Bellow is an example of how to use `[ProducesResponseType()]`.
```C#
[HttpGet("{id}")]
[ProducesResponseType(StatusCodes.Status200OK)]
[ProducesResponseType(StatusCodes.Status404NotFound)]
public async Task<ActionResult> GetById(int id)
{
    // Code for finding a user
    
    if (noIdMatch)
    {
        return NotFound(new ErrorResponse(ErrorCode.UserNotFound, "User not found"));
    }
    
    return Ok(new SuccessResponse<Object>(result));
}
```
You can also use `StatusCode(StatusCodes.Status200OK, objectToReturn)` for giving status codes to a response. 
The first attribute is a static class containing http status codes and the second attribute is the object to return. 
