# Proxy

For the Giraf project we only have two public IPs that both have a DNS name to
srv.giraf.cs.aau.dk. The firewall settings for those IPs are that only port ``80``
and port ``443`` are allowed through and since the different parts of the system
uses other ports, such as port ``5000`` and ``3306``, we need a reverse proxy
to pass the traffic intended for those ports into the Docker Swarm. In the following,
the configuration of the proxy will be elaborated upon.

## docker-compose.yml

Using the Docker Stack command for deploying to a production environment, a
``.yml`` file has to be passed to the command.
The file contains at least the following:

```yaml
version: '3'
services:
```

and can be elaborated with many more options. The file for the proxy is as follows:

```yaml
version: '3'

services:
    PROXY:
        image: nginx:1.15 # this will use the latest version of 1.15.x
        ports:
            - '80:80'       # expose 80 on the host and sent it to 80 in the container
            - '443:443'     # expose 443 on the host and sent it to 443 in the container
        volumes:            # mounts the nginx config folder inside the container
            - ./nginx/:/etc/nginx/
        networks:           # uses the frontend network to pass traffic into the containers
            - frontend

networks:
    frontend:               # creates a new network for frontend traffic
    backend:                # creates a new network for backend traffic
```

The code specifies a service called proxy that uses the nginx version 1.15.x and
that exposes the port 80 and 443 to the network. It has a volume attached where
the nginx config folder is mapped into the container. The networks are elaborated
in the [section about network](network.md).

## nginx.conf

The NGINX can be used for many different purposes and one of them is as a proxy.
The following config is a standard config for a reverse proxy that will enable
all sites in the ``/etc/nginx/sites-enabled/`` folder.

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

The API is file ``/etc/nginx/sites-enabled/API`` specifies where the traffic for
the API is supposed to go once the NGINX server receives it. We can use the
``proxy_pass http://API/`` inside Docker because it uses static DNS names inside
its network, all traffic for the API will be directed into the API service. This
means that the API can be accessed through http://srv.giraf.cs.aau.dk/API/ on both
port ``80`` and port ``443``.

```bash
server {
  listen 80;
  listen 443;

  server_name srv.giraf.cs.aau.dk;
    location /API/ {
      proxy_buffer_size   128k;
      proxy_buffers   4 256k;
      proxy_busy_buffers_size   256k;
      proxy_pass http://API/;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header Host $host;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```