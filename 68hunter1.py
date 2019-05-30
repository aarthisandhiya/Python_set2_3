a=int(input())
b=[int(a) for a in input().split()]
s=min(b)
k=max(b)
for i in range(0,len(b)):
    if b[i]==s:
        print(i+1,end=" ")
for i in range(0,len(b)):
    if b[i]==k:
        print(i+1,end=" ")
