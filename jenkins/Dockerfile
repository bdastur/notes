FROM centos

############################################################
# Add Tini
# https://github.com/krallin/tini
# Tini spawns a single child, and wait for it to exit, all
# the while reaping zombies and performing signal forwarding
############################################################
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /bin/tini
RUN chmod +x /bin/tini

############################################################
# Install any packages here
############################################################
RUN yum install -y java-1.8.0-openjdk-devel \
    wget \
    unzip


############################################################
# Jenkins is run with the `jenkins` user.
############################################################
ENV JENKINS_HOME /var/jenkins_home
ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000
ARG http_port=8080
ARG agent_port=50000

# Jenkins is run with user `jenkins`, uid = 1000
# If you bind mount a volume from the host or a data container,
# ensure you use the same uid
RUN groupadd -g ${gid} ${group} \
    && useradd -d "$JENKINS_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}


###########################################################
# Jenkins home directory is a volume, so configuration and build history
# can be persisted and survive image upgrades
###########################################################
VOLUME $JENKINS_HOME

###########################################################
# Environment variables. 
# These are used in the install-plugins.sh, jenkins-support
# scripts.
###########################################################
ENV JENKINS_SLAVE_AGENT_PORT ${agent_port}
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log
ENV JENKINS_UC https://updates.jenkins.io
ENV JENKINS_UC_EXPERIMENTAL=https://updates.jenkins.io/experimental

###########################################################
# Get jenkins and INSTALL
###########################################################
ENV JENKINS_VERSION 2.150.1-1.1
RUN wget https://pkg.jenkins.io/redhat-stable/jenkins-${JENKINS_VERSION}.noarch.rpm
RUN rpm -ivf jenkins-${JENKINS_VERSION}.noarch.rpm

###########################################################
# Copy the jenkins.war to proper location
###########################################################
RUN mkdir -p /usr/share/jenkins/ref
RUN cp /usr/lib/jenkins/jenkins.war /usr/share/jenkins/jenkins.war

###########################################################
# Copy the plugins.txt, install-plugins.sh, jenkins-support
# to proper locations.
# install-plugins.sh is used to install any
# jenkins plugins you need as part of the jenkins build.
###########################################################
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
COPY plugins.sh /usr/local/bin/plugins.sh
COPY install-plugins.sh /usr/local/bin/install-plugins.sh 
RUN chmod +x /usr/local/bin/install-plugins.sh
COPY jenkins-support /usr/local/bin/jenkins-support

###########################################################
# jenkins.sh is the startup script.
###########################################################
ADD jenkins.sh /usr/local/bin/jenkins.sh
RUN chmod +x /usr/local/bin/jenkins.sh


###########################################################
# Define the entry point
###########################################################
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]

###########################################################
# Install additional plugins here.
###########################################################
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt 

