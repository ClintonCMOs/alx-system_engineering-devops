# installs flask package

package {'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
}
#installs Werkzeug package

package {'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
