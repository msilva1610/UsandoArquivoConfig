# main.py

import sys
import config

import config

def connect_db(dbname):
    if dbname != config.DATABASE_CONFIG['dbname']:
        raise ValueError("Couldn't not find DB with given name")
    
    print('host: ' + config.DATABASE_CONFIG['host'])

connect_db('company')

config.DATABASE_CONFIG['user'] = 'mau'

print(config.DATABASE_CONFIG['user'])
