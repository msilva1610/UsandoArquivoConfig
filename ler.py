import os
import logging

os.environ['site'] = 'www.sky.com.br'


logging.basicConfig(filename='log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)



logging.debug("Running Urban Planning")

print (os.environ['site'])