school="Rai high school"
print(school)
rai={}
a_no=0
s_no=0
c_no=0
i=0
while i<10:
  id1=input("enter student id")
  nm=input("enter student name")
  cls=input("enter student class")
  sec=input("enter student section")
  roll=input("enter student roll")
  strm=input("enter student stream")
      
  rai[id1]=[nm,cls,sec,roll,strm]
  i+=1
print("rai",end=" ")    
print(rai)    
sorted_val=sorted(rai.values())
chak={}
for i in sorted_val:
    for k in rai.keys():
        if rai[k] == i:
            chak[k] = rai[k]
            break
print("chakrabarty",end=" ")  
print(chak)

ch11={}
for k in rai.keys():
        if rai[k][1] == '11':
            ch11[k]= rai[k]
print("ch11",end=" ")            
print(ch11)
ch12={}
for k in rai.keys():
        if rai[k][1] == '12':
            ch12[k]= rai[k]
print("ch12",end=" ")            
print(ch12)
no_student=len(ch11.keys())
no_student1=len(ch12.keys())
print("no of student in class 11")
print(no_student)
print("no of student in class 12")
print(no_student1)
for k in ch11.keys():
     if ch11[k][4] == 'Arts':
       a_no+=1
     elif ch11[k][4] == 'Science':
         s_no+=1
     else:
         c_no+=1
   
print("Arts Science  Commerce   of class11")
print(a_no,end="    ")
print(s_no,end="            ")
print(c_no)
for k in rai.keys():
    if rai[k][4] == 'Commerce':
      name=rai[k][0]
      print(name.upper(),end=",")
      print(rai[k][1],end=",")
      sec=rai[k][2]
      print(sec.upper(),end=",")
      print(rai[k][3])

for k in rai.keys():
  if rai[k][4] == 'Arts':
     rai[k][2] = 'G'
print(rai)
    
