sup=28124
def d(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s
list=[]
for i in range(1,sup):
    if d(i)>i:
        list.append(i)
a=[]
for i in range(sup):
    a.append(1)
for i in list:
    for j in list:
        t=i+j
        if t<sup:
            a[t]=0
s=0
for i in range(len(a)):
    if a[i]==1:
        s+=i
print(s)
