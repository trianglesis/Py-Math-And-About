"""
https://youtu.be/_JtPhF8MshA
"""

from examples.factorial import get_recursive_factorial

number = 5
# Factorial Inefficient
# rec_fact = get_recursive_factorial(number)
# print(rec_fact)


# Factorial efficient with "go" function:
#  Just as example where a is an accumulator or calculation step by step
def go(n, a):
    # go (n - 1) (a * n)
    while n > 0:
        a = a * n
        n = n - 1
    return a
# fact = go(number, 1)
# print(fact)


# Fib example
def fib_f(n):
    a = n - 1
    b = a + n
    return(a,b)

fib = fib_f(4)
print(fib)