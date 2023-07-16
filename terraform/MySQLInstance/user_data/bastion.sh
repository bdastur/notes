#!/bin/bash

echo "Mysql Server Setup Start." > /tmp/userdata.out

echo "Installing mysql community server" >> /tmp/userdata.out
sudo wget https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm
sudo dnf install -y mysql80-community-release-el9-1.noarch.rpm

dnf repolist enabled | grep "mysql.*-community.*"
sudo dnf install -y mysql-community-server




