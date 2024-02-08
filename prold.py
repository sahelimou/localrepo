school="Rai high school"
print(school)
rai={}
ch1={}
ch2={}
a_no=0
s_no=0
c_no=0
i=0
while i<3:
  id1=input("enter student id")
  nm=input("enter student name")
  cls=input("enter student class")
  sec=input("enter student section")
  roll=input("enter student roll")
  strm=input("enter student stream")
  if cls == '11':
      ch1[id1]=[nm,cls,sec,roll,strm]
      if strm == 'arts':
        a_no+=1
      if strm == 'science':
        s_no+=1
      if strm == 'commerce':
        c_no+=1
        
  if cls == '12':
      ch2[id1]=[nm,cls,sec,roll,strm]
    
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

  
#print(ch11)
#print(ch12)
ch11={}
for k in rai.keys():
        if rai[k][1] == '11':
            ch1[k]= rai[k]
print("ch11",end=" ")            
print(ch1)
ch12={}
for k in rai.keys():
        if rai[k][1] == '12':
            ch2[k]= rai[k]
print("ch12",end=" ")            
print(ch2)
no_student=len(ch11.keys())
no_student1=len(ch12.keys())
print("no of student in class 11")
print(no_student)
print("no of student in class 12")
print(no_student1)
for k in ch1.key():
     if ch1[k][4] == 'arts':
       a_no+=1
       elif ch1[k][4] == 'science':
         s_no+=1
         else:
           c_no+=1
   
print("Arts Science  Commerce")
print(a_no)
print(s_no)
print(c_no)
