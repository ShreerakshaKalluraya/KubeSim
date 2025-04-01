class HealthMonitor:
    def __init__(self, node_manager):
        self.node_manager = node_manager

    def receive_heartbeat(self, node_id, status, pods):
        if node_id in self.node_manager.nodes:
            self.node_manager.update_node_status(node_id, status)
            # Track pod health (simplified for now)
            for pod in pods:
                print(f"Pod {pod['pod_id']} health: {pod['status']}")
