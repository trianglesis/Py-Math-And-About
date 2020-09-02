"""
https://youtu.be/wMNrSM5RFMc

https://www.artima.com/forums/flat.jsp?forum=181&thread=75931

"""
# import math
import sys
sys.setrecursionlimit(5000)

# to_fact = 500
# print(math.factorial(to_fact))

"""
Simplest:
"""

def get_recursive_factorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * get_recursive_factorial(n-1)


def get_iterative_factorial(n):
    if n < 0:
        return - 1
    else:
        fact_step = 1
        for i in range(1, n+1):
            fact_step *= i
            print(i, fact_step)
        return fact_step


# print("get_recursive_factorial ", get_recursive_factorial(5))
# print("get_iterative_factorial ", get_iterative_factorial(5))


# def recursive_factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * recursive_factorial(n - 1)
#
#
# print(recursive_factorial(to_fact))
#
#
# def non_recurse_factorial(n):
#     ft = 1
#     while n > 0:
#         ft = ft * n
#         n = n - 1
#     return ft
#
#
# print(non_recurse_factorial(to_fact))
#
#
# def fact_recursive_1(n):
#     if n < 2:
#         return 1
#     return n * fact_recursive_1(n - 1)
#
#
# print(fact_recursive_1(to_fact))
#
#
# #  Lazy Python programmer
# def fact_recursive_2(x): return x > 1 and x * fact_recursive_2(x - 1) or 1
#
#
# print(fact_recursive_2(to_fact))
#
# #  Lazier Python programmer
# f_lam = lambda x: x and x * f_lam(x - 1) or 1
# print(f_lam(to_fact))
#
#
# def fact_lam_str(n):
#     return eval('*'.join(map(lambda x: repr(x), range(1, n + 1))))
#
#
# print(fact_lam_str(to_fact))
