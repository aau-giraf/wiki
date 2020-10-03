# Filling in the Appsettings.json file

The backend must have a [configuration enviroment](https://docs.microsoft.com/da-dk/aspnet/core/fundamentals/configuration/index?view=aspnetcore-2.2)
set up in order to be able to run.

Before building, you must copy ```⋯/GirafRest/appsettings.template.json```
to ```⋯/GirafRest/appsettings.Development.json``` and fill in the ```<>```s.

## Connection String

A [ConnectionString](https://docs.microsoft.com/en-us/ef/core/miscellaneous/connection-strings)
is needed, which tells Entity Core Framework how to connect to a database.
In this example the ConnectionString connects to a the giraf-dev database, which
is the development database. In contrast, giraf-prod should be used for production.

It must be on the form:

```json
"ConnectionStrings": {
    "DefaultConnection": "server=<db-host>;port=<db-port>;userid=<db-user>;password=<db-password>;database=<db-db>;Allow User Variables=True"
}
```

Fill in the following:

| Field | Description | Default |
|:---|:---|:---|
| ```<db-host>``` | DB server's address. Set this to localhost | |
| ```<db-port>``` | The port to use for communication with the server. | 3306, unless you specified otherwise during installation. |
| ```<db-user>``` | Name of the DB server's root user, or another user with the right privileges. | |
| ```<db-password>``` | Password of same. | |
| ```<db-db>``` | Name of the schema that will be created. Set this to giraf if you have no reason to do otherwise.| |

## JWT information

This information is required for creating the [JWT](https://jwt.io/) keys which
will be used for authorisation on the server.

It must be on the form:

```json
"Jwt": {
    "JwtKey": "<jwt-key>",
    "JwtIssuer": "<jwt-issuer>",
    "JwtExpireDays": 30
}
```

Fill in the following:

| Field | Description |
| :-----|:------------|
|```<jwt-key>``` | This is the skeleton key used to generate other keys. Secrecy only important for production. Use any string longer than 40 characters, e.g. this text field.|
| ```<jwt-issuer>``` | Name that will be displayed as the issuer of the key. Avoid using anything official-sounding, but perhaps write in a joke.|

## [Back](index.md)