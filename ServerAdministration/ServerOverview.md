# Server Overview

In this article we describe what servers there are, what they are running and how to access them.

There are 6 servers available, all running:
```
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.2 LTS
Release:	18.04
Codename:	bionic
```

|Web (Nginx)            |Git                                        |                             
|---                    |---                                        |                                
| API Proxies           | [Github](https://github.com/aau-giraf)    | 

An illustration of the current server architecture can be seen in [Server Structure](.ServerArchitecture.md)

The structure of how docker works can also be read about in [Docker Structure](.docker.md)

ITS is responsible for the NFS that is mounted on all the nodes and masters in `/swarm-nfs/`.

## Accessing the Server

To access the server you need to use SSH to the AAU gateway.
This is required since all SSH ports to the servers are closed and can only be accessed from inside the AAU network. 

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
| Legacy              | http://srv.giraf.cs.aau.dk/API      |
| Test                | http://srv.giraf.cs.aau.dk/TEST/API |

## READ: Access to the server
Access to the server is granted to all students, sudo rights are ONLY given to members of the Server Meta Group.

The Server Meta Group has to contact ITS to get sudo.


## NOTICE: Network access workaround

If you are at home, and cannot access the AAU SSH gateway, simply use [AAU VPN](https://www.its.aau.dk/vejledninger/vpn/)