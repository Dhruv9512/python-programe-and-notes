n = int(input("Enter range:- "))
for a in range(1,n+1):
    l = [int(j)**3 for j in str(a)]
    if a==sum(l):
        print(a)





# i,count=1,0
# while True:
#     if count==n:
#         break
#     else:
#         l = [int(j)**3 for j in str(i)]
#         if i==sum(l):
#            print(i)
#            count+=1
#     i+=1