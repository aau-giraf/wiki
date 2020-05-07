# GitHub Actions
The currently used Continous Integration Pipeline is GitHub Action, which provides 2.000 minutes free per month, running on either Ubuntu, MacOS or Windows, allowing us to test multiple platforms from our CI-Platform without cost.

## Weekplanner
The weekplanner built in 4 jobs:

 - `build-and-test-android`
 - `build-and-test-ios`
 - `deploy-to-playstore`
 - `deploy-to-appstore`

Of these jobs, the `build-and-test-android` job runs `flutter test` and `flutter build appbundle`, is run across all platforms, and produces an appbundle file, ready for upload to Google Play Store, in the `deploy-to-playstore`-task, which is dependent on this task, and furthermore only runs on master.

Due to the buildability, and iOS build requires XCode as a depedency, task `build-and-test-ios` only runs on MacOS, and produces a `app.ipa`-file, iOS App Store Package, and prepares this for `deploy-to-appstore`, that uploads a build to our App Store Connect-account, which can be pushed to internal test, or into release state.
This task also runs only on `master`-branch

## api_client
The testing-suite for the api_client is a bit more simple, it runs `flutter analyze`, and `flutter test`, to ensure tests and linting is passing.

## web-api
Similar to the api_client, the web-api suite runs by building a dotnet system in Release mode, to ensure deployability, and then runs `dotnet test`, to run the embedded GirafRest.Test project and the unit tests contained.

### Docker Hub
In addition to running unit tests in GitHub Actions, when pushed to `develop`- or `master`-branches Docker Hub picks up a webhook, and starts a build of the embedded Dockerfile, and tags this accordingly as either:

 - develop-1-aspnet
 - master-1-aspnet

When deploying into the [production swarm](../../server_administration/PractiaclDocker), these images are pulled into DEV and PROD environments accordingly.

## wiki
As the wiki is currently built using MKDocs, this repository is setup with a GitHub Actions script to build the source-files, markdown, into a static HTML page, and push this into the GitHub Pages-environment, allowing it to be reachable at [http://giraf-aau.github.io/wiki](giraf-aau.github.io/wiki).
