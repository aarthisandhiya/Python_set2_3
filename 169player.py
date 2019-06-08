a=input()
s=[]
for i in range(0,len(a)):
    if a[i] not in s:
        s.append(a[i])
        s.append(a.count(a[i]))
for i in range(0,len(s)):
    print(s[i],end="")
