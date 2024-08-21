l=[5,2,6,5,69,4,5,2,5]

n = int(input("Enter a key to find it's indexes:- "))
index=[ind for  ind,i in enumerate(l) if i==n ]
if sum(index)==0:
    print("Enter element is not in list....")
else:
   print(index)




