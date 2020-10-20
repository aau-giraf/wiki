# Account Endpoints

## Login

```

 /v1/Account/login

```

This endpoint allows the user to sign in to his/her account by providing valid username and password.\
The request body for the endpoint is a json object that takes a string for a username and a password:

```

{
    "username": "string",
    "password": "string"
}

```

Possible responses are a 200 Success code, 400 Bad Request or 401 Unauthorized.

## Register

``` 

/v1/Account/register

``` 

Registers a new user in the REST-API.  
The json object expects a username, password, display name department id and a role.

```

{
  "username": "string",
  "password": "string",
  "displayName": "string",
  "departmentId": 0,
  "role": 1
}

```

Possible responses are 200 Success, 400 Bad Request, 403 Forbidden, 409 Conflict or a 500 server error.

## Updating password

```

/v1/User/{id}/Account/password

``` 

Allows the user to update his password with and PUT request, if they know their old password.  
An example URL for updating password with a user ID ```http://localhost:5000/v1/User/fbfd2be6-414a-4c34-897b-49c3fad64d21/Account/password```
and the request body requires the old password and a new password:   

```

{
      "oldPassword": "password",
      "newPassword": "password"
}

```

The possible responses are 200 Success, 400 Bad Request, 403 Forbidden, 404 Not Found or 500 a server error.

## Set a new password

``` 

/v1/User/{id}/Account/password

```

Allows a user to set a new password with a POST request, if they forgot theirs.
The request then needs a new password as well as the given user password-reset-token:

```

{ 
  "password": "string",
  "token": "string"
}

```

Possible responses are 200 Success, 400 Bad Request, 401 Unauthorized and 404 Not Found.

## Requesting a password reset token

``` 

/v1/User/{id}/Account/password-reset-token 

``` 

Allows the user to get a password reset token for a given user.
This GET request outputs a password reset token for a given user, e.g.
Request URL: 

``` 

http://localhost:5000/v1/User/fbfd2be6-414a-4c34-897b-49c3fad64d21/Account/password-reset-token 
``` 

and response body:

```

{
"data": "'token string'"
}

```

The token string is the input in the POST request 'Set a new password'.
Possible response codes are 200 success, 401 Unauthorized and 404 Not Found.

## Delete user

``` 

/v1/Account/user/{userId}

```

Deletes the user with the given id.
The DELETE request takes the user id as input and prompts a response body with either a 200 Success, 400 Bad Request, 403 Forbidden, 409 Conflict or 500 a server error.

                                                                                                 