t=int(input("enter number of test cases:"))
k=input("enter cases:")
b=k.split(" ")
print(b)
for i in range(t):
    if(int(b[i])%2==0):
        print("maximum possible peieces for cuts ",int(b[i])," are:",((int(b[i])/2)**2))
    else:
        c=(int(b[i])+1)/2
        print("maximum possible peieces for cuts ",int(b[i])," are:",c*(c-1))
