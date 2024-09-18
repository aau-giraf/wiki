# Windows Setup Guide

**Be mindful that your computer needs to support virtualisation in order to run the Android Simulator!**

## Step 1. Install OpenJDK (or similar)

1. [Download OpenJDK](https://learn.microsoft.com/en-us/java/openjdk/download)
2. Run through the installer

## Step 2: Install Flutter

1. Create a folder where you want to install Flutter (e.g., `C:\dev`).
2. [Download the Flutter SDK](https://docs.flutter.dev/get-started/install/windows)
3. Extract the downloaded zip file into the folder you created (e.g., `C:\dev\flutter`).

4. Add Flutter to your PATH:

   - Open the Start menu and search for "Environment Variables"
   - Click on "Edit the system environment variables"
   - Click the "Environment Variables" button
   - Under "System variables", find the "Path" variable and click "Edit"
   - Click "New" and add the full path to the `flutter\bin` directory (e.g., `C:\dev\flutter\bin`)
   - Click "OK" to save the changes

5. Open a new PowerShell window and verify the installation:

```powershell
flutter --version
```

## Step 3: Set up Android Studio

1. [Download Android Studio](https://developer.android.com/studio)
2. Run the installer and follow the installation wizard.
3. During installation, ensure that the "Android Virtual Device" option is selected.
4. Once installed, open Android Studio.
5. Go to File > Settings > Plugins (on Windows)
6. Search for and **install the Flutter and Dart plugins**
7. Restart Android Studio to activate the plugins
8. Go into _Settings > Languages & Frameworks > Dart_ and set the relevant path to the Dart SDK, e.g. `C:\dev\flutter\bin\cache\dart-sdk`, and enable the `weekplanner` module

## Step 4. Installing MariaDB

1. [Download MariaDB](https://mariadb.org/download/)
2. Select the latest stable version for Windows and choose the appropriate package (MSI) for your system architecture (32-bit or 64-bit)
3. Run the wizard and set a root password you'll be able to remember later.
4. Select HeidiSQL and configure other options as needed (default settings are usually fine).
5. Open HeidiSQL and log in with the password you chose earlier
6. Right-click in the left panel, and choose _New > Database_ and make a database called `giraf`

## Step 5. Installing .NET with Entity Framework

1. [Download the .NET 8 SDK installer for Windows](https://dotnet.microsoft.com/download/dotnet/8.0)
2. Run the installer and follow the prompts
3. Run the following command: `dotnet --version` – you should see the installed .NET version (8.x.x)
4. Run the following command:

`dotnet tool install --global dotnet-ef`

You can then run `dotnet ef` to verify the installation.

## Running GIRAF

Refer to [this guide](./Running_GIRAF)

## Troubleshooting

If you encounter any issues:

- Ensure your Windows installation is up to date
- Run `flutter doctor` for diagnostics and follow its recommendations
- Check the official Flutter documentation for known issues
- For permission issues, try running PowerShell as Administrator
- Ensure Java is in your PATH environment variable
