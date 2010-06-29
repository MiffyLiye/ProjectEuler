a=600851475143
i=2
while True:
    if a!=1:
        if a%i==0:
            a/=i
        else:
            i+=1
    else:
        break
print(i)
