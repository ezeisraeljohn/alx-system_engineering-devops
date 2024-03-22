# Install the Flask
package { 'Flask':
        ensure   => '2.1.0',
        provider => 'pip3',
}

# Install Werkzeug version 2.1.1 using pip3 provider
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}