def fac(n):
    t=1
    for i in range(1,n+1):
        t*=i
    return t
limit=1000000
L=[0,1,2,3,4,5,6,7,8,9]
u=limit-1
t=limit-1
p=[]
for i in range(1,10):
    u=t//fac(10-i)
    t=t%fac(10-i)
    p.append(u)
for i in range(len(p)):
    print(L[p[i]],end='')
    L.pop(p[i])
print(L[0])
