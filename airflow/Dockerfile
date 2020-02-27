FROM centos as base

RUN yum install -y epel-release && \
    yum install -y gcc && \
    yum install -y python-devel python2-pip && \
    yum clean all

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install apache-airflow

# MySQL.
RUN yum install -y wget && \
    yum clean all

RUN wget https://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm
RUN rpm -ivh mysql57-community-release-el7-9.noarch.rpm 
RUN yum install -y mysql-server && \
    yum install -y mysql-devel && \
    yum clean all

RUN pip install MySQL-python 


FROM base as airflow
USER root
ADD scripts/* /airflow/scripts/ 
RUN export AIRFLOW_HOME=/root/airflow

CMD ["/bin/bash"]

