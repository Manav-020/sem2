t=int(input("enter number of test cases:"))
c=[]
for i in range(t):
    print("for case",i+1)
    a=int(input("enter start value:"))
    b=int(input("enter stop value:"))
    c.append((a,b))
for i in range(t):
    d=c[i]
    count=0
    for j in range(0,d[1]+1):
        if j**2>d[1]:
            exit
        if j**2>=d[0] and j**2<=d[1]:
            count+=1
    print(count)