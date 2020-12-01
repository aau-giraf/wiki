# Description of Controllers

This section gives a description for each of the controllers in the Web API.

## AccountController

The account controller contains all the endpoints related to authenticating users
e.g. log in, log out, register and reset password.

Endpoints can be found [here](./Endpoints/account_endpoints.md)

## ActivityController

The activity controller contains CRUD endpoints related to activities. It has been
created to avoid having to update the whole weekplan when changes are made to a
single activity.

Endpoints can be found [here](./Endpoints/activity_endpoints.md)

## UserController

While ```AccountController``` concerns itself with authentication, this controller
handles [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) actions
and other actions which can be taken on a user, as well as the user's data.

Endpoints can be found [here](./Endpoints/user_endpoints.md)

## DepartmentController

This controller contains CRUD endpoints for managing a department, including getting
a list of citizens for that department.

Endpoints can be found [here](./Endpoints/department_endpoints.md)

## PictogramController

This controller contains CRUD endpoints for managing pictograms, including their
access levels.

Endpoints can be found [here](./Endpoints/pictogram_endpoints.md)

## WeekController

In the WeekPlanner application, a citizen has different week schedules which contains
information about all of the citizen's activities for a given week.
This controller contains the CRUD methods for that week entity.

Endpoints can be found [here](./Endpoints/week_endpoints.md)

## WeekTemplateController

Week templates may be used by guardians in the WeekPlanner app when creating a new
week for a citizen. This controller contains CRUD endpoints for managing week templates.

Endpoints can be found [here](./Endpoints/week_template_endpoints.md)

## StatusController

The status controller purely used by the server groups to check the status of the
API, such as whether the API is running and if it has access to the database.

Endpoints can be found [here](./Endpoints/status_endpoints.md)

## ErrorController

By convention the ErrorController is linked to whenever there is an illegal request
such as a 404 request. The controller will always send back an ``ErrorResponse``.

Endpoints can be found [here](./Endpoints/error_endpoints.md)

