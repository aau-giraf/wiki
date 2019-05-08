# Repositories

There are many different repositories in the GIRAF project, but most of them are archived. These are not used any more, and will not be described here. The current repositories are the following:

1. web-api
2. api_client
3. weekplanner
5. giraf-production-swarm
6. wiki

## web-api
The web-api repository contains the backend API for the Giraf Project. This is used to establish communication between the database and the api_client.

## api_client
The api_client is responsible for communication between the applications and the web-api. Earlier the api_client was located in the weekplanner repository, but it is now used as a package so it can be used in other applications. 

## weekplanner
The weekplanner repository contains the Flutter Weekplanner application that is used to compile to both iOS and Android devices. This repository connect with other repositories by using the api_client as a package. 

## giraf-production-swarm
This repository contains the configuration file(`docker-compose.yml`) to control the Docker Swarm. 

## wiki
The wiki contains documentation of work done in the GIRAF project. The wiki should be updated so it always reflect the current status of the other repositories as well as other relevant artifacts. 

