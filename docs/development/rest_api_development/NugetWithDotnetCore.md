# NuGet packages with .NET Core

## What are NuGet packages

NuGet is an open source package manager, that allows you to add/remove libraries for your project. So NuGet packages are essentially libraries that you can include in your project.

## How do I get these packages

NuGets are most easily added through the NuGet package manager in visual studio but can also added through the CLI as follows:
```dotnet add GirafRest.csproj package <packageName> [-v <versionNumber>```

Open your GirafRest.csproj file and you should find a PackageReference to the new package now run:
```dotnet restore```
Simple as that! Next chapter is about databases where MySQL will be looked at, but also how migrations are made and why they're needed. [Head on over here](./Database.md).