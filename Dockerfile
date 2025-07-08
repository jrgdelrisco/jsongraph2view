# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install system dependencies for pygraphviz and graphviz
RUN apt-get update && \
    apt-get install -y graphviz graphviz-dev gcc pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the default command (adjust as needed)
CMD ["python", "-m", "jsongraph2view"]
