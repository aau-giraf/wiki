# Error Endpoints

## Post status code

````

/v1/Error

```` 

This endpoint is reached when an error happens in the routing.
Possible query:

* statusCode (int): The statuscode gotten when the error happened

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

## Get status code

````

/v1/Error

```` 

This endpoint is reached when an error happens in the routing.

## Update status code

````

/v1/Error

```` 

This endpoint is reached when an error happens in the routing.

## Delete status code

````

/v1/Error

```` 

This endpoint is reached when an error happens in the routing.

## Patch status code

````

/v1/Error

````

 This endpoint is reached when an error happens in the routing.