a=int(input())
b=[str(a) for a in input().split()]
#print(b)
b.sort()
for i in b:
    print(i.lower())
