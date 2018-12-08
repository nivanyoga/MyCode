import sys
import os

path = os.path.abspath('.') # default is current dir
if len(sys.argv) == 2:
    path = sys.argv[1]
exts = []
print (path)
for root, dirs, files in os.walk(os.path.expanduser(path)):
    for fn in files:
        print (fn)
        bn, ext = os.path.splitext(fn)
        print (bn)
        if not ext in exts:
            exts.append(ext)
            #if ext:
                #print (ext)
