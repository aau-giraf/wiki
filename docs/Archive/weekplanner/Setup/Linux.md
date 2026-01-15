# Linux Setup Guide

## Step 1: Update and Upgrade Your System

Before installing new software, it's a good practice to update your system:

```bash
sudo apt update && sudo apt upgrade -y
```

## Step 2: Install OpenJDK

Install OpenJDK using your distribution's package manager:

```bash
sudo apt install default-jdk
```

Verify the installation:

```bash
java --version
```

## Step 3: Install Flutter

_Please refer to the [Flutter installation guide](https://docs.flutter.dev/get-started/install/linux/android) if you face issues_

### Prerequisites

#### Install required dependencies

```bash
sudo apt install clang cmake ninja-build pkg-config libgtk-3-dev liblzma-dev
```

### Installation

1. Download Flutter:

```bash
wget https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.24.1-stable.tar.xz
```

2. Extract the downloaded file:

```bash
tar xf flutter_linux_3.24.1-stable.tar.xz
```

3. Add Flutter to your PATH. Add this line to your `~/.bashrc` or `~/.zshrc` file:

```bash
export PATH="$PATH:[PATH_TO_FLUTTER_GIT_DIRECTORY]/flutter/bin"
```

Replace `[PATH_TO_FLUTTER_GIT_DIRECTORY]` with the path where you extracted Flutter.

4. Reload your shell configuration:

```bash
source ~/.bashrc  # or source ~/.zshrc if you're using Zsh
```

5. Verify the installation:

```bash
flutter --version
```

## Step 4: Install .NET 8.0

1. Add the Microsoft package signing key and repository:

```bash
wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb
```

2. Install the .NET 8.0 SDK:

```bash
sudo apt update && sudo apt install -y dotnet-sdk-8.0
```

3. Verify the installation:

```bash
dotnet --version
```

## Step 5: Install MariaDB

1. Install MariaDB:

```bash
sudo apt install mariadb-server
```

2. Secure the MariaDB installation:

```bash
sudo mysql_secure_installation
```

Follow the prompts to set a root password and secure your installation.

## Running GIRAF

Refer to [this guide](../Running_GIRAF)

## Troubleshooting

If you encounter any issues:

- Ensure your Linux distribution is up to date
- Run `flutter doctor` for diagnostics and follow its recommendations
- Check system logs for any error messages: `journalctl -xe`
- Ensure all required dependencies are installed
- If you're using a different Linux distribution, consult its documentation for equivalent commands

Note: This guide assumes you're using a Debian-based distribution like Ubuntu. If you're using a different distribution, you may need to adjust some commands (e.g., use `yum` instead of `apt` for Red Hat-based systems).
