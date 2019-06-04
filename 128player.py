a=int(input())
prod=1
b=[int(a) for a in input().split()]
if len(b)==1:
    if b[0]%2==0:
        print("even")
    elif b[0]%2==1:
        print("odd")
else:
    if len(b)>1:
        for i in range(0,len(b)):
            prod=prod*b[i]
        if prod%2==0:
            print("even")
        elif prod%2==1:
            print("odd")
