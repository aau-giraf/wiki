# Error Endpoints

## Post Status Code

````

/v1/Error

```` 

This endpoint is reached when an error happens in the routing.
Possible query:

- statusCode (int): The statuscode gotten when the error happened

Example request URL:

````

http://localhost:5000/v1/Error?statusCode=400

````

Example response body:

```` 

{
  "message": "Statuscode: 400",
  "details": "",
  "errorKey": "UnknownError"
}

````

## Get Status Code

````

/v1/Error

```` 

This endpoint is reached when an error happens in the routing.

## Update Status Code

````

/v1/Error

```` 

This endpoint is reached when an error happens in the routing.

## Delete Status Code

````

/v1/Error

```` 

This endpoint is reached when an error happens in the routing.

## Patch Status Code

````

/v1/Error

````

This endpoint is reached when an error happens in the routing.