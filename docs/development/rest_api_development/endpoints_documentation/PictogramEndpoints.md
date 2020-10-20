# Pictogram Endpoints

## Get all public pictograms

````

/v1/Pictogram

```` 

Get all public GirafRest.Models.Pictogram pictograms available to the user (i.e the public pictograms and those owned by the user (PRIVATE) and his department (PROTECTED)).
Possible queries:

* query (string): the query string. pictograms are filtered based on this string if passed.
* page (integer): Page number.
* pageSize (integer): Number of pictograms per page.

Example request URL with page and pageSize query:

````

http://localhost:5000/v1/Pictogram?page=1&pageSize=1

````

Response body:

````

{
  "data": [
    {
      "id": 1,
      "lastEdit": "2020-10-19T13:02:25.080748Z",
      "title": "som",
      "accessLevel": 1,
      "imageHash": "secure hash",
      "imageUrl": "/v1/pictogram/1/image/raw"
    }
  ]
}

````

Possible status response codes are 200 Success, 400 Bad Request and 404 Not Found.

## Create pictogram

````

/v1/Pictogram

````

Create a new GirafRest.Models.Pictogram pictogram.
Request body required for this POST request:

````
{
  "title": "string",
  "accessLevel": 1,
  "imageHash": "string"
}
````

Status response codes are 200 Success, 400 Bad Request and 404 Not Found.

## Check given pictogram authorization 

```

/v1/Pictogram/{id}

``` 

Read the GirafRest.Models.Pictogram pictogram with the specified id and check if the user is authorized to see it.
Status response codes are 200 Success, 401 Unauthorized, 403 Forbidden, 404 Not Found and 500 Server Error.

## Update pictogram

````

/v1/Pictogram/{id}

```` 

Update info of a GirafRest.Models.Pictogram pictogram.
Request body required for this PUT request:

````

{
  "title": "string",
  "accessLevel": 1,
  "imageHash": "string"
}

````

Status response codes are 200 Success, 400 Bad Request, 401 Unauthorized, 403 Forbidden and 404 Not Found.

## Delete pictogram

````

/v1/Pictogram/{id}

```` 

Delete the GirafRest.Models.Pictogram pictogram with the specified id.
Status response codes are 200 Success, 401 Unauthorized, 403 Forbidden and 404 Not Found.

## Update pictogram image

````

/v1/Pictogram/{id}/image

```` 

Update the image of a GirafRest.Models.Pictogram pictogram with the given Id.
Example response body:

````

{
  "data": {
    "id": 1,
    "lastEdit": "2020-10-19T13:02:25.080748Z",
    "title": "som",
    "accessLevel": 1,
    "imageHash": "secure hash",
    "imageUrl": "/v1/pictogram/1/image/raw"
  }
}

````

Status response codes are 200 Success, 401 Unauthorized, 403 Forbidden and 404 Not Found.

## Get pictogram image

````

/v1/Pictogram/{id}/image

````

Read the image of a given pictogram as a sequence of bytes.
Status response codes are 200 Success, 401 Unauthorized, 403 Forbidden and 404 Not Found.

## Get raw pictogram image

````

/v1/Pictogram/{id}/image/raw

```` 

Reads the raw pictogram image. You are allowed to read all public pictograms aswell as your own pictograms or any pictograms shared within the department.
Status response codes are 200 Success, 401 Unauthorized, 403 Forbidden and 404 Not Found.
