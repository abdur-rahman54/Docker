# Stage 1: Build stage with all dependencies
FROM python:3.12-alpine as build-stage

LABEL maintainer="Abdur Rahman"

# Install build dependencies
RUN apk add --no-cache \
        gcc \
        musl-dev \
        linux-headers \
        python3-dev \
        libffi-dev \
        openssl-dev

# Install Jupyter Notebook and dependencies
RUN pip install --no-cache-dir jupyter

# Stage 2: Final stage with minimal runtime environment
FROM python:3.12-alpine

LABEL maintainer="Abdur Rahman"

# Install runtime dependencies
RUN apk add --no-cache \
        libffi \
        openssl

# Copy only the installed packages from the build stage
COPY --from=build-stage /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=build-stage /usr/local/bin /usr/local/bin

# Create a directory for the notebook
WORKDIR /notebooks

# Expose the Jupyter Notebook port
EXPOSE 8888

# Run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

