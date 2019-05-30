a,b=map(int,input().split())
s=[]
c=0
for i in range(0,a):
    e=input()
    s.append(e)
for i in range(0,len(s)-1):
    for j in range(1,len(s)):
        if str(s[i])==str(s[j]):
            c=c+1 
    if c==b-1:
        print("yes")
        break
else:
    print("no")
