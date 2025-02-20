l=int(input("enter start value:"))
r=int(input("enter end value:"))
max=0
for i in range(l,r+1):
    for j in range(l,r+1):
        if(max<i^j):
            max=i^j
print("maximum value of xor is:", max)