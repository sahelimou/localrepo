class Student:
    def __init__(self,student_name,marks):
        self.student_name=student_name
        self.marks=marks
s=Student('ravi',80)
print(s.student_name)
print(s.marks)
s.marks=75
print(s.marks)
    
    
