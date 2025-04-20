# Base image
FROM python:3.9-slim

# Working directory
WORKDIR /app

# Copy all node simulator files
COPY . /app
COPY register_node_2.json .
# Install dependencies
RUN pip install --no-cache-dir flask requests

# Install curl (optional if you need)
RUN apt-get update && apt-get install -y curl

# Command to run either app.py or node scripts
CMD ["sh", "-c", "if [ \"$NODE_ID\" = \"\" ]; then python app.py; else python register_node.py && python node_heartbeat.py; fi"]
