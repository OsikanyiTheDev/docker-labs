This lab is about how containers communicate with each other and with the outside world.


Bridge network (default) → containers talk on same host
Host network → container uses host’s network directly
None network → isolated container
Custom bridge network → best practice for multi-container apps


#list networks
docker network ls

#inspect a network
docker network inspect bridge


#create a custom network 
docker network create my-network

#run a container on a network
docker run -d --name web --network my-network nginx

#connect a running container to a network
docker network connect my-network container_name

#disconnect a container
docker network disconnect my-network container_name

#remove a network
docker network rm my-network
