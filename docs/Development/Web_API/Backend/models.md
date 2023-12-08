# Models

The models in the Web API is a collection of classes, which is used throughout
the application. A list of these classes can be found below.

|Model name | Usage|
|:----------|:-----|
|```AccessLevel``` | Used to define access level for pictograms. It has three values, PUBLIC for pictograms that are accessible to all users, PROTECTED for pictograms that are only accessible to users in a given department and PRIVATE for pictograms that are accessible only for a given user. |
| ```Department``` | Used to define a department containing users and additional resources the users can access.|
|```GirafRole``` | Used to specify a role, contains role/policy string definitions for authorization. Currently (either) ```Citizen```, ```Guardian```, ```Department``` and ```SuperUser```.|
| ```GirafUser``` | Used to define relevant data for a user.|
|```Pictogram``` | Used for storing the image of a pictogram as well as meta-information such as its name.|
| ```Setting``` | Used to specify the settings particular to a user. This includes number of days shown at a time, and the colour theme. |
| ```WeekdayColor``` | Used to represent a field in settings that specifies the background colour to use when displaying a particular week day.|
| ```Weekday``` | Used to represent a citizen's day with a number of activities each represented as a pictogram.|
| ```WeekBase``` | The base class from which Week and WeekTemplate inherits. Contains an ID, a name, a thumbnail and up to 7 days. |
| ```Week``` | Used to define a users schedule for a week at a certain year and week-number. |
| ```WeekTemplate``` | Used to define a generic template that can be used as a base when a new week is being planned.|
| ```Activity``` | Used to represent an activity on a weekday, contains pictograms and timers - can be a choiceboard.|
| ```DepartmentResource``` | Defines a relationship between a Deparments and a Pictograms.|
| ```GuardianRelation``` | Defines a relationship between Guardians and Citizens.|
| ```UserResource``` | Defines a relationship between Users and Pictograms.|
| ```AlternateName``` | Represents an alternate name for a Pictogram.|
| ```PictogramRelation``` | Defines a relationship between Activities and Pictograms.|
| ```Timer``` | Represents a timer, with start time progress and length.|











