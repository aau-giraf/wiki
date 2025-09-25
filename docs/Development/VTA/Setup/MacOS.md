# macOS Setup Guide

This guide explains how to set up **frontend development** of the **Visual Tangible Artifacts (VTA) Giraf app** on macOS using an **iPad simulator**.

---

## Prerequisites

Make sure your system meets the following requirements:

- **Operating System**: macOS 10.15 (Catalina) or newer

  - Intel or Apple Silicon chips are supported
  - ⚠️ **macOS 10.14 (Mojave) and earlier are not supported** — Flutter requires macOS 10.15+

- **Free Disk Space**: ~25-30 GB may be needed for frontend development setup

  - Xcode: ~15 GB
  - Flutter SDK: ~1.5 GB
  - Dependencies and simulators: ~10-15 GB

- **Apple ID**: Required for Xcode and iOS simulator downloads

---

## Required Software Installation

### 1. Install Homebrew (Package Manager)

If you don't have Homebrew installed:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After installation, add Homebrew to your PATH (follow the instructions shown after installation).

### 2. Install Git

```bash
brew install git
```

Verify installation:

```bash
git --version
```

### 3. Install Xcode

1. Open the **App Store**
2. Search for **Xcode** and install it (this will take a while - ~15 GB download)
3. Open Xcode and accept the license agreements
4. Install additional components when prompted

Alternatively, install via command line:

```bash
xcode-select --install
```

### 4. Install Flutter SDK

#### Option A: Using Homebrew

```bash
brew install flutter
```

#### Option B: Manual Installation (Recommended)

1. Download Flutter from: https://docs.flutter.dev/get-started/install/macos/mobile-ios
2. Extract to desired location (e.g., `~/development/flutter`)
3. Add Flutter to your PATH in `~/.zshrc` or `~/.bash_profile`:

   ```bash
   export PATH="$PATH:$HOME/development/flutter/bin"
   ```

4. Reload your terminal or run:

   ```bash
   source ~/.zshrc
   ```

### 5. Install CocoaPods

CocoaPods is required for iOS dependencies:

```bash
sudo gem install cocoapods
```

If you encounter Ruby version issues:

```bash
brew install ruby
gem install cocoapods
```

---

## Setup Steps

### Step 1: Clone the Repository

Open Terminal and navigate to your desired directory:

```bash
git clone https://github.com/aau-giraf/visual-tangible-artefacts.git
cd visual-tangible-artefacts
```

### Step 2: Verify Flutter Installation

Run Flutter doctor to check for any issues:

```bash
flutter doctor
```

### Step 3: Set Up iOS Simulator

#### 3.1 Check Available iOS Runtimes

```bash
xcrun simctl list runtimes | grep iOS
```

This will show available iOS versions, e.g.:

```
iOS 17.5 (17.5 - 21F79) - com.apple.CoreSimulator.SimRuntime.iOS-17-5
iOS 18.1 (18.1 - 22B83) - com.apple.CoreSimulator.SimRuntime.iOS-18-1
```

#### 3.2 Create iPad Simulator

Use the latest iOS runtime from step 3.1:

```bash
xcrun simctl create "VTA iPad Pro" "com.apple.CoreSimulator.SimDeviceType.iPad-Pro-13-inch-M4" "com.apple.CoreSimulator.SimRuntime.iOS-18-1"
```

This command returns a device UUID, e.g.: `A1B2C3D4-E5F6-7890-ABCD-EF1234567890`

#### 3.3 Verify Simulator Creation

```bash
xcrun simctl list devices | grep "VTA iPad Pro"
```

### Step 4: Set Up Flutter Project

Navigate to the Flutter app directory:

```bash
cd Frontend/vta_app
```

Get Flutter dependencies:

```bash
flutter pub get
```

For iOS-specific setup:

```bash
cd ios
pod install
cd ..
```

### Step 5: Install .NET 8.0 SDK

#### Option A: Install using Homebrew

```bash
brew install dotnet@8
```

#### Option B: Manual Installation

1. Download the .NET 8.0 SDK installer from https://dotnet.microsoft.com/en-us/download/dotnet/8.0
2. Run the installer and follow the prompts to complete the installation.

## Running the Flutter App

1. Start the iPad simulator:

```bash
   ```bash
   xcrun simctl boot "VTA iPad Pro"
   ```

2. Open Simulator app:

   ```bash
   open -a Simulator
   ```

3. From `Frontend/vta_app`, run the Flutter app:

   ```bash
   flutter run
   ```

---

## Troubleshooting

### Common Issues

#### Flutter Doctor Issues

- **Xcode not found**: Ensure Xcode is installed and run `sudo xcode-select -s /Applications/Xcode.app/Contents/Developer`
- **CocoaPods not installed**: Run `sudo gem install cocoapods`
- **iOS toolchain issues**: Open Xcode and accept the license agreements, or run `sudo xcodebuild -license accept`

#### iOS Simulator Issues

- **Simulator not starting**: Try `xcrun simctl erase all` to reset simulators
- **App not installing**: Clean Flutter build with `flutter clean && flutter pub get`

#### Build Issues

- **iOS build failures**: Try `cd ios && pod install && cd ..` from the Flutter app directory
- **Certificate issues**: Ensure you're signed into Xcode with an Apple ID

---
