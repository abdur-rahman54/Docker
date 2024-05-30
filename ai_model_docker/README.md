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

## Installation

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/abdur-rahman54/Docker.git
    cd Docker/ai_model_docker
    ```

2. Build the Docker image:
    ```bash
    docker build -t iris-classification:latest .
    ```

3. Run the Docker container:
    ```bash
    docker run --rm --it iris-classification:latest
    ```

## Usage

Currently its a offline Docker implementation. You can only use it on your local machine.