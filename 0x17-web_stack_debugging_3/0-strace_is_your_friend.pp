# Debug and fix Apache server returning error 500, correct php typo.

exec { 'wordpress_fix':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path => '/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
