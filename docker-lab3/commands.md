# Lab 3 – Docker Volumes

#starting a new Ubuntu container
docker run -it ubuntu bash

#creating a file test.txt inside the container
echo "Docker is awesome!" > test.txt

ls

cat test.txt

#exit the container
exit

#deleting the container
docker ps -a
docker rm <container_id_here>




#without an attached volume data inside container is lost


## Create volume
docker volume create mydata

## Run container with volume
docker run -d -v mydata:/app/data ubuntu

## Inspect volume
docker volume inspect mydata
