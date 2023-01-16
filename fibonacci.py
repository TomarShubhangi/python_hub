"""Q15.WAP in python to define a module to find fibbonacci series
& saves and import the module to another program"""
# Fibonacci numbers module
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end =" ")
        a, b = b, a+b
    print()
