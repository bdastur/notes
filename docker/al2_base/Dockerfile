ARG VERSION="latest"
FROM amazonlinux:$VERSION
LABEL version="1.0"
MAINTAINER bdastur@gmail.com

RUN echo "Build Base AL2 Image"

ARG VERSION
RUN echo $VERSION > image_version

ENV FOO=/bar
ENV my_new_var="A new Var $FOO"

RUN echo ${FOO}
RUN echo $my_new_var
RUN echo $SHELL
RUN echo env

RUN env > al2_env


ADD ./data /al2_data
ADD ./scripts/start.sh /start.sh
RUN chmod +x start.sh

CMD ["./start.sh"]



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

