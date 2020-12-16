# Status Endpoints

## API Ping

````

/v1/Status

```` 

GET request for checking if the API is running.
Example response body:

````

{
  "data": "GIRAF API is running!"
}

````

Possible status response code is 200 Success.

## Database Connection Ping

````

/v1/Status/database

```` 

GET request for checking connection to the database.
Example response body:

````

{
  "data": "Connection to database"
}

````

Possible status responses code are 200 Success and 503 server error.

## Get Git Version

````

/v1/Status/version-info

```` 

Endpoint for getting git version info i.e. branch and commithash.
Example response body:

````

{
  "data": "CommitHash: ref: refs/heads/feature/114"
}

````

Possible status response is 200 Success.