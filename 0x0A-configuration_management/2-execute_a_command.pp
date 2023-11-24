# kils killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
