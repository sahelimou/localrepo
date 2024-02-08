class Emp:
    def __init__(self,name,id1,addr):
        self.name=name
        self.id1=id1
        self.addr=addr

    def display(self):
        print(self.name)
        print(self.id1)
        print(self.addr)

emp1=Emp('riya',56,'1ABC')
emp2=Emp('rani',75,'2CDE')
emp1.display()
emp2.display()
emp1.age=23
print(emp1.age)
 
