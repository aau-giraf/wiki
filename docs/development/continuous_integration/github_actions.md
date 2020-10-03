# GitHub Actions

The currently used Continuous Integration Pipeline is GitHub Actions, which provides
2.000 minutes free per month. It can run on either Ubuntu, MacOS, or Windows, allowing
us to test multiple platforms from our CI-Platform without cost.

## Weekplanner

The weekplanner is built in 4 jobs from the same workflow: [main.yml](https://github.com/aau-giraf/weekplanner/blob/develop/.github/workflows/main.yml)

    - `build-and-test-android`
    - `build-and-test-ios`
    - `deploy-to-playstore`
    - `deploy-to-appstore`

### Android

Given these jobs, the `build-and-test-android` job runs `flutter test` and
`flutter build appbundle`, on all platforms, and produces an appbundle file.

This bundle is ready for upload to Google Play Store, in the
`deploy-to-playstore`-task that only runs on master.

### iOS

Builds to iOS requires Xcode to build dependency, so the task `build-and-test-ios`
only runs on MacOS, and produces an `app.ipa`-file, iOS App Store Package.

This file is then prepared for `deploy-to-appstore`, which uploads the build to
our App Store Connect-account, which can be pushed to internal test, or into release
state. This task also runs only on `master`-branch.

## api_client

This job is built in one task: [lint-and-test.yml](https://github.com/aau-giraf/api_client/blob/develop/.github/workflows/lint-and-test.yml)

The testing-suite for the api_client is a bit more simple, it runs `flutter analyze`,
and `flutter test`, to ensure tests and linting is passing.

## web-api

This job is built in two tasks: [dotnettest.yml](https://github.com/aau-giraf/web-api/blob/develop/.github/workflows/dotnettest.yml)
and [dockerimage.yml](https://github.com/aau-giraf/web-api/blob/develop/.github/workflows/dockerimage.yml)

Similar to the api_client, the web-api suite runs by building a dotnet system in
Release mode, to ensure deployability, and then runs `dotnet test`, to run the embedded
GirafRest.Test project and the unit tests contained.

### GitHub Packages

In addition to running unit tests, when pushed to any branch GitHub Actions starts
another job, starts a build of the embedded Dockerfile, and tags this accordingly
as either:

    - **master**: aau-giraf/web-api/web-api:latest
    - **develop**: aau-giraf/web-api/web-api:develop
    - **issue/123**: aau-giraf/web-api/web-api:issue-123

When deploying into the [production swarm](../../server_administration/PracticalDocker),
these images are pulled into DEV and PROD environments accordingly.

## wiki

This job is built in one task: [page-build.yml](https://github.com/aau-giraf/wiki/blob/master/.github/workflows/page-build.yml)

As the wiki is currently built using MKDocs, this repository is set up with a GitHub
Actions script to build the source files, markdown, into a static HTML page, and
push this into the GitHub Pages-environment, allowing it to be reachable at [http://giraf-aau.github.io/wiki](giraf-aau.github.io/wiki).

This is run using an existing GitHub Action, [mhausenblas/mkdocs-deploy-gh-pages](https://github.com/mhausenblas/mkdocs-deploy-gh-pages),
thus being the simplest of the builds.
