# MacOS Setup Guide

## Step 1: Install Homebrew

If you don't have Homebrew installed, you'll need to install it first:

- Open Terminal (Applications > Utilities > Terminal).
- Run the following command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Follow the prompts to complete the installation.
- Verify the installation:

```bash
brew --version
```

## Step 2: Install OpenJDK

- Open your Terminal and run:

```bash
brew install openjdk
```

## Step 3: Installing Xcode

Xcode is necessary for iOS development and running the iOS simulator:

- Install Xcode
  - Open the App Store on your Mac.
  - Search for "Xcode" and click "Get" or the download icon.
  - Wait for the download and installation to complete (this may take some time as Xcode is a large application).
- Once Xcode is installed, open it to accept the license agreement.

After Xcode is installed, install the Xcode Command Line Tools and the iOS simulator:

Command Line Tools:

- Open Terminal (or iTerm etc.)
- Run `xcode-select --install`
- Accept the prompt to install

iOS Simulator:

- Run `xcodebuild -downloadPlatform iOS`
- Run the simulator with `open -a Simulator`

## Step 4: Installing Flutter and Dart

### Prerequisites

#### CocoaPods

- Install CocoaPods by running `sudo gem install cocoapods` in your terminal

#### Rosetta

- Some Flutter components require the Rosetta 2 translation process on Macs running Apple silicon. To run all Flutter components on Apple silicon, install Rosetta 2.

Run in your terminal:

```bash
sudo softwareupdate --install-rosetta --agree-to-license
```

#### Installation

The recommended IDE for Flutter is [VS Code](https://code.visualstudio.com/docs/setup/mac) with the [Flutter extension](https://marketplace.visualstudio.com/items?itemName=Dart-Code.flutter)

- Open Terminal and run:

```bash
brew install --cask flutter
```

- Wait for installation. Then verify your installation:

```bash
flutter doctor
```

## Step 5. Install .NET

- Open your Terminal and run `brew install dotnet`

## Step 6. Install MariaDB

- Open your Terminal and run `brew install mariadb`

## Running GIRAF

Refer to [this guide](./Running_GIRAF)

## Troubleshooting

If you encounter any issues:

- Ensure your macOS is up to date
- Try running `brew doctor` to check for any Homebrew-related issues
- Ensure Xcode and Command Line Tools are up to date: `softwareupdate --all --install --force`
- Run `flutter doctor` for diagnostics and follow its recommendations
