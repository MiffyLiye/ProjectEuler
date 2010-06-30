a,b,s=1,2,0
s+=b
while True:
    c=a+b
    a=b
    b=c
    if b>4000000:
        break
    elif b%2==0:
        s+=b
print(s)
