# Docker Basics

```bash

#  Checks image locally if not available then pulls from docker hub
sudo docker run <image>

sudo docker run hello-world

sudo docker ps -a

sudo docker rm <container id>

sudo docker images

sudo docker rmi <image name>

# Creating a image and Running it in a container

mkdir chaal_app

cd chaal_app

touch app.py

touch Dockerfile

sudo docker images

sudo docker build -t chaal-app:0.1 .

sudo docker images

sudo docker run -d -p 5000:5000 chaal-app:0.1

sudo docker stop <container name/id>

sudo docker rm <container name/id>

sudo docker rmi <image name>

```