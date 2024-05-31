# Jupyter Notebook Docker Image

This repository contains a Dockerfile for building a Docker image that runs Jupyter Notebook. The image is based on Alpine Linux to keep it minimal and includes the necessary dependencies to run Jupyter Notebook efficiently.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Dockerfile](#dockerfile)
- [Build the Docker Image](#build-the-docker-image)
- [Run the Docker Container](#run-the-docker-container)
- [Automate Versioning with GitHub Actions](#automate-versioning-with-github-actions)
- [Maintainer](#maintainer)

## Prerequisites

- Docker installed on your machine. You can download(Windows version) it from [here](https://www.docker.com/products/docker-desktop).
- A Docker Hub account if you plan to push your images to Docker Hub.

To install Docker on Ubuntu or Debian Linux:
```
sudo apt install docker.io
```

## Dockerfile
Dockerfile explanation

## Build the Docker Image

To build the Docker image, navigate to the directory containing the Dockerfile and run the following command:

```sh
docker build -t jupyter .
```

Run the Docker images
```
sudo docker run -p 8888:8888 -v $(pwd)/notebooks:/notebooks jupyter
```