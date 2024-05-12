# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files into the container
COPY ai_model.pkl .
COPY app.py .
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Python script when the container starts
CMD ["python", "app.py"]

