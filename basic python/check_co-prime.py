a = int(input("Enter a first number:- "))
b = int(input("Enter a second number:- "))

la = [n for n in range(2,a+1) if a%n==0] 
lb = [n for n in range(2,b+1) if b%n==0] 
check=True
maxi=max(la,lb)
i=0
for  n in maxi:
    if len(min(la,lb))-1==i:
        break
    if n==lb[i]:
       check=False
       break

if check:
    print("it is a co-prime")
else:
    print("it is not a co-prime")
    