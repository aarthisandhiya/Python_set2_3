a=int(input())
b=[int(a) for a in input().split()]
for i in range(0,len(b)-1):
    j=i+1 
    if b[j]<b[i]:
        print(b[j],end=" ")
    else:
        print("-1",end=" ")
else:
    if b[-1]<b[0]:
        print(b[-1])
    else:
        print("-1")
        
