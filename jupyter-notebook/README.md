# Jupyter Notebook Docker Image

This repository contains a Dockerfile for building a Docker image that runs Jupyter Notebook. The image is based on the `Python 3.11 alpine` variant to keep it lightweight and efficient. It includes Jupyter Notebook and all necessary dependencies, ensuring a streamlined setup for data science and development work. The Dockerfile follows best practices for security and maintainability, including running the notebook as a non-root user and minimizing the number of layers in the image.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Dockerfile](#dockerfile)
- [Build the Docker Image](#build-the-docker-image)
- [Run the Docker Container](#run-the-docker-container)


## Prerequisites

Before you can build and run the Docker image for Jupyter Notebook, ensure you have the following prerequisites installed on your system:
1. __Docker__:
	- Install Docker from the [official Docker website](https://www.docker.com/products/docker-desktop).
	- A Docker Hub account if you plan to push your images to Docker Hub.

	- To install Docker on Ubuntu or Debian Linux:
	```
	sudo apt install docker.io
	```
2. __Git__  (Optional): Required if you want to clone this repository.
	- Install Git from the [official Git website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
	
	- To clone the repository:
	```
	git clone https://github.com/abdur-rahman54/Docker.git
	```

## Dockerfile

The `Dockerfile` defines the steps required to build a Docker image for running `Jupyter Notebook`. 

Below is a detailed explanation of each part of the Dockerfile:

```
# Use a specific version tag to ensure reproducibility
FROM python:3.11-alpine
```
This line specifies the base image for the Docker build. The `python:3.11-alpine` image is a lightweight version of Python 3.11, which helps keep the Docker image small and efficient.


```
# Metadata as labels
LABEL maintainer="Abdur Rahman"
LABEL description="A Docker image for running Jupyter Notebook"
```
These lines add metadata to the Docker image, including the maintainer's name and a brief description of the image's purpose.

```
# Install Jupyter Notebook and dependencies
RUN apk update && \
    apk add --no-cache build-base linux-headers python3-dev && \
    pip install --no-cache-dir jupyter && \
    apk del build-base python3-dev && \
	rm -rf /var/cache/apk/*
```

This section installs Jupyter Notebook along with any necessary dependencies:

- `apk update` updates the package lists.
- `apk add --no-cache build-base linux-headers python3-dev` installs essential build tools without unnecessary packages.
- `pip install --no-cache-dir jupyter` installs Jupyter Notebook using pip.
- `apk del build-base python3-dev` removes the build tools to reduce the image size.
- `rm -rf /var/lib/apt/lists/*` clean up unnecessary files to further reduce the image size.



```	
# Create a non-root user and set up permissions
RUN adduser -D jupyteruser
WORKDIR /home/jupyteruser/notebooks
RUN chown -R jupyteruser:jupyteruser /home/jupyteruser/notebooks
```

This section enhances security by creating a non-root user:
	
- `adduser -D jupyteruser` creates a new user named `jupyteruser`.
- `WORKDIR /home/jupyteruser/notebooks` sets the working directory for subsequent instructions to `/home/jupyteruser/notebooks`.
- `chown -R jupyteruser:jupyteruser /home/jupyteruser/notebooks` changes the ownership of the notebooks directory to the new user.

	
```
# Expose the Jupyter Notebook port
EXPOSE 8888
```
This line informs Docker that the container will listen on port 8888 at runtime. This is the default port for Jupyter Notebook.

```
# Switch to the non-root user
USER jupyteruser
```

This instruction switches the user context to `jupyteruser`, ensuring that the Jupyter Notebook runs with non-root privileges, enhancing security.

```
# Set the entrypoint to Jupyter Notebook
ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

Finally, this line sets the default command to run when the container starts:

- `jupyter notebook` starts the Jupyter Notebook server.
- `--ip=0.0.0.0` makes the server accessible from any network interface.
- `--port=8888` sets the server to run on port 8888.
- `--no-browser` prevents the server from trying to open a web browser.
- `--allow-root` allows the notebook to be run as the root user, which is needed because Docker containers often run as root.

## Build the Docker Image

To build the Docker image for Jupyter Notebook, follow these steps:

1. **Navigate to the directory containing the Dockerfile:**

	Open a terminal and change to the directory where your `Dockerfile` is located.
	For this project, use:

	```
	cd Docker/jupyter-notebook/
	```
2. **Build the Docker Image:**

	Use the `docker build` command to create the Docker image. The `-t` flag tags the image with a name (`jupyter` in this case).
	
	```sh
	docker build -t jupyter .
	```
	This command will read the `Dockerfile` in the current directory (denoted by `.`) and build the image with the specified tag.

3. **Run the Docker Container:**
	
	Once the image is built, you can run it using the `docker run` command. This command will start a new container from the `jupyter` image, map port 8888 of the container to port 8888 on your host, and mount the current directory's `notebooks` folder to `/notebooks` inside the container.

	```
	sudo docker run --rm -p 8888:8888 -v $(pwd)/notebooks:/home/jupyteruser/notebooks jupyter
	```

	- `--rm`: Automatically removes the container when it exits. This helps to keep your system clean by removing unnecessary containers.
	- `-p 8888:8888` maps port 8888 on your local machine to port 8888 in the container, making the Jupyter Notebook accessible at `http://localhost:8888`.
	- `-v $(pwd)/notebooks:/home/jupyteruser/notebooks` mounts the `notebooks` directory from your current path to the `/home/jupyteruser/notebooks` directory in the container, ensuring your notebooks are stored on your host machine. If you want to work with your existing notebooks, navigate to their directory first, then run this command, replacing `$(pwd)/notebooks` with the appropriate directory path. All other parts of the command remain the same.
	
After running the container, you will see a URL in the terminal output that you can open in your web browser to access the Jupyter Notebook interface.

![jupyter trminal](https://github.com/abdur-rahman54/Docker/blob/main/images/Jupytr%20Terminal.jpg)

To terminate the terminal session, simply press `Ctrl + C`.



## Files

- [Dockerfile](Dockerfile): This Dockerfile leverages the `alpine` base image to create a small, efficient, and secure Jupyter Notebook image. It follows best practices by installing dependencies temporarily and running the application as a non-root user.
- [Dockerfile-Jupyter-slim](Dockerfile-Jupyter-slim):  Designed for ease of use, this Dockerfile uses the `slim` base image. While it is more straightforward and beginner-friendly, it results in a larger image and operates with root permissions, which might be less secure.

### How to Switch to the Slim Version

To switch to the slim version after cloning the repository:
1. Rename the original `Dockerfile` to `Dockerfile-alpine`:

`
mv Dockerfile Dockerfile-alpine
`

2. Rename `Dockerfile-Jupyter-slim` to `Dockerfile`:

`
mv Dockerfile-Jupyter-slim Dockerfile
`

You can then build the Docker image using the slim version instructions.