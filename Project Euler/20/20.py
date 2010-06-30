def fac(n):
    t=1
    for i in range(1,n+1):
        t*=i
    return t
b=str(fac(100))
t=0
for i in b:
    t+=int(i)
print(t)
