import random
i=0
b=[]
while i<10:
    b.append(random.randint(0,1))
    i+=1
count,i=0,0
print(b)
c=[]
while i<9:
    if b[i]==0:
        count+=1
        if b[i+1]==1:
            c.append(count)
            count=0
    i+=1
c.sort()
print(c)
print("longest string of zeros is",c[len(c)-1])
