n=int(input())
lis=[1000,500,100,50,10,1]
c=0
while n>0:
    for i in range(0,len(lis)):
        if n>=lis[i]:
            n=n-lis[i]
            c+=1
            break
print(c)
