import math
limit=2000000
p=[2,3]
while True:
    i=p[len(p)-1]+2
    while True:
        sqrt=math.sqrt(i)
        win=1
        for j in range(len(p)):
            if i%p[j]==0:
                win=0
                break
            if p[j]>sqrt:
                break
        if win==1:
            p.append(i)
            break
        else:
            i+=1
    if p[len(p)-1]>=limit:
        break
s=0
for i in range(len(p)-1):
    s+=p[i]
print(s)
