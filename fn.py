def greet1(name,grt):    
    print(name+grt)

def greet(name,msg="Good morning!"):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + msg)
def greetmulti(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)

greet1('madhu','hi')
greet('Paul')
greet("Bruce", "How do you do?")
greet(msg = "How do you do?",name = "Bruce")
greetmulti("Monica", "Luke", "Steve", "John")     
greetmulti("Monica")          


print(greet.__doc__)
