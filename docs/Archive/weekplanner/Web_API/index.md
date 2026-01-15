# Overview

This section gives an overview of the Web API.

## Definition of a Web API

A Web API is an application programming interface located on a web-server.
It manages the retrieval of requests as well as passing along an associated responses
through the HTTP/HTTPS protocol. Such requests are usually in the format of JavaScript
Object Notation (JSON) or Extensible Markup Language (XML).

## Purpose

The [Web API](https://github.com/aau-giraf/web-api) repository handles the server-side in
the GIRAF project, and it is programmed in C# and uses .NET Core. More specifically
the Web API is responsible for the handling of all communication coming from and to the
[api_client](https://github.com/aau-giraf/api_client).
If it is a valid request this leads to an [endpoint](Endpoints_and_Controllers/controller_descriptions.md)
and if not then an error response is returned. Most request would require the Web API
to communicate with the [database](Backend/database.md) that stores all the data related
to the GIRAF Project, which allows several of components to be communicating information
to the common database.

## How is the Web API called

The Web API is called through the [api_client](https://github.com/aau-giraf/api_client). 
The GIRAF project spans several applications, where each may be required to
communicate with the Web API. To alleviate the requirement of implementing
communication with the GIRAF backend in several applications, the Web API, a
common api-client project has been initiated. Formally it is a Dart package that
can be used to implement communication with the Web API in any front-end framework
Flutter project e.g. the Weekplanner application.

## Architecture

The architecture of the Web API is explained [here](architecture.md).

## Backend

The backend of the Web API consists of a database and the Entity Framework.
A description of the database can be found [here](./Backend/database.md).

## Endpoints and Controllers

Information about the endpoints and controllers in the Web API can be found
[here](./Endpoints_and_Controllers/index.md). 

## Run the Web API Locally

A guide on how to build and run the Web API locally can be found in the [Setup Guide](../../Getting_Started/setup.md).

## Settings

Information on the settings that can be set in the Web API can be found [here](settings.md).

## Testing the Web API

An overview of the Web API testing projects can be found [here](Testing.md).
