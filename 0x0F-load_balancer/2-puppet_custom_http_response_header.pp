#Puppet file to Configure servers and custom http header

exec { 'system_update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
   ensure => installed,
   require => Exec['system_update']
}

file { '/var/www/html/index.html':
  content => "Hello World!',
  require => Package['nginx']
}

exec { 'redirect_me':
  command => 'sed -i '/listen 80 default_server/a \	rewrite ^/redirect_me https://intranet.alxswe.com/ permanent;' /etc/nginx/sites-available/default'
  provider => 'shell',
  require => Package['nginx']
}

file_line { 'add_http_header':
  ensure => 'present',
  path => '/etc/nginx/sites-available/default',
  after => 'location / {',
  line  => 'add_header X-Served-By $hostname;'
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => Exec['redirect_me']
}
