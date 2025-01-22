#to find the factorial of 2 number
n=int(input("enter number:"))
i=1
p=1
while i<=n:
    p*=i
    i+=1
print("factorail of number",n,"is",p)