a=int(input("Enter a number to print odd number:- "))
b=input("Enter which number you want odd or even:- ")

i=1
if b=="odd":
    while  i<=a*2:
   
        if not i%2==0:
           print(i)
        i+=1
else:
    while i<=a*2:
        if  i%2==0:
            print(i)
        i+=1 
