# Introduction

The REST API handles the server-side of Giraf. As such it is responsible for responding
pictograms, weekdays, schedules and such when the applications request them.
The REST API is written in Microsoft ASP.NET Core and consists of four parts.

1. The model layer, which contains definitions of all relevant classes, eg. Pictogram,
   Frame and so forth. This layer also contains definitions of data transfer object
   (DTO) classes, which is used for defining which data should be passed in each request.
1. The service layer, which contains a number of controllers. The responsibility
   of the controllers is to respond to requests, i.e. fetch data, check if it is
   valid and take an appropriate action.
1. A separate Unit test project
1. Integration tests written in python

In addition to these layers ASP.NET Core requires a number of classes that defines
how to setup the program. In summary these classes are:

1. ```GirafDbContext```, which defines the structure of the database associated
   with the project.
1. ```Startup```, which configures the program and adds services (built-in features
   such as database management, authentication and how to respond to unauthorized access).
1. ```GirafExtensions```, which defines extension methods for carrying out custom
   configuration of some components, e.g. logging and password requirements.

## Build and run the repository

Information on dependencies as well how to build and run is available in the
[Build and run the web-api locally](./BuildAndRunLocally.md)-section of the wiki.

You may want to see an [elaboration on how to set AppSettings.json](./ConnectionString.md)
or some notes on [NuGet](./NugetWithDotnetCore.md).
