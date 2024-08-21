class student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name=name
        self.marks1=int(marks1)
        self.marks2=int(marks2)
        self.marks3=int(marks3)
    
    @property
    def print_AVG(self):
        print(self.name)
        print(f"The average of {self.marks1},{self.marks2} and {self.marks3} is:- {round(self.marks1+self.marks2+self.marks3/3)}")
    
    @print_AVG.setter
    def print_AVG(self,value):
        name = value.split("of")[1]
        self.marks1=int(name.split(",")[0])
        name = name.split(",")[1]
        self.marks2=int(name.split("and")[0])
        name = name.split("and")[1]
        self.marks3 = int(name.split("is")[0])
   
        

s1 = student("Dhruv sharma",25,26,28)

s1.print_AVG="The average of 10,20 and 30 is:- ?"
s1.print_AVG

