# 
import time
from pod_scheduler import PodScheduler

class HealthMonitor:
    def __init__(self, node_manager,pod_scheduler, timeout=15):
        self.node_manager = node_manager
        self.pod_scheduler = pod_scheduler
        self.timeout = timeout

    def receive_heartbeat(self, node_id, status, pods):
        if node_id in self.node_manager.nodes:
            self.node_manager.nodes[node_id]["status"] = status
            self.node_manager.nodes[node_id]["last_heartbeat"] = time.time()
            # ❌ No pods overwrite here anymore

    def check_failures(self):
        current_time = time.time()
        for node_id, data in self.node_manager.nodes.items():
            if current_time - data.get("last_heartbeat", 0) > self.timeout:
                if data["status"] != "unhealthy":
                    print(f"[FAILURE] Node {node_id} missed heartbeat. Marking as unhealthy.")
                    data["status"] = "unhealthy"
                    self.reschedule_pods(node_id)

    def reschedule_pods(self, failed_node_id):
        failed_pods = self.node_manager.nodes[failed_node_id]["pods"]
        self.node_manager.nodes[failed_node_id]["pods"] = []

        for pod in failed_pods:
            print(f"[RESCHEDULING] Attempting to reschedule Pod {pod['pod_id']}")
            pod_id, new_node = self.pod_scheduler.schedule_pod(pod["cpu"], pod["memory"])
            print(f"[Rescheduler] Pod {pod_id} moved from failed node {failed_node_id} to {new_node}")
            if new_node:
                print(f"[RESCHEDULED] Pod {pod['pod_id']} moved to {new_node}")
                self.pod_scheduler.pods[pod['pod_id']]['node_id'] = new_node
            else:
                print(f"[FAILED] No suitable node found for Pod {pod['pod_id']}")

