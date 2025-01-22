r0=[]
r1=[]
r2=[]
r3=[]
r4=[]
comp=[]
for i in range(1,10001):
    if i%5==0:
        r0.append(i)
    elif i%5==1:
        r0.append(i)
    elif i%5==2:
        r0.append(i)
    elif i%5==3:
        r0.append(i)
    elif i%5==4:
        r0.append(i)
    comp.append(i)
if comp==(r0+r1+r2+r3+r4):
    print("equivalence if valid")
else:
    print("equivalance is not valid")
