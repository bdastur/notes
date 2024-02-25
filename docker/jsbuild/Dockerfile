ARG VERSION="latest"
FROM al2base:$VERSION
LABEL version="1.0"
MAINTAINER bdastur@gmail.com

RUN echo "Build javascript builder image"

RUN dnf install -y less \
    sudo \
    npm \
    wget \
    vim

RUN sudo npm install yarn -g
RUN sudo npm install parcel -g
RUN sudo npm install @heroicons/react -g
RUN sudo npm install @headlessui/react -g
RUN yarn add react react-dom
#RUN npm install -d tailwindcss postcss
#RUN npm install @heroicons/react
#RUN npm install @headlessui/react


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

