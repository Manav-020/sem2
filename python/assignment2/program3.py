t=int(input("enter number of test cases:"))
n=[]
i=0
while i<t:
    x=int(input("enter number:"))
    n.append(x)
    i+=1
i=0
while i<t:
    count=0
    z=n[i]
    while z!=0:
        b=z%10
        if b==0:
            z=int(z/10)
            continue
        elif n[i]%b==0:
            count+=1
        z=int(z/10)
    print(count,"digits in number",n[i],"exactly divides number",n[i])
    i+=1
    


