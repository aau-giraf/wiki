# Connect to Local Web API

- In the app repository in the `…/<app_repository>/assets/environments.json`
  file line 2 change the `http://srv.giraf.cs.aau.dk/DEV/API` to:
    - If using an Android emulator: `http://10.0.2.2:5000`
    - If using a hardware device: Turn on "Use USB Tethering" in the device under
     networks settings. Next get your computers local ip under network settings,
     this should be used in the `environments.json` file followed by `:5000`, e.g.
     `http://192.168.42.130:5000`
- Now: Simply run the app from your desired editor.
- If you are having problems in this step and are using either Android Studio or
  IntelliJ, delete the `build` folder created by the IDE and rebuild it. This should
  make sure that correct `environments.json` file is read.
- 