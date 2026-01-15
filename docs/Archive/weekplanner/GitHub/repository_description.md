# Repositories

There are many different repositories in the GIRAF project, but most of them are
archived as of 2019. This section  describes first all active repositories and
then the archived so it is easy to see what the repositories contain.

## Active Repositories

These repositories are those that as of 2019 are active in the GIRAF project. 

### web-api

The repository contains the backend for the GIRAF Project, namely a RESTful API
using .NET Core and written in C#. The contents of the repository is further
detailed in [REST API Introduction](../Web_API/architecture.md).

### wiki

The wiki repository containing information about the GIRAF project, including
information for people starting out with GIRAF. The wiki should be updated so
it always reflect the current status of the other repositories as well as other
relevant artifacts. 

### api_client

API client for Flutter to communicate with the web-api (2019: Only weekplanner
uses flutter). This is a Dart package that can be used to implement
communication with the web-api in any flutter project. Earlier the api_client
was located in the weekplanner repository, but it is now used as a package so
it can be used in other applications. 

### weekplanner

The weekplanner repository can be found [here](https://github.com/aau-giraf/weekplanner).

This is a frontend repository. The Weekplanner application is written in Flutter.

The Weekplanner is an application to create and maintain a week schedule of a
citizen. This schedule shows a plan of the activities due for the day/week of a
citizen and is essentially an important tool. 
It is a digitisation of an already existing week plan that the guardians
maintain on a pin-up board at the institutions. 
The weekplanner repository contains the Flutter Weekplanner application that is
used to compile to both iOS and Android devices.

The weekplanner repository is dependent on the [api_client](#api_client)
repository, which it uses to communicate with the backend, hosted in [web-api](#web-api).

### web-api-dotnetcore-build 

Docker containers for the development branch of the webAPI (2019).

### giraf-production-swarm

Repository for the production docker swarm for the entire GIRAF project. This
repository consists mainly of a configuration file, which is responsible for
telling docker how to initialize a docker stack. The stack contains the proxy
service, the API's and the database and runs them in docker containers. The
stack is deployed and run on the servers inside a docker swarm. When changes
need to be made to the stack, the configuration file needs to be changed
accordingly. 
This repository does not interact with any other reposistories, it is merely
used to correctly deploy everything onto the servers. More info can be found in
README.md in the [swarm repository](https://github.com/aau-giraf/giraf-production-swarm).

### pictogram-reader

The pictogram repository can be found [here](https://github.com/aau-giraf/pictogram-reader).

The pictogram-reader should be an application that allows citizens to communicate
with the use of pictograms. The app should read the pictograms out loud. For
inspiration take a look at the archived repository Pictoreader. This should not
be implemented before the weekplanner is done, but the PO group could start
working on prototypes, widgets and making issues.

This application should be written in Flutter.

## Archived Repositories

These repositories are all archived as of 2019. We keep them as a reference
point for future development.

### category-game

The Category Game (also known as ‘Kategorispillet’ in Danish) is a game that
asks the player to group up different pictograms into categories either
predefined or defined in the Category Manager. The game itself consists of a
train which must drop off the pictograms at different stations according to
their grouping. (Giraf2016_ServerDevelopment.pdf)

### launcher

The GIRAF Launcher is meant to replace the default launcher of the device and
is used to launch the applications of the GIRAF Application Suite, but could
also be used to launch other third party applications. It has a home screen
like any android OS has, which is where the applications can be launched from.
Additionally the options menu and administration panel is opened from here.
(Giraf2016_ServerDevelopment.pdf)

### life-stories

Life Story (also known as ‘Livshistorier’ in Danish) is similar to the Sequence
application but is used to remember what actions were taken by a citizen
throughout the day, or as a way of communicating since some citizens have a lot
of trouble with their verbal communication.
It is meant to give the citizens a way to communicate with other people other
than verbally.
They can create a set of pictograms showing what they did in the weekends and
then show others these stories. (Giraf2016_ServerDevelopment.pdf)

### pictocreator

A tool for creating personal pictograms. These can be created from existing
pictograms, camera pictures, or drawn by the user. (SW613F15_Pictosearch.pdf)

### pictoreader

The Pictoreader can display and read out-loud a series of pictograms.
(Giraf2016_ServerDevelopment.pdf)

### timer

The timer (also known as ‘Tidstager’ in Danish) is an application which can
limit the amount of time another application is allowed to be active for. This
is often useful in combination with the Week Schedule, which can feature
elements like, e.g., 10 minutes of playing the Category Game, or how long a
third party application, e.g. a video game, could be open for.
(Giraf2016_ServerDevelopment.pdf)

### voice-game

Voice Game (also known as ‘Stemmespillet’ in Danish) is a game in which the
purpose is to control a car, either avoiding obstacles or gathering stars,
using only your voice. This is supposed to help the citizens learn to control
the volume of their voice, as some has troubles with either speaking too loudly
too silently. (Giraf2016_ServerDevelopment.pdf)

### showcaseview-lib

Unused repository.

### pictosearch-lib

The PictoSearch-Lib is a library containing all classes relating to
the search of pictograms. (SW609F17)

### pictogram-lib

This project contain all classes that is used for the pictograms. (sw604f14)

### giraf-component-lib

This repository contains a lot of the essential functionality for the GIRAF
project, such as GUI elements and classes for the graphics of applications
(SW609F17)

### weekplanner-test

Fork of weekplanner, unused.

### old Server

Old (pre-2019) images for running the server, containes Docker, Kickstart and
Kubernetes images.

### deployment

Server deployment tools for Kubernetes (Outdated)

### server

Old server deployment tools using Kubernetes, includes old backup scripts.
(Outdated)

### Category Manager

A tool for managing categories of pictograms for each citizen. This
include adding, editing and deleting categories. (SW613F15_Pictosearch.pdf)

### Xamarin Android

Image for compiling WeekPlanner Android project.

### Sequence

A tool for creating, and viewing, sequences of pictograms. A sequence is a
set of pictograms, defining a sequence of actions for citizens.
(SW613F15_Pictosearch.pdf)
