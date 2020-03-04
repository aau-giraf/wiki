# Endpoints and Controllers

## EndPoints and [Swagger](./Swagger.md)

For documentation of endpoints and examples of how to use the endpoints, see: [Swagger UI(master)](http://web.giraf.cs.aau.dk:5000/swagger/)

## Description of Controllers

### AccountController

The account controller contains all the endpoints related to authenticating users e.g. log in, log out, register and reset password.

### ActivityController

The activity controller contains CRUD endpoints related to activities. It has been created to avoid having to update the whole weekplan when changes are made to a single activity.

### UserController

While ```AccountController``` concerns itself with authentication, this controller handles [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) actions and other actions which can be taken on a user, as well as the user's data.

### DepartmentController

This controller contains CRUD endpoints for managing a department, including getting a list of citizens for that department.

### PictogramController

This controller contains CRUD endpoints for managing pictograms, including their access levels.

### WeekController

In the WeekPlanner application, a citizen has different week schedules which contains information about all of the citizen's activities for a given week. This controller contains the CRUD methods for that week entity.

### WeekTemplateController

Week templates may be used by guardians in the WeekPlanner app when creating a new week for a citizen. This controller contains CRUD endpoints for managing week templates.

### StatusController

The status controller purely used by the server groups to check the status of the API, such as whether the API is running and if it has access to the database.

### ErrorController

By convention the ErrorController is linked to whenever there is an illegal request such as a 404 request. The controller will always send back an ```ErrorResponse```.

### Next

A quick aside on [Naming Conventions](./NamingConventions.md) or
Description of the [Swagger](./Swagger.md) endpoint linked in the top of the article.
