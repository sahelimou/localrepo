
def make_fibonacci(n):
    fib = []
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        fib.append(a)
        return tuple(fib)
    

tuple1=()
tuple1=make_fibonacci(5)
print(tuple1)
