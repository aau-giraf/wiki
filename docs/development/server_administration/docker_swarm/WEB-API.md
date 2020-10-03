# WEB API

The WEB API is a DotNet Core 2.2 application built as a REST API which serves all
request to and from the Giraf Project. The WEB API has previously been served via
the software development kit (SDK) via Docker.  This resulted in a huge Docker Image
consuming `2.24 GB`. Along with enormous file size, it also included the `appsettings.json`
file which contains the database's username and password in plaintext.

Before the WEB API could be migrated from the old servers to the new one, the Docker
Imaged needed to be made smaller in size, do to the limited disk space in the new
servers. And the `appsettings.json` file needed to be removed from the finished
Docker Image.

To make these changes, only the Dockerfile needed to be changed. The two different
versions of the file can be seen below.

### Old Dockerfile

```dockerfile
# base image from dockerhub
FROM microsoft/aspnetcore-build:2
# execute command to setup environment
# RUN apt-get update && apt-get -y install sqlite3 && rm -rf /var/lib/apt/lists/*

# copy local files to container
COPY . /srv/

# copy appsettings from script_stuff

WORKDIR /srv/GirafRest

ENV ASPNETCORE_ENVIRONMENT=Production

#RUN dotnet add package Microsoft.EntityFrameworkCore.Design

RUN dotnet restore

# list available dbcontext (sometimes usefull)
# RUN dotnet ef dbcontext list

RUN dotnet ef database update

RUN dotnet build

EXPOSE 5000
ENTRYPOINT ["dotnet", "run", "--list"]
```

### New Dockerfile

```dockerfile
# Using microsoft dotnet software development kit as
# the build envionment.
FROM mcr.microsoft.com/dotnet/core/sdk:2.2 AS build-env
WORKDIR /app

# Copy csproj and restore as distinct layers
COPY GirafRest/*.csproj ./
RUN dotnet restore

# Copy everything else and build
COPY ./GirafRest/ ./

# Build the app for production
RUN dotnet publish -c Release -o out

#------------------------------------------#

# Using microsoft aps net core 2.2 as hosting envionment
FROM mcr.microsoft.com/dotnet/core/aspnet:2.2 AS runtime-env
WORKDIR /srv

# COPY from build envionment into local container.
COPY --from=build-env /app/out .

# Remove the appsettings files from the container
# so no passwords are pushed to docker hub
RUN rm appsettings*

# Expose the port intented for communications
EXPOSE 5000

# Start running the app.
ENTRYPOINT ["dotnet", "GirafRest.dll", "--list"]
```

The changes resulted in a Docker Image that has decreased in size form `2.24Gb`
to `339Mb` and where the `appsettings` file is only needed during compilation and
is later removed before the image is pushed to Docker Hub.

The repository can be found her: [https://hub.docker.com/r/giraf/web-api](https://hub.docker.com/r/giraf/web-api)
