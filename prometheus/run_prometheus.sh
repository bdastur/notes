#!/bin/bash

IMAGE_NAME="bdastur/prometheus:2.21.0"
CONTAINER_NAME="prometheus"
VOLUME_NAME="prometheus_data"
volume=$(docker volume list | grep ${VOLUME_NAME})
echo "Volume present: $volume"                                                  

# If volume does not exists yet. Create it
if [[ -z $volume ]]; then
    echo "Volume does not exist. Creating"
    docker volume create ${VOLUME_NAME}
fi

# Check if prometheus container is already present.
container_exited=$(docker ps -a | grep ${CONTAINER_NAME} | grep Exited)
echo "Container: $container_exited"
if [[ ! -z $container_exited ]]; then
    echo "Container exited. Cleanup"
    docker rm -f ${CONTAINER_NAME}
fi


docker run -p 9090:9090 \
    --volume ${VOLUME_NAME}:/data \
    --name prometheus \
    ${IMAGE_NAME} \
    /usr/local/bin/prometheus \
    --config.file /etc/prometheus/prometheus.yml \
    --storage.tsdb.path /prometheus_data/ \
    --web.console.libraries /etc/prometheus/console_libraries/ \
    --web.console.templates /etc/prometheus/consoles &


