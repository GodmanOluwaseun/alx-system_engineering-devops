#Puppet file to Configure servers and custom http header

exec { 'configure-http':
  command => 'apt-get update;
  sudo apt-get -y install nginx;
  sudo sed -i "/location \/ {/a \ add_header X-Served-By $SERVER_NAME;" /etc/nginx/sites-available/default;
  sudo service nginx restart',
  provider => shell,
}
