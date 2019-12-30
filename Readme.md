# Docker Basics

```bash

#  Checks image locally if not available then pulls from docker hub
docker run <image>

docker run hello-world

docker ps -a

docker rm <container id>

docker images

docker rmi <image name>

# Creating Image with app

mkdir web_app

cd web_app

yarn init -y

yarn add express

touch server.js

touch Dockerfile .dockerignore

docker build -t web-app-image .

docker images

# Runnign image in container

docker run --name web-app -d -p 5000:8080 web-app-image

docker container ls

docker ps -a

docker logs web-app

# To Access the container bash

docker exec -it web-app /bin/bash

# Other Commands

docker start <container name/id>

docker stop <container name/id>

docker rm <container name/id>

docker rmi <image name>

docker images

docker container ls

docker network ls

docker volume ls

docker logs <container>

```
