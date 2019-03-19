This server is the one of two master serveres for the Docker Swarm that supports the Giraf project at Aalborg University.

On the entire setup all servers has DockerCE installed and at the time of this writing with version 18.09.3.
Since the AAU network uses the same ip range that docker uses by deafult this docker network ip range has been changed.
Each local docker installation has been configured to use 10.14.0.0/16 and the briged network across the swarm uses 10.10.0.0/16 as ip range.

For the swarm each network had to be created by hand on each machine with the following command:

	docker network create --subnet 10.10.0.0/16 -o com.docker.network.bridge.enable_icc=false -o com.docker.network.bridge.name=docker_gwbridge docker_gwbridge

The local docker network setup can be found at /etc/docker/deamon.json

The current layout of the docker swarm is as follows:

ID                            HOSTNAME                    STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
yny9ky6b6zczqrjzxd7sl71k6 *   giraf-master00.srv.aau.dk   Ready               Active              Leader              18.09.3
2n08r588w9p8xazc5cm8r6o9o     giraf-master01.srv.aau.dk   Ready               Active              Reachable           18.09.3
wrr68nqt116tk1rszwvdv1nmk     giraf-node00.srv.aau.dk     Ready               Active                                  18.09.3
bhh5mitvwzdhzbky1cjne9ffg     giraf-node01.srv.aau.dk     Ready               Active                                  18.09.3
as7n375y2gwcj5vf4h73h9ron     giraf-node02.srv.aau.dk     Ready               Active                                  18.09.3
koclcs8nxt0y6qu4ho511la0m     giraf-node03.srv.aau.dk     Ready               Active                                  18.09.3

and the network is as follows:

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


The docker swarm is serving the WEB API for the Giraf Project with an number of replicas to ensure that at least one of the WEB API's har aviable to serve clients.

The swarm is intended to run its services as a stack. 
