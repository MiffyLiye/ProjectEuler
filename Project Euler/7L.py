limit=10001
p=[2,3]
while True:
    i=p[len(p)-1]+2
    while True:
        win=1
        for j in range(len(p)):
            if i%p[j]==0:
                win=0
                break
        if win==1:
            p.append(i)
            break
        else:
            i+=1
    if len(p)==limit:
        break
print(p[len(p)-1])
