# Configuring the Development Environment

This guide provides step-by-step instructions to set up the development environment for the VTA project.

This guide assumes you have already followed the platform-specific setup guides for [Windows](./Windows.md), [macOS](./MacOS.md), or [Linux](./Linux.md).

## Important Note

The files created in this guide, has been added to `.gitignore` to avoid committing sensitive information to the repository. Do not add any sensitive information to any other files that are committed to the repository.

## Prerequisites

All nessecary secrets and connection strings can be found in the project's KeePass. See the [GIRAF Passwords](../../../Getting_Started/ownership_transfer.md) section for more information.

<!-- TODO: Sort out the link above -->

## Backend Configuration

### AppSettings.json

Create a file named `AppSettings.json` in the `/Backend/VTA.API/` directory containing the following configurations:

```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "ConnectionStrings": {
    "DefaultConnection": "<connection_string>"
  },
  "AllowedHosts": "*",
  "Secret": {
    "SecretKey": "<secret_key>",
    "ValidIssuer": "<issuer>",
    "ValidAudience": "<audience>"
  }
}
```

NOTE: Do not add any sensitive information to `AppSettings.Developement.json` as it is committed to the repository.

## Frontend Configuration

### app_settings.json

Create a file named `app_settings.json` in the `/Frontend/vta_app/assets/cfg/` directory containing the following configurations:

```json
{
  "ApiSettings": {
    "BaseUrl": {
      "Local": "<local_url>",
      "Remote": "<remote_url>"
    }
  },
  "OpenAi": {
    "ApiKey": "<api_key>"
  }
}
```
