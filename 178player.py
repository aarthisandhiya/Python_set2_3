a=input()
s=''
for i in range(0,len(a)):
    if a.count(a[i])>1:
        d=a[i].upper()
        s=s+str(d)+''
    else:
        s=s+str(a[i])+''
print(s)
