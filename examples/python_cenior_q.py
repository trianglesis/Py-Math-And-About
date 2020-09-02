"""
https://github.com/MaximAbramchuck/awesome-interview-questions#python
"""


class C:
  dangerous = 2


c1 = C()
c2 = C()
print("c1.dangerous {}".format(c1.dangerous))

c1.dangerous = 3
print("c1.dangerous {}".format(c1.dangerous))
print("c2.dangerous {}".format(c2.dangerous))

del c1.dangerous
print("c1.dangerous {}".format(c1.dangerous))

C.dangerous = 3
print("c2.dangerous {}".format(c2.dangerous))


list_ = ['a', 'b', 'c', 'd', 'e']
print(list_[:10])