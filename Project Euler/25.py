a,b=1,1
n=2
while True:
    c=a+b
    a=b
    b=c
    n+=1
    if b>10**999:
        break
print(n)
