# Creates a file named 'school' in the '/tmp' directory with the specified attributes.
# The file will have read, write, and execute permissions for the owner (www-data),
# and read and execute permissions for the group (www-data) and others.
# The content of the file will be set to 'I love Puppet'.

file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
