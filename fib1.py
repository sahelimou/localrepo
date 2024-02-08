fib=(0,)
n=int(input('Please enter a number '))
a,b=0,1
for i in range(n):
 a, b = b, a+b
 fib=fib+(a,)
print(fib)     
