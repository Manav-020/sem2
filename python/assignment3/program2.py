def check(x=0):
    a,b,flag=0,1,0 
    c=a+b
    while x>=c:
        a=b
        b=c
        if x==c:
            flag=1
            print("its fibo")
            break
        c=a+b
    if(flag==0):
        print("notfibo")
a=[]
t=int(input("enter number of test cases:"))
for i in range(t):
    b=int(input("enter number:"))
    a.append(b)
for i in range(t):
    check(a[i])
