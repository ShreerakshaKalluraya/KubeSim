# import os, json, requests
# import time
# SERVER_URL = os.environ.get("SERVER_URL", "http://api-server:5000") # Change made here: localhost -> api-server
# NODE_ID = os.environ["NODE_ID"]
# NODE_FILE = os.environ["NODE_FILE"]

# # with open(NODE_FILE) as f:
# #     data = json.load(f)

# # data["node_id"] = NODE_ID

# # resp = requests.post(f"{SERVER_URL}/register_node", json=data)

# # if resp.status_code == 200:
# #     print(f"[{NODE_ID}] Successfully registered.")
# # else:
# #     print(f"[{NODE_ID}] Failed to register: {resp.text}")
# for _ in range(5):  # Retry up to 5 times
#     try:
#         response = requests.post(f"{SERVER_URL}/register_node", json={"node_id": "node-1"})
#         if response.status_code == 200:
#             print("Node registered successfully!")
#             break
#     except requests.exceptions.ConnectionError:
#         print("Connection to API server failed. Retrying in 5 seconds...")
#         time.sleep(5)
# else:
#     print("Failed to connect to API server after multiple attempts.")

# import os, json, requests
# import time

# # Get the server URL from the environment, defaulting to 'api-server:5000'
# SERVER_URL = os.environ.get("SERVER_URL", "http://172.21.0.2:5000")
# NODE_ID = os.environ["NODE_ID"]  # Node ID should be passed as an environment variable
# NODE_FILE = os.environ["NODE_FILE"]  # Path to the node file (JSON) should also be passed

# # Load the node data from the provided JSON file
# with open(NODE_FILE) as f:
#     data = json.load(f)

# # Add/modify the node_id field in the data from environment variable
# data["node_id"] = NODE_ID

# # Retry the connection to the server
# for _ in range(5):  # Retry up to 5 times
#     try:
#         response = requests.post(f"{SERVER_URL}/register_node", json=data)
#         if response.status_code == 200:
#             print(f"[{NODE_ID}] Successfully registered.")
#             break
#     except requests.exceptions.ConnectionError:
#         print(f"[{NODE_ID}] Connection to API server failed. Retrying in 5 seconds...")
#         time.sleep(5)
# else:
#     print(f"[{NODE_ID}] Failed to connect to API server after multiple attempts.")


import os
import json
import requests
import time

API_SERVER_URL = os.environ.get("API_SERVER_URL", "http://localhost:5000")
REGISTER_NODE_URL = f"{API_SERVER_URL}/register_node"

NODE_ID = os.environ["NODE_ID"]
NODE_FILE = os.environ["NODE_FILE"]

# Load node info from file
with open(NODE_FILE) as f:
    data = json.load(f)

data["node_id"] = NODE_ID

# Try registering node
for _ in range(5):  # 5 retries
    try:
        response = requests.post(REGISTER_NODE_URL, json=data)
        if response.status_code == 200:
            print(f"[{NODE_ID}] Successfully registered.")
            break
    except requests.exceptions.ConnectionError:
        print(f"[{NODE_ID}] Connection to API server failed. Retrying in 5 seconds...")
        time.sleep(5)
else:
    print(f"[{NODE_ID}] Failed to connect to API server after multiple attempts.")
