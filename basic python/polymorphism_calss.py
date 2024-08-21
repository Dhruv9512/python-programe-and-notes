class add:
    def __init__(self,v):
        self.value=v;
       
    
    
    def display(self):
        print("The value is:- ",self.value)


    def __add__(self,y):
       
        new_value=self.value + y.value
        return add(new_value)
    
   
    

v1=add(5)
v2=add(5)
# v1.display()
v3=v1+v2
ans = v3.display()



