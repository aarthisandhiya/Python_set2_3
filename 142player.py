a,b=map(int,input().split())
s=[]
c=0
for i in range(0,a):
    e=input()
    s.append(e)
for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
        if str(s[i])==str(s[j]):
            c=c+1 
            #print(s[i],"==",s[j])
    if c==b:
        print("yes")
        break
    
else:
    print("no")
