a=input()
s=""
c=0
for i in range(len(a)):
    if a[i]==" ":
        s=s+a[i]
    elif  c%2!=0:
        s=s+a[i]
        c=c+1 
    else:
        s=s+a[i].upper()
        c=c+1
print(s)
    
