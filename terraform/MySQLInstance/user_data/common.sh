#!/bin/bash
set -e

echo "Mysql Server Setup Start."  2>&1 | tee -a /tmp/userdata.out

echo "Installing mysql community server" 2>&1 | tee -a /tmp/userdata.out 
sudo wget https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm
sudo dnf install -y mysql80-community-release-el9-1.noarch.rpm

dnf repolist enabled | grep "mysql.*-community.*"
sudo dnf install -y mysql-community-server

# Start mysqld server.
systemctl start mysqld.service

# Identify password.
cat /var/log/mysqld.log | grep "A temporary password is generated" 2>&1 | tee -a /tmp/userdata.out 

backupPassword="Pass-word1"
adminPassword="Pass-word1"
password=$(cat /var/log/mysqld.log  | grep "A temporary password is generated" | awk -F"for root@localhost: " '{print $2}')
echo "Password: $password" 2>&1 | tee -a /tmp/userdata.out 
mysql --connect-expired-password -u root -p$password -e "ALTER USER 'root'@'localhost' IDENTIFIED BY '$adminPassword';"
echo "Here 1" 2>&1 | tee -a /tmp/userdata.out
mysql -u root -p$adminPassword -e "CREATE USER 'backup'@'%' IDENTIFIED BY '$backupPassword';"
mysql -u root -p$adminPassword -e "GRANT ALL PRIVILEGES ON *.* TO 'backup'@'%' WITH GRANT OPTION;"
echo "Bootstraping MysqlDB completed" 2>&1 | tee -a /tmp/userdata.out 


