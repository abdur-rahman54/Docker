# Docker

This repository serves as a training course for beginners, providing a straightforward and comprehensive introduction to Docker. It aims to demonstrate the basic concepts and practical applications of Docker in an easy-to-understand manner, making it accessible for those new to containerization technology. Through various examples and hands-on projects, learners will gain a solid foundation in using Docker for application deployment and management.


For cloning this repository.:
```
git clone https://github.com/abdur-rahman54/Docker.git
```

## Table of Contents

- [Prerequisites](#prerequisites)
- [Docker Explanation](#docker-explanation)
- [Project Overview](#project-overview)
- [Maintainer](#maintainer)
- [Contributing](#contributing)
- [License](#license)


## Prerequisites

Before you can build and run the Docker image, ensure you have the following prerequisites installed on your system:

1. __Docker__:
	- Install Docker by following the instructions on the [official Docker website](https://www.docker.com/products/docker-desktop).
	- A Docker Hub account if you plan to push your images to Docker Hub.

	To install Docker on Ubuntu or Debian Linux:
	```
	sudo apt install docker.io
	```
2. __Git__ (optional): Required if you want to clone this repository.
	- Install Git from the [official Git website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

	To install __Git__ on Ubuntu or Debian Linux:
	```
	sudo apt install git
	```

3. __Python__ (Optional): Required only if you want to run the Python code locally on your machine.
	- Install Python from the [official Python website](https://www.python.org/downloads/).
	
## Docker Explanation

Docker is a powerful platform designed to simplify the creation, deployment, and running of applications by using containerization technology. It allows developers to package applications and their dependencies into lightweight, portable containers that can run consistently across any environment. By using Docker, you can ensure that your applications are easily deployable, scalable, and maintainable, with a consistent setup that reduces compatibility issues and streamlines the development workflow.

### Build the Docker image: 

To build the Docker image, use the following command format:
	
	```
	docker build -t <image name> .
	```

Note: Ensure you include the dot (`.`) at the end of the command to specify the current directory as the build context.

### Run the Docker container: 

To run a Docker container from the Docker image, use this command format:

	```
	docker run <image name>
	```
	
## Project Overview

This repository contains two projects that demonstrate the use of Docker for different applications:

1. [iris-model](./iris-model): Developing and deploying an AI model for iris flower classification using Docker.

2. [jupyter-notebook](./jupyter-notebook): Building and running a Jupyter Notebook using Docker.


## Maintainer

This Docker image for Jupyter Notebook is maintained by __Abdur Rahman__.

- GitHub: [github.com/abdur-rahman54](github.com/abdur-rahman54)
- LinkedIn: [https://www.linkedin.com/in/abdur-rahman55/](https://www.linkedin.com/in/abdur-rahman55/)
- Email: abdur.rahman59354@gmail.com

## Contributing

Contributions to this project are welcome! Whether you want to suggest improvements, report issues, or contribute code, feel free to get involved.


## License

This project is licensed under the [MIT License](./LICENSE), allowing for open collaboration and distribution of the code.