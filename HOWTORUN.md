In terminal:
docker-compose build

docker ps: a container should be runnning
If not then start the container:docker run -d --name kubesim-api-server kubesim-api-server:latest

check logs(shows even if containers are not running):docker logs kubesim-api-server

docker ps again: check if the container is running

docker exec -it <container_id> curl http://localhost:5000/: this should route you to your home page

To register a node:
Create a json file with the resource requirements.
Run your command (with necessary changes):
docker exec -it d3c4bf1d677b curl -X POST http://localhost:5000/register_node -H "Content-Type: application/json" --data-binary "@/tmp/register.json"

check if the node is added :
docker exec -it d3c4bf1d677b curl http://localhost:5000/list_nodes
-------------------------------------------------------------------------------


docker build -t node_simulator -f Dockerfile .

python -m api_server.app

docker exec -it acaca9572126d90da870e4f39a2106ad490d9d201ac669d829f60faf34043c88 curl -X POST http://localhost:5000/register_node_1 -H "Content-Type: application/json" --data-binary "KubeSim\register_node_1.json"

docker exec -it d3c4bf1d677b curl -X POST http://localhost:5000/launch_pod -H "Content-Type: application/json" --data-binary "@/tmp/launch_pod.json"
curl http://localhost:5000/list_nodes 

----------------------------------
python -m api_server.app
docker-compose up --build


----------------------------------------------------
LATEST:18th april
 docker network create kubesim-net
 docker build -t kubesim-api-server .
  docker build -t node-simulator .
 docker run -d --name kubesim-api-server --network kubesim-net -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock kubesim-api-server
 in the node-simualtor directory:
 docker run -d --name node-1 --network kubesim-net -e NODE_ID=node-1 -e API_URL=http://kubesim-api-server:5000/heartbeat -e NODE_FILE=/app/register_node_2.json node-simulator

docker run --name node-simulator-container-node2 --network="kubesim-net" `
  -e NODE_ID=node-2 `
  -e NODE_FILE=/app/register_node_2.json `
  -e API_SERVER_URL=http://172.21.0.2:5000 `
  -v C:\Users\prady\Downloads\kubernetes\kubesim\node-simulator\register_node_2.json:/app/register_node_2.json `
  node-simulator
(it worked here)

docker run --name node-simulator-container-node1 --network="kubesim-net" `
  -e NODE_ID=node-1 `
  -e NODE_FILE=/app/register_node_1.json `
  -e API_SERVER_URL=http://172.21.0.2:5000 `
  -v C:\Users\prady\Downloads\kubernetes\kubesim\node-simulator\register_node_1.json:/app/register_node_1.json `
  node-simulator

docker run --name node-simulator-container-node3 --network="kubesim-net" `
  -e NODE_ID=node-3 `
  -e NODE_FILE=/app/register_node_3.json `
  -e API_SERVER_URL=http://172.21.0.2:5000 `
  -v C:\Users\prady\Downloads\kubernetes\kubesim\node-simulator\register_node_3.json:/app/register_node_3.json `
  node-simulator




(Invoke-WebRequest -Uri "http://localhost:5000/list_nodes" -UseBasicParsing).Content
--to check list of nodes

Invoke-WebRequest -Uri http://localhost:5000/launch_pod `
                  -Method POST `
                  -Body '{"cpu":1,"memory":512}' `
                  -ContentType "application/json"
--launch a pod
--gets assigned to  node-1


Invoke-WebRequest -Uri http://localhost:5000/launch_pod `
                  -Method POST `
                  -Body '{"cpu":3,"memory":512}' `
                  -ContentType "application/json" 

gets assigned to node-1

Invoke-WebRequest -Uri http://localhost:5000/launch_pod `
                  -Method POST `
                  -Body '{"cpu":3,"memory":512}' `
                  -ContentType "application/json" 
                  
--gets assigned to  node-3





 docker exec -it node-1 curl http://kubesim-api-server:5000                                                                       Welcome to the Kubernetes Simulation API Server!                

  curl http://localhost:5000

  docker ps: two container must show here

  if netwrk issue chck if bth containers are in same netwrk:
  docker network inspect kubesim-net

  try pining server:
   docker exec -it node-1 bash

heartbeat received:
$jsonBody = Get-Content -Raw -Path "C:\Users\prady\Downloads\kubernetes\KubeSim\node-simulator\heartbeat.json" 

 Invoke-WebRequest -Uri http://localhost:5000/heartbeat -Method POST -Headers @{ "Content-Type" = "application/json" } -Body $jsonBody

Invoke-WebRequest -Uri http://localhost:5000/list_nodes -Method GET