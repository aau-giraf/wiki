# Overview

This section gives an overview and guidelines for the endpoints and controllers
in the Web API.

## Authorization in Endpoints

A description on the authorization system used for the endpoints can be found
[here](./Authorization/index.md).

## Endpoint and Controller Guidelines

Guidelines to the endpoints and controllers can be found [here](guidelines.md).

## Controller Descriptions

Descriptions of the controllers in the Web API can be found [here](controller_descriptions.md).

## Endpoint Descriptions

Descriptions of the endpoints for each controller can be found [here](./Endpoints/index.md).

## Data Transfer Objects (DTO)

Data Transfer Objects (DTOs) are used to communicate data in the controllers both
as input and output for the methods, while containing only the essential from each
model. All models have a corresponding DTO with the exception of AccessLevel and
GirafRole, as they are not used directly in any controllers currently. In addition
to those there are also six DTOs related to account/user management.

NOTE: An object should never leave the server unless it has been packed in a corresponding DTO.

NOTE: All DTOs must have parameterless constructors, because it is required by Newtonsoft
when deserializing incomming requests.

## Swagger

An overview of the endpoints and controllers used by the GIRAF project can be found
[here](https://srv.giraf.cs.aau.dk/PROD/API/swagger).

More information on how Swagger is used in the Web API can be found [here](swagger.md). 

