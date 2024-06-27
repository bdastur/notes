ARG VERSION="latest"
FROM al2base:$VERSION
LABEL version="1.0"
MAINTAINER bdastur@gmail.com

RUN echo "Build buildbot image"

EXPOSE 8010

RUN dnf groupinstall -y "Development Tools"
RUN dnf install -y python3-pip

RUN pip install buildbot[bundle]
RUN pip install buildbot-worker 
RUN pip install setuptools-trial

# set master.
RUN mkdir -p ~/buildbot-test/master_root
RUN mkdir -p ~/buildbot-test/worker_root

#RUN pip install bpython

CMD ["/bin/bash"]

#    1  pip install --upgrade pip
#    2  pip install buildbot
#    3  sudo pip install buildbot
#    4  yum install sudo
#    5  sudo pip install buildbot
#    6  sudo dnf install build-essentials python3-dev libssl-dev libffi-dev
#    7  buildbot create-master my_master
#    8  mkdir -p ~/buildbot-test/master_root
#    9  cd ~/buildbot-test/master_root/
#   10  buildbot create-master my_master
#   11  pwd
#   12  ls
#   13  buildbot start my_master
#   14  ls
#   15  find / -name twistd.log
#   16  more /root/buildbot-test/master_root/my_master/twistd.log
#   17  less /root/buildbot-test/master_root/my_master/twistd.log
#   18  ls
#   19  ls my_master/
#   20  mv my_master/master.cfg.sample my_master/master.cfg
#   21  buildbot start my_master
#   22  less /root/buildbot-test/master_root/my_master/twistd.log
#   23  pip install buildbot-www
#   24  buildbot start my_master
#   25  less /root/buildbot-test/master_root/my_master/twistd.log
#   26  pip install buildbot-gird-view
#   27  pip search buildbot
#   28  pip list
#   29  pip install buildbot[bundle]
#   30  buildbot start my_master
#   31  ps -ef
#   32  ps
#   33  yum install ps
#   34  sudo dnf install procps
#   35  ps
#   36  buildbot start my_master
#   37  ps -ef
#   38  mkdir -p ~/buildbot-test/worker_root
#   39  cd ~/buildbot-test/worker_root/
#   40  pip install buildbot-worker
#   41  pip install setuptools-trial
#   42  buildbot-worker create-worker my_worker localhost example-worker pass
#   43  ls
#   44  ls my_worker/
#   45  history

