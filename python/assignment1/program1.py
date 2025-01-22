a=[]
b=[]
c=[]
i=0
while i<51:
    a.append(i)
    b.append(i**2)
    i+=1
g=97
i=1
while g<=122:
    c.append(chr(g)*i)
    i+=1
    g+=1
print(a)
print(b)
print(c)