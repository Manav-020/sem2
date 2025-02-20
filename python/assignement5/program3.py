from itertools import permutations
q = int(input("enter test cases:"))
for i in range(q):
    s = input("enter string:")
    if s == s[::-1]:
        print("no answer")
    else:
        x = ["".join(p) for p in list(permutations(s))]
        x.sort()
        index = x.index(s)
        print(x[index+1])