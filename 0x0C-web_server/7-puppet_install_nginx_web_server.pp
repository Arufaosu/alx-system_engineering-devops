# File: 7-puppet_install_nginx_web_server.pp

$VERBOSE = nil

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => '<html><body>Hello World!</body></html>',
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    listen 80;
    server_name localhost;

    location / {
        root /var/www/html;
        index index.html;
    }

    location /redirect_me {
        rewrite ^ https://www.example.com/ permanent;
    }
}",
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
  notify => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
