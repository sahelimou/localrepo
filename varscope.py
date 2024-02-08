x = 20
def my_func():
	x=10
	#global x
	#x=10
	print("Value inside function:",x)
	
	#print("access the global value:",x)


my_func()
print("Value outside function:",x)
