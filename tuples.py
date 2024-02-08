tuple1=(456, 700, 200)
print(max(tuple1))
print(min(tuple1))
print(type(tuple1))
print(len(tuple1))
y = list(tuple1)
y[1] = "kiwi"
y.append(700)
x = tuple(y)
print(x)
fruits = ("apple", "banana", "cherry","lichi")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
mytuple = fruits * 2

print(mytuple) 
