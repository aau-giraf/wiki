# Architecture

In the following, the server architecture for the giraf project will be explained.

## Old Servers (DISCONTINUED)

| Name      | IP            | Specs |
| :---      | :---          | :---  |
| Master00  | 192.38.56.37  | 2 GB RAM 2xCPU Disk: 22 GB OS: CentOS Linux release 7.5.1804 (Core) |
| Node01    | 172.19.0.244  | 2 GB RAM 1xCPU Disk: 22 GB OS: CentOS Linux release 7.5.1804 (Core) |
| Node02    | 172.19.0.245  | 2 GB RAM 1xCPU Disk: 22 GB OS: CentOS Linux release 7.5.1804 (Core) |
| Node03    | 192.38.56.36  | 2 GB RAM 1xCPU Disk: 22 GB OS: CentOS Linux release 7.5.1804 (Core) |
| GitLab    | 192.38.56.136 | 4 GB RAM 2xCPU Disk: 46 GB OS: CentOS Linux release 7.5.1804 (Core) |
| web01     | 192.38.56.38  | 2 GB RAM 1xCPU Disk: 22 GB OS: CentOS Linux release 7.4.1708 (Core) |
| Backup01  | 172.19.0.235  | 4 GB RAM 2xCPU Disk: 10 GB OS: CentOS Linux release 7.2.1511 (Core) |

The only user on these servers are root, and each server has everything open to
the internet and is hence under heavy attack from malicious users trying to brute-force
the passwords.

## New Servers

| Name | Internal IP | External IP| Specs |
|:---- | :---------- | :--------- | :-----|
| giraf-master00.srv.aau.dk | 172.19.10.29 | 192.38.56.151 | Ram: 4 GB 2xCPU Disk: 24 GB OS: Ubuntu Server 18.04.2 |
| giraf-master01.srv.aau.dk | 172.19.10.30 | 192.38.56.153 | Ram: 4 GB 2xCPU Disk: 24 GB OS: Ubuntu Server 18.04.2 |
| giraf-node00.srv.aau.dk   | 172.19.10.31 | N/A | Ram: 2 GB 1xCPU Disk: 24 GB OS: Ubuntu Server 18.04.2             |
| giraf-node01.srv.aau.dk   | 172.19.10.32 | N/A | Ram: 2 GB 1xCPU Disk: 24 GB OS: Ubuntu Server 18.04.2             |
| giraf-node02.srv.aau.dk   | 172.19.10.33 | N/A | Ram: 2 GB 1xCPU Disk: 24 GB OS: Ubuntu Server 18.04.2             |
| giraf-node03.srv.aau.dk   | 172.19.10.34 | N/A | Ram: 2 GB 1xCPU Disk: 24 GB OS: Ubuntu Server 18.04.2             |

The two public IP's for the project only has port 80 and port 443 open.
Each node has been configured to use the ```10.14.0.0/16``` subnet for the local
docker daemon. For the swarm overlay network, the ```10.10.0.0/16``` subnet is used.

### Web-API

The WEB API runs in a docker container, which is routed by NGINX.
The WEB API is only available on port 80 and 443 on the URLs shown below.

| Stage               | URL                                 |
|---                  |---                                  |
| Production          | http://srv.giraf.cs.aau.dk/PROD/API |
| Development         | http://srv.giraf.cs.aau.dk/DEV/API  |
| Test                | http://srv.giraf.cs.aau.dk/TEST/API |

### Network Drives

ITS is responsible for the NFS that is mounted on all the nodes and masters in
`/swarm-nfs/`.

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

### The Docker Setup

More information on Docker can found [here](./Docker/index.md).

#### Nodes

| ID                           | HOSTNAME                   | STATUS             | AVAILABILITY       | MANAGER STATUS     | ENGINE VERSION |
|:-----------------------------|:---------------------------|:-------------------|:-------------------|:-------------------|:---------------|
| yny9ky6b6zczqrjzxd7sl71k6 *  | giraf-master00.srv.aau.dk  | Ready              | Active             | Leader             | 18.09.3        |
| 2n08r588w9p8xazc5cm8r6o9o    | giraf-master01.srv.aau.dk  | Ready              | Active             | Reachable          | 18.09.3        |
| wrr68nqt116tk1rszwvdv1nmk    | giraf-node00.srv.aau.dk    | Ready              | Active             |                    | 18.09.3        |
| bhh5mitvwzdhzbky1cjne9ffg    | giraf-node01.srv.aau.dk    | Ready              | Active             |                    | 18.09.3        |
| as7n375y2gwcj5vf4h73h9ron    | giraf-node02.srv.aau.dk    | Ready              | Active             |                    | 18.09.3        |
| koclcs8nxt0y6qu4ho511la0m    | giraf-node03.srv.aau.dk    | Ready              | Active             |                    | 18.09.3        |

#### Network

```bash
[
    {
        "Name": "ingress",
        "Id": "esq3c70wonolez79eifsqeqhc",
        "Created": "2019-03-15T09:32:18.169968631+01:00",
        "Scope": "swarm",
        "Driver": "overlay",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "10.255.0.0/16",
                    "Gateway": "10.255.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": true,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "ingress-sbox": {
                "Name": "ingress-endpoint",
                "EndpointID": "f8f1417b758bc994a9c77aeda536b0a9e4294226baf29117382913e88bac8702",
                "MacAddress": "02:42:0a:ff:00:02",
                "IPv4Address": "10.255.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {
            "com.docker.network.driver.overlay.vxlanid_list": "4096"
        },
        "Labels": {},
        "Peers": [
            {
                "Name": "b6a2fb9fd60e",
                "IP": "172.19.10.29"
            },
            {
                "Name": "e17ba5bebf00",
                "IP": "172.19.10.31"
            },
            {
                "Name": "8a720eeaec16",
                "IP": "172.19.10.32"
            },
            {
                "Name": "9a1a09913233",
                "IP": "172.19.10.34"
            },
            {
                "Name": "b38a3e1ca567",
                "IP": "172.19.10.33"
            },
            {
                "Name": "943610ab56f5",
                "IP": "172.19.10.30"
            }
        ]
    }
]
```
