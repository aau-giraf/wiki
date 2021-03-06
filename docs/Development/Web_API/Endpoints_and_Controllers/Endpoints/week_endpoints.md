# Week Endpoints

## Get List of Week Schedules Given User ID

```

/v2/User/{userId}/week

```

Gets list of GirafRest.Models.DTOs.WeekDTO for all weeks belonging to the user with the provided id, days are not included.
A User identifier is needed for the GirafRest.Models.GirafUser to get schedules.

```

/v2/User/{userId}/week

```

Gets list of GirafRest.Models.DTOs.WeekDTO for all weeks belonging to the user with the provided id, days not are included.

* A User identifier is needed for the GirafRest.Models.GirafUser to get schedules.

Possible status code responses are 200 Success, 403 Forbidden and 404 Not Found.

## Get a List of Week Schedules Given User ID

```

/v1/User/{userId}/week

``` 

Gets list of GirafRest.WeekNameDTO for all schedules belonging to the user with the provided id.

* A User identifier is needed for the GirafRest.Models.GirafUser to get schedules.

Possible status code responses are 200 Success, 403 Forbidden and 404 Not Found.

## Get List of Week Schedules with Specified User ID and Week and Year

```

/v1/User/{userId}/week/{weekYear}/{weekNumber}

``` 

Gets the GirafRest.Models.DTOs.WeekDTO with the specified week number and year for the user with the given id.

* userId is the identifier of the GirafRest.Models.GirafUser to request schedule for.
* weekYear is the year of the week schedule to fetch.
* weekNumber is the week number of the week schedule to fetch.

Possible status code responses are 200 Success, 403, Forbidden and 404 Not Found.

## Update Week Information

````

/v1/User/{userId}/week/{weekYear}/{weekNumber}

```` 

Updates the entire information of the week with the given year and week number.

* userId is the identifier of the GirafRest.Models.GirafUser to request schedule for.
* weekYear is the year of the week schedule to fetch.
* weekNumber is the week number of the week schedule to fetch.

An example of a successful week PUT request:

````

{
      "thumbnail": {
        "id": 0,
        "lastEdit": "2020-10-19T18:49:26.879Z",
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
                  "lastEdit": "2020-10-19T18:49:26.879Z",
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
      ]
    }

````

Possible status code responses are 200 Success, 403, Forbidden and 404 Not Found.

## Delete a Week

````

/v1/User/{userId}/week/{weekYear}/{weekNumber}

````

Deletes all information for the entire week with the given year and week number.

* {userId} is the identifier of the GirafRest.Models.GirafUser to request a schedule for.
* {weekYear} is the year of the week schedule to fetch.
* {weekNumber} is the week number of the week schedule to fetch.

Possible status code responses are 200 Success, 403, Forbidden and 404 Not Found.

