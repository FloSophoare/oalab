#!/usr/bin/python3
import sys, os

myFile = open(sys.argv[1], 'a+')
n = os.path.getsize(sys.argv[1])
print(n)
if n > 510:
    print('ERROR: boot block too large: %s bytes.(max 510)\n' % n)
    sys.exit()
print('OK: boot block is %s bytes.(max 510)\n' % n)
for i in range(1, 510-n):
    myFile.write('\0')
myFile.write('\x55')
myFile.write('\xAA')
myFile.close()

