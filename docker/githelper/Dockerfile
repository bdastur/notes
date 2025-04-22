ARG VERSION="latest"
FROM amazonlinux:$VERSION
LABEL version="1.0"
LABEL author="bdastur@gmail.com"

RUN yum update -y
RUN yum install sudo \
                gcc \
                vim-enhanced \
                git -y


ADD ./scripts/start.sh /start.sh
ADD ./configs/gitconfig /.gitconfig


CMD ["./start.sh"]

