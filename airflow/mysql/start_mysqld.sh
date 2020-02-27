#!/bin/bash
set -ex

echo "Starting Mysql"

MYSQL_DATADIR="/var/lib/mysql"
SQLINIT_FILE="/tmp/sqlinit.txt"
CLIENT_PASSWORDFILE="${HOME}/.my.cnf"

# Initialize insecure. This creates a root user with no password
if [ ! -d $MYSQL_DATADIR ]; then
    mysqld --initialize-insecure
fi


pid=$(ps -ef | grep "mysqld --daemonize" | grep -v grep | awk -F" " '{print $2}')
echo "PID: $pid"
if [ ! -z $pid ]; then
    echo "Killing mysql daemon!"
    kill -9 $pid
fi

cat > ${SQLINIT_FILE} <<EOF
SHOW databases;
CREATE database airflow;
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root';
commit;
EOF

touch ${CLIENT_PASSWORDFILE}
cat > ${CLIENT_PASSWORDFILE} <<EOF
[client]
password=root
EOF


# Start mysql daemon.
mysqld --daemonize --init-file=${SQLINIT_FILE}


mysql -u root -proot -e 'show databases;'

