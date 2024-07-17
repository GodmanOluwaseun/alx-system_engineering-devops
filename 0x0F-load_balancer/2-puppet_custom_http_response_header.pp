#Puppet file to Configure servers and custom http header

exec { 'system_update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
   ensure => installed,
   require => Exec['system_update'],
}

file_line { 'add_http_header':
  ensure => 'present',
  path => '/etc/nginx/sites-available/default',
  after => 'location / {',
  line  => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

service { 'nginx':
  ensure => 'running,'
  enable => 'true',
  subscribe => File['/etc/nginx/sites-available/default'],
}
