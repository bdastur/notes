FROM centos
MAINTAINER bdastur@gmail.com

USER root

############################################################
# Add Tini
# https://github.com/krallin/tini
# Tini spawns a single child, and wait for it to exit, all
# the while reaping zombies and performing signal forwarding
############################################################
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /bin/tini
RUN chmod +x /bin/tini


RUN yum install -y glibc-common \
    java-1.8.0-openjdk-devel \
    wget \
    unzip git jq && \
    yum clean all


ADD https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-client/2.2/swarm-client-2.2-jar-with-dependencies.jar /usr/local/bin/swarm-client-2.2-jar-with-dependencies.jar

ADD scripts/start.sh /usr/bin/
RUN chmod +x /usr/bin/start.sh

#ENTRYPOINT ["/bin/tini", "--", "/usr/bin/start.sh"]
ENTRYPOINT ["/bin/bash"]


