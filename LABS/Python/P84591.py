def absValue(x):
    if x>=0:
        return x
    else:
        return -x

def power(x, p):
    return x**p

def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True

def slowFib(n):
    if n <= 1:
        return n
    else:
        return slowFib(n-1) + slowFib(n-2)

def quickFib(n):
    a = 0
    b = 1
    for i in range(0,n):
        a, b = b, b+a
    return a
