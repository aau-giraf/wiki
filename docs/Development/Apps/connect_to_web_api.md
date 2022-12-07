# Connect to Local Web API

- In the weekplanner repository locate: `…/<app_repository>/assets/environments.dev.json` 
  file line 2 change the `https://srv.giraf.cs.aau.dk/DEV/API` to:
    - If using an Android emulator: `http://localhost:5000`
    - If using a physical Android device on Windows: Plug your phyiscal device in and thereafter locate the Command Prompt where you will need to write the following: `adb reverse tcp:5000 tcp:5000`. Problems could occur if your physical Android device's Android version is not equal to or above Android 12. After that is completed do the steps above.
    - If using a phyiscal Android device and the steps above did not help try the following: Turn on "Use USB Tethering" in the device under networks settings. Next get your computer's local ip under network settings, this should be used in the environments.json file followed by :5000, e.g. http://192.168.42.130:5000
- In the web-api repository locate: `…/<app_repository>/GirafRest/appsettings.Development.json` file line 3 change the `"DefaultConnection": "server=192.38.56.153;port=3306;userid=root;password=Giraf123;database=giraf;Allow User Variables=True"` which could look different, to: `"DefaultConnection": "server=localhost;port=3306;userid=root;password=<password to your local database>;database=giraf;Allow User Variables=True"`
- Now: Simply run the app from your desired editor (Android Studio is recommended).
- If you are having problems with connecting to the database while being certain that the database is online and you are using either Android Studio or IntelliJ, try deleting the `build` folder created by the IDE in the weekplanner and rebuild it. This should make sure that correct `environments.json` file is read.
