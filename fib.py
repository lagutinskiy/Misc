def fib(n):
    total = 0
    if n < 0:
        total = 0
    elif n == 1:
        total = 1
    else:
        total = fib(n-2) + fib(n-1)
    return total

print(fib(35))
