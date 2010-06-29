r=0
for i in range(100,1000):
    for j in range(100,1000):
        s=str(i*j)
        f=[]
        e=[]
        for k in range(len(s)):
            f.append(s[k])
            e.insert(0,s[k])
        if f==e:
            if i*j>r:
                r=i*j
print(r)
            
