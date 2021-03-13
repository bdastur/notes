#!/bin/bash

echo "Executing docker build"

IMAGE_NAME="bdastur/gobuilder:1.0"


docker build --tag bdastur/gobuilder:1.0 -f Dockerfile.builder  .
docker rm -f extract
docker create --name extract bdastur/gobuilder:1.0
docker cp extract:/workspace/sampleproj sp


