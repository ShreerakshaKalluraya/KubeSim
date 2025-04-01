# Use a lightweight Python image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files
COPY ./node-simulation.py .

# Install any dependencies
RUN pip install --no-cache-dir requests

# Run the node simulation script (this will simulate heartbeat)
CMD ["python", "node-simulation.py"]
