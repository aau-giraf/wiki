# Docker Swarm configuration

The Docker Swarm is manged via the `docker-compose.yml` file that can be found in [GitHub](https://github.com/aau-giraf/giraf-production-swarm).

The `docker-compose.yml` file consists of the following:
```yaml
version: '3.7'

services:
    PROXY:                       # NGINX proxy service for the swarm
        image: nginx:1.15        # This will use the latest version of 1.15.x
        ports:                   # Exposes for 80 and 443 from the service to the swarm network(public)
            - '80:80'
            - '443:443'
        volumes:                 # Mounts the nginx config folder inside the container as read only
            - /swarm-nfs/nginx/:/etc/nginx/:r
            - /swarm-nfs/certbot/:/var/www/html/
        networks:                # Attaches the network
            - frontend
        deploy:                  # Deploy options
            replicas: 3          # Number er services
        healthcheck:             # Docker healthcheck restarts of the nginx service is not running three times in a row, service might be out for a maximum of 30 secunds
            test: ["CMD-SHELL", "service nginx status || exit 1"]
            interval: 10s
            timeout: 10s
            retries: 3

    API_PROD:                    # API service used for production
        image: giraf/web-api:1   # This will use version 1 of the API hosted on hub.docker.com
        networks:                # Attaches the network
            - frontend
            - backend
        environment:             # Sets local envionment for dotnet
            ASPNETCORE_ENVIRONMENT: Production
        deploy:                  # Deploy options
            replicas: 3          # Number of services
        volumes:                 # Mounts the two NFS file shares into the container
            - /swarm-nfs/cdn/pictograms/:/pictograms
            - /swarm-nfs/api/appsettings.Develop.json:/srv/appsettings.json
        healthcheck:             # Docker healthcheck restart of it fails three times in a row, service may be out for a maximum of 30 seconds
            test: ["CMD-SHELL", "curl --fail http://localhost:5000/v1/Status || exit 1"]
            interval: 10s
            timeout: 10s
            retries: 3

    API_DEV:                     # API service used for development
        image: giraf/web-api:1   # This will use version 1 of the API hosted on hub.docker.com
        networks:                # Attaches the network
            - frontend
            - backend
        environment:             # Sets local envionment for dotnet
            ASPNETCORE_ENVIRONMENT: Production
        deploy:                  # Deploy options
            replicas: 3          # Number of services
        volumes:                 # Mounts the two NFS file shares into the container
            - /swarm-nfs/cdn/pictograms/:/pictograms
            - /swarm-nfs/api/appsettings.Develop.json:/srv/appsettings.json
        healthcheck:             # Docker healthcheck restart of it fails three times in a row, service may be out for a maximum of 30 seconds
            test: ["CMD-SHELL", "curl --fail http://localhost:5000/v1/Status || exit 1"]
            interval: 10s
            timeout: 10s
            retries: 3

    API_TEST:                    # API service for testing new versions of the API before deploying to the other services.
        image: giraf/web-api:1   # This will use version 1 of the API hosted on hub.docker.com
        networks:                # Attaches the network
            - frontend
            - backend
        environment:             # Sets local envionment for dotnet
            ASPNETCORE_ENVIRONMENT: Production
        deploy:                  # Deploy options
            replicas: 1          # Number of services
        volumes:                 # Mounts the two NFS file shares into the container
            - /swarm-nfs/cdn/pictograms/:/pictograms
            - /swarm-nfs/api/appsettings.Develop.json:/srv/appsettings.json
        healthcheck:             # Docker healthcheck restart of it fails three times in a row, service may be out for a maximum of 30 seconds
            test: ["CMD-SHELL", "curl --fail http://localhost:5000/v1/Status || exit 1"]
            interval: 10s
            timeout: 10s
            retries: 3

    DB:                          # The DB service will be changed to use the production database later once it has been migrated. The httpd image is only for testing.
        image: mysql:8.0.19
        command: --default-authentication-plugin=mysql_native_password
        volumes:                 # Mounts the mysql files from the NFS to the container
            - /swarm-nfs/mysql/:/var/lib/mysql/
        environment:             # MySQL root password
            MYSQL_ROOT_PASSWORD: <password>
        networks:                # Attaches the network
            - backend
        deploy:                  # Deploy options
            restart_policy:      # On failure restart the service
                condition: on-failure

networks:                        # Defines networks in the swarm
    frontend:                    # Creates a new network for frontend traffic
    backend:                     # Creates a new network for backend traffic
```

## Updating the Docker Swarm

In order to update the running Docker Stack ssh to one of the master servers and execute do the following steps:

1. ssh to a master server, see [her](../ServerOwnership.md) for more information.
2. Clone the [GitHub repository](https://github.com/aau-giraf/giraf-production-swarm) onto the server or pull any new changes to the existing.
3. Verify the changes in the `docker-compose.yml` file are as expected.
4. Run `docker stack deploy -c docker-compose.yml Giraf`
5. Use the `docker service ls` command to verify that all services has started as expected.
6. Run the following command to logout of the server, `exit`.
