thisset = {"apple", "banana", "cherry"}    
print(thisset)     
print("banana" in thisset)    
thisset.add("mango")    
print(thisset)
thisset.update(["orange","lichi"])
print(thisset)
thisset.remove("banana")
print(thisset)
thisset.discard("banana")
print(thisset)


thisset.clear()    

print(thisset)
set1 = {"a", "b" , "c"}    
set2 = {1, 2, 3}    

set3 = set1.union(set2)    
print(set3)      

