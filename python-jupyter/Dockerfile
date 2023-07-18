FROM python:3
LABEL maintainer="Abdur Rahman"

# Install Jupyter Notebook and dependencies
RUN pip install jupyter

# Create a directory for the notebook
WORKDIR /notebooks

# Expose the Jupyter Notebook port
EXPOSE 8888

# Run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

