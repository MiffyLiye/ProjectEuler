def fine(a,b,c):
    if a**2+b**2==c**2:
        return 0
    else:
        return 1
s=1000
for a in range(1,334):
    b=a+1
    while True:
        c=s-a-b
        if fine(a,b,c)==0:
            print(a*b*c)
            break
        else:
            b+=1
        if b>667:
            break

