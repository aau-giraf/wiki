#Activity Endpoints
##
###Create activity
````/v2/Activity/{userId}/{weekplanName}/{weekYear}/{weekNumber}/{weekDayNmb}```` Add a new activity to a given weekplan on the given day.

Bulletpoints of parameters for this request:
* {userId} (string): 
id of the user that you want to add the activity for.
* {weekplanName} (string): name of the weekplan that you want to add the activity on.
* {weekYear} (integer): year of the weekplan that you want to add the activity on.
* {weekNumber} (integer): week number of the weekplan that you want to add the activity on.'
* {weekDayNmb} (integer): day of the week that you want to add the activity on (Monday=1, Sunday=7).

Example response body:
```` 
{
  "pictograms": [
    {
      "id": 0,
      "lastEdit": "2020-10-20T02:58:02.072Z",
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
````
Possible status code responses are 201 Success, 400 Bad Request, 403 Forbidden and 404 Not Found.

###Delete activity
````/v2/Activity/{userId}/delete/{activityId}```` Delete an activity with a given id.
Bulletpoints of parameters for this request:
* {userId} (string): id of the user you want to delete an activity for.
* {activityId} (integer): id of the activity you want to delete.

Possible status code responses are 200 Success, 403 Forbidden, 404 Not Found.

###Get Activity 
````/v2/Activity/{userId}/{activityId}````Gets a given activity for a given user.
Bulletpoints of parameters for this request:
* {userId} (string): id of the user you want to delete an activity for.
* {activityId} (integer): id of the activity you want to delete.

Example response body:
````
{
  "data": {
    "pictograms": [
      {
        "id": 6,
        "lastEdit": "2020-10-19T13:02:25.082867Z",
        "title": "alting",
        "accessLevel": 1,
        "imageHash": "secure hash",
        "imageUrl": "/v1/pictogram/6/image/raw"
      }
    ],
    "order": 0,
    "state": 2,
    "id": 1,
    "isChoiceBoard": false,
    "timer": null
  }
}
````
Possible status code response is 200 Success.

###Update activity given user
````/v2/Activity/{userId}/update```` Updates an activity with a given id.
* {userId} (string): id of the user you want to delete an activity for.

Request body required for this PATCH request:
```` 
{
  "pictograms": [
    {
      "id": 0,
      "lastEdit": "2020-10-20T03:09:26.772Z",
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
````
Possible status code response are 200 Success, 400 Bad Request, 403 Forbidden and 404 Not Found.