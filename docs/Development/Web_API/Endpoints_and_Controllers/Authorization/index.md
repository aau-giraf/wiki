# Overview

In this section there are information about the authorization system that has been
used in the Web API.

# Authorization

[Identity](https://docs.microsoft.com/en-us/aspnet/core/security/authentication/identity?view=aspnetcore-2.1&tabs=visual-studio)
is a membership management system present in the ASP.NET Core framework.
It can be used to manage all user related actions e.g. login, register, authorization.

Identity is used in combination with [JSON Web Tokens](https://jwt.io/) to authenticate
users, as described in the [Token authentication](token_authentication.md) page.

## Users

The class ```GirafUser``` has been written for the project, which is derived from ```IdentityUser```.
Identity itself is set up as a service in the ```Startup``` class.
Account management(registering, logging in etc.) is done through the ```AccountController```,
while actions and data related to a user is handled in the ```UserController```.

## Resolving Authorization at Endpoints

Whether or not a user is authorised to perform a given action is resolved within
each individual method. This means that changes to access policies will require
editing of every affected endpoint, as well as a lot of the authorisation logic
being copy-pasta.

To combat this, the class ```GirafAuthenticationService```(derived ```IAuthenticationService```
has been created. In time, every endpoint should make a call to a relevant method
in this class(e.g. ```HasDepartmentEditRights(user, department)``` ), but currently
it is only used in ```UserController``` and ```WeekTemplateController```.
.