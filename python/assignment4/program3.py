s=input("enter string:")
for i in range(97,123):
    if s.find(chr(i))!=-1:
        flag=1
    else:
        print("not a pangram")
        flag=0
        break
if flag==1:
    print("pangram")