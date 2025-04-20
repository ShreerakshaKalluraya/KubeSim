class PodScheduler:
    def __init__(self, node_manager):
        self.node_manager = node_manager
        self.pod_counter = 1
        self.pods = {}  # Track all pods and where they are scheduled

    def schedule_pod(self, cpu, memory):
        for node_id, node in self.node_manager.nodes.items():
            if node['status'] == 'healthy' and node['cpu'] >= cpu and node['memory'] >= memory:
                pod_id = f"pod-{self.pod_counter}"
                self.pod_counter += 1

                # Deduct resources
                node['cpu'] -= cpu
                node['memory'] -= memory

                # Add pod to node
                pod_info = {"pod_id": pod_id, "cpu": cpu, "memory": memory, "status": "running"}
                node['pods'].append(pod_info)

                # Track pod globally
                self.pods[pod_id] = {"node_id": node_id, **pod_info}

                return pod_id, node_id

        return None, None  # No suitable node
