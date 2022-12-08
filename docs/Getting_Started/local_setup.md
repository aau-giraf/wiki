# How to setup a local development environment for GIRAF

## Installing MySQL
![mysql install 1](https://user-images.githubusercontent.com/9339576/205648638-5f536ca6-df97-405d-9d20-172bbda4649a.png)
![mysql install 2](https://user-images.githubusercontent.com/9339576/205648739-29ca9f66-3a6b-402e-8fa1-fd30c89e0505.png)
![mysql install 3](https://user-images.githubusercontent.com/9339576/205648754-ba42849c-adce-4afa-9a4b-eaa2df0595a6.png)
![mysql install 4](https://user-images.githubusercontent.com/9339576/205648786-ce1f657f-2f2f-4605-a8d6-f9f9a864d2ce.png)
If any of the downloads fail, just click "Try Again"
![mysql install 5](https://user-images.githubusercontent.com/9339576/205648824-9c58bc7b-ec42-4618-bb11-c75671a80741.png)
![mysql install 6](https://user-images.githubusercontent.com/9339576/205648856-7d835a53-335f-4dba-9f79-2cd8fa1e7591.png)
![mysql install 7](https://user-images.githubusercontent.com/9339576/205648865-2c3d33df-c738-43ca-9190-d48ee5b9cdf1.png)
![mysql install 8](https://user-images.githubusercontent.com/9339576/205648879-0fc0da6f-8b85-4948-8ffd-de4e765fd7ea.png)
![mysql install 9](https://user-images.githubusercontent.com/9339576/205648895-4038155c-54cd-4df9-8227-f3fd9ae82c0d.png)
![mysql install 10](https://user-images.githubusercontent.com/9339576/205648903-58b4c585-a1b8-48a6-b0dd-4f20117e93fe.png)
![mysql install 11](https://user-images.githubusercontent.com/9339576/205648914-6c465226-3afc-4cae-81d0-f72e10ffa127.png)
![mysql install 12](https://user-images.githubusercontent.com/9339576/205648928-c0c895c0-d6a5-40b9-a28d-6b3e07df6c89.png)
![mysql install 13](https://user-images.githubusercontent.com/9339576/205648943-c6b77ae6-9696-4ae8-b626-13f9189a8161.png)
![mysql install 14](https://user-images.githubusercontent.com/9339576/205651124-f6525e7a-06ea-4a50-a196-689f45f03081.png)
![mysql install 15](https://user-images.githubusercontent.com/9339576/205651141-88e8142f-14cb-4a6a-b220-cebbb434963b.png)
![mysql install 16](https://user-images.githubusercontent.com/9339576/205651151-888c1019-004f-4419-b24c-85bc1fa03359.png)
![mysql install 17](https://user-images.githubusercontent.com/9339576/205651166-c49df712-1b15-48ca-a787-e0772561c3d2.png)
![mysql install 18](https://user-images.githubusercontent.com/9339576/205651184-0f0ed707-ef80-4fc3-90d3-4d1ed6f3a88d.png)

## Starting the MySQL server
![tjenester1](https://user-images.githubusercontent.com/9339576/205654164-d6e0fe7a-e2f7-41e4-8248-3fed82e3b87b.png)
![tjenester2](https://user-images.githubusercontent.com/9339576/205654211-6cee68a5-2ac0-4a9c-854f-fc641f61f132.png)

## Configuring Weekplanner and Web-API repositories to work locally
1. Go to weekplanner/lib/main.dart
2. Change `'assets/environments.dev.json'` to `'assets/environments.local.json'` on line 29
3. Go to web-api/GirafRest/appsettings.Development.json
4. Change the server variable to `server=localhost` in the `DefaultConnection` key

## Building the database for the Web-API and running it with sample data
1. Open command prompt in web-api/GirafRest
![Command Prompt](https://user-images.githubusercontent.com/9339576/206396781-67c4ec1b-8190-4eb5-afeb-98e3e741f295.png)
2. Type `dotnet-ef database update`
3. Type `dotnet run --sample-data`

## Making sure everything works
1. Run the weekplanner application on your emulator
2. Login using the default credentials
* Username: `guardian-dev`
* Password: `password`

If you successfully log in and see output in the Web-API console window, then you are successfully running everything locally

## Updating the database when changes are made to the Web-API without migrations
1. Drop the `giraf` database in the MySQL server
![updatedb1](https://user-images.githubusercontent.com/9339576/205662140-c550d8f7-1015-4e81-b27c-7e22e59677cb.png)
![updatedb2](https://user-images.githubusercontent.com/9339576/205662200-39e7f0a7-2ea3-40a1-b6b6-278060d812ea.png)
2. [Rebuild the database](https://github.com/aau-giraf/.github/blob/main/wiki/setup-guide/local_setup.md#building-the-database-for-the-web-api-and-running-it-with-sample-data)
