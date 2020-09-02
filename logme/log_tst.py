import logging
import sys

def cons_test_logger():
    """
    Create very detailed log for pattern testing.
    $ chgrp loggroup logdir
    $ chmod g+w logdir
    $ chmod g+s logdir
    $ usermod -a -G loggroup myuser
    $ umask 0002
    """

    """
    If you want to do custom logging, you should use the 
    folder /var/log/my-logs, to which you have full read/write access, including adding + deleting files....
    
    # getent group celery
    celery:x:1004:user,apache
    
    # getent group loggroup
    loggroup:x:1003:user,apache

    # getent group apache
    apache:x:48:

    usermod -a -G apache user
    
    """
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

    cons_handler = logging.StreamHandler(stream=sys.stdout)
    cons_handler.setLevel(logging.DEBUG)
    cons_format = logging.Formatter('%(asctime)-24s'
                                    # '%(levelname)-8s'
                                    '%(module)-20s'
                                    '%(funcName)-22s'
                                    'L:%(lineno)-6s'
                                    '%(message)8s')
    cons_handler.setFormatter(cons_format)
    log.addHandler(cons_handler)

    return log
