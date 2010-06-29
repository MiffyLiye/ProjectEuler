N=6
limit=pow(10,N)
def f(n):
    if n%2==0:
        p=int(n/2)
    else:
        p=3*n+1
    return p
def count(n):
    t=n
    k=0
    while True:
        if t==1:
            k+=1
            break
        else:
            t=f(t)
            k+=1
    return k
s=[0]
for i in range(1,10):
    s.append(count(i))
for j in range(1,N):
    for i in range(pow(10,j),pow(10,j+1)):
        t=f(i)
        k=0
        while True:
            i=f(i)
            k+=1
            if i<pow(10,j):
                s.append(s[i]+k)
                break
u=0
n=0
for i in range(len(s)):
    if s[i]>u:
        u=s[i]
        n=i
print(n)
      
    
