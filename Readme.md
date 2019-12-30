# Docker Basics

```bash

#  Checks image locally if not available then pulls from docker hub
docker run <image>

docker run hello-world

docker ps -a

docker rm <container id>

docker images

docker rmi <image name>

# Creating a image and Running it in a container

mkdir chaal_app

cd chaal_app

touch app.py

touch Dockerfile

docker images

docker build -t chaal-app-image .

docker images

docker run --name chaal-app -d -p 5000:5000 chaal-app-image

docker ps -a

docker logs chaal-app

docker stop <container name/id>

docker start <container name/id>

docker rm <container name/id>

docker rmi <image name>

```
