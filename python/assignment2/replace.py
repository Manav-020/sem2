a=input("enter string:")
b=[input("enter part of string to replace:"),input("enter replaced part:")]
if len(b[0])==len(b[1]):
    c=b[0]
    d=b[1]
    z=''
    for i in a:
        for j in range(len(c)):
            if i==b[j]:
                z=z+d[j]
            else:
                z=z+i
    print("replaced string is:",z)
else:
    print("invalid operation")