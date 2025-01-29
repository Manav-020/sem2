a=input("enter string:")
b=a[0]

for i in range(1,len(a)):
    if i%2!=0:
        c=a[i:i+1]
        d=c.capitalize()
        b=b+d
    else:
        b=b+a[i]
print(b)
    