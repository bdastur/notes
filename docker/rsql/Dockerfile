ARG VERSION="2.0.20220606.1"
FROM amazonlinux:$VERSION
LABEL version="1.0"
MAINTAINER bdastur@gmail.com

RUN echo "Build Base AL2 Image"

ENV ODBC_VERSION=1.4.56.1000
ENV RSQL_VERSION=1.0.5

RUN yum update -y && \
    yum install -y unixODBC less && \
    yum clean all

RUN rpm -i \
    https://s3.amazonaws.com/redshift-downloads/drivers/odbc/${ODBC_VERSION}/AmazonRedshiftODBC-64-bit-${ODBC_VERSION}-1.x86_64.rpm \
    https://s3.amazonaws.com/redshift-downloads/amazon-redshift-rsql/${RSQL_VERSION}/AmazonRedshiftRsql-${RSQL_VERSION}-1.x86_64.rpm

RUN cp /opt/amazon/redshiftodbc/Setup/odbc.ini ~/.odbc.ini
RUN ln -s /usr/bin/less /usr/bin/more

ENV ODBCINI=~/.odbc.ini
ENV ODBCSYSINI=/opt/amazon/redshiftodbc/Setup
ENV AMAZONREDSHIFTODBCINI=/opt/amazon/redshiftodbc/lib/64/amazon.redshiftodbc.ini


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

