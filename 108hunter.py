a=int(input())
b=str(a)
k=[]
s=[]
summ=0
for i in range(0,len(b)):
    s.append(b[i])
#print(s)
k=list(map(int,s))
#print(k)
if len(k)==1:
    #print(k[0])
    print(k[0]**2)
else:
    for i in range(0,len(k)-1):
        summ=summ+(k[i]**k[i+1])
    else:
        summ=summ+(k[-1]**k[0])
    print(summ)
