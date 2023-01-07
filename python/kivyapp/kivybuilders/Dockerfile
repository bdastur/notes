FROM ubuntu:22.04

ENV USER="user"
ENV HOME_DIR="/home/${USER}"
ENV WORK_DIR="${HOME_DIR}/hostcwd"

# Install required packages.
RUN apt update -y
RUN apt install -y \
    autoconf automake build-essential ccache cmake gettext git \
    libffi-dev libltdl-dev libtool libssl-dev openjdk-17-jdk \
    patch pkg-config python3-pip python3-setuptools \
    sudo unzip zip zlib1g-dev \
    vim

# Install pip modules.
RUN pip3 install --upgrade Cython buildozer kivy

# Create a non root sudo user (Buildozer throws a working if running in root mode)
RUN useradd --create-home --shell /bin/bash ${USER}
RUN usermod -append --groups sudo ${USER}
RUN echo  "%sudo ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers 
   
USER ${user}
WORKDIR ${WORK_DIR}

CMD ["/bin/bash"]
