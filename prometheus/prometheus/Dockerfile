FROM centos as base

RUN mkdir /etc/prometheus && \
    mkdir /data && \
    mkdir /prometheus


RUN yum install -y wget
RUN wget https://github.com/prometheus/prometheus/releases/download/v2.21.0/prometheus-2.21.0.linux-amd64.tar.gz
RUN tar -xzvf prometheus-2.21.0.linux-amd64.tar.gz && \
    cp prometheus-2.21.0.linux-amd64/prometheus /usr/local/bin/prometheus && \
    cp prometheus-2.21.0.linux-amd64/promtool /usr/local/bin/promtool && \
    cp -R prometheus-2.21.0.linux-amd64/console_libraries /etc/prometheus/console_libraries && \
    cp -R prometheus-2.21.0.linux-amd64/consoles /etc/prometheus/consoles && \
    cp prometheus-2.21.0.linux-amd64/prometheus.yml /etc/prometheus/prometheus.yml


ADD ./start.sh /start.sh 
RUN chmod +x /start.sh

EXPOSE 9090/tcp
VOLUME ["/prometheus_data"]


CMD ["/start.sh"]
#ENTRYPOINT ["/usr/local/bin/prometheus" $@]
