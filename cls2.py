class Person:
    "This is person class"
    def __init__(self, n, c):
        self.name=n 
        self.city=c 
    def display(self):
        print(self.name)
        print(self.city)
        
p=Person("mita","delhi")
p.age = 40
q=Person("rita","kolkata")
print(Person.__doc__)
p.display()
print(p.age)
q.display()
    
