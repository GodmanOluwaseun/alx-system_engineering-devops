#Set the config of an ssh file

file_line { ‘Set private key’:
  Path => ‘~/.ssh/ssh_config’,
  line => ’	IdentityFile ~/.ssh/school’,
  match => ‘^IdentityFile’, 
}

file_line { ‘Set password check off’.:
  path => ‘~/.ssh/ssh_config’,
  line => ‘	PasswordAuthentication no’,
  match => ‘^PasswordAuthentication’,
}
