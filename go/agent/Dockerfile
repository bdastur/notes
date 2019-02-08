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
    docker \
    unzip git jq && \
    yum clean all


