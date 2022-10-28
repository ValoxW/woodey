#!/usr/bin/python

import subprocess, time

def system(cmd):
  subprocess.call(cmd, shell=True)

file = open("/proc/sys/fs/file-max", "w")
file.write ("999999999999999999")
file.close()
time.sleep(1)
system ("sed -i 's/1024/9999999/g' /usr/include/bits/typesizes.h")
system ("ulimit -n 99999")
