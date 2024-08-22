# Reconfigure OS limits file to increase limits for user

exec { 'increase_hard_limit':
  command => 'sed -i "s/^holberton hard.*/holberton hard nofile 65536/" /etc/security/limits.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

exec { 'increase_soft_limit':
  command => 'sed -i "s/^holberton soft.*/holberton soft nofile 65536/" /etc/security/limits.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
