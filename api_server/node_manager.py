# from .docker_controller import launch_node_container
# import time

# class NodeManager:
#     def __init__(self):
#         self.nodes = {}  # Store nodes by node_id

#     # def add_node(self, cpu, memory):
#     #     node_id = f"node-{len(self.nodes) + 1}"
#     #     self.nodes[node_id] = {"cpu": cpu, "memory": memory, "pods": [], "status": "healthy"}
#     #     return node_id
#     def add_node(self, cpu, memory):
#         node_id = f"node-{len(self.nodes) + 1}"
#         self.nodes[node_id] = {"cpu": cpu, "memory": memory, "pods": [], "status": "healthy", "last_heartbeat": time.time()}
#         launch_node_container(node_id, cpu)
#         return node_id
    
#     def get_all_nodes(self):
#         return self.nodes

#     def update_node_status(self, node_id, status):
#         if node_id in self.nodes:
#             self.nodes[node_id]["status"] = status


import docker
import docker
import time

class NodeManager:
    def __init__(self):
        self.nodes = {}
        self.client = docker.from_env()

    def add_node(self, cpu, memory):
        node_id = f"node-{len(self.nodes) + 1}"
        self.nodes[node_id] = {
            "cpu": cpu,
            "memory": memory,
            "pods": [],
            "status": "healthy",
            "last_heartbeat": time.time()
        }
    

    def get_all_nodes(self):
        return self.nodes  # Return all registered node
        # Launch container using pre-built node image
        self.client.containers.run(
            "node-simulator",
            detach=True,
            environment={
                "NODE_ID": node_id,
                "API_URL": "http://api-server:5000/heartbeat"
            },
            name=node_id,
            network="kubenet"
        )

        return node_id
