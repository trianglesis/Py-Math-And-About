"""
https://www.toptal.com/python/interview-questions
"""
# import aiohttp as aiohttp

"""
Example 1: 
Many will mistakenly expect list1 to be equal to [10] and list3 to be equal to ['a'], thinking that the list 
argument will be set to its default value of [] each time extendList is called.
"""

# def extendList(val, list=[]):
#     print(val)
#     list.append(val)
#     return list
#
#
# list1 = extendList(10)
# list2 = extendList(123, [])
# list3 = extendList('a')
#
# print("list1 = %s" % list1)
# print("list2 = %s" % list2)
# print("list3 = %s" % list3)

"""
Example 2: 
The reason for this is that Python s closures are late binding. 
Finally, the easiest fix may be to simply replace the return values [] with ():

def multipliers():
  return (lambda x : i * x for i in range(4))
"""

#
# def multipliers():
#     return [lambda x : i * x for i in range(4)]
#
# print([m(1) for m in multipliers()])
# print([m(2) for m in multipliers()])
# print([m(4) for m in multipliers()])


"""
Example 3: 
Finally, if the value is then changed in the Parent (for example, when we execute the statement Parent.x = 3), 
that change is reflected also by any children that have not yet overridden the value 
(which in this case would be Child2). That s why the third print statement outputs 3 2 3.
"""

# class Parent(object):
#     x = 1
#
# class Child1(Parent):
#     pass
#
# class Child2(Parent):
#     pass
#
#
# print(Parent.x, Child1.x, Child2.x)
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x)

"""
Example 4: 
Finally, if the value is then changed in the Parent (for example, when we execute the statement Parent.x = 3), 
that change is reflected also by any children that have not yet overridden the value 
(which in this case would be Child2). That s why the third print statement outputs 3 2 3.
"""

# def div1(x,y):
#     print("%s/%s = %s" % (x, y, x/y))
#
# def div2(x,y):
#     print("%s//%s = %s" % (x, y, x//y))
#
# div1(5,2)
# div1(5.,2)
# div2(5,2)
# div2(5.,2.)

"""
https://docs.python.org/3/whatsnew/2.2.html#pep-238-changing-the-division-operator
Py 2.7:

5/2 = 2
5.0/2 = 2.5
5//2 = 2
5.0//2.0 = 2.0

Py 354:
5/2 = 2.5
5.0/2 = 2.5
5//2 = 2
5.0//2.0 = 2.0

"""

"""Example 5:
does NOT create a list containing 5 distinct lists; rather, it creates a a list of 5 references to the same list
"""

# ex_list = [ [ ] ] * 5
# print(type(ex_list))
# print(ex_list)
# print("=====")
#
# print(ex_list[0])
# ex_list[0].append(10)
# print(ex_list[0])
# print(ex_list)
# print("=====")
#
# print(ex_list[1])
# ex_list[1].append(20)
# print(ex_list[1])
# print(ex_list)
# print("=====")
#
# ex_list.append(30)
# print(ex_list)


"""Example 6:
(a) even numbers, and
(b) from elements in the original list that had even indices

The expression works by first taking the numbers 
that are at the even indices, and then filtering out all the odd numbers.
"""
#          0  1  2  3   4   5   6   7   8
# ex_list = [1, 3, 5, 8, 10, 13, 18, 36, 78]
# print(ex_list[::2])
# print(ex_list[::3])
#
# print("ex_list[::2] ", [x for x in ex_list[::2] if x % 2 == 0])
# print("ex_list ", [x for x in ex_list if x % 2 == 0])


"""Example 7:
Actually, the code shown will work with the standard dictionary object in python 2 or 3 that is normal behavior. 
Subclassing dict is unnecessary. 
However, the subclass still won t work with the code shown because __missing__ returns 
a value but does not change the dict itself:

But since version 2.5, a defaultdict object has been available in the collections module (in the standard library.)

"""


# class DefaultDict(dict):
#     # def __missing__(self, key):
#     #     return []
#     def __missing__(self, key):
#         newval = []
#         self[key] = newval
#         return newval
#
#
# d = DefaultDict()
# d['florp'] = 127
# print(d)


"""Example 8:
A good answer would suggest a specific async mock library and async test case approach, including an ephemeral event 
loop that's guaranteed to terminate (i.e. with a max number of steps before timeout.)

A great answer would point out that synchronisation problems are fundamentally the same in synchronous and asynchronous 
code, the difference being preemption granularity.

A beautiful answer would take into account that the above code only has one flow (easy) compared to some other code 
where flows are mixed (e.g. merging two streams into one, sorting, etc). 
For example, consider following upgrade to the given code:
"""


# async def logs(cont, name):
#     conn = aiohttp.UnixConnector(path="/var/run/docker.sock")
#     async with aiohttp.ClientSession(connector=conn) as session:
#         async with session.get("http://xx/containers/{cont}/logs?follow=1&stdout=1") as resp:
#             async for line in resp.content:
#                 print(name, line)
#
#
# keep_running = True
#
#
# async def logs_n(cont, name):
#     conn = aiohttp.UnixConnector(path="/var/run/docker.sock")
#     async with aiohttp.ClientSession(connector=conn) as session:
#         async with session.get("http://xx/containers/{cont}/logs?follow=1&stdout=1") as resp:
#             async for line in resp.content:
#                 if not keep_running:
#                     break
#                 print(name, line)

"""Example 9:

Write a function that prints the least integer that is not present in a given list and cannot be 
represented by the summation of the sub-elements of the list.

E.g. For a = [1,2,5,7] the least integer not represented by the list or a slice of the list is 4, 
and if a = [1,2,2,5,7] then the least non-representable integer is 18.
"""