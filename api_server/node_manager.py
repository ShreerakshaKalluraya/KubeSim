class NodeManager:
    def __init__(self):
        self.nodes = {}  # Store nodes by node_id

    def add_node(self, cpu, memory):
        node_id = f"node-{len(self.nodes) + 1}"
        self.nodes[node_id] = {"cpu": cpu, "memory": memory, "pods": [], "status": "healthy"}
        return node_id

    def get_all_nodes(self):
        return self.nodes

    def update_node_status(self, node_id, status):
        if node_id in self.nodes:
            self.nodes[node_id]["status"] = status
