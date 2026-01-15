# Feature Overview

This page is an overview of the features that should be implemented in the application.
Each feature has a description, and a list of related issues, that should describe 
the details of the required solution.  
This is meant to eliminate the need to look through all the repositories for issues
related to a specific feature.  


## Folder System  

The citizens at Egebakken are divided into grades, and the citizens at Birken 
are divided into groups. The class system is meant to organise the overview of 
citizens in a way that reflects this.     
This should be done by creating a folder system, where each folder is a collection 
of citizens.   

### Issues

| Issue | Description  |
| -------- | -------------|
| [weekplanner#510](<https://github.com/aau-giraf/weekplanner/issues/510>)    | Update weekplanner with a new 'Folder' screen and bloc |
| [web-api#134](<https://github.com/aau-giraf/web-api/issues/134>)            | Update web-api with new Folder entity |
| [api_client#61](<https://github.com/aau-giraf/api_client/issues/61>)        | Update the api client with the folder entity |
| [weekplanner#512](<https://github.com/aau-giraf/weekplanner/issues/512>)    | As a guardian I would like to be able to move a citizen from one folder to another |
| [weekplanner#513](<https://github.com/aau-giraf/weekplanner/issues/513>)    | As a guardian I would like to be able to make a new folder |
| [weekplanner#677](<https://github.com/aau-giraf/weekplanner/issues/677>)    | As a guardian I would like to be able to create nested folders |


## Additional User Roles  

Aside from the guardian and citizen roles, there should be an administrator role 
and a parent role.  
Administrators should be able to create and delete guardians, as well as delete 
citizens. This role is an extension of the guardian role, meaning an administrator 
should also have all the privileges of a guardian.  
Parents should only be able to access their own children, and should have limited 
privileges to make changes in the application.  
  
The administrator role is meant to make it easier for guardians to use the app. 
The administrators at an institution should be a few guardians, 
with more knowledge of the application. 
The other guardians will then be able to contact a colleague, and ask them 
to carry out an administrative task. This could also serve to reduce the 
number of mistakes, by limiting the access to critical features to a few 
experienced guardians.


### Issues

| Issue | Description  |
| -------- | -------------|
| [web-api#164](<https://github.com/aau-giraf/web-api/issues/164>)            | Add support for new user types |
| [api_client#78](<https://github.com/aau-giraf/api_client/issues/78>)        | Add support for new user types |
| [weekplanner#624](<https://github.com/aau-giraf/weekplanner/issues/624>)    | As an administrator I would like to be able to reset a user’s password |
| [weekplanner#625](<https://github.com/aau-giraf/weekplanner/issues/625>)    | As an administrator I would like to be able to create a new user |
| [weekplanner#626](<https://github.com/aau-giraf/weekplanner/issues/626>)    | As an administrator I would like to be able to delete a user |
| [weekplanner#627](<https://github.com/aau-giraf/weekplanner/issues/627>)    | As an administrator I would like to be able to elevate a guardian to be an administrator |
| [weekplanner#628](<https://github.com/aau-giraf/weekplanner/issues/628>)    | As an administrator I would like a settings page for my extended permissions |
| [weekplanner#629](<https://github.com/aau-giraf/weekplanner/issues/629>)    | As a parent I should only be able to access my children’s week plans |
| [weekplanner#662](<https://github.com/aau-giraf/weekplanner/issues/662>)    | As an administrator I would like to be able to demote a guardian to no longer be an administrator |

## Offline Mode  

The app should be functional offline, and whenever possible continue working 
in the same manner, as if it had been online.  
The customers from Egebakken wanted this functionality as the citizens at the 
institution could become dependent on the app. Therefore it should not stop 
working if there is no internet connection. Futheremore it is to ensure that 
the behaviour of the app is consistent, as unexpected behaviour could upset or 
confuse some of the citizens.

There is a guide on how to implement the offline functionality [here](<https://aau-giraf.github.io/wiki/development/>).  
  
The issues related to this feature have the label "Offline mode".  

### Issues

| Issue | Description  |
| -------- | -------------|
| [weekplanner#9](<https://github.com/aau-giraf/weekplanner/issues/9>)        | As a guardian, I would like that the app is fully available offline so that I can still use it if the internet is down |
| [api_client#80](<https://github.com/aau-giraf/api_client/issues/80>)        | As a developer I would like an interface for the offline features |
| [weekplanner#388](<https://github.com/aau-giraf/weekplanner/issues/388>)    | As a guardian I would like to be able to log in when offline if I have been logged in online before |
| [weekplanner#389](<https://github.com/aau-giraf/weekplanner/issues/389>)    | As a developer I need code infrastructure for a local database and model adapters in order to implement offline functionality |
| [api_client#72](<https://github.com/aau-giraf/api_client/issues/72>)        | As a developer I need code infrastructure for a local database and model adapters in order to implement offline functionality |
| [weekplanner#390](<https://github.com/aau-giraf/weekplanner/issues/390>)    | As a guardian I would like my latest changes (offline and online) to be synchronized with the online database when my device is online.  |
| [weekplanner#397](<https://github.com/aau-giraf/weekplanner/issues/397>)    | As a guardian I would like to be able to take a picture to use as a pictogram in offline mode and optionally sync it when online again. |
| [weekplanner#400](<https://github.com/aau-giraf/weekplanner/issues/400>)    | As a citizen I would like to mark an activity in the current week as completed while offline. |
| [weekplanner#402](<https://github.com/aau-giraf/weekplanner/issues/402>)    | As a citizen I would like to use an activity’s timer while offline. |
| [weekplanner#405](<https://github.com/aau-giraf/weekplanner/issues/405>)    | As a guardian I would like to cancel activities in the current weekplan while offline. |
| [weekplanner#406](<https://github.com/aau-giraf/weekplanner/issues/406>)    | As a guardian I would like to use the timer functionality in the current weekplan while offline. |
| [weekplanner#407](<https://github.com/aau-giraf/weekplanner/issues/407>)    | As a guardian I would like to edit the weekplan's activities for the current week while offline. |
| [weekplanner#408](<https://github.com/aau-giraf/weekplanner/issues/408>)    | As a guardian I would like to view the current week in the weekplans overview while offline |
| [weekplanner#409](<https://github.com/aau-giraf/weekplanner/issues/409>)    | As a guardian I would like to edit the weekplan for the current week while offline. |
| [weekplanner#410](<https://github.com/aau-giraf/weekplanner/issues/410>)    | As a guardian I would like to create and delete weekplans while offline |
| [weekplanner#411](<https://github.com/aau-giraf/weekplanner/issues/411>)    | As a guardian I would like to use all functionalities as a guardian not limited to the current week |
| [weekplanner#412](<https://github.com/aau-giraf/weekplanner/issues/412>)    | As a guardian I would like to access and edit a citizen’s settings while offline |
| [weekplanner#414](<https://github.com/aau-giraf/weekplanner/issues/414>)    | As a citizen I would like to be able to view my activities and my weekplan for the current week while offline. |
| [weekplanner#415](<https://github.com/aau-giraf/weekplanner/issues/415>)    | As a guardian I would like to view my activities and the weekplan for the current week while offline. |
| [weekplanner#632](<https://github.com/aau-giraf/weekplanner/issues/632>)    | As a guardian I would like to have the pictograms that are used in my citizens' week plans to be available offline |

## Pictogram Management  

Pictograms are central to GIRAF, many of the tasks in the product backlog 
concern the management of pictograms.   
This is a collection of issues that all concern the management of pictograms 
in the application. 

### Issues

| Issue | Description  |
| -------- | -------------|
| [weekplanner#134](<https://github.com/aau-giraf/weekplanner/issues/134>)    | As a guardian, I would like a way to add pictograms by taking a picture from my camera so that I can quickly improvise if the system does not have the activity I want  |
| [weekplanner#219](<https://github.com/aau-giraf/weekplanner/issues/219>)    | As a guardian I would like a visual representation of where the pictogram I'm dragging is going to end up on the weekplan so that I can easily place it correctly |
| [weekplanner#227](<https://github.com/aau-giraf/weekplanner/issues/227>)    | As a guardian, I would like the search for pictograms to be ordered by how popular a pictogram is, so that I can find the most commonly used pictogram quickly |
| [weekplanner#266](<https://github.com/aau-giraf/weekplanner/issues/266>)    | As a guardian I would like to be able to edit a text to a pictogram in a weekplan so that other guardians know what I mean by it |
| [weekplanner#572](<https://github.com/aau-giraf/weekplanner/issues/572>)    | As a user i would like to sort my pictograms by categories when searching. |
| [weekplanner#631](<https://github.com/aau-giraf/weekplanner/issues/631>)    | As a guardian I would like to delete a pictogram, but any activities that use that pictogram should stay, and their picture should be replace by a red warning |
| [weekplanner#634](<https://github.com/aau-giraf/weekplanner/issues/634>)    | As a guardian I would like to receive a warning if I’m copying a week plan with an activity that is missing a pictogram |
| [weekplanner#635](<https://github.com/aau-giraf/weekplanner/issues/635>)    | As a guardian I would like to delete a pictogram without changing the name of activities that use it |
| [weekplanner#639](<https://github.com/aau-giraf/weekplanner/issues/639>)    | As a guardian I would like a page for managing pictograms without selecting a citizen |
| [weekplanner#640](<https://github.com/aau-giraf/weekplanner/issues/640>)    | As a guardian I would like a page for managing pictograms after selecting a citizen |
| [weekplanner#643](<https://github.com/aau-giraf/weekplanner/issues/643>)    | As a guardian I would like to be able to view more pages when searching for pictograms |
| [weekplanner#644](<https://github.com/aau-giraf/weekplanner/issues/644>)    | As a guardian I would like the images that I upload to be cropped to fit the activity box |
| [weekplanner#652](<https://github.com/aau-giraf/weekplanner/issues/652>)    | As a guardian I would like to be able to have pictograms in upper case and lower case |
| [weekplanner#666](<https://github.com/aau-giraf/weekplanner/issues/666>)    | As a guardian I would like for "Offentlig" to be renamed to "Institution" when uploading pictograms |
| [weekplanner#667](<https://github.com/aau-giraf/weekplanner/issues/667>)    | As a guardian I would like for the bar on the "Add pictogram" page to be consistent with the rest of the application |
| [weekplanner#671](<https://github.com/aau-giraf/weekplanner/issues/671>)    | As a guardian I would like to have names under the pictograms when searching for them |
| [weekplanner#672](<https://github.com/aau-giraf/weekplanner/issues/672>)    | As a guardian I would like for photos added as pictograms to have the same aspect ratio as standard pictograms |
| [weekplanner#676](<https://github.com/aau-giraf/weekplanner/issues/676>)    | As a guardian I would like to be able to decide how a photo added as a pictogram should be cut to have the same aspect ratio as standard pictograms |
