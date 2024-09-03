# Running GIRAF

## Preliminaries

1. Clone both `https://github.com:aau-giraf/weekplanner.git` and `https://github.com:aau-giraf/web-api.git` as mentioned in "[Environment Setup](/Setup/Index)"

## Step 1. Running the Web-API

1. Open `appsettings.Development.json` in the cloned `web-api/GirafAPI` directory from earlier and change `password` to what you selected when installing MariaDB
2. Navigate to the cloned `web-api` directory from earlier, either in Terminal (macOS/Linux) or PowerShell (Windows), and run:
   1. `dotnet restore`
   2. `dotnet-ef database update`
   3. `dotnet run --sample-data`

## Step 2. iOS Simulator

1. Open Simulator app (CMD + Space to search for it)
2. Navigate to the `weekplanner` directory, that you cloned
3. Run `cp .env.example .env` in your Terminal
4. Run `flutter pub get` in your Terminal
5. Run `flutter run` in your Terminal

## Step 2. Android Simulator

1. Open the `weekplanner` directory that you cloned
2. Copy `.env.example`, and rename the copy to `.env`
3. Open Android Studio
4. Select the pre-installed Android emulator near the top-right corner, or create a new device in _Tools > Device Manager_
5. Select the `main.dart` runtime and press _Run_
