a,b=map(str,input().split())
c=0
for i in range(0,len(a)):
    for j in range(i,len(b)):
        if a[i]==b[j]:
            c=c+1
            #print(a[i],"==",b[j])
if c>=2:
    print("yes")
else:
    print("no")
