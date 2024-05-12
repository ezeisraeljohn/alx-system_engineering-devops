$settings_file = '/var/www/html/wp-settings.php'

file { $settings_file:
  ensure => file,
}

exec { 'fix_typo_in_settings_config':
  command     => "sed -i 's/phpp/php/g' ${settings_file}",
  path        => ['/bin', '/usr/bin', '/usr/sbin'],
  refreshonly => true,
  subscribe   => File[$settings_file],
}

