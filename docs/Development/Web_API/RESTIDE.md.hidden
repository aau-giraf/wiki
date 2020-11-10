# REST IDE

## Setting up you IDE for REST

### Running the rest api in Visual Studio 2017

If you wish to open the project in Visual Studio you may open the root-folder of
the project.

#### Specifying program arguments

Before deploying you may wish to edit the program arguments, which can be done by
clicking **Project -> GirafRest Properties... -> Debug**.
You should now see a text field called Application arguments, in which any arguments
may be specified. Visual Studio now automatically launches the program with these
arguments.

#### Restoring NuGet packages

Visual Studio 2017 can restore your NuGet packages by right-clicking the root folder
of the project in the Solution Explorer (in this case Solution 'GirafRest') and
selecting 'Restore NuGet packages'.

#### Run the unit tests

Visual Studio has a so-called 'Test Explorer', that you can find by navigating to
**Test --> Windows --> Test Explorer**.
We have grouped all unit tests in playlists, such that each controller may be tested
independently.
You may specify the desired playlist by clicking Playlists and the desired controller
(specified by the resource it controls).
If the list does not show anything else than All Tests, please press 'Open Playlist
file' and navigate to GirafRest.Test/Playlists, where all playlists may be found.

The next step is to run the tests, which is done by clicking 'Run All'.
Tests that pass will be marked with green and any that fails will be marked with
a red X.

#### Package Manager Console

Visual Studio's Package Manager Console may be used to apply migrations.
For information on this, please see `https://docs.microsoft.com/en-us/nuget/tools/package-manager-console`
and `https://docs.microsoft.com/en-us/ef/core/miscellaneous/cli/powershell`