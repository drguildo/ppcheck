#!/usr/bin/env python

import cgi
from os import environ as env

myip = "127.0.0.1"

if __name__ == "__main__":
  form = cgi.FieldStorage()

  print 'Content-type: text/plain\n'

  if env['REMOTE_ADDR'] == myip:
    print "junk"
  elif env.has_key('HTTP_X_FORWARDED_FOR') and env['HTTP_X_FORWARDED_FOR'] == myip:
    print "junk"
  else:
    if form.has_key("ppcheck"):
      print "ok"
    else:
      print "junk"
