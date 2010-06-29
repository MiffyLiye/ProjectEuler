n=20
def C(n,m):
    t=1
    for i in range(m):
        t*=n-i
    for i in range(1,m+1):
        t/=i
    return int(t)
print(C(2*n,n))
