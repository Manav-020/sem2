def digitalroot(x):
    while x>=10:
        sum=0
        n=x
        while n!=0:
            b=n%10
            sum+=b
            n=int(n/10)
        x=sum
    print("digital root of above number is:",x)

x=int(input("enter number:"))
digitalroot(x)