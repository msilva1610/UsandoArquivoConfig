#!/usr/bin/python
 
import threading
import time
import logging
import datetime
from random import randint


logging.basicConfig(filename='mythread07.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

logging.debug("Programa iniciou")

t = []
Numthreads = 100

for i in range(Numthreads):
    t.append(i)


def worker01(message):
    tempoinicial = datetime.datetime.now()
    espera = randint(1,60)
    time.sleep(espera)
    tempofinal = datetime.datetime.now()
    tempototal = (tempofinal - tempoinicial)
    msg = message + " : " + str(tempototal)
    print (msg)
    logging.debug(msg)

 
for i in range(Numthreads):
    args = "Thread {} sendo finalizada".format(i)
    t[i] = threading.Thread(target=worker01,args=(args,))
    t[i].start()

print ("Finalizando programa")