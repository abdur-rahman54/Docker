# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files into the container
COPY docker-model.py requirements.txt model.pkl ./

# Install any necessary build dependencies temporarily
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Python script when the container starts
CMD ["python", "docker-model.py"]

