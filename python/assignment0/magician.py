#magician
n=int(input("enter number of boxes:"))
x=int(input("enter box at which you want to hide coin:"))
s=int(input("enter number of swaps to perform:"))
a=[]
for i in range(n):
    if (i+1)==x:
        a.append(1)
    else:
        a.append(0)
j=0
print(a)
while j<s:
    print("swap",j+1,)
    s1=int(input("select box1:"))
    s2=int(input("select box2:"))
    temp=a[s1-1]
    a[s1-1]=a[s2-1]
    a[s2-1]=temp
    j+=1
b=0
for el in a:
    if el==1:
        print("coin is present in the box:",b+1)
        break
    b+=1