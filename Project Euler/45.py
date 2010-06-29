import math
def H(n):
    return n*(2*n-1)
def iH(x):
    d=1+8*x
    if sq(d)==1:
        return 0
    else:
        t=(1+int(math.sqrt(d)))
        if t%4==0:
            return t//4
        else:
            return 0
def P(n):
    return n*(3*n-1)//2
def iP(x):
    m=(1+int(math.sqrt(1+24*x)))//6
    if P(m)==x:
        return 0
    else:
        return 1
def T(n):
    return n*(n+1)//2
def iT(x):
    m=(-1+int(math.sqrt(1+8*x)))//2
    if T(m)==x:
        return 0
    else:
        return 1
limit=3
s=0
n=0
while True:
    n+=1
    if iP(H(n))==0 and iT(H(n))==0:
        s+=1
    if s>=limit:
        break
print(H(n))

