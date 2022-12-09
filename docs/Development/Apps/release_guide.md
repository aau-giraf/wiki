# Flutter Release of Giraf
When you have to make a release of Giraf then the `pubspec.yaml` file must be updated so when building it the bundle gets the correct version number. This means that you have to find the key-word version and update it e.g. `version: 1.2.2` to `version: 1.3.0`. It is also possible to add a suffix if it is a new build (`+1`, `+hotfix `) or a pre-release (`-beta.2`, `-rc.1`) if it should be necessary.

If you are unsure what version number your release should have, you can take a look at this page:
https://semver.org it is also available in danish https://semver.org/lang/da/

You need to get access to the Giraf project's keepass so that you can use the Apple Developer Account that is on there and also the Android account. It is also possible to add your own personal Apple Developer Account to the Girafs Venner Team.
## Android Release
Here is the official flutter guide to release on Android: https://docs.flutter.dev/deployment/android

## iOS Release
Here is the official flutter guide to release on iOS: https://docs.flutter.dev/deployment/ios

Priliminary requirements for creating a build and release a flutter app for iOS is that you need Xcode which means that you must do it on a Mac computer. Remember to have an Apple Developer Account that is connected to the Girafs Venner Team.

List over all the different steps for creating a iOS release:
* Open ios folder in Xcode and check for errors and warnings
    * Click **Automatically manage signing**
* Run `flutter build ipa`
* Drag and drop the ipa file in Transporter and click deliver
* Update App Store Connect
    * Update gdpr
    * Update which encryption has been used
    * Ensure that the test user still is active in the database
    * Write text for **What's New in This Version**

#### Open ios folder in Xcode and check for errors and warnings
The first thing that needs to be done is that in the weekplanner repository find the ios folder and open that in Xcode, then select the Runner target then under the **Signing & Capabilities** tab add the Apple Developer Account in the **Teams** section. Also under the **Signing & Capabilities** tab set the **Automatically manage signing** to true, this makes it esiaer to create the IPA file. Lastly check/update what the minimum requirements are for running the app, e.g., the iOS version.

#### Run flutter build ipa
Open a terminal under the weekplanner repository and run the command `flutter build ipa` and then fix the possible errors or warnings. The command will create an IPA file if it passes with no exceptions. Now proseed to the next step.

#### Drag and drop the ipa file in Transporter and click deliver
If you have not done it already then go to App Store and download **Transporter**. Open transporter and drag the ipa file from **weekplanner/build/ios/ipa** and drop it in to the transporter app and wait until it is ready and then click deliver. Then the IPA file will be transferred to App Store Connect.

#### Update App Store Connect
First of go to https://appstoreconnect.apple.com and log in with your Apple Developer Account.

You might not need to update this, but we had to so check that the gdpr is up to date and the same for then it comes to what types of encryption has been used.