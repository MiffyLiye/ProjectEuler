def count(n):
    p=[0,3,3,5,4,4,3,5,5,4,
       3,6,6,8,8,7,7,9,8,8]
    q=[0,3,6,6,5,5,5,7,6,6]
    s=0
    t=n
    if n>=100:
        u=n//100
        t=n%100
        s+=p[u]+7
        if t!=0:
            s+=3
            if t<20:
                s+=p[t]
            else:
                u=t//10
                t=t%10
                s+=q[u]+p[t]
    else:
        if t<20:
            s+=p[t]
        else:
            u=t//10
            t=t%10
            s+=q[u]+p[t]
    return s
s=0
for i in range(1,1000):
    s+=int(count(i))
s+=11
print(s)
