def f(n):
    t=0
    for k in range(1,n):
        if (10**k-1)%n==0:
            t=k
            break
    return t
k=0
d=1
for i in range(1,1001):
    t=f(i)
    if t>k:
        d=i
        k=t
print("d=",d,"k=",k)
