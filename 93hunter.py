a=input()
s=[]
for i in range(0,len(a)):
    if i%2!=0:
        s.append(a[i])
    else:
        d=a[i].upper()
        s.append(d)
for i in range(0,len(s)):
    print(s[i],end="")
    
