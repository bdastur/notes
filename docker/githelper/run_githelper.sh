#!/bin/bash

echo "Run git container"
sourcePath=$1
destPath=$2

if [[ -z $sourcePath ]]; then
    echo "Usage ./run_git_container.sh <path to git workspace> <dest path in container>"
    exit 1
fi

if [[ -z $destPath ]]; then
    echo "Usage ./run_git_container.sh <path to git workspace> <dest path in container>"
    exit 1
fi

docker rm -f githelper
docker run -it --volume $sourcePath:$destPath --name githelper githelper:latest /bin/bash


