#!/usr/bin/env bash
# Using puppet to connect

file { '/home/your_username/.ssh/config':
  ensure  => present,
  owner   => 'your_username',
  group   => 'your_username',
  mode    => '0600',
}

file_line { 'Turn off passwd auth':
  path    => '/home/your_username/.ssh/config',
  line    => 'PasswordAuthentication no',
  match   => '^#PasswordAuthentication', # Uncomments the line if commented
  require => File['/home/your_username/.ssh/config'],
}

file_line { 'Declare identity file':
  path    => '/home/your_username/.ssh/config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#IdentityFile', # Uncomments the line if commented
  require => File['/home/your_username/.ssh/config'],
}
