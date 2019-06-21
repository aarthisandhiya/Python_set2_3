a=int(input())
d=[]
c=0
for i in range(0,a):
    s=input()
    d.append(s)
lis=[]
dictt={}
e={}
word=['a','e','i','o','u','A','E','I','O','U']
for i in range(0,len(d)):
    f=d[i]
    for j in range(0,len(f)):
        for k in range(0,len(word)):
            if f[j]==word[k]:
                c=c+1
    dictt.update({f:c})      
    c=0
#print(dictt)
for i ,k in dictt.items():
    lis.append(i)
print(lis)
for i in lis:
    print(i)
r=lis[::-1]
#print(r)

#print(sorted(dictt,reverse=True))
#print(e)
