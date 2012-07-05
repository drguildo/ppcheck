#!/usr/bin/env python

import socket
import sys
import threading
import time
import urllib

class ProxyScanner(threading.Thread):
  def __init__(self, proxy):
    threading.Thread.__init__(self)
    self.proxy = proxy
  def run(self):
    try:
      d = urllib.urlencode({ "ppcheck": "ppcheck"}) # Check for POST support.
      u = urllib.urlopen(checker, d, { "http": "http://" + self.proxy})
    except KeyboardInterrupt:
      raise
    except:
      return
    else:
      result = u.readline().strip()
      if result == "ok":
        print self.proxy

checker = "http://www.example.net/check.cgi" # Use a hostname as some proxies don't do DNS.
numthreads = 100

if len(sys.argv) < 2:
  sys.exit()

try:
  f = open(sys.argv[1])
except:
  print "Couldn't open %s." % sys.argv[1]
  sys.exit()

socket.setdefaulttimeout(20)

try:
  for l in f:
    while threading.activeCount() == numthreads:
      time.sleep(2)
    thread = ProxyScanner(l.strip())
    thread.start()
except KeyboardInterrupt:
  sys.exit()

f.close()
