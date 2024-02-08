test_string=input("enter the string")
# printing original string
print ("The original string is : " +  test_string)
  
# using split()
# to count words in string
res = len(test_string.split())
  
# printing result
print ("The number of words in string are : " +  str(res))
total=0
for i in test_string:
    total = total + 1
 
print("Total Number of Characters in this String = ", total)
