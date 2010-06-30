limit=10000
def d(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s
list=[]
for i in range(limit):
    list.append(1)
for i in range(1,limit):
    t=d(i)
    if i==d(t) and i!=t:
        list[i]=0
        if i<limit:
            list[t]=0
s=0
for i in range(limit):
    if list[i]==0:
        s+=i
print(s)
