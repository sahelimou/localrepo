class Person:
    "This is person class"
    def display(self):
        print("person base class")
    
class Q(Person):
    def disp(self):
        print("this is child class")
    

q = Q()
q.disp()
q.display()
