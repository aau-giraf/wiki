# Proxy

For the Giraf project we only have two public IP's that both has an DNS A name to srv.giraf.cs.aau.dk. The firewall settings for those ips are that only port ```80``` and port ```443``` are allowed through and since the different parts of the system uses other ports such as port ```5000``` and ```3306``` we need an reverse proxy to pass the traffic intended for those port into our Docker Swarm. In the following the configuration of the proxy will be elaborated upon.

## docker-stack.yml

Then using the ocker stack command for deploying to an production environment the stack file by convention has the name ```docker-stack.yml```.
The file contains at least the following:

```yml
version: '3'
services:
```

and can be elaborated with many more options. The file for the proxy is as follows:

```yml
version: '3'

services:
    proxy:
        image: nginx:1.15 # this will use the latest version of 1.15.x
        ports:
            - '80:80'       # expose 80 on the host and sents it to 80 in the container
            - '443:443'     # expose 443 on the host and sents it to 443 in the container
        volumes:            # mounts the nginx config folder inside the container as readonly
            - ./nginx/:/etc/nginx/
        networks:           # uses the frontend network to pass trafic into the containers
            - frontend

networks:
    frontend:               # creates a new network for frontend traffic
```

The code specifies a service called proxy that uses the nginx version 1.15.x and that exposes the port 80 and 443 to the network. It has a volume attached where the nginx config folder is mapped into the container. It is attached to a network called frontend witch is used to exchange information between the proxy and the API. There will also be an network for backend communication between the API and the Database server.

## nginx.conf

The NGINX can be used for many different purposes and one of them is as an proxy. The following config is a standard config for a reverse proxy that will enable all sites in the ```/etc/nginx/sites-enabled/``` folder. 

```bash
worker_processes  1;

events {
    worker_connections  1024;
}


http {
    upstream srv.giraf.cs.aau.dk {
        server proxy;
    }
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;
    include /etc/nginx/sites-enabled/*;
    gzip  on;
    client_max_body_size 20m;
}
```

## API

The API is file under ```/etc/nginx/sites-enabled/``` specifies where the traffic for the API is supposed to go once the NGINX server receives it. We can use the ```proxy_pass http://API``` since docker uses static DNS names inside its network all traffic for the API will be directed into the API container.

```bash
server {
  listen 80;
  listen 443;

  server_name srv.giraf.cs.aau.dk;
    location / {
      proxy_buffer_size   128k;
      proxy_buffers   4 256k;
      proxy_busy_buffers_size   256k;
      proxy_pass http://API;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header Host $host;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

