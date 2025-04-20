# import os
# import requests
# import time

# API_URL = "http://localhost:5000/heartbeat"
# NODE_ID = os.getenv("NODE_ID")
# CPU = int(os.getenv("CPU"))

# pods = []

# while True:
#     try:
#         requests.post(API_URL, json={
#             "node_id": NODE_ID,
#             "status": "healthy",
#             "pods": [{"pod_id": pod_id, "status": "running"} for pod_id in pods]
#         })
#         print(f"[{NODE_ID}] Sent heartbeat.")
#     except Exception as e:
#         print(f"[{NODE_ID}] Failed to send heartbeat: {e}")
#     time.sleep(5)
# inside node_sim/ directory

# import os, requests, time

# NODE_ID = os.environ['NODE_ID']
# API_URL = os.environ.get("API_URL", "http://172.21.0.2:5000/heartbeat") # Change made here: docker.host.internal -> api-server

# pods = []

# while True:
#     try:
#         requests.post(API_URL, json={
#             "node_id": NODE_ID,
#             "status": "healthy",
#             "pods": pods
#         })
#         print(f"[{NODE_ID}] Sent heartbeat")
#     except Exception as e:
#         print(f"[{NODE_ID}] Failed to send heartbeat: {e}")
#     time.sleep(5)

import os
import requests
import time

NODE_ID = os.environ['NODE_ID']
API_SERVER_URL = os.environ.get("API_SERVER_URL", "http://localhost:5000")  # Flexible

HEARTBEAT_URL = f"{API_SERVER_URL}/heartbeat"

pods = []

while True:
    try:
        requests.post(HEARTBEAT_URL, json={
            "node_id": NODE_ID,
            "status": "healthy",
            "pods": pods
        })
        print(f"[{NODE_ID}] Sent heartbeat")
    except Exception as e:
        print(f"[{NODE_ID}] Failed to send heartbeat: {e}")
    time.sleep(5)
