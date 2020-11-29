# Overview

In this article we describe what servers there are, what they are running and how
to access them.

There are 6 servers available, all running:

```
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.2 LTS
Release:	18.04
Codename:	bionic
```

|Name                       |Internal IP    |External IP   |
|---                        |---            |---           |
|giraf-master00.srv.aau.dk  |172.19.10.29   |192.38.56.151 |
|giraf-master01.srv.aau.dk  |172.19.10.30   |192.38.56.153 |
|giraf-node00.srv.aau.dk    |172.19.10.31   |N/A           |
|giraf-node01.srv.aau.dk    |172.19.10.32   |N/A           |
|giraf-node02.srv.aau.dk    |172.19.10.33   |N/A           |
|giraf-node03.srv.aau.dk    |172.19.10.34   |N/A           |

|Web (Nginx)            |Git                                        |
|---                    |---                                        |
| API Proxies           | [Github](https://github.com/aau-giraf)    |

An illustration of the current server architecture can be seen in [Server Structure](architecture.md)

The structure of how docker works can also be read about in [Docker Structure](Docker/general_information.md)

ITS is responsible for the NFS that is mounted on all the nodes and masters in
`/swarm-nfs/`.

## Accessing the Server

To access the server you need to SSH to the AAU gateway.
This is required since all SSH ports to the servers are closed and can only be
accessed from inside the AAU network.

`ssh -t sshgw.aau.dk -l <USERNAME>@student.aau.dk  ssh 172.19.10.<ip>`

|Name                       |Internal IP    |External IP   |
|---                        |---            |---           |
|giraf-master00.srv.aau.dk  |172.19.10.29   |192.38.56.151 |
|giraf-master01.srv.aau.dk  |172.19.10.30   |192.38.56.153 |
|giraf-node00.srv.aau.dk    |172.19.10.31   |N/A           |
|giraf-node01.srv.aau.dk    |172.19.10.32   |N/A           |
|giraf-node02.srv.aau.dk    |172.19.10.33   |N/A           |
|giraf-node03.srv.aau.dk    |172.19.10.34   |N/A           |


## Web-API

The WEB API runs in a docker container, which is routed by NGINX.
The WEB API is only available on port 80 and 443 on the URLs shown below.

| Stage               | URL                                 |
|---                  |---                                  |
| Production          | http://srv.giraf.cs.aau.dk/PROD/API |
| Development         | http://srv.giraf.cs.aau.dk/DEV/API  |
| Test                | http://srv.giraf.cs.aau.dk/TEST/API |

## Networking Drives and specific server-setups

As mentioned above, ITS will attach a network drive at `/swarm-nfs/`, which should
include the following:

   - api/
       - appsettings.Develop.json
       - appsettings.Production.json
       - appsettings.Testing.json
   - backup/
   - cdn/
       - dev/
       - pictograms/
       - test/
       - pictograms/
       - prod/
       - pictograms/
   - certbot/
   - mysql/
   - nginx/
       - certs/
       - sites-enabled/
       - nginx.conf

Furthermore, the master00 server, should execute the following cronjob:

```bash
certbot renew --webroot -w /swarm-nfs/certbot/ -d srv.giraf.cs.aau.dk --post-hook "cp -RL /etc/letsencrypt/live/srv.giraf.cs.aau.dk/. /swarm-nfs/nginx/certs/"
```

This is done to ensure a single point of certificate-authority on the first masterserver,
that after renewing the certificate, moves it into the /swarm-nfs/nginx/certs.
This is done to ensure that the certificate is available on all of the servers,
and that the nginx Giraf_PROXY service mounts this folder and the certificate.

## READ: Access to the server

Access to the server is granted to all students, sudo rights are ONLY given to members
of the Server Meta Group.

The Server Meta Group has to contact ITS to get sudo.
More can be found in [Server Ownership](access.md)

## NOTICE: Network access workaround

If you are at home, and cannot access the AAU SSH gateway, simply use [AAU VPN](https://www.its.aau.dk/vejledninger/vpn/)

## VIDEO: Short video on how to connect

https://youtu.be/KZYsAJDHlxo
