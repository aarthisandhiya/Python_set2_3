a=input()
minn=0
lis=[]
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        s=a[i:j+1]
        k=s[::-1]
        #print(s)
        #print(k)
        if s==k:
            #print(len(s))
            #print(len(k))
            lis.append(len(a)-len(k))
print(min(lis))
