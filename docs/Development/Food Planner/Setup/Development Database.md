# Development Database

The development database should be used as a source of realistic, read-only data. Clone or import its contents into a local database that the backend connects to - **never** point the backend directly at the development database.

## Connecting to the Development Database

When connecting to the database, it is recommended in most cases to connect using the `readonly` role. To do so you must first be connected to the AAU network or the [AAU VPN](https://www.en.its.aau.dk/instructions/vpn#set-up-vpn-on-windows-and-mac-) ([Cisco Secure Client download](https://kb.itd.commonwealthu.edu/books/network/page/download-cisco-secure-client)). After connecting to the network or VPN, use the following credentials:

- Host: `130.225.39.155`
- Port: `5432`
- Username: `readonly`
- Password: `postgres`

After connecting to the database you can migrate the data to a local database in different ways, for example using `pg_dump` and `pg_restore`, or with database management tools such as pgAdmin or DBeaver.

## Updating the Development Database

If it is necessary to update the development database, log in as the `postgres` superuser. The credentials for the `postgres` role can be requested.

Note that the `postgres` role has full privileges. Make a backup before making any changes to ensure data can be recovered if something goes wrong.
