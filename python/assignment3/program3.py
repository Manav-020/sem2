t=int(input("enter test cases:"))
n=[]
for i in range(t):
    b=int(input("enter cycle count:"))
    n.append(b)
for i in n:
    height=1
    for j in range(0,i):
        if(j%2!=0):
            height+=1
        if(j%2==0):
            height=height*2
    print(height)
if(t==0):
    print(height)
