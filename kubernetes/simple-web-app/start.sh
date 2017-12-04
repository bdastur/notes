#!/bin/sh

echo "START CONTAINER"

# This is our simple web app.
python -m SimpleHTTPServer 5001 &

# It does not make practical sense, but this is to
# test the liveness and readiness Probes,
# which look for /tmp/healthy and /tmp/ready files.

while true;
do
    echo "Health check"
    echo "ok" > /tmp/healthy
    echo "ok" > /tmp/ready
    sleep 50
done
