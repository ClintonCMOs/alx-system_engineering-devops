# Setting open file limit to 4096
exec { 'set_UNLIMIT':
  command => 'sed -i "s/LIMIT=\"-n 15\"/ulimit=\"-n 4096\"/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restarting Nginx
exec { 'restart_nginx':
  command => 'sudo service nginx restart',
  path    => ['/usr/sbin/', '/usr/bin/']
}
