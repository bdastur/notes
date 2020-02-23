FROM centos as base

RUN yum install -y epel-release && \
    yum install -y gcc && \
    yum install -y python-devel python2-pip && \
    yum clean all

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install apache-airflow


FROM base as airflow
USER root
ADD scripts/* /airflow/scripts/ 
RUN export AIRFLOW_HOME=/root/airflow

CMD ["/bin/bash"]

