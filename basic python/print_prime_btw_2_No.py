a = int(input("first number:- "))
b = int(input("second number:- "))


# while a<b:
#     i=2
#     while i<a:
#         if a%i==0:
#             a+=1   
#             i=1  
#         if a>b:
#             break
#         i+=1
#     else:
#         print(a)
#         a+=1
 
 
 
#-------------------- Best way --------------------------     
def prime(n):
    for a in range(2,n):
        if n%a==0:
            return False
    return True

l=[ n for n in range(a,b+1) if prime(n)]
print(l)
        
       
   