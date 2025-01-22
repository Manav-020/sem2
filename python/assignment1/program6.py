i=0
b=[]
while i<4:
    print("enter point ",i+1)
    x=int(input("enter x:"))
    y=int(input("enter y:"))
    z=int(input("enter z:"))
    a=(x,y,z)
    b.append(a)
    i+=1
i=0
q=[]
while i<4:
    t=b[i]
    min=1000000000
    j=3
    while j>=0:
        if(j==i):
            j-=1
            continue
        else:
            h=b[j]
            d=(t[0]-h[0])**2 + (t[1]-h[1])**2 +(t[2]-h[2])**2
            if d<min:
                min=d
                k=j
            j-=1
    q.append({b[i],b[k]})
    i+=1
print(q) 


