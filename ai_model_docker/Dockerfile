FROM python:3.11-alpine

# Install build essentials and necessary libraries for compiling
RUN apk update && \
    apk add --no-cache build-base && \
    apk add --no-cache gcc

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]

