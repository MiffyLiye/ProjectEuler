def gcd(a,b):
    while True:
        c=a%b
        a=b
        b=c
        if c==0:
            break
    return a
def lcm(a,b):
    return int(a*b/gcd(a,b))
s=1
for i in range(2,21):
    s=lcm(s,i)
print(s)
    
