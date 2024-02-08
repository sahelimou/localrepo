import math
n=int(input("enter the second"))
s=60
m=n/s
s=n%s
h=m/60
m=m%60
print(math.floor(h),"")
print(math.floor(m),"")
print(math.floor(s))
