FROM python:2-alpine
MAINTAINER bdastur

RUN apk update

# Bash is needed only for testing.
RUN apk add bash

RUN apk add gcc python-dev musl-dev mariadb-dev 
RUN apk add mysql-client

ADD src/start.sh /start.sh
RUN chmod +x /start.sh


CMD ["/start.sh"] 

