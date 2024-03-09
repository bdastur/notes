ARG VERSION="latest"
FROM al2base:$VERSION
LABEL version="1.0"
MAINTAINER bdastur@gmail.com

RUN echo "Build python builder image"

RUN dnf install -y gcc \
    g++ \
    python3-devel \
    python3-pip \
    vim \
    wget \
    less


RUN pip install -U setuptools wheel
RUN pip install -U spacy
RUN pip install pytz
RUN python3 -m spacy download en_core_web_sm
RUN pip install chatterbot==1.0.4
RUN pip install bpython


#RUN dnf install -y $JAVA_VERSION \
#    wget \
#    unzip \
#    findutils


#RUN mkdir /opt/gradle /gradlestage
#RUN cd /gradlestage && wget https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip 
#RUN unzip -d /opt/gradle/ gradle-$GRADLE_VERSION-bin.zip



#bash-5.2# history | grep install
#   16  yum install sudo
#   25  dnf install gcc
#   52  dnf install vim-enhanced
#   60  dnf install libnl3-cli
#   65  dnf install more
#   66  dnf install less
#   79  dnf install python3-pip
#   81  pip install flask
#   90  dnf install python3-devel
#   94  pip install bpython
#  101  history | grep install
#bash-5.2# 

