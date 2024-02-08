class cls1:
    cnt=0
    def __init__(self):
        cls1.cnt=cls1.cnt+1
        
    
c1=cls1()
c2=cls1()
c3=cls1()
print(cls1.cnt)
