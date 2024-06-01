# Docker

it's a kind of training course for beginners. I am trying to demonstrate some basic of Docker so that beginners can understand easily.

To clone the repository:
```
git clone https://github.com/abdur-rahman54/Docker.git
```


This repository contains two projects that demonstrate the use of Docker for different applications:

1. Developing and deploying an AI model for iris flower classification using Docker.
2. Building and running a Jupyter Notebook using Docker.

## Table of Contents

- [Prerequisites](prerequisites)
- [Docker Explanation](#docker-explanation)
- [Project Overview](#project-overview)
- [Docker Deployment](#docker-deployment)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


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
	

### Build the Docker image: 

To build the Docker image, use the following command format:
	
	```
	docker build -t <image name> .
	```

Note: Don't forget to include the dot (`.`) at the end of the command to specify the current directory as the build context.

### Run the Docker container: 

To run a Docker container from the Docker image, use this command format:

	```
	docker run <image name>
	```
	
## Project Overview

This repository contains two projects that demonstrate the use of Docker for different applications:

1. [iris-model](./iris-model): Developing and deploying an AI model for iris flower classification using Docker.
2. [jupyter-notebook](./jupyter-notebook): Building and running a Jupyter Notebook using Docker.