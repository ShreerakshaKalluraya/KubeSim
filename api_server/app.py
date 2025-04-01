from flask import Flask, request, jsonify
from node_manager import NodeManager
from health_monitor import HealthMonitor
from pod_scheduler import PodScheduler

app = Flask(__name__)

node_manager = NodeManager()
health_monitor = HealthMonitor(node_manager)
pod_scheduler = PodScheduler(node_manager)

@app.route('/')
def home():
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
    cpu = data['cpu']
    memory = data['memory']
    pod_id, assigned_node = pod_scheduler.schedule_pod(cpu, memory)
    return jsonify({"message": f"Pod {pod_id} assigned to node {assigned_node}"}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
