############################################################
# Simple Python Client 
#
############################################################
ARG VERSION="latest"

FROM python:3-alpine
LABEL version="1.0"
MAINTAINER bdastur

Run echo "Build simple python client"
RUN apk update

# Bash is needed only for testing.
RUN apk add bash

RUN apk add gcc

ADD src/client.py /client.py
RUN chmod +x /client.py


CMD ["./client.py"] 

