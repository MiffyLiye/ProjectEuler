limit=500
def div(n):
    k=[]
    for i in range(1,n+1):
        if n%i==0:
            k.append(i)
    return k
def count(n):
    if n%2==0:
        p=div(int(n/2))
        q=div(n+1)
    else:
        p=div(n)
        q=div(int((n+1)/2))
    r=[]
    for i in p:
        for j in q:
            r.append(i*j)
    r.sort()
    s=[]
    s.append(r[0])
    for i in range(1,len(r)):
        if s[len(s)-1]<r[i]:
            s.append(r[i])
    s.pop()
    return len(s)
n=1
while True:
    if count(n)>=limit:
        break
    else:
        n+=1
print(int(n*(n+1)/2))
    
        
