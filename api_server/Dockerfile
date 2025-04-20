# # Use a Python base image
# FROM python:3.8-bullseye

# # Set the working directory in the container
# WORKDIR /app

# # Copy the entire api-server directory into the container
# COPY ../api_server/ .

# # Install required dependencies
# RUN pip install --no-cache-dir flask requests

# # Expose port for the Flask app
# EXPOSE 5000

# # Command to run your Flask app (entry point)
# CMD ["python", "app.py"]

# FROM python:3.9
# WORKDIR /app
# COPY node_heartbeat.py .
# RUN pip install requests
# CMD ["python", "node_heartbeat.py"]

# FROM python:3.9-slim

# WORKDIR /app

# COPY node_heartbeat.py .
# COPY register_node.py .
# COPY register_node_1.json .
# COPY register_node_2.json .
# COPY register_node_3.json .

# RUN pip install flask requests
# RUN pip install --no-cache-dir docker
# RUN apt-get update && apt-get install -y curl

# CMD ["sh", "-c", "if [ \"$NODE_ID\" = \"\" ]; then python app.py; else python register_node.py && python node_heartbeat.py; fi"]

# Base image
FROM python:3.9-slim

# Working directory
WORKDIR /app
# COPY node_heartbeat.py .
# COPY register_node.py .
# COPY register_node_1.json .
# COPY register_node_2.json .
# COPY register_node_3.json .

# Copy all the API server files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask requests

RUN pip install --no-cache-dir docker
RUN apt-get update && apt-get install -y curl

# Expose port
EXPOSE 5000

# Run app.py
CMD ["python", "app.py"]
