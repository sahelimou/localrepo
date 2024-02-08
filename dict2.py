text = {1: "Hello", 2: "all"} 
  
text.clear() 
print('text =', text)

x = ('key1', 'key2', 'key3')
y = (10,20,30)    

thisdict = dict.fromkeys(x, y)

print(thisdict)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

print(car)

car.popitem()

print(car)

x = car.setdefault("model", "Bronco")

print(x)
print(car)    
