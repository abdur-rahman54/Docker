# Use a specific version tag to ensure reproducibility
FROM python:3.11-slim

# Metadata as labels
LABEL maintainer="Abdur Rahman"
LABEL description="A Docker image for running Jupyter Notebook"

# Install Jupyter Notebook and dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    pip install --no-cache-dir jupyter && \
    apt-get purge -y build-essential && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user and set up permissions
RUN useradd -m jupyteruser
WORKDIR /home/jupyteruser/notebooks
RUN chown -R jupyteruser:jupyteruser /home/jupyteruser/notebooks

# Expose the Jupyter Notebook port
EXPOSE 8888

# Switch to the non-root user
USER jupyteruser

# Set the entrypoint to Jupyter Notebook
ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
