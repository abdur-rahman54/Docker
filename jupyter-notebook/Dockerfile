# Use a specific version tag to ensure reproducibility
FROM python:3.11-alpine

# Metadata as labels
LABEL maintainer="Abdur Rahman"
LABEL description="A Docker image for running Jupyter Notebook"

# Install Jupyter Notebook and dependencies
RUN apk update && \
    apk add --no-cache build-base linux-headers python3-dev && \
    pip install --no-cache-dir jupyter && \
    apk del build-base python3-dev && \
    rm -rf /var/cache/apk/*

# Create a non-root user and set up permissions
RUN adduser -D jupyteruser
WORKDIR /home/jupyteruser/notebooks
RUN chown -R jupyteruser:jupyteruser /home/jupyteruser/notebooks

# Expose the Jupyter Notebook port
EXPOSE 8888

# Switch to the non-root user
USER jupyteruser

# Set the entrypoint to Jupyter Notebook
ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
