# Build and Run the web-api locally

To run the project locally with a MySQL database first do the following:

## 0. Prerequisites

- Download and install .NET Core 3.1 SDK or a version backwardly compatible with
  it `(https://dotnet.microsoft.com/download/dotnet-core/3.1)`.
- Download MySQL installer `(https://dev.mysql.com/downloads/installer/)`.
   - Install MySQL server 8.0, under the setup, create a root account with password
     `password`, and add a user with username `user` with password `password`.
   - (Optional) Install Workbench.
- For Linux users:
   - Run `apt install libc6-dev` and `apt install libgdiplus` to install dependencies
     required by `System.Drawing.Common`.
- For Mac users:
   - Run `brew install mono-libgdiplus` to install dependencies required by `System.Drawing.Common`.

## 1. Clone the web_api Repository from GitHub

## 2. Setup the Connection to the Local MySQL Server

- In the `…\web-api\GirafRest` create a copy of the file `appsettings.template.json`
  and name it `appsettings.Development.json`.
- Open the created file `appsettings.Development.json` file with a text editor.
- Change the following (Remember to remove the "<" and ">"):
   - The DefaultConnection on line 3 making it use the previously setup database
     name and user, change to: `"DefaultConnection": "server=localhost;port=3306;userid=user;password=password;database=giraf;Allow User Variables=True"`
   - The `Jwt.JwtKey` on line 24 to be any (random) string of, at least 40, alpha-numeric characters.
   - The `Jwt.JwtIssuer` on line 25 to your name or organization. For example `Aalborg University`
   - The `IpRateLimiting.GeneralRules.Limit` to `2000`

## 3. Open a Terminal and Navigate to …\ web-api\GirafRest Folder

- Run `dotnet restore`
- Run `dotnet ef database update`
- Run `dotnet run --sample-data`

The flags that can be used for the run:

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

## 4. (Optional) To Login via Swagger

- Make an Account/Login request with valid login-info (username: `Tobias`, password: `password`)
- Copy the `data` field containing the token.
- Click on the green Authorize button (Or the padlocks).
- Write `bearer [your-token]` (note the space) in the input-field.
- Click Authorize and close the pop-up.
- You are now authorized and can make authorized requests.

## 5. Let weekplanner use the Local Database and Giraf web_api Server

- In the weekplanner repository in the `…/weekplanner/assets/environments.json`
  file line 2 change the `http://srv.giraf.cs.aau.dk/DEV/API` to:
   - If using an Android emulator: `http://10.0.2.2:5000`
   - If using a hardware device: Turn on "Use USB Tethering" in the device under
     networks settings. Next get your computers local ip under network settings,
     this should be used in the `environments.json` file followed by `:5000`, e.g.
     `http://192.168.42.130:5000`
- Now: Simply run the Weekplanner application from your desired editor.
- If you are having problems in this step and are using either Android Studio or
  IntelliJ, delete the `build` folder created by the IDE and rebuild it. This should
  make sure that correct `environments.json` file is read.
