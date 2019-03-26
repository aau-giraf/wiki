# Networking Docker Swarm

Networking in a Docker Swarm is fairly easy. In the docker-compose.yml file simply add the name of the networks and specify which services is connected to which network. A service can be connected to 0 or more networks and a network not connected to anything does not make any sense.

The Docker Swarm has two networks to separate different services in case one of them i compromised by an intruder.

The frontend network is used to exchange information between the NGINX Proxy and the API.

The backend network is used to exchange information between the API and database.

Since the database has the most sensitive information that we want to protect it makes sense to isolate it from the open internet.
