FROM centos
MAINTAINER bdastur@gmail.com

USER root

RUN groupadd -g 4111 brd && useradd -u 2111 -g 4111 brd 

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

RUN mkdir -p /projects/{bin,pkg,src}
RUN chmod -R 777 /projects/{bin,pkg,src}

ENV GOPROJPATH "$HOME/projects"
ENV GOPATH "/go"
ENV GOBIN "$GOPROJPATH/bin"
ENV PATH=$PATH:$GOBIN:/usr/local/go/bin


RUN wget https://dl.google.com/go/go1.11.5.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go1.11.5.linux-amd64.tar.gz

#RUN wget https://github.com/golang/dep/releases/download/v0.5.0/dep-linux-amd64 -o dep && chmod +x dep
RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh -o install.sh
RUN bash install.sh

RUN wget https://github.com/Masterminds/glide/releases/download/v0.13.2/glide-v0.13.2-linux-amd64.tar.gz


RUN go get "github.com/fzipp/gocyclo" && \
    go get -u "golang.org/x/lint/golint" && \
    go get "github.com/client9/misspell/cmd/misspell"
