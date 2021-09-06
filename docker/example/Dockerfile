ARG VERSION="latest"
FROM amazonlinux:$VERSION

LABEL application="example" OS="AL2"

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
