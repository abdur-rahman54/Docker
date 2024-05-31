# Docker

it's a kind of training course for beginners. I am trying to demonstrate some basic of Docker so that beginners can understand easily.

## Prerequisites

Before you can build and run the Docker image for Jupyter Notebook, ensure you have the following prerequisites installed on your system:
1. __Docker__:
	- Install Docker from the [official Docker website](https://www.docker.com/products/docker-desktop).
	- A Docker Hub account if you plan to push your images to Docker Hub.

	To install Docker on Ubuntu or Debian Linux:
	```
	sudo apt install docker.io
	```
2. __Git__ (optional, for cloning the repository):
	- Install Git from the [official Git website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
	
	To clone the repository:
	```
	git clone https://github.com/abdur-rahman54/Docker.git
	```

## Build the Docker image: 
	To build the Docker image, use the following command format:
	
	```
	docker build -t <image name> .
	```

	Note: You can use any name you prefer for the image instead of `iris-classification`. Don't forget to include the dot (`.`) at the end of the command to specify the current directory as the build context.

## Run the Docker container: 

	To run a Docker container from the Docker image, use this command format:

	```
	docker run <image name>
	```