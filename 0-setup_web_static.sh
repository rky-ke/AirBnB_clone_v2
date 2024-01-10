#!/usr/bin/env bash
set -e
# sets up my web servers for the deployment of web_static
echo -e "\e[1;32m START\e[0m"

#--Updating the packages
sudo apt-get -y update
sudo apt-get -y install nginx
echo -e "\e[1;32m Packages updated\e[0m"
echo

#--create the directories
sudo mkdir -p /data/web_static/{releases/test,shared}

echo -e "\e[1;32m directories created\e[0m"
echo

#--adds test string
echo "<h1>Welcome to www.iamrkyegon.tech</h1>" > /data/web_static/releases/test/index.html
echo -e "\e[1;32m Test String added\e[0m"
echo

# Remove the symbolic link if it already exists
sudo rm -f /data/web_static/current

# Create a new symbolic link
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data

# Configure Nginx
cat <<EOF | sudo tee /etc/nginx/sites-available/default > /dev/null
server {
    listen 80;
    server_name _;
    add_header X-Served-By \$hostname;

    location / {
        root /var/www/html;
        index index.html;
    }
        location /hbnb_static/ {
        alias /data/web_static/current/;
    }

}
EOF

#--restart NGINX
sudo service nginx restart
echo -e "\e[1;32m restart NGINX\e[0m"
