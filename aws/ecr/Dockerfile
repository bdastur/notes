FROM python:2-alpine
MAINTAINER behzad_dastur@symantec.com

RUN apk update

# Bash is needed only for testing.
RUN apk add bash

RUN apk add gcc python-dev

RUN pip install requests
RUN pip install kafka-python
RUN pip install pyYAML


ADD start.sh /start.sh
RUN chmod +x /start.sh


CMD ["/start.sh"] 

