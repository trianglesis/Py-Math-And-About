import random
"""
https://youtu.be/DEwgZNC-KyE?t=998

"""


# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def reveal_identity(self):
#         print("My name is {}".format(self.name))
#
#
# class SuperHero(Person):
#     def __init__(self, name, hero_name):
#         super(SuperHero, self).__init__(name)
#         self.hero_name = hero_name
#
#     def reveal_identity(self):
#         print("init super")
#         super(SuperHero, self).reveal_identity()
#         print("print hero")
#         print("...And I am {}".format(self.hero_name))
#
#
# adam = Person('Adam')
# adam.reveal_identity()
#
# wade = SuperHero("Wade Wilson", "DeadPool")
# wade.reveal_identity()


"""
https://www.careerride.com/python-interview-questions.aspx
"""

#
# class upcase:
#     def __init__(self, out):
#         self._out = out
#     def write(self, s):
#         self._outfile.write(s.upper())
#     def __getattr__(self, name):
#         return getattr(self._out, name)


"""
Singleton:
https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
"""
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


# x = OnlyOne('sausage')
# print("OnlyOne('sausage')   ", x)
# y = OnlyOne('eggs')
# print("OnlyOne('eggs')      ", y)
# z = OnlyOne('spam')
# print("OnlyOne('spam')      ", z)
#
# print("x                    ", x)
# print("y                    ", y)
# print("z                    ", z)
#
# print("repr(x)              ", repr(x))
# print("repr(y)              ", repr(y))
# print("repr(z)              ", repr(z))

tuple_ex = (1,2,3,4)
_the_list = [1,2,3,4]
_the_list.append(6)
set_ex = {1,2,3,4,5}

d_dict_ob = {"1": "one", "2": "two", "3": "three", "4": "four"}
d_dict_1 = {'1': 'one', '2': 'two', '3': 'three', '4': 'four'}
d_dict_alt = dict(one = 'one')
d_dict_2 = {"3": "three"}


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


l = sorted(random.randint(0,1000) for num in range(100))


def binary_search(in_list, n):
   """
   # TODO provide doc string

   """
   for item in in_list:
       while item == n:
           return item


# binary_search(l, 35) ==


def fact(n):
    x = 1
    if n == 0:
        return x

    for i in range(n):
        x = n * i
    return x


strings_sum = "1" + "2"
print(strings_sum)

int_sum = 1 + 2
print(int_sum)

# __slots__
# d = deque()
# garbage
# factorial
# binary three
# сложность алгоритма
