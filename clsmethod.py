class Person:
    "This is person class"
    def __init__(self,name,age):
        self.n = name
        self.a = age
    
p=Person("Raj",40)

print(getattr(p,'n'))
setattr(p,'a',23)
print(getattr(p,'a'))
print(hasattr(p,'a'))
delattr(p,'a')
print(p.n)    
    
