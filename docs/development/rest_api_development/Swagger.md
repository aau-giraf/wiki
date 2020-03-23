# Swagger Guide

Swagger is a framework of API developer tools. Swagger defines a human and computer readable interface for understanding and documenting a given REST-API. As such Swagger can be used to e.i.\ generate client-side APIs in different languages.

## Generate client-side API

Consider the case where you want to generate a client in C# using the HTTP library RestSharp. This can be done by e.g. downloading swagger-codegen from [swagger](https://github.com/swagger-api/swagger-codegen), navigating to the swagger-codegen-cli.jar file and executing the following command:

```Bash
java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate -i http://localhost:5000/swagger/v1/swagger.json -l csharp -o Client/Generated/
```

This will produce a set of request methods and DTOs.

Using Swagger to see endpoints and make requests

Another nice thing about swagger is that all endpoints are documented in the swagger GUI which can be found by navigating to [name](http://web.giraf.cs.aau.dk:5000/swagger/). At the GUI the different endpoints and DTOs are displayed and examples of how to call the endpoints are displayed as well a option for making requests to the endpoints and get the response back.

## Next

Then comes [Unit Tests](./UnitTesting.md).