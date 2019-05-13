# Repositories

There are many different repositories in the GIRAF project, but most of them are archived as of 2019. In this section a short desribtion of each repository will be presented.

## Active repositories
These repositories are those that as of 2019 are in actively used in the Giraf project. 

### web-api
The backend Restfull API for the Giraf Project. The API is a .net-core project written in C#. The wiki should be updated so it always reflect the current status of the other repositories as well as other relevant artifacts. 

### wiki 
The wiki repository containing information about the GIRAF project, including information for people starting out with GIRAF.

### api_client
API client for Flutter to communicate with the web-api (2019: Only weekplanner uses flutter). This is a Dart package that can be used to implement communication with the web-api in any flutter project. Earlier the api_client was located in the weekplanner repository, but it is now used as a package so it can be used in other applications. 

### weekplanner
The Weekplanner is an application to create and maintain a week schedule of a citizen. This schedule shows a plan of the activities due for the day/week of a citizen and is essentially an important tool. It is a digitalisation of an already existing week plan that the guardians maintain on a pin-up board at the instituions. The weekplanner repository contains the Flutter Weekplanner application that is used to compile to both iOS and Android devices.

### web-api-dotnetcore-build 
Docker containers for the development branch of the webAPI (2019).

### giraf-production-swarm
Repository for the production docker swarm for the entire GIRAF project. (2019)

## Archived Repositories
These repositories are all archived as of 2019. We keep them as a reference point for future development.

### Category-game
The Category Game (also known as ‘Kategorispillet’ in Danish) is a game that asks the player to group up different pictograms into categories either predefined or defined in the Category Manager. The game itself consists of a train which must drop off the pictograms at different stations according to their grouping. (Giraf2016_ServerDevelopment.pdf)

### Launcher
The GIRAF Launcher is meant to replace the default launcher of the device and is used to launch the applications of the GIRAF Application Suite, but could also be used to launch other third party applications. It has a home screen like any android OS has, which is where the applications can be launched from. Additionally the options menu and administration panel is opened from here. (Giraf2016_ServerDevelopment.pdf)

### Life-stories
Life Story (also known as ‘Livshistorier’ in Danish) is similar to the Sequence application but is used to remember what actions were taken by a citizen throughout the day, or as a way of communicating since some citizens have a lot of trouble with their verbal communication.
It is meant to give the citizens a way to communicate with other people other than verbally.
They can create a set of pictograms showing what they did in the weekends and then show others these stories. (Giraf2016_ServerDevelopment.pdf)

### Pictocreator
A tool for creating personal pictograms. These can be created from existing
pictograms, camera pictures, or drawn by the user. (SW613F15_Pictosearch.pdf)

### Pictoreader
The Pictoreader can display and read out-loud a series of pictograms. (Giraf2016_ServerDevelopment.pdf)

### Timer
The timer (also known as ‘Tidstager’ in Danish) is an application which can limit the amount of time another application is allowed to be active for. This is often useful in combination with the Week Schedule, which can feature elements like, e.g., 10 minutes of playing the Category Game, or how long a third party application, e.g. a video game, could be open for. (Giraf2016_ServerDevelopment.pdf)

### Voice-game
Voice Game (also known as ‘Stemmespillet’ in Danish) is a game in which the purpose is to control a car, either avoiding obstacles or gathering stars, using only your voice. This is supposed to help the citizens learn to control the volume of their voice, as some has troubles with either speaking too loudly too silently. (Giraf2016_ServerDevelopment.pdf)

### Showcaseview-lib
Unused repository.

### Pictosearch-lib
The PictoSearch-Lib is a library containing all classes relating to
the search of pictograms. (SW609F17)

### Pictogram-lib
This project contain all classes that is used for the pictograms. (sw604f14)

### Giraf-component-lib
This repository contains a lot of the essential functionality for the GIRAF project, such as GUI elements and classes for the graphics of applications (SW609F17)

### Weekplanner-test
Fork of weekplanner, unused.

### old-server
Old (pre-2019) images for running the server, containes Docker, Kickstart and Kibernetes images.

### deployment
Server deployment tools for Kubernetes (Outdated)

### server
Old server deployment tools using Kubernetes, includes old bacup scripts. (Outdated)

### category-manager
A tool for managing categories of pictograms for each citizen. This
include adding, editing and deleting categories. (SW613F15_Pictosearch.pdf)

### xamarin-android
Image for compiling WeekPlanner Android project.

### sequence
A tool for creating, and viewing, sequences of pictograms. A sequence is a
set of pictograms, defining a sequence of actions for citizens. (SW613F15_Pictosearch.pdf)



