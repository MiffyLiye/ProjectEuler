import datetime
d0=datetime.date(1900,1,7)
s=0
for i in range(1901,2001):
    for j in range(1,13):
        d=datetime.date(i,j,1)
        t=d-d0
        if t.days%7==0:
            s+=1
print(s)
