############################################################
# Simple Python Server
#
############################################################
ARG VERSION="latest"

FROM python:3-alpine
LABEL version="1.0"
MAINTAINER bdastur

Run echo "Build simple app container"
RUN apk update

# Bash is needed only for testing.
RUN apk add bash

RUN apk add gcc python3-dev 

ADD src/server.py /server.py
RUN chmod +x /server.py


CMD ["./server.py"] 

