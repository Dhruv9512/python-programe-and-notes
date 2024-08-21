def sec_lowest_score_index(score,name):
        winner=min(score)
        for v in range(0,score.count(winner)):
            name.pop(score.index(winner))
            score.remove(winner)
        second=min(score)    
        sec_score_list=[name[i] for i,v in enumerate(score) if v==second]     
        return sorted(sec_score_list)
         
name,score=[],[]
for _ in range(int(input("Enter length:- "))):
    name.append(input("Enter name:- "))
    score.append(float(input("Enter score:- ")))

for v in sec_lowest_score_index(score,name) :
    print(v)

