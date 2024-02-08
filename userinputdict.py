n=int(input("enter a number of elements in the dict: "))
my_dict = {}
for i in range (n):
      key=input("Enter name :")
      value=input("Enter phno. :")
      my_dict.update({key: value})
print(my_dict)
nm=input("enter a name")
if nm in my_dict.keys():
      print(my_dict[nm])
else:
     print("error")
