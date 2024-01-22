# enables user holberton to login without errors

# increases hard file limit for Holberton user
exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '/^holberton hard/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

# increases soft file limit for Holberton user
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton soft/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
