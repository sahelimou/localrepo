list1=["rose","lotus","jasmine","tulip"]
print(type(list1))
print(list1[1])
print(list1[-2])    
print(list1[2:4])
print(list1[-3:-1])    
print(list1[:3])    
print(list1[2:])
print(list1[:])
list2=["lotus","rose",1,3,4,7,9];
print(list2[1:6:2])
print(list1==list2)
list1[3]="sunflower"
for x in list1:    
    print(x)
print("rose" in list1)
print(len(list1))
print(list2*2)
list3=list1+list2
print(list3)
#l1=[x for x in list1 if "rose" in x]
#l2=[x for x in list1]
#l3=[x for x in range(10) if x < 10]

#if "rose" in list1:
#    print("rose exist in the list")    
list1.append("tulip")    
print(list1)
  
list1.insert(4,"merrygold")
print(list1)
list1.remove("merrygold")
print(list1)
#mylist=list(list1)
#print(mylist)
#list1.extend(list2)
#print(list3)
list3.pop()
print(list3)
print(list1)
del list1
list1.clear()
