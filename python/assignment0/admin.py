c=int(input("enter number of party members:"))
i=0
x=[]
y=[]
print("enter tag of party members")
while i<c:
    b=int(input("enter tag:"))
    x.append(b)
    y.append(b)
    i+=1
count=0
i=0
y.sort()
while i<c:
    t=tuple(x)
    z=t.index(y[c-1-i])
    if x[c-1-i]!=y[c-1-i]:
        x[z],x[c-1-i]=x[c-1-i],x[z]
        count+=1
    i+=1
print(count)     


    