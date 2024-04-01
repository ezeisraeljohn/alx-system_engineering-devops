# 2-puppet_custom_http_response_header.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}

# Define custom HTTP header in Nginx configuration
file { '/etc/nginx/conf.d/custom_http_header.conf':
  ensure  => present,
  content => "add_header X-Served-By $::hostname;",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

