import numpy as np
n=int(input("enter size of array"))
a=[]
for i in range(n):
    a.append(input("enter string:"))
a=np.array(a)
rj=np.char.rjust(a,15,"_")
lj=np.char.ljust(a,15,"_")
c=np.char.center(a,15,"_")
print(rj)
print(lj)
print(c)