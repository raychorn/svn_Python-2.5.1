#!C:\Python25\python.exe

# Twisted, the Framework of Your Internet
# Copyright (c) 2001-2004 Twisted Matrix Laboratories.
# See LICENSE for details.


### Twisted Preamble
# This makes sure that users don't have to set up their environment
# specially in order to run these programs from bin/.
import sys, os
path = os.path.abspath(sys.argv[0])
while os.path.dirname(path) != path:
    if os.path.basename(path).startswith('Twisted'):
        sys.path.insert(0, path)
        break
    path = os.path.dirname(path)
### end of preamble

from twisted.words.scripts import im
im.run()

