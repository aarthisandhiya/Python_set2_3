a,b=map(int,input().split())
c=a^b
d=bin(c)
#print(d)
countt=0
for i in d:
    if i=='1':
        countt=countt+1 
print(countt)
