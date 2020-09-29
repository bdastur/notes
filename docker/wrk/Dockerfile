FROM centos as base

RUN  yum -y groupinstall "Development Tools" && \
     yum install -y openssl-devel git && \
     git clone https://github.com/wg/wrk.git

RUN cd wrk && make 
RUN cd wrk && cp wrk /usr/local/bin/wrk

CMD ["/bin/bash"]

