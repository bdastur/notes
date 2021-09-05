FROM amazonlinux:latest
MAINTAINER bdastur@gmail.com

USER root

RUN yum install -y \
    shadow-utils.x86_64 \
    wget tar gzip \
    gcc make && \
    yum clean all && \
    rm -rf /var/lib/yum/yumdb

RUN groupadd -g 4111 brd && useradd -u 2111 -g 4111 brd

ENV PATH=$PATH:/usr/local/go/bin:/root/go/bin

RUN wget https://golang.org/dl/go1.17.linux-amd64.tar.gz
RUN tar -xzf go1.17.linux-amd64.tar.gz -C /usr/local/

# Golangci-lint linter.
RUN curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh -s -- -b $(go env GOPATH)/bin v1.42.0

# Create path for source.
RUN mkdir /src


############################################################
# Add Tini
# https://github.com/krallin/tini
# Tini spawns a single child, and wait for it to exit, all
# the while reaping zombies and performing signal forwarding
############################################################
#ENV TINI_VERSION v0.18.0
#ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /bin/tini
#RUN chmod +x /bin/tini


#RUN yum install -y glibc-common \
#    java-1.8.0-openjdk-devel \
#    wget \
#    docker \
#    unzip git jq && \
#    yum clean all

#RUN mkdir -p /projects/{bin,pkg,src}
#RUN chmod -R 777 /projects/{bin,pkg,src}

#ENV GOPROJPATH "$HOME/projects"
#ENV GOPATH "/go"
#ENV GOBIN "$GOPROJPATH/bin"
#ENV PATH=$PATH:$GOBIN:/usr/local/go/bin

#RUN wget https://golang.org/dl/go1.17.linux-amd64.tar.gz
#RUN tar -C /usr/local -xzf go1.17.linux-amd64.tar.gz

#RUN wget https://github.com/golang/dep/releases/download/v0.5.0/dep-linux-amd64 -o dep && chmod +x dep
#RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh -o install.sh
#RUN bash install.sh
#RUN wget https://github.com/Masterminds/glide/releases/download/v0.13.2/glide-v0.13.2-linux-amd64.tar.gz

# Golangci-lint linter.
#RUN curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh -s -- -b $(go env GOPATH)/bin v1.42.0

#RUN go get "github.com/fzipp/gocyclo" && \
#    go get -u "golang.org/x/lint/golint" && \
#    go get "github.com/client9/misspell/cmd/misspell"
