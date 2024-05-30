# Iris Classification AI Model

This project demonstrates a simple AI model for classifying Iris flowers using the famous Iris dataset from sklearn. The model is deployed using Docker for easy distribution and usage.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Model](#model)
- [Docker Deployment](#docker-deployment)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to create a machine learning model that classifies Iris flowers into one of three species: Setosa, Versicolour, and Virginica. The model is trained using the Iris dataset from sklearn and is then packaged into a Docker container for deployment.

## Dataset

The Iris dataset contains 150 samples of Iris flowers, each described by four features:
- Sepal length
- Sepal width
- Petal length
- Petal width

Each sample belongs to one of three species of Iris flowers:
- Iris Setosa
- Iris Versicolour
- Iris Virginica

## Model

A simple machine learning model is created using the following steps:
1. Load the Iris dataset from sklearn.
2. Split the dataset into training and testing sets.
3. Train a classifier (e.g., Random forest) on the training set.
4. Evaluate the classifier on the testing set.

## Docker Deployment

The trained model is packaged into a Docker container to ensure consistency and ease of deployment across different environments. The Docker container includes all necessary dependencies and the model itself.



### Prerequisites

- Docker installed on your machine

If you dont have Docker on your machine then follow this step:

For Ubuntu or debain linux
```
sudo apt install docker.io
```

Windows user can download Docker from [here](https://www.docker.com/products/docker-desktop/)

## Installation

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/abdur-rahman54/Docker.git
    cd Docker/iris-model
    ```

2. Build the Docker image: To build the Docker image, use the following command format:
	```
	docker build -t <image name> .
	```
For example, to build an image named iris-classification:
    ```bash
    docker build -t iris-classification .
    ```
Note: You can use any name you prefer for the image instead of iris-classification. Don't forget to include the dot (.) at the end of the command to specify the current directory as the build context.

3. Run the Docker container: To run a Docker container from the Docker image, use this command format:
```
docker run <image name>
```
Since we named the image iris-classification in the previous step, we can use that name to run the container:
    ```bash
    docker run --rm -it iris-classification
    ```
In this command:
- --rm: Automatically removes the container when it exits. This helps to keep your system clean by removing unnecessary containers.
- -it: Combines two flags, -i (interactive) and -t (pseudo-TTY). This allows you to interact with the container via the terminal.

You should replace 'iris-classification' with your own image name if you used a different name during the build process.

## Contributing

Contributions are welcome! If you have alternative solutions, improvements, or additional resources, please feel free to submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a pull request



## Usage

Currently its a offline Docker implementation. You can only use it on your local machine.