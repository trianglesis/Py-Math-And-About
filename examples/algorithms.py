import time
import random
"""
https://youtu.be/zeULw-a7Mw8
"""


# Making case:
def timing_dec(func):

    def wrapper(*args):
        ts = time.time()
        print("Time start: ", ts)
        result = func(*args)
        te = time.time()
        print("Time end:   ", te)
        print("Time spent: {} func: {}".format((te - ts) * 1000, func.__name__))
        return result
    return wrapper


the_list = [x for x in range(1, 100000000)]
# the_list = sorted(random.randint(0, 1000) for num in range(100000000))


# Linear Search:
@timing_dec
def linear_search(data_list, search_item):
    """
    Time spent: 3.9975643157958984 func: linear_search
    Is in list: True index: 4999 item: 5000
    """
    for i in range(len(data_list)):
        if data_list[i] == search_item:
            return "Is in list: {} index: {} item: {}".format(True, i, search_item)
    return False, None


print(" <====> Start linear search <====>")
run_search = linear_search(the_list, 5000)
print(run_search)


# Binary search
@timing_dec
def binary_search(data_list, search_item):

    start = 0
    end = len(data_list) - 1  # Important

    while start <= end:
        middle = (start + end) // 2  # integer division - result rounded int
        if search_item == data_list[middle]:
            return "Is in list: {} index: {} item: {}".format(True, middle, search_item)
        elif search_item < data_list[middle]:
            end = middle - 1  # Remove from middle to the end (search in left direction)
        else:
            start = middle + 1  # Remove from middle to the start (search in right direction)
    return False


print(" <====> Start binary_search search <====>")
run_bin_search = binary_search(the_list, 5000)
print(run_bin_search)


# Recursive binary search
def binary_search_recursive(time_start, data_list, search_item, start, end):
    if start > end:
        return False
    else:
        middle = (start + end) // 2
        if search_item == data_list[middle]:
            time_sp = (time.time() - time_start) * 1000
            return "Is in list: {} index: {} item: {} TS: {}".format(True, middle, search_item, time_sp)
        elif search_item < data_list[middle]:
            return binary_search_recursive(time_start, data_list, search_item, start, middle-1)
        else:
            return binary_search_recursive(time_start, data_list, search_item, middle+1, end)


print(" <====> Start binary_search_recursive search <====>")
run_binary_search_recursive = binary_search_recursive(time.time(), the_list, 5000, 0, len(the_list) - 1)
print(run_binary_search_recursive)
