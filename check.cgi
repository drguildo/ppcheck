#!/usr/bin/env python

import cgi
from os import environ as env

myip = "127.0.0.1"

if __name__ == "__main__":
  form = cgi.FieldStorage()

  print 'Content-type: text/plain\n'

  for v in env.values():
    if v.find(myip) != -1:
      print "junk"
      return

  print "ok"
