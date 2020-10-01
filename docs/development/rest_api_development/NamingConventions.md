# Naming Conventions

This guide describes the naming conventions used on the controllers in this project along with presenting what the different part of URLs are used to in this project.

## Controllers

A controller should always be named after the resource it controls, i.e. UserController if the controller is responsible for handling requests for user data.
The reason for this convention is that the client-side of the REST api extracts the name of the class that the request involves and issues a request to ```host/class_name```.

ASP.NET has a neat way of enforcing this name convention, which is annotating the controller classes with ```[Route("[controller]")]``` as it automatically fetches the resource-type of the controller, i.e. User in UserController.

## URL structure

A URL consists of at most four parts in the following structure ```host/resource/identifier/sub-resource/sub-identifier```.
The different parts of the URL are as follows:

- host: The host denotes the website that hosts the REST API.
  If you are debugging locally host will be localhost:5000 by default.
  When deployed online the REST API is hosted on http://web.giraf.cs.aau.dk:5000 - note that the index page is empty.
  If you wish to check if the REST API is actually running, you may visit the [StatusController](http://web.giraf.cs.aau.dk:5000/status).
- resource: The resource denotes a class of the system, examples of resouces are Pictograms, Weekdays and so fourth.
  This part of the URL is always preferably specified in singularity but sometimes it can make sense not to do it
- identifier: Denotes some identifier like for instance username
- sub-resource and sub-identifier means that you can nest like for instance localhost:5000/user/username/guardian/id

## Next

Now on to [Swagger](./Swagger.md).