# Department Endpoints

## Get Department Names

````

/v1/Department

```` 

Get request for getting all the department names.
Example response body:

````

{
  "data": [
    {
      "id": 1,
      "name": "Bajer plejen"
    },
    {
      "id": 2,
      "name": "Tobias' stue for godt humør"
    }
  ]
} 

````

Possible status code responses are 200 Success and 404 Not Found.

## Create a Department

````

/v1/Department

```` 

Create a new department. It is only necessary to supply the departments name.
Request body required for this POST request:

````

{
  "name": "string",
  "members": [
    {
      "displayName": "string",
      "userId": "string"
    }
  ],
  "resources": [
    0
  ]
} 

````

Possible status code responses are 200 Success, 400 Bad Request, 403 Forbidden, 404 Not Found and 500 Server Error.

## Get Given Department

````

/v1/Department/{id}

```` 

Get the department with the specified id.
Example response body:

```` 

{
  "data": {
    "id": 2,
    "name": "Tobias' stue for godt humør",
    "members": [
      {
        "displayName": "Tobias Tobiassss",
        "userRole": "Department",
        "userId": "b12a7cb9-de27-44ff-9d91-7b8b06db8269"
      },
      {
        "displayName": "Simon Sim",
        "userRole": "Citizen",
        "userId": "0fc4a29a-ac65-4c2f-a7db-20e6af21e4c9"
      },
      {
        "displayName": "Harald Graatand",
        "userRole": "Guardian",
        "userId": "132b458a-1e84-45c8-a61d-042407faa817"
      },
      {
        "displayName": "Kurt Andersen",
        "userRole": "Citizen",
        "userId": "68ea551d-376d-4da1-8030-e833e2982dc9"
      },
      {
        "displayName": "Deck",
        "userRole": "Citizen",
        "userId": "a4e2f736-757b-4495-8372-e0cd9cc93ef7"
      }
    ],
    "resources": []
  }
}

````

Possible status code responses are 200 Success, 403 Forbidden and 404 Not Found.

## Get Citizen Names

````

/v1/Department/{id}/citizens

```` 

Gets the citizen names.
Example response body:

```` 

{
  "data": [
    {
      "displayName": "Simon Sim",
      "userRole": "Citizen",
      "userId": "0fc4a29a-ac65-4c2f-a7db-20e6af21e4c9"
    },
    {
      "displayName": "Kurt Andersen",
      "userRole": "Citizen",
      "userId": "68ea551d-376d-4da1-8030-e833e2982dc9"
    },
    {
      "displayName": "Deck",
      "userRole": "Citizen",
      "userId": "a4e2f736-757b-4495-8372-e0cd9cc93ef7"
    }
  ]
}

````

Possible status code responses are 200 Success, 403 Forbidden and 404 Not Found.

## Add User to a Department

````

/v1/Department/{departmentId}/user/{userId}

````

Add an existing user, that does not have a department, to the given department. 
Requires role Department, Guardian or SuperUser.
Possible status code responses are 200 Success, 400 Bad Request, 401 Unauthorized, 403 Forbidden and 409 Conflict.

## Change Department Name

````

/v1/Department/{departmentId}/name

```` 

Handles changing name of a Department.
Request body required for this PUT request:

```` 

{
  "id": 0,
  "name": "string"
}

````

Possible status code responses are 200 Success, 400 Bad Request, 403 Forbidden and 404 Not Found.

## Delete Department

````

/v1/Department/{departmentId}

```` 

Endpoint for deleting the GirafRest.Models.Department with the given id.
Possible status code responses are 200 Success, 403 Forbidden and 404 Not Found.
