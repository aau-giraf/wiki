# Windows Setup Guide

This guide explains how to set up development of the **Visual Tangible Artifacts Giraf app** on a Windows PC using an **Android emulator**.

---

## Prerequisites

Make sure your system meets the following requirements:

- **Operating System**: 64-bit Windows 10 or Windows 11
  > ⚠️ 32-bit (x86) Windows is **not supported** — Android Studio, Flutter, and the emulator all require 64-bit Windows.

- **Free Disk Space**: Up to ~35 GB may be needed if you start with nothing installed (real usage is usually lower).

- **CPU Virtualization Enabled**: Enabled in BIOS/UEFI (Intel VT-x or AMD-V).
  > [Enable virtualization (Microsoft Guide)](https://support.microsoft.com/en-us/windows/enable-virtualization-on-windows-c5578302-6e43-4b4b-a449-8ced115f58e1)

- **Git for Windows Installed**: [Download & Install](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

- **Windows Developer Mode Enabled**: [Enable Developer Mode](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development)

- **Android Studio Installed** (full install, includes SDK and Emulator): [Download](https://developer.android.com/studio/install)

- **Flutter SDK Installed** (with `flutter\bin` added to your PATH): [Install Guide](https://docs.flutter.dev/get-started/install/windows/mobile#install-the-flutter-sdk)

---

## Setup Steps

---

### Step 1: Clone the repository

Open a terminal of your choice (e.g. Command Prompt, PowerShell, VSCode Terminal etc.), and clone the repository into your chosen directory by running:

```bash
git clone https://github.com/aau-giraf/visual-tangible-artefacts.git
```

---

### Step 2: Navigate to the project frontend

```bash
cd vta-giraf/Frontend/vta_app
```

---

### Step 3: Configure Android Studio SDK

1. Open **Android Studio**.

2. Go to **File > Settings > Languages & Frameworks > Android SDK**.

3. In the **SDK Tools** tab, make sure the following are checked:

   ✅ Android SDK Command-line Tools

   ✅ Android Emulator

   ✅ Android SDK Platform-Tools

> ℹ️ By default, Android Studio already installs at least one Android SDK platform and sets up sample virtual devices in the **Virtual Device Manager**, but **Android SDK Command-line Tools** usually isn't installed by default.

---

### Step 4: Accept Android Licenses

In the terminal run:

```bash
flutter doctor --android-licenses
```

Press **`y`** to accept each license.

---

### Step 5: Verify Flutter Installation

In the terminal run:

```bash
flutter doctor
```

Confirm that **Android toolchain** and **Android Studio** show no issues.

---

### Step 6: Start the Android Emulator

- In Android Studio, go to **Tools > Virtual Device Manager**.

- You should already see a default virtual device (e.g. Medium Phone).

- Select it and click **▶ Start**.

> Tip: You can also launch from the terminal:

```bash
flutter emulators
flutter emulators --launch <emulator_id>
```

---

### Step 7: Run the App

From the project frontend folder (`Frontend/vta_app`):

```bash
flutter run
```

Select your emulator if prompted.

---

### Step 8: Install .NET 8.0 SDK

1. Download the .NET 8.0 SDK installer from <https://dotnet.microsoft.com/en-us/download/dotnet/8.0>
2. Run the installer and follow the prompts to complete the installation.

### Bonus: Running as a Windows App

If you also want to build and run the app as a native Windows desktop application:

1. Install **Visual Studio** (full IDE, not VS Code).

2. Select the **“Desktop development with C++”** workload, including all default components.
   > [Visual Studio Download](https://visualstudio.microsoft.com/downloads/)

3. Run:

```bash
flutter doctor
```

You should now see **Windows desktop** listed as a supported platform, and can now choose it as an option when running the app.

---
