#Set the config of an ssh file

file_line { ‘Set private key’:
  Path => ‘etc/ssh/ssh_config’,
  line => ’	IdentityFile ~/.ssh/school’,
  match => ‘^IdentityFile’, 
}

file_line { ‘Set password check off’.:
  path => ‘etc/ssh/ssh_config’,
  line => ‘	PasswordAuthentication no’,
  match => ‘^PasswordAuthentication’,
}
