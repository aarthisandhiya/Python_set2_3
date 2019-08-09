a,b=map(str,input().split())
lis=[]
for i in range(len(b)):
    for j in range(len(a)):
        if b[i]==a[j] and a[j] not in lis:
            lis.append(b[i])
#print(lis)
print("".join(list(lis)))
