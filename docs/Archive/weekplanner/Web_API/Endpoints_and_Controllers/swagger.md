# Swagger

Swagger is a framework of API developer tools.
Swagger defines a human and computer readable interface for understanding and documenting
 a given REST-API.
As such Swagger can be used to e.i.\ generate client-side APIs in different languages.
Another nice thing about swagger is that all endpoints are documented in the swagger
 GUI which can be found by navigating to [http://web.giraf.cs.aau.dk:5000/swagger/](http://web.giraf.cs.aau.dk:5000/swagger/).
At the GUI the different endpoints and DTOs are displayed and examples of how to
 all the endpoints are displayed as well a option for making requests to the endpoints
  and get the response back.

## Generate a client-side API

Because the REST-API integrates swagger as middle-ware it is possible to generate
 a client-side API in your preferred language.
In order to do so, follow the steps:

- Run the web-api locally
- Navigate to swagger: `http://localhost:5000/swagger/`
- Copy the url to the swagger json file on top of the site

## Generate a client in C# using the HTTP library RestSharp

- Download swagger-codegen from [swagger](https://github.com/swagger-api/swagger-codegen)
- Navigate to the swagger-codegen-cli.jar file and execute the following command:

```Bash
java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate -i
 http://localhost:5000/swagger/v1/swagger.json -l csharp -o Client/Generated/
```

This will produce a set of request methods and DTOs.
