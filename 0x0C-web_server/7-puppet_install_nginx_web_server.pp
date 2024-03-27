# nginx_config.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Enable Nginx default site
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

# Create HTML directory
file { '/var/www/html':
  ensure => directory,
}

# Create index.html file with Hello World
file { '/var/www/html/index.html':
  ensure  => present,
  content => '<html><body>Hello World!</body></html>',
}

# Configure redirection for /redirect_me
file { '/etc/nginx/sites-available/redirect_me':
  ensure  => present,
  content => template('nginx/redirect_me.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Enable redirection site
file { '/etc/nginx/sites-enabled/redirect_me':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/redirect_me',
  require => File['/etc/nginx/sites-available/redirect_me'],
  notify  => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/redirect_me'],
}
