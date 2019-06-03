#!/usr/bin/python
 
import threading
import time
import logging
import datetime
from random import randint


logging.basicConfig(filename='logthreads.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

logging.debug("Programa iniciou")

t = []
Numthreads = 20

for i in range(Numthreads):
    t.append(i)


def worker01(message):
    tempoinicial = datetime.datetime.now()
    espera = randint(1,10)
    time.sleep(espera)
    tempofinal = datetime.datetime.now()
    tempototal = (tempofinal - tempoinicial)
    msg = message + " : " + str(tempototal)
    print (msg)
    logging.debug(msg)

 
for i in range(Numthreads):
    args = "Thread {} sendo executada".format(i)
    t[i] = threading.Thread(target=worker01,args=(args,))
    t[i].start()
    while t[i].isAlive():
        print ("Aguardando thread")
        time.sleep(1)

print ("Thread morreu")
print ("Finalizando programa")