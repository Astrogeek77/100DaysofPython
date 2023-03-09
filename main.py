from functools import reduce
import random

# # print("Hello world")

# name = "gautam"

# print(name[0:-4])

# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     return n * factorial(n-1)


# def fib(n):
#     if (n == 0):
#         return 0
#     elif (n <= 2):
#         return 1
#     return fib(n-1) + fib(n-2)


# n = 3
# print(f"Factorial of {n} is {factorial(n)}")
# print(f"Fibonacci series till {n} is", end=": ")

# for i in range(0, n+1):
#     print(fib(i), end=", ")

# # s = {1: 2}
# # print(type(s))

# s1 = {1: 2, 3: 2, 5: 2}
# s2 = {2: 2, 4: 2}

# s1.update(s2)
# sorted(s1)
# print("\n", sorted(s1))

# n = 100
# mylist = [random.randrange(1, n, 1) for i in range(10)]

# print("-" * 30)
# print("My List: ", mylist)
# print("-" * 30)

# accumulateList = reduce(lambda x, y: x + y, mylist)
# print("Accumulate List Sum: ", accumulateList)
# print("-" * 30)

# doubleList = list(map(lambda x: x * 2, mylist))
# print("Doubled List: ", doubleList)
# print("-" * 30)

# evenList = list(filter(lambda x: x % 2 == 0, mylist))
# print("Even List: ", evenList)
# print("-" * 30)

# oddList = list(filter(lambda x: x % 2 == 1, mylist))
# print("Odd List: ", oddList)
# print("-" * 30)

import logging


def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(
            f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        print(f"{func.__name__} returned {result}")
        return result
    return decorated


@log_function_call
def add(a, b):
    print(a + b)
    # return a + b


add(1, 2)
