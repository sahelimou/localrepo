thisdict =	{
  "brand": "Maruti",    
  "model": "zen",    
  "colour": "red",    
  "year": 1990    
}
print(thisdict)
x=thisdict.get("brand")
print(x)
thisdict["model"]=800
x=thisdict["model"]    
print(x)    
for x in thisdict:    
  print(x)     
for x in thisdict.values():    
  print(x)     
for x, y in thisdict.items():    
  print(x, y)     
if "brand" in thisdict:    
  print("Yes, 'brand' is one of the keys in the thisdict dictionary")
  thisdict["price"] = 600000
print(thisdict)
thisdict.pop("model")    
print(thisdict)
thisdict.popitem()    
print(thisdict)
mydict = dict(thisdict)       
print(mydict)    
