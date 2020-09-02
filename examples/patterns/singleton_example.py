"""
https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
"""

from logme.log_tst import cons_test_logger
log = cons_test_logger()
# log = logging.getLogger("core.corelogger")

# Singleton/SingletonPattern.py


class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)


x = OnlyOne('sausage')
y = OnlyOne('eggs')
z = OnlyOne('spam')
log.info("x sausage: %s", x)
log.info("y eggs: %s", y)
log.info("z spam: %s", z)

log.info("repr(x) %s", repr(x))
log.info("repr(y) %s", repr(y))
log.info("repr(z) %s", repr(z))

# Singleton/BorgSingleton.py
# Alex Martelli's 'Borg'


class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):
    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg

    def __str__(self): return self.val


# Singleton/ClassVariableSingleton.py
class SingleTone(object):
    __instance = None

    def __new__(cls, val):
        if SingleTone.__instance is None:
            SingleTone.__instance = object.__new__(cls)
        SingleTone.__instance.val = val
        return SingleTone.__instance
