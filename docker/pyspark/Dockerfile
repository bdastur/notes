FROM spark:3.5.3-scala2.12-java17-ubuntu

USER root

RUN set -ex; \
    apt-get update; \
    apt-get install -y python3 python3-pip; \
    apt-get install -y r-base r-base-dev; \
    rm -rf /var/lib/apt/lists/*

RUN apt update; \
    apt install -y vim

RUN pip install pyspark boto3 bpython

ENV R_HOME /usr/lib/R

#USER spark
