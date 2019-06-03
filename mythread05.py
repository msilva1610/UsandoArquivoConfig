#!/usr/bin/python
 
import threading
import time

t = []

Numthreads = 5

for i in range(Numthreads):
    t.append(i)


def worker01(message):
    print (message)
    time.sleep(10)

 
for i in range(Numthreads):
    args = "Thread {} sendo executada".format(i)
    t[i] = threading.Thread(target=worker01,args=(args,))
    t[i].start()
    while t[i].isAlive():
        print ("Aguardando thread")
        time.sleep(1)

print ("Thread morreu")
print ("Finalizando programa")