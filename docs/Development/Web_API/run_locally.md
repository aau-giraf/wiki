# Run the Web API Locally

This section describes how the Web API is setup on a developer's local machine.

## Prerequisites

### .NET Core SDK

- Download and install .NET Core 3.1 SDK or a version backwardly compatible with
  it `(https://dotnet.microsoft.com/download/dotnet-core/3.1)`.

### MySQL Database

- Download MySQL installer `(https://dev.mysql.com/downloads/installer/)`.
    - Install MySQL server 8.0, under the setup, create a root account with password
     `password`, and add a user with username `user` with password `password`.
    - (Optional) Install Workbench.

### System.Drawing.Common (Only Linux and Max Users)

- For Linux users:
    - Run `apt install libc6-dev` and `apt install libgdiplus` to install dependencies
     required by `System.Drawing.Common`.
- For Mac users:
    - Run `brew install mono-libgdiplus` to install dependencies required by `System.Drawing.Common`.

## Setup Web API

1. Clone the web_api repository from GitHub.
1. Setup the connection to the local MySQL server.
    1. In the `…\web-api\GirafRest` create a copy of the file `appsettings.template.json`
      and name it `appsettings.Development.json`.
    1. Open the created file `appsettings.Development.json` file with a text editor.
    1. Change the following (Remember to remove the "<" and ">"):
        - The DefaultConnection on line 3 making it use the previously setup database
         name and user, change to: `"DefaultConnection": "server=localhost;port=3306;userid=user;password=password;database=giraf;Allow User Variables=True"`
        - The `Jwt.JwtKey` on line 24 to be any (random) string of, at least 40, alpha-numeric characters.
        - The `Jwt.JwtIssuer` on line 25 to your name or organization. For example `Aalborg University`
        - The `IpRateLimiting.GeneralRules.Limit` to `2000` 
1. Open a terminal and navigate to the …\ web-api\GirafRest folder.
    1. Run `dotnet tool install --global dotnet-ef`, if you do not have the
       tool `dotnet-ef` installed 
    1. Run `dotnet restore`
    1. Run `dotnet ef database update`        
    1. Run `dotnet run --sample-data`         

`dotnet run` can be run with the following parameters in the Web API:

```c#
--prod=[true|false]   | If true then connect to production db, defaults to false.
--port=integer        | Specify which port to host the server on, defaults to 5000.
--list                | List options.
--sample-data         | Tells the rest-api to generate some sample data. This only works on an empty database.
--pictograms=integer  | Specify how many sample pictograms to generate. Default is 200. Only works when --sample-data is set.
--logfile=string      | Toggles logging to a file, the string specifies the path to the file relative to the working directory.
```

Once the API is running locally you can navigate to `http://localhost:5000/swagger/`
to see and tryout requests to the endpoints. We recommend keeping a text file with
often-used DTOs and bearer tokens as part of your workflow.

## (Optional) Login via Swagger

1. Make an Account/Login request with valid login-info (username: `Tobias`, password: `password`)
1. Copy the `data` field containing the token.
1. Click on the green Authorize button (Or the padlocks).
1. Write `bearer [your-token]` (note the space) in the input-field.
1. Click Authorize and close the pop-up.
1. You are now authorized and can make authorized requests.

## Connect GIRAF apps to the Web API

Information on how to connect to the Web API from the GIRAF apps can be found
[here](../Apps/connect_to_web_api.md).
