#!/usr/bin/env bash

set -xe

MOUNTED_REPOS_DIR=/etc/yum.repos.d.mount
YUM_REPO_LOCATION=/etc/yum.repos.d
SWARM_CLIENT_JAR="swarm-client-2.2-jar-with-dependencies.jar"

if [ -d "${MOUNTED_REPOS_DIR}" ]; then
    echo "Copying RPM sources from ${MOUNTED_REPOS_DIR} to the default yum repo location in ${YUM_REPO_LOCATION}"
    find ${MOUNTED_REPOS_DIR} -maxdepth 1 -type f -exec cp {} ${YUM_REPO_LOCATION}/ \;
fi

exec java -jar /usr/local/bin/${SWARM_CLIENT_JAR} \
    -master http://$MASTER_PORT_8080_TCP_ADDR:$MASTER_PORT_8080_TCP_PORT $EXTRA_PARAMS

