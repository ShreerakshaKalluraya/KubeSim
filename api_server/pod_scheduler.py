class PodScheduler:
    def __init__(self, node_manager):
        self.node_manager = node_manager
        self.pod_counter = 1

    def schedule_pod(self, cpu, memory):
        for node_id, node in self.node_manager.nodes.items():
            if node['cpu'] >= cpu and node['memory'] >= memory:
                node['pods'].append(self.pod_counter)
                self.pod_counter += 1
                return self.pod_counter - 1, node_id
        return None, None  # No suitable node found
