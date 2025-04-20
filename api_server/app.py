from flask import Flask, request, jsonify
# import os

# os.getcwd()
from node_manager import NodeManager
from health_monitor import HealthMonitor
from pod_scheduler import PodScheduler
import threading
import time

app = Flask(__name__)

print("creating node_manager")
node_manager = NodeManager()
print("creating pod_scheduler")
pod_scheduler = PodScheduler(node_manager)
print("creating health_monitor")
health_monitor = HealthMonitor(node_manager,pod_scheduler)



@app.route('/')
def home():
    print("in home")
    return 'Welcome to the Kubernetes Simulation API Server!'

@app.route('/register_node', methods=['POST'])
def register_node():
    data = request.json
    cpu = data['cpu']
    memory = data['memory']
    node_id = node_manager.add_node(cpu, memory)
    return jsonify({"message": f"Node {node_id} registered successfully"}), 200

@app.route('/heartbeat', methods=['POST'])
def heartbeat():
    data = request.json
    node_id = data['node_id']
    status = data['status']
    pods = data['pods']
    health_monitor.receive_heartbeat(node_id, status, pods)
    return jsonify({"message": "Heartbeat received"}), 200

@app.route('/list_nodes', methods=['GET'])
def list_nodes():
    nodes = node_manager.get_all_nodes()
    return jsonify(nodes), 200

@app.route('/launch_pod', methods=['POST'])
def launch_pod():
    data = request.json
    cpu = data.get('cpu')
    memory = data.get('memory')

    pod_id, assigned_node = pod_scheduler.schedule_pod(cpu, memory)

    if pod_id:
        return jsonify({
            "message": f"Pod {pod_id} assigned to node {assigned_node}",
            "pod_id": pod_id,
            "node_id": assigned_node
        }), 200
    else:
        return jsonify({
            "error": "No suitable node found. Not enough resources or no healthy nodes."
        }), 400
    
@app.route('/health', methods=['GET'])
def health_check():
    return "API server is healthy", 200



if __name__ == '__main__':
    
    print("Hello! I am in app.py, line 70")
    def monitor_nodes():
        while True:
            health_monitor.check_failures()
            time.sleep(10)  # every 10 seconds

    threading.Thread(target=monitor_nodes, daemon=True).start()

    app.run(debug=True, host="0.0.0.0", port=5000)
#debug=True reloading of the app whenever you make changes and provide detailed error logs
