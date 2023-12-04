# 2-puppet_custom_http_response_header.pp

package { 'nginx':
  ensure => installed,
}

$hostname = $::hostname

file { '/etc/nginx/sites-available/custom_header':
  ensure  => present,
  content => "add_header X-Served-By ${hostname};\n",
}

file { '/etc/nginx/sites-enabled/custom_header':
  ensure  => link,
  target  => '/etc/nginx/sites-available/custom_header',
  require => File['/etc/nginx/sites-available/custom_header'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/custom_header'],
}
