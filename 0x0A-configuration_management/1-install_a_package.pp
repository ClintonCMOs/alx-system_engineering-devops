#install flask package
exec { 'install flask':
  command => 'pip3 install "Flask==2.1.0" "Werkzeug==2.1.1"',
  path    => '/usr/bin/',
  unless  => 'pip3 list | grep -q "Flask==2.1.0"',
}
