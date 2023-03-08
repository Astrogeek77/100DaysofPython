# # print("Hello world")

# name = "gautam"

# print(name[0:-4])

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    return n * factorial(n-1)


def fib(n):
    if (n == 0):
        return 0
    elif (n <= 2):
        return 1
    return fib(n-1) + fib(n-2)


n = 3
print(f"Factorial of {n} is {factorial(n)}")
print(f"Fibonacci series till {n} is", end=": ")

for i in range(0, n+1):
    print(fib(i), end=", ")

# s = {1: 2}
# print(type(s))

s1 = {1: 2, 3: 2, 5: 2}
s2 = {2: 2, 4: 2}

s1.update(s2)
sorted(s1)
print("\n", sorted(s1))
