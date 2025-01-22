n=[]
i=0
while i<10:
    print("enter name of student ",i+1,end=":")
    b=input()
    if len(b)>15:
        z=b[14:0:-1]
        n.append(z)
    else:
        n.append(b[::-1])
    i+=1
for l in n:
    print("name of student ",l)
