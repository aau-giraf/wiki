# Practical Docker in a swarm

In the following the installation and setup process of DockerCE and Docker Swarm is described and at the end, some examples on how to use Docker Services is given.

## Installation of Docker 

To install DockerCE on a node in the Swarm the following command can be used to set up the local Docker environment:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh | sh get-docker.sh
```

Once the Docker engine has been installed it is recommended that the user is added to the Docker group so that every Docker command is not run as root, use the following command to do so:

```bash
sudo usermod -aG docker <USERNAME>@student.aau.dk
```

If the Docker installation is going to be used in a Docker Swarm at AAU, the following changes are needed since the AAU network is running on the default Docker subnet.

For local installations use the following.

```bash
nano /etc/docker/daemon.json
```

and insert the following:

```json
{
  "bip": "10.14.0.1/16",
  "ipv6": false
}
```

For the Swarm overlay network first create the network manualy with the following command:

```bash
docker network create --subnet 10.10.0.0/16 -o com.docker.network.bridge.enable_icc=false -o com.docker.network.bridge.name=docker_gwbridge 
```

## Initializing the Swarm

REMEMBER TO CREATE THE NETWORK FIRST
On the first master server run the following command:

```bash
docker swarm init
```

### Adding a manager to the Swarm

REMEMBER TO CREATE THE NETWORK FIRST
Once the Docker Swarm is initialized used the following command on the first master server to get the join token for the swarm:

```basj
docker swarm join-token --manager
```

The output is copied to the new master server.

### Adding a worker to the Swarm

REMEMBER TO CREATE THE NETWORK FIRST
To add a worker to the Swarm first run the following command on one of the managers:

```bash
docker swarm join-token worker
```

The output should be run on the servers intended to be workers in the Swarm.

Now the Docker Swarm has been created and is ready to serve.

Use the following command to verify the Swarm setup:

```bash
docker swarm ls
```

The output should look like this:

| ID                           | HOSTNAME                   | STATUS             | AVAILABILITY       | MANAGER STATUS     | ENGINE VERSION |
| :--------------------------- | :------------------------- | :----------------- | :----------------- | :----------------- | :------------- |
| yny9ky6b6zczqrjzxd7sl71k6 *  | giraf-master00.srv.aau.dk  | Ready              | Active             | Leader             | 18.09.3        |
| 2n08r588w9p8xazc5cm8r6o9o    | giraf-master01.srv.aau.dk  | Ready              | Active             | Reachable          | 18.09.3        |
| wrr68nqt116tk1rszwvdv1nmk    | giraf-node00.srv.aau.dk    | Ready              | Active             |                    | 18.09.3        |
| bhh5mitvwzdhzbky1cjne9ffg    | giraf-node01.srv.aau.dk    | Ready              | Active             |                    | 18.09.3        |
| as7n375y2gwcj5vf4h73h9ron    | giraf-node02.srv.aau.dk    | Ready              | Active             |                    | 18.09.3        |
| koclcs8nxt0y6qu4ho511la0m    | giraf-node03.srv.aau.dk    | Ready              | Active             |                    | 18.09.3        |


## Examples of using a service

Once the Docker Swarm has been set up, it can be used to serve the different parts of the project. In the following, we will give some examples of how to work with the Swarm.

### Example nginx

To create a new service use the following:

```bash
docker service create --name nginx-giraf-proxy --replicas 2 -p 80:80 -p 443:443 nginx:1.15
```

Be running this command an service with two containers will be stated and the containers will have port 80 and 443 exposed to the internet and can be accessed on the Swarms public IP's. The two containers will be running the nginx version 1.15.

To upgrade the version that a service uses run the following to downgrade or upgrade the service:

```bash
docker service update --image nginx:1.12 nginx-giraf-proxy
```

To encrease the number of contaners a service creates use the following command:

```bash
docker service scale nginx-giraf-proxy=5
```

To verify the service use the following command:

```bash
docker service ps nginx-giraf-proxy
```

The outpus should look like this:

| ID                 | NAME               | IMAGE              | NODE                       | DESIRED STATE      | CURRENT STATE           | ERROR              | PORTS |
| :------------------|:-------------------|:-------------------|:---------------------------|:-------------------|:------------------------|:-------------------|:-----|
| iksklc50ttxt       | nginx-giraf-proxy.1| nginx:latest       | giraf-master01.srv.aau.dk  | Running            | Running 29 minutes ago  |                    ||

Note that the ports exposed are not listed in this view since it is served through the service and can be seen then running the following command:

```bash
docker service ls
```

| ID                 | NAME               | MODE               | REPLICAS           | IMAGE              | PORTS |
| :------------------|:-------------------|:-------------------|:-------------------|:-------------------|:------|
| k6nuoecmam6m       | proxy              | replicated         | 5/5                | nginx:latest       | *:80->80/tcp, *:443->443/tcp|
