c=input("enter string:")
s=input("enter subsrting you want to check:")
flag=0
a=int(input("enter start value:"))
b=int(input("enter end value:"))
if a<b :
    if a>=0 and b<len(c):
        for i in range(b,a-1,-1):
            z=''
            for j in range(len(s),0,-1):
                z=z+(c[i-j])
            if z==s:
                flag=1
                print("found at index",i-len(s))
                break
            if a>=0 and b>=len(c):
                for j in range(len(s),0,-1):
                    z=''
                    for j in range(1,len(s)+1):
                        z=z+(c[i-j])
                    if z==s:
                        flag=1
                        print("found at index",i-len(s))
                        break
if flag==0:
    print("subsrting not found")
