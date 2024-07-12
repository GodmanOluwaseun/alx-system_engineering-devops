#Puppet file to configure new ubuntu machine.

exec { 'system_update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => installed,
  require => Exec['system_update'],
}

file { '/var/www/html/index.html':
  content => 'Hello World',
  require => Package['nginx'],
}

exec { 'redirect_me':
  command => 'sed -i "listen 80 default_server/a\	rewrite ^/redirect_me https://intranet.alxswe.com/ permanent;" /etc/nginx/sites-available/default',
  provder => 'shell',
  require => package['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => Exec['redirect_me'],
}
