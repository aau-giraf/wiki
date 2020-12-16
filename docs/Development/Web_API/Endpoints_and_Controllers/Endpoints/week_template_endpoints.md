# WeekTemplate Endpoints

## Get Week Schedule Templates for the Authenticated User

````

/v1/WeekTemplate

```` 

Gets all schedule templates for the currently authenticated user. Available to all users.
Possible status code responses are 200 Success, 403 forbidden and 404 Not Found status codes.

## Create Week Template

````

/v1/WeekTemplate

````

Creates new week template in the department of the given user. Available to Supers, Departments and Guardians.
After successful execution, a new week template will be created.
An example of a successful week template POST request:

````

{
      "thumbnail": {
        "id": 0,
        "lastEdit": "2020-10-19T16:44:58.607Z",
        "title": "string",
        "accessLevel": 1,
        "imageHash": "string"
      },
      "name": "string",
      "days": [
        {
          "day": 1,
          "activities": [
            {
              "pictograms": [
                {
                  "id": 0,
                  "lastEdit": "2020-10-19T16:44:58.607Z",
                  "title": "string",
                  "accessLevel": 1,
                  "imageHash": "string"
                }
              ],
              "order": 0,
              "state": 1,
              "id": 0,
              "isChoiceBoard": true,
              "timer": {
                "startTime": 0,
                "progress": 0,
                "fullLength": 0,
                "paused": true,
                "key": 0
              }
            }
          ]
        }
      ],
      "id": 0
    }

````

Responses are 201 Success, 400 Bad Request, 403 Forbidden and 404 Not Found.

## Get Week Template for a Given User

````

/v1/WeekTemplate/{id}

```` 

Gets the week template with the specified id. Available to all users.

* An id integer is needed for the week template to fetch.

Possible responses are 200 Success, 403 Forbidden and 404 Not Found.

## Update Week Template for a Given User

````

/v1/WeekTemplate/{id}

```` 

Overwrite the information of a week template. Available to all Supers, and to Departments and Guardians of the same department as the template.

* An id integer is needed for week template to overwrite.

Possible responses are 200 Success, 400 Bad Request, 401 Unauthorized, 403 Forbidden and 404 Not Found.

## Delete Week Template for a Given User

````

/v1/WeekTemplate/{id}

```` 

Deletes the template of the given ID. Available to all Supers, and to Departments and Guardians of the same department as the template.

* An id integer is needed for the week template to delete.

Possible responses are 200 Success, 401 Unauthorized, 403 Forbidden and 404 Not Found.