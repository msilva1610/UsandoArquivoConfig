#!/usr/bin/python3

import _thread
import time

# Define a function for the thread
def executar( threadName, delay):
    print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
   _thread.start_new_thread( executar, ("Thread-1", 2, ) )
   _thread.start_new_thread( executar, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass