a=int(input())
c=0
b=[int(a) for a in input().split()]
for i in range(0,len(b)-1):
    if i%2==1 and b[i]>b[i-1]:
        c=c+1 
    elif i%2==0 and b[i]<b[i+1]:
        c=c+1
#print(c)
if c==a-1:
    print("yes")
else:
    print("no")
