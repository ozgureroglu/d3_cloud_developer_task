#!/bin/bash
sudo su
yum update -y
yum install httpd -y
systemctl start httpd
systemctl enable httpd
# Add the name of the instance to index file to show the ALB requests reach to different nodes
echo 'Welcome to Instance: '${HOSTNAME}>> /var/www/html/index.html
