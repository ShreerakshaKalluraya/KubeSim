import docker

client = docker.from_env()

def launch_node_container(node_id, cpu):
    container = client.containers.run(
        image="node_simulator",  # You need to build this Docker image
        environment={"NODE_ID": node_id, "CPU": str(cpu)},
        name=node_id,
        detach=True,
        network_mode="host"  # Allow container to reach the Flask API
    )
    return container
