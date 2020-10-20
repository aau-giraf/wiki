# User Endpoints

## Get user

````

/v1/User

```` 

Find information about the currently authenticated user.
Possible status code responses are 200 Success and 404 Not Found.

## Get given user

````

/v1/User/{id}

```` 

Find information on the user with the username supplied as a url query parameter or the current user.
Status code responses are 200 Success, 400 Bad Request, 403 Forbidden and 404 Not Found.

## Update given user

````

/v1/User/{id}
```` 

Updates the user with the information in GirafRest.Models.DTOs.GirafUserDTO
Example user PUT request body:

````
{
  "role": 1,
  "username": "string",
  "displayName": "string"
}
````

Status code responses are 200 Success, 400 Bad Request, 403 Forbidden, 404 Not Found and 409 Conflict.

## Get given user-settings

````

/v1/User/{id}/settings

```` 

Get user-settings for the user with the specified Id
Status code responses are 200 Success, 400 Bad Request, 403 Forbidden and 404 Not Found.

## Update given user-settings

````

/v1/User/{id}/settings

```` 

Updates the user settings for the user with the provided id.
Example user-setting PUT request body:

````
{
  "orientation": 1,
  "completeMark": 1,
  "cancelMark": 1,
  "defaultTimer": 1,
  "timerSeconds": 0,
  "activitiesCount": 0,
  "theme": 1,
  "nrOfDaysToDisplay": 0,
  "greyScale": true,
  "lockTimerControl": true,
  "pictogramText": true,
  "weekDayColors": [
    {
      "hexColor": "string",
      "day": 1
    }
  ]
}

````

Status code responses are 200 Success, 400 Bad Request, 403 Forbidden and 404 Not Found.

## Get given user icon

```

/v1/User/{id}/icon

``` 

Endpoint for getting the UserIcon for a specific User-
Possible status code responses are 200 Success and 404 Not found.

## Update given user icon

````

/v1/User/{id}/icon

```` 

Sets the user icon of the given user.
Status code responses are 200 Success, 400 Bad Request, 403 Forbidden and 404 Not Found.

## Delete given user icon

````

/v1/User/{id}/icon

```` 

Deletes the user icon for a given user.
Status code responses are 200 Success, 400 Bad Request, 403 Forbidden and 404 Not Found.

## Get given raw user icon

```

/v1/User/{id}/icon/raw

``` 

Gets the raw user icon for a given user.
Status code responses are  200 Success and 404 Not Found.

## Get given user's citizens

````

/v1/User/{id}/citizens

````

Gets the citizens of the user with the provided id. The provided user must be a guardian.
Status code responses are 200 Success, 400 Bad Request, 403 Forbidden and 404 Not Found.

## Get given user's guardians

````

/v1/User/{id}/guardians

```` 

Gets the guardians for the specific citizen corresponding to the provided id.
Status code responses are 200 Success, 400 Bad Request, 403 Forbidden and 404 Not Found.

## Create relation between guardian and citizen

````

/v1/User/{id}/citizens/{citizenId}

```` 

POST request to add a relation between the authenticated user (guardian) and an existing citizen.
Status code responses are  200 Success, 403 Forbidden and 404 Not Found.
