############################################################
# Simple Python application.
#
############################################################
ARG VERSION="latest"

FROM python:2-alpine
LABEL version="1.0"
MAINTAINER bdastur

Run echo "Build simple app container"
RUN apk update

# Bash is needed only for testing.
RUN apk add bash

RUN apk add gcc python-dev musl-dev mariadb-dev 
RUN apk add mysql-client

ADD src/start.sh /start.sh
RUN chmod +x /start.sh


CMD ["./start.sh"] 

