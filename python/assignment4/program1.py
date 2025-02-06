t = int(input("Enter number of test cases:"))
a = []
for i in range(t):
    print("Enter case", i+1)
    s = input("Enter string:")
    a.append(s)
for i in a:
    k,count=0,0
    if i==i[::-1]:
        print(0)
    else:
        j=i[::-1]
        for k in range(len(i)):
            if j[k]!=i[k]:
                count+=1
        print(count)
