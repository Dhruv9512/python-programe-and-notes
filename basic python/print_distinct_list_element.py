l = [2,5,5,3,9,8,8]
dic={}
# disc={n:l.count(n) for n in l}

# print(disc)




for e in l:
    if e in dic:
       dic[e]+=1
    else:
        dic[e]=1

print(dic)