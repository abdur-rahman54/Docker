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
3. Train a classifier (e.g., Logistic Regression, Decision Tree) on the training set.
4. Evaluate the classifier on the testing set.

## Docker Deployment

The trained model is packaged into a Docker container to ensure consistency and ease of deployment across different environments. The Docker container includes all necessary dependencies and the model itself.

## Installation

### Prerequisites

- Docker installed on your machine

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/iris-classification.git
    cd iris-classification
    ```

2. Build the Docker image:
    ```bash
    docker build -t iris-classification:latest .
    ```

3. Run the Docker container:
    ```bash
    docker run -p 5000:5000 iris-classification:latest
    ```

## Usage

Once the Docker container is running, the model can be accessed via a web API. The following endpoints are available:

- `GET /`: Returns a welcome message.
- `POST /predict`: Takes a JSON payload with the features of an Iris flower and returns the predicted species.

Example JSON payload for prediction:
```json
{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

