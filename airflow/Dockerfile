FROM centos

ADD scripts/* /airflow/scripts/

RUN yum install -y epel-release && \
    yum install -y gcc && \
    yum install -y python-devel python2-pip && \
    yum clean all

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip install apache-airflow

RUN export AIRFLOW_HOME=~/airflow




CMD ["/bin/bash"]

