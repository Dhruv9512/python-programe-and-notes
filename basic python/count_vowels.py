str = input("Enter a string:- ")

def check(str):
    for n in str:
        if not n>='A' and n<='z':
            return False
    return True

#          -------------   1 method ------------------
if check(str):
    count=1
    for n in str:
        if (n=='a'or n=='A') and (n=='e'or n=='E') and (n=='i'or n=='I')and (n=='o'or n=='O') and (n=='u'or n=='U'):
            count+=1
                              
    print(count)  
else:
    print("Invalid value.....")   





                              
        