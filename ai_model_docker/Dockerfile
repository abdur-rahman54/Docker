# Use the official Python image as the base image
FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files into the container
COPY . .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Python script when the container starts
CMD ["python", "app.py"]

