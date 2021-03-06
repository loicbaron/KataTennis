#!/usr/bin/env python3
config = {
    'SQL_DATABASE_URI': 'sqlite:///katatennis/db/database.db?check_same_thread=False',
    'SQL_ISOLATION_LEVEL': 'SERIALIZABLE',
    'SQL_ECHO': True,
    'SQL_ECHO_POOL': False,
    'SQL_CONVERT_UNICODE': True,
    'SQL_POOL_SIZE': None,
    'SQL_POOL_TIMEOUT': None,
    #'SQL_POOL_RECYCLE': 3600,
    #'SQL_MAX_OVERFLOW': 10,
    'SQL_AUTOCOMMIT': False,
    'SQL_AUTOFLUSH': True,
    'SQL_EXPIRE_ON_COMMIT': True
}
