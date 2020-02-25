# Setting Up Flutter Projects
- [Downloading and Installing Flutter](#downloading-and-installing-flutter)
- [Android Setup](#android-setup)
- [iOS and iPadOS Setup - ONLY FOR MAC USERS](#ios-and-ipados-setup---only-for-mac-users)
  - [Personal Apple Developer Account](#personal-apple-developer-account)
- [Setup Your IDE](#setup-your-ide)
  - [IntelliJ and Android Studio](#intellij-and-android-studio)
  - [Visual Studio Code](#visual-studio-code)
  - [Verify Setup](#verify-setup)
- [Compiling and Running](#compiling-and-running)
  - [IntelliJ and Android Studio](#intellij-and-android-studio)
 - [Visual Studio Code](#visual-studio-code-1)
- [Notes](#notes)
## Downloading and Installing Flutter
1. Go to [flutter.dev](https://flutter.dev/docs/get-started/install) and select your operating system.
    - Make sure you have Git installed.
    - For Mac: Make sure you have the listed command-line tools available.
    - For Linux: Make sure you have the listed command-line tools and shared libraries available.
2. Follow the instructions on how to download and unzip Flutter.
3. Update your path according to the instructions.

## Android Setup
1. [Download and install Android Studio](https://developer.android.com/studio).
2. If you have an Android device, [enable USB debugging](https://developer.android.com/studio/debug/dev-options) and plug it in to your computer.
    - For Windows: You might need to install the [Google USB Driver](https://developer.android.com/studio/run/win-usb).
3. [Setup the Android emulator](https://flutter.dev/docs/get-started/install/windows#install-android-studio) and run it.
4. Run `flutter devices` and check that the emulator and, if applicable, the Android device is listed.
    - If not, try running `flutter doctor` to see if there are problems with the Android toolchain.
    
## iOS and iPadOS Setup - ONLY FOR MAC USERS
1. Download the latest version of Xcode from the App Store.
2. Setup the command line tools, to use the new version of Xcode you just installed:
```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
sudo xcodebuild -runFirstLaunch
```
3. Also make sure you have accepted the license agreement:
```bash
sudo xcodebuild -license
```
4. You can open the simulator app by finding it with spotlight, or by running:
```bash
open -a Simulator
```
5. If you want, run the following command to allow full screen mode:
```bash
defaults write com.apple.iphonesimulator AllowFullscreenMode -bool YES
```
6. Install cocoapods:
```bash
sudo gem install cocoapods
pod setup
```
### Personal Apple Developer Account
To get a personal Apple Developer account, you need to follow these steps
1. Launch Xcode.
2. Invoke __Xcode > Preferences__ (<kbd>⌘ + ,</kbd>).
3. Go to Accounts, and add one by clicking the '+' icon. Sign in with your Apple ID.
4. Select your account and click "Manage Certificates" and then click the '+' icon.
You now have an Apple Developer certificate. You may need to add new ones once in a while, but just follow steps 1, 2 and 4.

Now you need to add yourself as a developer to the Flutter project. To do this, you need to open the project in Xcode.

1. Open a new project in Xcode (<kbd>⌘ + O</kbd>) and locate the `ios` folder. This is the one you should open. 
2. Now you should be able to see two folders `Runner` and `Pods` in the left column. Double click on `Runner` and click on __Signing & Capabilities__. 
3. Here you need to add yourself as the team. You also need a unique Bundle Identifier, just write some string that is unique.

If you want to deploy to a physical iOS device, you need to first accept your computer (when connecting to a device), and then accept yourself on the device as a developer.
After building the project in Xcode to your device, you should go to:
__Settings > General > Device Management (Administration af enhed)__  and add yourself as a trusted developer.

Note that __Device Management__ option only appears after the project is build. There you need to select and trust yourself as developer.

## Setup Your IDE
### IntelliJ and Android Studio
1. Start IntelliJ/Android Studio.
2. Open plugin preferences.
    - Windows/Linux: __File > Settings > Plugins__
    - MacOS: __Preferences > Plugins__
3. Select __Marketplace__, find the Flutter plugin and click __Install__.
4. Click __Yes__ when prompted to install the Dart plugin.
5. Click __Restart__ when prompted.

### Visual Studio Code
1. Start VS Code.
2. Invoke __View > Command Palette__.
3. Type "install", and select `Extensions: Install Extensions`.
4. Type "flutter" in the extensions search field, select Flutter in the list, and click Install. This also installs the required Dart plugin.

### Verify Setup
1. Run `flutter doctor` to verify that everything is setup properly.
![flutter doctor](https://i.imgur.com/0XC906V.png "flutter doctor")

## Compiling and Running
### IntelliJ and Android Studio
1. Select an Android/iOS virtual device or the Android/iOS device in the toolbar.  
    ![toolbar](https://i.imgur.com/7RE2qan.png "Android Studio/IntelliJ Toolbar")
    -  If the virtual device doesn't show up in the IDE toolbar, and the "Open Android Emulator: …" option is not shown, use `flutter emulators` to list available emulators and then run `flutter emulators --launch <emulator id>` to launch it. It should then appear in the toolbar.
2. Make sure that `main.dart` is selected as the run configuration.
3. Press <img src="https://i.imgur.com/BEvXOqT.png" alt="Run" width="20px" align="top"> to run without debugging or <img src="https://i.imgur.com/Lhng0Hq.png" alt="Debug" width="20px" align="top"> to debug.
4. While the app is running, save files or press <img src="https://i.imgur.com/bP2pSIS.png" alt="Hot reload" width="20px" align="top"> to apply the changes instantly.
    - Some changes requires using hot restart (<img src="https://i.imgur.com/yCvF97E.png" alt="Hot restart" width="20px" align="top">). See [docs](https://flutter.dev/docs/development/tools/hot-reload) for more information.

### Visual Studio Code 
1. Locate the VS Code status bar (the blue bar at the bottom of the window):
    ![Status bar](https://i.imgur.com/5NxR84J.png?3 "Status bar")
2. Select a device from the __Device Selector__ area.
    - If no device is available and you want to use a device simulator, click "No Devices" and select an emulator.
    - Otherwise, make sure that your device is connected and setup properly.
3. Go to the __Debug and Run__ menu (<img src="https://i.imgur.com/NR1E5TQ.png" alt="D&R" width="20px" align="top">)
4. Press __Create a launch.json file__.
5. Invoke __Debug > Start Debugging__ or __Debug > Run without debugging__ as normal.
6. While the app is running, save files or press <img src="https://i.imgur.com/JjoCWDm.png" alt="Hot reload" width="20px" align="top"> to apply the changes instantly.
    - Some changes requires using hot restart (<img src="https://i.imgur.com/X8NIyyF.png" alt="Hot restart" width="20px" align="top">). See [docs](https://flutter.dev/docs/development/tools/hot-reload) for more information.

###### NOTES
- [weekplanner](https://github.com/aau-giraf/weekplanner)
    - Last compiled and verified to work with Flutter 1.12.13+hotfix.8.


